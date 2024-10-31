#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "data_structs.h"
#include "matrix_operations.h"

// #include <suitesparse/umfpack.h>
// #include <suitesparse/GraphBLAS.h>
// #include <omp.h>

void calculate_q_src(
  double *qsrc, SrcMatrixEntry *mScatt, SrcMatrixEntry *mFiss, 
  double keff, double **phi, int eneG, CoarseNode coarse_node, 
  int g, int phi_idx
);

double check_transport_convergence(
  double **jin_prev, double **jin_new, int numSurfaces, int eneG
);

void check_power_convergence(
  double keff_prev, double keff_new,
  double **phi_prev, double **phi_new, int numRegions, int eneG,
  double *power_converge, double *phi_convergence
);

double calculate_keff(
  double **phi_prev, double **phi_new, int numRegions, int eneG, double keff_prev
);

void print_icm_matrix(
  MatrixEntry matrix_entry, int g
);

void print_vector(
  double **vector, int rows, int cols, char *name, int transport_iter
);

OutputData power_iteration_with_transport_sweep(
  IcmMatrixes icm_matrixes, ConvergenceData convergence, MeshData mesh
) {
  // -----------------------------------------
  clock_t start, end;
  double cpu_time_used;
  start = clock();
  // -----------------------------------------

  int eneG = convergence.energyGr;

  // allocate phi_prev and phi_new ----------------------------------------
  double **phi_prev = (double **)malloc(eneG * sizeof(double));
  double **phi_new = (double **)malloc(eneG * sizeof(double));
  for (int g = 0; g <  eneG; g++) {
    phi_prev[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    phi_new[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    for (int r = 0; r <  mesh.numRegions; r++) {
      phi_prev[g][r] = 1.0;
      phi_new[g][r] = 1.0;
    } 
  }

  // initialize ji_prev, ji_new, jo_prev ----------------------------------
  double **jin_prev = (double **)malloc(eneG * sizeof(double));
  double **jin_new = (double **)malloc(eneG * sizeof(double));
  double **jout_new = (double **)malloc(eneG * sizeof(double));
  for (int g = 0; g < eneG; g++) {
    jin_new[g] = (double *)malloc(mesh.numSurfaces * sizeof(double));
    jin_prev[g] = (double *)malloc(mesh.numSurfaces * sizeof(double));
    jout_new[g] = (double *)malloc(mesh.numSurfaces * sizeof(double));
    for (int s = 0; s <  mesh.numSurfaces; s++) {
      jin_new[g][s] = 1.0;
      jin_prev[g][s] = 1.0;
      jout_new[g][s] = 1.0;
    } 
  }
  // ----------------------------------------------------------------------

  // allocation of: Qsrc, mRJi, 
  /*
    Allocation for each different coarse node regarding the resultant size of 
    the matrix operation.

    It is an array of
  */
  int numMainNodes = mesh.numMainNodes;

  IcmOperations *icm_ops = (IcmOperations *)malloc(sizeof(IcmOperations));
  icm_ops->qsrc = (IcmOperationEntry *)malloc(numMainNodes * sizeof(IcmOperationEntry));
  icm_ops->mSJi = (IcmOperationEntry *)malloc(numMainNodes * sizeof(IcmOperationEntry));
  icm_ops->mTQ = (IcmOperationEntry *)malloc(numMainNodes * sizeof(IcmOperationEntry));
  icm_ops->mRJi = (IcmOperationEntry *)malloc(numMainNodes * sizeof(IcmOperationEntry));
  icm_ops->mUQ = (IcmOperationEntry *)malloc(numMainNodes * sizeof(IcmOperationEntry));

  CoarseNode *mainCoarseNodes_array = mesh.mainCoarseNodes_array;

  for (int i = 0; i < numMainNodes; i++){
    CoarseNode m_node = mainCoarseNodes_array[i];

    icm_ops->qsrc[i].numValues = m_node.numRegions;
    icm_ops->qsrc[i].vector = (double *)malloc(m_node.numRegions * sizeof(double));
    icm_ops->mSJi[i].numValues = m_node.numRegions;
    icm_ops->mSJi[i].vector = (double *)malloc(m_node.numRegions * sizeof(double));
    icm_ops->mTQ[i].numValues = m_node.numRegions;
    icm_ops->mTQ[i].vector = (double *)malloc(m_node.numRegions * sizeof(double));
    icm_ops->mRJi[i].numValues = m_node.numSurfaces;
    icm_ops->mRJi[i].vector = (double *)malloc(m_node.numSurfaces * sizeof(double));
    icm_ops->mUQ[i].numValues = m_node.numSurfaces;
    icm_ops->mUQ[i].vector = (double *)malloc(m_node.numSurfaces * sizeof(double));
  }
  

  // allocation of the Output data: -----------------------------------------------

  OutputData output;
  output.keff = (double *)malloc(convergence.max_iterations * sizeof(double));
  output.transport_iterations = (int *)malloc(convergence.max_iterations * sizeof(int));
  output.phi = (double *)malloc(eneG * mesh.numRegions * sizeof(double));
  output.phi_convergence = (double *)malloc(eneG * mesh.numRegions * sizeof(double));
  
  
  // ------------------------------------------------------------------------
  printf("Allocation completed \n");

  // initialize keff
  double keff_prev = 1.0;
  double keff_new = 1.0;
  output.keff[0] = 1.0;
  output.transport_iterations[0] = 1.0;



  // initialize convergence values
  double k_converge = 1.0;
  double phi_converge = 1.0;
  double pow_convergence[2] = {
    k_converge, phi_converge
  };
  
  int iteration = 1;

  SrcMatrixEntry *mScatt = icm_matrixes.mScat_i;
  SrcMatrixEntry *mFiss = icm_matrixes.mFiss_i;

  printf("Power iteration loop starting \n");
  while (   // power loop
    (k_converge >= convergence.tolerance  || phi_converge >= convergence.tolerance)
    &&  iteration < convergence.max_iterations
  ) {

    double j_converge = 1.0;
    int transport_iter = 1;
    printf("Beginning transport iterations: \n");
    
    while (  // transport loop
      j_converge >= convergence.tolerance && 
      transport_iter < convergence.max_iterations
    ) {
      // if (transport_iter < 5) {
      //   char name_file_phi_new[] = "phi_new.txt";
      //   char name_file_jout_new[] = "jout_new.txt";
      //   char name_file_jin_new[] = "jin_new.txt";
      //   char tr_iter_phi_new_name[50];
      //   char tr_iter_jin_new_name[50];
      //   char tr_iter_jout_new_name[50];
      //   sprintf(tr_iter_phi_new_name, "tr%i_power%i_%s",transport_iter,iteration,name_file_phi_new);
      //   sprintf(tr_iter_jin_new_name, "tr%i_power%i_%s",transport_iter,iteration,name_file_jin_new);
      //   sprintf(tr_iter_jout_new_name, "tr%i_power%i_%s",transport_iter,iteration,name_file_jout_new);
      //   print_vector(
      //     phi_new, eneG, mesh.numRegions, tr_iter_phi_new_name, transport_iter
      //   );
      //   print_vector(
      //     jout_new, eneG, mesh.numSurfaces, tr_iter_jout_new_name, transport_iter
      //   );
      //   print_vector(
      //     jin_new, eneG, mesh.numSurfaces, tr_iter_jin_new_name, transport_iter
      //   );
      // }

      // Transport iterations ----------------------------------------------
      for (int g = 0; g < eneG; g++) {
        int phi_idx = 0;
        int jin_idx = 0;
        // printf("Coarse node:");
        for (int cid = 0; cid < mesh.numCoarseNodes; cid++) {
          
          CoarseNode coarse_node = mesh.coarse_nodes[cid];
          int eq_node = coarse_node.equivalent_coarse_node;
          MatrixEntry mR_n = icm_matrixes.mR_n[eq_node];
          MatrixEntry mS_n = icm_matrixes.mS_n[eq_node];
          MatrixEntry mT_n = icm_matrixes.mT_n[eq_node];
          MatrixEntry mU_n = icm_matrixes.mU_n[eq_node];
 
          // calculate  q_src with phi_prev and keff_prev ---------------------
          double *q_src = icm_ops->qsrc[eq_node].vector;
          calculate_q_src(
            q_src, mScatt, mFiss, keff_prev, phi_prev, eneG, coarse_node, g, 
            phi_idx
          );

          // Calculate phi_new ------------------------------------------------
          double *mSJi = icm_ops->mSJi[eq_node].vector;
          multiplyMatrixVector(
            mS_n.matrix[g], coarse_node.numRegions, coarse_node.numSurfaces,
            jin_prev[g], coarse_node.numSurfaces, jin_idx,
            mSJi
          );
          
          double *mTQ = icm_ops->mTQ[eq_node].vector;
          multiplyMatrixVector(
            mT_n.matrix[g], coarse_node.numRegions, coarse_node.numRegions,
            q_src, coarse_node.numRegions, 0,
            mTQ
          );
    
          sumVectors(
            mSJi, coarse_node.numRegions, mTQ, coarse_node.numRegions,
            phi_new[g], phi_idx
          );
          
          // printf(" Completed \n");
        
          // Calculate the new j_out ------------------------------------------
          double *mRJi = icm_ops->mRJi[eq_node].vector;
          multiplyMatrixVector(
            mR_n.matrix[g], coarse_node.numSurfaces, coarse_node.numSurfaces,
            jin_prev[g], coarse_node.numSurfaces, jin_idx,
            mRJi
          );

          double *mUQ = icm_ops->mUQ[eq_node].vector;
          multiplyMatrixVector(
            mU_n.matrix[g], coarse_node.numSurfaces, coarse_node.numRegions,
            q_src, coarse_node.numRegions, 0,
            mUQ
          );

          sumVectors(
            mRJi, coarse_node.numSurfaces, mUQ, coarse_node.numSurfaces,
            jout_new[g], jin_idx
          );
          
          phi_idx += coarse_node.numRegions;
          jin_idx += coarse_node.numSurfaces;

          for (int i = 0; i < coarse_node.numRegions; i++) {
            icm_ops->qsrc[eq_node].vector[i] = 0.0;
            icm_ops->mSJi[eq_node].vector[i] = 0.0;
            icm_ops->mTQ[eq_node].vector[i] = 0.0;
          }
          for (int i = 0; i < coarse_node.numSurfaces; i++) {     
            icm_ops->mRJi[eq_node].vector[i] = 0.0;
            icm_ops->mUQ[eq_node].vector[i] = 0.0;
          }
        }

        // Transfer the J_in -------------------------------------------
        for (int a = 0; a < mesh.numSurfaces; a++) {
          int tr_idx = mesh.currents_transfer_idxs[a];
          jin_new[g][tr_idx] = jout_new[g][a];
        }
      }
      // Check J_in convergence: -------------------------------------------
      j_converge = check_transport_convergence(
        jin_prev, jin_new, mesh.numSurfaces, eneG
      );
      // Update Jin_prev with Jin_new for next ransport iteration ----------
      for (int g = 0; g < eneG; g++) {
        for (int a = 0; a < mesh.numSurfaces; a++) {
          jin_prev[g][a] = jin_new[g][a];
          // jout_new[g][a] = 1.0;
        }
      }
      transport_iter ++;
      // if (transport_iter == 4){break;}
    }
    printf("Transport iterations terminated \n");

  
    // calculate  keff new;
    keff_new = calculate_keff(
      phi_prev, phi_new, 
      mesh.numRegions, eneG, keff_prev
    );

    check_power_convergence(
      keff_prev, keff_new, phi_prev, phi_new, mesh.numRegions, eneG,
      pow_convergence, output.phi_convergence
    );

    k_converge = pow_convergence[0];
    phi_converge = pow_convergence[1];
    
    // update keff and phi for the next iteration -----------------------------
    for (int g = 0; g < eneG; g++) {
      for (int r = 0; r < mesh.numRegions; r++) {
        phi_prev[g][r] = phi_new[g][r];
      }
      for (int a = 0; a < mesh.numSurfaces; a++) {
        // jin_prev[g][a] = 1.0;
      }
    }

    keff_prev = keff_new;

    // Print iteration data
    printf("Transport convergence: %.8E \n", j_converge);
    printf("Transport iterations: %i \n", transport_iter-1);
    printf("Keff convergence: %.8E \n", k_converge);
    printf("Phi convergence: %.8E \n", phi_converge);
    printf("Keff: %.15f \n", keff_new);
    printf("iteration: %i \n", iteration);
    // output data: ---------------------------------------------------
    output.keff[iteration] = keff_new;
    output.transport_iterations[iteration] = transport_iter-1;
    // printf("tr_iter in array: %i\n", output.transport_iterations[iteration]);
    // ----------------------------------------------------------------
    printf("output data recorded\n");
    printf(" -----------------------\n");


    // break;
    // if (iteration == 10){break;}
    iteration ++;
  }

  output.keff_convergence = k_converge;
  output.power_iterations = iteration;
  output.time_iterations = 0.0;
  for (int g = 0; g < eneG; g++) {
    for (int r = 0; r < mesh.numRegions; r++) {
      int idx_gr = (g * mesh.numRegions) + r;
      // printf("%i, ", idx_gr);
      output.phi[idx_gr] = phi_new[g][r];
    }
  }
  
  

  printf("\nICM terminated with %i power iterations\n", iteration);
  for (int g = 0; g <  eneG; g++) {
    free(phi_prev[g]);
    free(phi_new[g]);
    free(jin_new[g]);
    free(jin_prev[g]);
    free(jout_new[g]);
  }
  free(phi_prev);
  free(phi_new);
  free(jin_new);
  free(jin_prev);
  free(jout_new);
  


  for (int i = 0; i < numMainNodes; i++){
    CoarseNode m_node = mainCoarseNodes_array[i];
    free(icm_ops->qsrc[i].vector);
    free(icm_ops->mSJi[i].vector);
    free(icm_ops->mTQ[i].vector);
    free(icm_ops->mRJi[i].vector);
    free(icm_ops->mUQ[i].vector);
  }
  free(icm_ops->qsrc);
  free(icm_ops->mSJi);
  free(icm_ops->mTQ);
  free(icm_ops->mRJi);
  free(icm_ops->mUQ);
  free(icm_ops);

  end = clock();
  
  cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
  output.time_iterations = cpu_time_used;
  printf("Time power iteration method: %f seconds\n", cpu_time_used);
  printf("Exiting function \n");


  // printf("%i  %i", output.transport_iterations[0], output.transport_iterations[1]);
  return output;
}


void calculate_q_src(
  double *qsrc, SrcMatrixEntry *mScatt, SrcMatrixEntry *mFiss, 
  double keff, double **phi, int eneG, CoarseNode coarse_node, int g,
  int phi_idx
) {
  // printf("%i", coarse_node.numRegions);
  for (int r = 0; r < coarse_node.numRegions; r++) {
    int req_idx = coarse_node.equivalentRegions[r];
    double **mScat_i = mScatt[req_idx].matrix;
    double **mFiss_i = mFiss[req_idx].matrix;

    double scatt_term = 0.0;
    double fiss_term = 0.0;
    
    for(int gp = 0; gp < eneG; gp++){
      scatt_term += mScat_i[g][gp] * phi[gp][phi_idx+r];
      fiss_term += mFiss_i[g][gp] * phi[gp][phi_idx+r];
    }
    qsrc[r] = scatt_term + fiss_term / keff;
    // printf("phi_idx: %i \n", *phi_idx);
  }

}

double check_transport_convergence(
  double **jin_prev, double **jin_new, int numSurfaces, int eneG
){
  double converge = 0.0;
  for (int g = 0; g < eneG; g++) {

    for (int a = 0; a < numSurfaces; a++) {
      double new_converge_val = (jin_new[g][a] - jin_prev[g][a])/jin_prev[g][a];
      // printf("%.8f ", new_converge_val);

      if (new_converge_val < 0.0) {
        new_converge_val *= -1;
      }
      // printf("%.8f \n", new_converge_val);

      if (new_converge_val > converge){
        converge = new_converge_val;
      }
    }
  }
  return converge;
}

void check_power_convergence(
  double keff_prev, double keff_new, 
  double **phi_prev, double **phi_new, int numRegions, int eneG,
  double *power_converge, double *phi_convergence
){
  double k_converge = fabs(keff_new - keff_prev) / keff_prev;
  

  double phi_converge = 0.0;
  for (int g = 0; g < eneG; g++) {
    for (int a = 0; a < numRegions; a++) {
      double new_phi_converge_val = fabs(phi_new[g][a] - phi_prev[g][a])/phi_prev[g][a];

    
      phi_convergence[g * numRegions + a] = new_phi_converge_val;
      if (new_phi_converge_val > phi_converge){
        phi_converge = new_phi_converge_val;
      }
    }
  }

  power_converge[0] = k_converge;
  power_converge[1] = phi_converge;
  
}

double calculate_keff(
  double **phi_prev, double **phi_new, 
  int numRegions, int eneG, double keff_prev
) {
  double new_dot_prod = 0.0;
  double prev_dot_prod = 0.0;

  for (int g = 0; g < eneG; g++) {

    for (int a = 0; a < numRegions; a++) {
      new_dot_prod += phi_prev[g][a] * phi_new[g][a];
      prev_dot_prod += phi_prev[g][a] * phi_prev[g][a];
    }
  }

  double keff_new = keff_prev * new_dot_prod / prev_dot_prod;

  return keff_new;
}

void print_icm_matrix(MatrixEntry matrix_entry, int g) {
  printf("Num rows: %i \n", matrix_entry.numRows);
  printf("Num cols: %i \n", matrix_entry.numCols);

  for (int i = 0; i < matrix_entry.numRows ; i++) {
    for (int j = 0; j < matrix_entry.numCols ; j++) {
      printf("%.8f ", matrix_entry.matrix[g][i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

void print_vector(double **vector, int rows, int cols, char *name, int transport_iter) {
  // printf();
  FILE *file = fopen(name, "w");
  // if (transport_iter == 1){
  //   file = fopen(name, "w");
  // }
  // else {
  //   file = fopen(name, "a");
  // }
  if (file == NULL) {
    perror("Error opening file");
    return;
  }
  fputs("------------- Transport iter --------- \n", file);

  for (int i = 0; i < rows; i++){
    for (int j = 0; j < cols; j++){
      fprintf(file, "%.12f\n", vector[i][j]);
    }
  }
  // Close the file
  fclose(file);
}

