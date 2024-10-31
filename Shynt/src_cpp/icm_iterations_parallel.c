#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <time.h>
#include <math.h>

#include "data_structs.h"
#include "matrix_operations.h"
#include <omp.h>


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
  double *power_converge, double *phi_convergence, int iteration,
  double **nuFiss_i, int *eq_reg_list, double *mainRegions_vol
);

double calculate_keff(
  double **phi_prev, double **phi_new, double *mainRegions_vol,
  int numRegions, int eneG, 
  double keff_prev, double **nuFiss_i, int *eq_reg_list
);
double *calculate_fission_src(
  int numRegions, int eneG, double **nuFiss_i,  
  int *eq_reg_list, double *mainRegions_vol, double **phi
);

void print_icm_matrix(
  MatrixEntry matrix_entry, int g
);

void print_vector(
  double **vector, int rows, int cols, char *name, int transport_iter
);

void split_line(char* line, double* jin, double* jout, int count) {
  char* token = strtok(line, ",");  // Get the index
  int g = atoi(token);
  token = strtok(NULL, ","); // drop the energy cid
  token = strtok(NULL, ","); // drop the energy sid
  
  token = strtok(NULL, ",");
  jin[count] = atof(token);

  token = strtok(NULL, ",");
  jout[count] = atof(token);

  token = strtok(NULL, ","); // drop the last value

}

OutputData power_iteration_with_transport_sweep(
  IcmMatrixes icm_matrixes, ConvergenceData convergence, MeshData mesh, int num_omp
) {
  // -----------------------------------------
  // printf("OpenMP version: %d\n", _OPENMP);
  omp_set_num_threads(num_omp);
  
  clock_t start, end;
  double cpu_time_used;
  start = clock();
  // -----------------------------------------
  printf("Number of coarse nodes from C-API:  %i\n", mesh.numCoarseNodes);
  
  int eneG = convergence.energyGr;

  // allocate phi_prev and phi_new ----------------------------------------
  double **phi_prev = (double **)malloc(eneG * sizeof(double));
  double **phi_prev_prev = (double **)malloc(eneG * sizeof(double));
  double **phi_new = (double **)malloc(eneG * sizeof(double));
  double **residual_phi_old = (double **)malloc(eneG * sizeof(double));
  double **residual_phi_new = (double **)malloc(eneG * sizeof(double));
  double **residual_cheb1 = (double **)malloc(eneG * sizeof(double));


  for (int g = 0; g <  eneG; g++) {
    phi_prev[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    phi_prev_prev[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    phi_new[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    residual_phi_old[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    residual_phi_new[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    residual_cheb1[g] = (double *)malloc(mesh.numRegions * sizeof(double));
    
    for (int r = 0; r <  mesh.numRegions; r++) {
      phi_prev[g][r] = 1.0;
      phi_prev_prev[g][r] = 1.0;
      phi_new[g][r] = 1.0;
      residual_phi_old[g][r] = 1.0;
      residual_phi_new[g][r] = 1.0;
      residual_cheb1[g][r] = 1.0;

    } 
  }

  // initialize ji_prev, ji_new, jo_prev ----------------------------------
  // int *vector = (int *)calloc(n, sizeof(int));
  double **jin_prev = (double **)malloc(eneG * sizeof(double));
  double **jin_new = (double **)malloc(eneG * sizeof(double));
  double **jout_new = (double **)malloc(eneG * sizeof(double));
  for (int g = 0; g < eneG; g++) {
    jin_new[g] = (double *)malloc(mesh.numSurfaces * sizeof(double));
    jin_prev[g] = (double *)malloc(mesh.numSurfaces * sizeof(double));
    jout_new[g] = (double *)malloc(mesh.numSurfaces * sizeof(double));
    for (int s = 0; s <  mesh.numSurfaces; s++) {
      jin_new[g][s] = 0.0;
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

  IcmOperationsParallel *icm_ops = (IcmOperationsParallel *)malloc(sizeof(IcmOperationsParallel));
  icm_ops->qsrc = (double ***)malloc(num_omp * sizeof(double));
  icm_ops->mSJi = (double ***)malloc(num_omp * sizeof(double));
  icm_ops->mTQ =  (double ***)malloc(num_omp * sizeof(double));
  icm_ops->mRJi = (double ***)malloc(num_omp * sizeof(double));
  icm_ops->mUQ =  (double ***)malloc(num_omp * sizeof(double));

  CoarseNode *mainCoarseNodes_array = mesh.mainCoarseNodes_array;

  for (int thread = 0; thread < num_omp; thread ++){
    // printf("num thread %i\n", thread);
    icm_ops->qsrc[thread] = (double **)malloc(numMainNodes * sizeof(double));
    icm_ops->mSJi[thread] = (double **)malloc(numMainNodes * sizeof(double));
    icm_ops->mTQ[thread] =  (double **)malloc(numMainNodes * sizeof(double));
    icm_ops->mRJi[thread] = (double **)malloc(numMainNodes * sizeof(double));
    icm_ops->mUQ[thread] =  (double **)malloc(numMainNodes * sizeof(double));
    for (int i = 0; i < numMainNodes; i++){
      CoarseNode m_node = mainCoarseNodes_array[i];

      icm_ops->qsrc[thread][i] = (double *)malloc(m_node.numRegions  * sizeof(double));
      icm_ops->mSJi[thread][i] = (double *)malloc(m_node.numRegions  * sizeof(double));
      icm_ops->mTQ[thread][i] =  (double *)malloc(m_node.numRegions  * sizeof(double));
      icm_ops->mRJi[thread][i] = (double *)malloc(m_node.numSurfaces * sizeof(double));
      icm_ops->mUQ[thread][i] =  (double *)malloc(m_node.numSurfaces * sizeof(double));
    }
  }
  

  // allocation of the Output data: -----------------------------------------------

  OutputData output;
  output.keff = (double *)malloc(convergence.max_iterations * sizeof(double));
  output.phi = (double *)malloc(eneG * mesh.numRegions * sizeof(double));
  output.jin = (double *)malloc(eneG * mesh.numSurfaces * sizeof(double));
  output.jout = (double *)malloc(eneG * mesh.numSurfaces * sizeof(double));
  output.transport_iterations = (int *)malloc(eneG*convergence.max_iterations * sizeof(int));
  output.phi_convergence = (double *)malloc(eneG * convergence.max_iterations * sizeof(double));
  double *epsilon_array = (double *)malloc(convergence.max_iterations * sizeof(double));
  
  // ------------------------------------------------------------------------
  // Reading J boundary
  // FILE* file = fopen("/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/src_cpp/4r-J.csv", "r");
  // if (file == NULL) {
  //     perror("Error opening file");
  //     return output;
  // }

  // char line[1024];
  // int max_elements = 506161;  // Number of elements you want to handle

  // double* jin_csv = malloc(max_elements * sizeof(double));
  // double* jout_csv = malloc(max_elements * sizeof(double));


  // // Skip the header line
  // fgets(line, sizeof(line), file);

  // int count = 0;
  // // Read each line of the CSV file
  // while (fgets(line, sizeof(line), file)) {
  //     line[strcspn(line, "\n")] = '\0';  // Remove the newline character

  //     // Split the line into numeric values and store them
  //     split_line(line, jin_csv, jout_csv, count);
  //     printf("Index = %i, Jin = %f, Jout = %f \n", count, jin_csv[count], jout_csv[count]);

  //     count++;
  // }

  // fclose(file);
  // -------------------------------------------------------------------------
  // Equivalence list of regions
  int *eq_reg_list = (int *)malloc(mesh.numRegions * sizeof(int));

  int eq_idx = 0;
  for (int cid = 0; cid < mesh.numCoarseNodes; cid++) {
    CoarseNode coarse_node = mesh.coarse_nodes[cid];
    for(int r = 0; r < coarse_node.numRegions; r++) {
      eq_reg_list[eq_idx] = coarse_node.equivalentRegions[r];
      eq_idx ++;
    }
  }
  printf("Allocation completed \n");

  // initialize keff
  double keff_prev = 0.8;
  double keff_new = 1.0;
  output.keff[0] = 1.0;
  output.transport_iterations[0] = 0;
  epsilon_array[0] = 0.0;

  // initialize convergence values
  double k_converge = 1.0;
  double phi_converge = 1.0;
  double pow_convergence[2] = {
    k_converge, phi_converge
  };
  

  SrcMatrixEntry *mScatt = icm_matrixes.mScat_i;
  SrcMatrixEntry *mFiss = icm_matrixes.mFiss_i;
  double **nuFiss_i = icm_matrixes.nuSigFiss_i;

  printf("Power iteration loop starting \n");
  int boundary_counter = 0;
  // Parameters for Chebyshev acceleration:
  double dr_prev = 0.0;
  double dr_new = 1.0;
  double dr0 = 0.0;
  int chebyshev_iteration = 0;
  double alpha = 1.0;
  double beta = 0.0;
  double chev_prev = 1.0;
  double chev_prev_prev = 1.0;
  double chev_new = 1.0;
  double gamma = 0.0;

  int iteration = 1;
  int free_iteration = 4;
  int iterations_accelerated = free_iteration;
  double cheb_iter_check = 10;

  bool acceleration = false;


  while (   // power loop
    (k_converge >= convergence.tolerance  || phi_converge >= convergence.tolerance)
    &&  iteration < convergence.max_iterations
  ) {

    
    printf("Beginning transport iterations: \n");
    printf("Transport iterations completed (g): ");
    
    

    for (int g = 0; g < eneG; g++) {
      int transport_iter = 0;
      double j_converge = 1.0;

      


      while (  // transport loop
        j_converge >= convergence.tolerance //&& 
        // transport_iter < convergence.max_iterations
      ) {
        // Transport iterations ----------------------------------------------
        transport_iter ++;
 
        int cid;
        #pragma omp parallel for private(cid)
        
        for (cid = 0; cid < mesh.numCoarseNodes; cid++) {
          // printf("Coarse_node %i \n", cid);

          int thread_id = omp_get_thread_num();
          CoarseNode coarse_node = mesh.coarse_nodes[cid];

          int eq_node = coarse_node.equivalent_coarse_node;
          int phi_idx = coarse_node.phi_idx;
          int jin_idx = coarse_node.jin_idx;

          MatrixEntry mR_n = icm_matrixes.mR_n[eq_node];
          MatrixEntry mS_n = icm_matrixes.mS_n[eq_node];
          MatrixEntry mT_n = icm_matrixes.mT_n[eq_node];
          MatrixEntry mU_n = icm_matrixes.mU_n[eq_node];
 
        
          // calculate  q_src with phi_prev and keff_prev ---------------------
          double *q_src = icm_ops->qsrc[thread_id][eq_node];
          calculate_q_src(
            q_src, mScatt, mFiss, keff_prev, phi_prev, eneG, coarse_node, g, 
            phi_idx
          );

          // Calculate phi_new ------------------------------------------------
          double *mSJi = icm_ops->mSJi[thread_id][eq_node];
          multiplyMatrixVector(
            mS_n.matrix[g], coarse_node.numRegions, coarse_node.numSurfaces,
            jin_prev[g], coarse_node.numSurfaces, jin_idx,
            mSJi
          );
          
          double *mTQ = icm_ops->mTQ[thread_id][eq_node];
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
          double *mRJi = icm_ops->mRJi[thread_id][eq_node];
          multiplyMatrixVector(
            mR_n.matrix[g], coarse_node.numSurfaces, coarse_node.numSurfaces,
            jin_prev[g], coarse_node.numSurfaces, jin_idx,
            mRJi
          );

          double *mUQ = icm_ops->mUQ[thread_id][eq_node];
          multiplyMatrixVector(
            mU_n.matrix[g], coarse_node.numSurfaces, coarse_node.numRegions,
            q_src, coarse_node.numRegions, 0,
            mUQ
          );

          sumVectors(
            mRJi, coarse_node.numSurfaces, mUQ, coarse_node.numSurfaces,
            jout_new[g], jin_idx
          );
          
        }

        // Transfer the J_in -------------------------------------------
        boundary_counter = 0;
        // printf("%i\n", mesh.numSurfaces);
        int nid =  0;
        
        // Transfer Jout to Jin -----------------------------------------------
        for (int a = 0; a < mesh.numSurfaces; a++) {
          jin_new[g][a] = 0.0;
        }
        for (nid = 0; nid < mesh.numCoarseNodes; nid++) {
          
          CoarseNode coarse_node = mesh.coarse_nodes[nid];
          TwinSurfaceInfoArray *surfaces_info = coarse_node.twin_surfaces_info;
          int numSurfaces = coarse_node.numSurfaces;
          for (int ss = 0; ss < numSurfaces; ss++) {
            TwinSurfaceInfo *twin_info_array = surfaces_info[ss].array;
            int num_twins = surfaces_info[ss].twins_number;
            for (int tw = 0; tw < num_twins; tw++){
              TwinSurfaceInfo tw_info = twin_info_array[tw];
              int from_surf = tw_info.from_surf - 1;
              int to_surf = tw_info.to_surf - 1;
              double weight = tw_info.weight;
              if (from_surf == to_surf) {
                boundary_counter ++;
                // is boundary
                if (mesh.bc) {
                  // reflective
                  jin_new[g][to_surf] = jout_new[g][from_surf];
                }
                else {
                  // void
                  jin_new[g][to_surf] = 0.0;
                  // int idx = g*mesh.numSurfaces + to_surf;
                  // jin_new[g][to_surf] = jin_csv[idx];
                }
              }
              else {
                // is not boundary
                jin_new[g][to_surf] += jout_new[g][from_surf] * weight;
              }
            }
          }
        }
      
        // --------------------------------------------------------------------
        
        // Check J_in convergence: -------------------------------------------
        j_converge = check_transport_convergence(
          jin_prev, jin_new, mesh.numSurfaces, g
        );
        // Update Jin_prev with Jin_new for next transport iteration ----------
        // for (int g = 0; g < eneG; g++) {
        for (int a = 0; a < mesh.numSurfaces; a++) {
          jin_prev[g][a] = jin_new[g][a];
          // jout_new[g][a] = 1.0;
        }
        // }


      }
      
      
      
      int idx_tr_iter = ((iteration) * eneG) + g;
      output.transport_iterations[idx_tr_iter] = transport_iter;


      printf("%i, ", transport_iter);
      
    }

    // Calculate new  residuals ---------------------------------
    for (int g = 0; g < eneG; g++){
      substractVectors(
        phi_new[g], mesh.numRegions, 0,
        phi_prev[g], mesh.numRegions, 0,
        residual_phi_new[g], 0
      );
    }
    // ---------------------------------------------------

    // Acceleration -----------------------------------------
    if (iteration > iterations_accelerated){ // calculation of coefficients
      chebyshev_iteration = iteration - iterations_accelerated;
      printf("\nAcceleration iteration: %i\n", chebyshev_iteration);

      if (chebyshev_iteration == 1){
        dr0 = dr_new;
        for (int g = 0; g < eneG; g++){
          for (int r = 0; r < mesh.numRegions; r++) {
            residual_cheb1[g][r] = residual_phi_new[g][r];
          }
        }
        alpha = 2 / (2 - dr0);
        beta = 0;
        gamma = acosh((2/dr0)-1);
      }
      else if (chebyshev_iteration > 1){
        alpha=(4/dr0)*(cosh((chebyshev_iteration-1)*gamma)/cosh(chebyshev_iteration*gamma));
        beta = (1-(dr0/2))-1/alpha;
      }
      
      // Chebyshev extrapolation --
      for (int g = 0; g < eneG; g++){
        for (int r = 0; r < mesh.numRegions; r++) {
          phi_new[g][r] = phi_prev[g][r] + alpha*(residual_phi_new[g][r] + beta*(phi_prev[g][r] - phi_prev_prev[g][r]));
        }
      }
        

      if (chebyshev_iteration == cheb_iter_check) {
        printf("Chebysev DR recalculation\n");
        // Recalculation of the dominance ratio i guess
        // with the residual of the first accelerated iteration

        double *fission_src_residual_new = calculate_fission_src(
          mesh.numRegions, eneG, nuFiss_i, eq_reg_list, mesh.mainRegions_volume, 
          residual_phi_new
        );
        double *fission_src_residual_cheb1 = calculate_fission_src(
          mesh.numRegions, eneG, nuFiss_i, eq_reg_list, mesh.mainRegions_volume, 
          // residual_cheb1
          residual_phi_old

        );
        double numerator =  dot_product_vector(
          fission_src_residual_new, fission_src_residual_new, mesh.numRegions
        );
        double denominator =  dot_product_vector(
          fission_src_residual_cheb1, fission_src_residual_cheb1, mesh.numRegions
        );
        // double _E = sqrt(numerator/denominator);
        dr_new = sqrt(numerator/denominator);

            
        // double x = (2/dr0) - 1;
        // double _E_star = 1/cosh((cheb_iter_check-1)*acosh(x));
        
        // counter=counter+1; // counter to store E_star
        // E_star_array(counter,1)=E_star;
        // dr_new = (dr0/2)*( 
        //   cosh(
        //     acosh(_E/_E_star)/(cheb_iter_check-1)
        //   ) + 1
        // );
        printf("dr_new %.8f\n", dr_new);
        // printf("_E %.8f\n", _E);
        // printf("_E_star %.8f\n", _E_star);


        if ((dr_new-dr_prev)/dr_new < 0.001){
          cheb_iter_check *= 2;
        }
        
        // DR_array(outer_counter,1)=DR;
        dr_prev = dr_new;
        iterations_accelerated = iteration;
        // Line above now equalizes with the trasnport counter and then next iteration
        // outer_counter will be higher by one and will enter acceleration
        // as a first cheb iteration
      }
      else {
        // TODO store the dominance ratio in a vector
      }

    }


      
    

    
    // ---------------------------------------------------

    // Calculate dominance ratio --------------------------
    if (iteration > 1 && iteration <= free_iteration) {
      double *fission_src_residual_new = calculate_fission_src(
        mesh.numRegions, eneG, nuFiss_i, eq_reg_list, mesh.mainRegions_volume, 
        residual_phi_new
      );
      double *fission_src_residual_old = calculate_fission_src(
        mesh.numRegions, eneG, nuFiss_i, eq_reg_list, mesh.mainRegions_volume, 
        residual_phi_old
      );
      double numerator =  dot_product_vector(
        fission_src_residual_new, fission_src_residual_new, mesh.numRegions
      );
      double denominator =  dot_product_vector(
        fission_src_residual_old, fission_src_residual_old, mesh.numRegions
      );
      dr_new = sqrt(numerator/denominator);
      if (iteration >= iterations_accelerated){
        if (dr_new > 0.5){
          // i dont really know why is this "if" here
          // I think it is to make sure that the dr_new is actually greater 
          // than 0.5
          dr_prev = dr_new;
          iterations_accelerated = iteration; 
          // iterations_accelerated  value is adjusted until dr_new > 0.5
        }
        else {
          iterations_accelerated = iteration + 1;
        }
      }
    }

    // ----------------------------------------------------

    printf("\nBoundaries: %i, \n", boundary_counter);
    
    // calculate  keff new;
    keff_new = calculate_keff(
      phi_prev, phi_new, mesh.mainRegions_volume,
      mesh.numRegions, eneG, keff_prev, nuFiss_i, eq_reg_list
    );
    // keff_new = 1.477791646402194;
    // keff_prev = 1.477791646402194;

    check_power_convergence(
      keff_prev, keff_new, phi_prev, phi_new, mesh.numRegions, eneG,
      pow_convergence, output.phi_convergence, iteration, nuFiss_i, 
      eq_reg_list,  mesh.mainRegions_volume
    );
    

    k_converge = pow_convergence[0];
    phi_converge = pow_convergence[1];
    epsilon_array[iteration] = k_converge;
    // update keff, residual, phi for the next iteration ----------------------
    for (int g = 0; g < eneG; g++) {
      for (int r = 0; r < mesh.numRegions; r++) {
        phi_prev_prev[g][r] = phi_prev[g][r];
        phi_prev[g][r] = phi_new[g][r];
        residual_phi_old[g][r] = residual_phi_new[g][r];
      }
      for (int a = 0; a < mesh.numSurfaces; a++) {
        jin_prev[g][a] = jin_new[g][a];
      }
    }
    keff_prev = keff_new;
    // ------------------------------------------------------------------------
    


    // Print iteration data
    // printf("Transport convergence: %.8E \n", j_converge);
    printf("\nKeff convergence: %.8E \n", k_converge);
    printf("Phi convergence: %.8E \n", phi_converge);
    printf("Keff: %.15f \n", keff_new);
    printf("iteration: %i \n", iteration);
    // printf("Jout 217171, 217172, 217173\n");
    // printf("%.8E  %.8E  %.8E \n", jout_new[0][217170], jout_new[0][217171], jout_new[0][217172]);
    // printf("Jin 217171, 217172, 217173\n");
    // printf("%.8E  %.8E  %.8E \n", jin_new[0][217170], jin_new[0][217171], jin_new[0][217172]);
    // if (iteration > 3){
    //   dr_prev = epsilon_array[iteration-1]/epsilon_array[iteration-2];
    //   dr_new = epsilon_array[iteration]/epsilon_array[iteration-1];
    // }
    printf("Dominance ratio prev: %.8E \n", dr_prev);
    printf("Dominance ratio new: %.8E \n", dr_new);
    printf("sqrt in PI\n");
    // printf("dr_new - dr_prev: %.8E \n", fabs(dr_new-dr_prev));


    printf(" -----------------------\n");
    fflush(stdout);

    // output data: ---------------------------------------------------
    output.keff[iteration] = keff_new;
    // output.transport_iterations[iteration] = transport_iter-1;
    // ----------------------------------------------------------------

    iteration ++;

    // break;
    // if (iteration == 5){break;}
  }

  output.keff_convergence = k_converge;
  output.power_iterations = iteration-1;
  output.time_iterations = 0.0;
  for (int g = 0; g < eneG; g++) {
    for (int r = 0; r < mesh.numRegions; r++) {
      int idx_gr = (g * mesh.numRegions) + r;
      // printf("%i, ", idx_gr);
      output.phi[idx_gr] = phi_new[g][r];
    }
    for (int a = 0; a < mesh.numSurfaces; a++) {
      int idx_gr = (g * mesh.numSurfaces) + a;
      // printf("%i, ", idx_gr);
      output.jin[idx_gr] = jin_new[g][a];
      output.jout[idx_gr] = jout_new[g][a];

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
  
  for (int thread = 0; thread < num_omp; thread ++){
    
    for (int i = 0; i < numMainNodes; i++){
      free(icm_ops->qsrc[thread][i]);
      free(icm_ops->mSJi[thread][i]);
      free(icm_ops->mTQ[thread][i]);
      free(icm_ops->mRJi[thread][i]);
      free(icm_ops->mUQ[thread][i]);
    }
    free(icm_ops->qsrc[thread]);
    free(icm_ops->mSJi[thread]);
    free(icm_ops->mTQ[thread]);
    free(icm_ops->mRJi[thread]);
    free(icm_ops->mUQ[thread]);
  }  

  free(icm_ops->qsrc);
  free(icm_ops->mSJi);
  free(icm_ops->mTQ);
  free(icm_ops->mRJi);
  free(icm_ops->mUQ);
  free(icm_ops);
  // free(jin_csv);
  // free(jout_csv);
  end = clock();
  
  cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
  output.time_iterations = cpu_time_used;

  printf("Time power iteration method: %f seconds\n", cpu_time_used);
  printf("Exiting function \n");

  // printf("%.8f  %.8f", output.phi[0][0], output.phi[0][1]);
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
  double **jin_prev, double **jin_new, int numSurfaces, int g
){
  double converge = 0.0;
  

  for (int a = 0; a < numSurfaces; a++) {
    double new_converge_val = fabs(jin_new[g][a] - jin_prev[g][a])/jin_prev[g][a];


    if (new_converge_val > converge){
      converge = new_converge_val;
    }
  
  }
  return converge;
}

void check_power_convergence(
  double keff_prev, double keff_new, 
  double **phi_prev, double **phi_new, int numRegions, int eneG,
  double *power_converge, double *phi_convergence, int iteration,
  double **nuFiss_i, int *eq_reg_list, double *mainRegions_vol
){
  /*
    Funcion that calculates 
      - the square norm of the vevctor phi_new - phi_prev
      - the convergence value of keff
      - the residual
  */
  double k_converge = fabs(keff_new - keff_prev) / keff_prev;


  double *fission_src_new = calculate_fission_src(
    numRegions, eneG, nuFiss_i, eq_reg_list, mainRegions_vol, phi_new
  );
  double *fission_src_prev = calculate_fission_src(
    numRegions, eneG, nuFiss_i, eq_reg_list, mainRegions_vol, phi_prev
  );

  double phi_converge = 0.0;
  double sum_fsrc_new_m_prev = 0.0;
  double sum_fsrc_prev = 0.0;
  
  for (int a = 0; a < numRegions; a++) {
    sum_fsrc_new_m_prev += fabs(fission_src_new[a] - fission_src_prev[a]);
    sum_fsrc_prev += fission_src_prev[a];
  }
  phi_converge = sum_fsrc_new_m_prev / sum_fsrc_prev;


  for (int g = 0; g < eneG; g++) { // loop to calculate the euclidean norm of the flux
    double norm_flux = 0.0;
    for (int a = 0; a < numRegions; a++) {
      // double new_phi_converge_val = fabs(phi_new[g][a] - phi_prev[g][a])/phi_prev[g][a];
      // double square_phinew_phiprev;
      norm_flux += pow(phi_new[g][a] - phi_prev[g][a], 2);
      
      // phi_convergence[g*numRegions + a] = new_phi_converge_val;
      // if (new_phi_converge_val > phi_converge){
      //   phi_converge = new_phi_converge_val;
      // }
    }

    phi_convergence[((iteration) * eneG) + g] = sqrt(norm_flux);
  }

  power_converge[0] = k_converge;
  power_converge[1] = phi_converge;
  
}

double *calculate_fission_src(
  int numRegions, int eneG, double **nuFiss_i,  
  int *eq_reg_list, double *mainRegions_vol, double **phi
){
  double *fiss_src = (double *)malloc(numRegions * sizeof(double));
  

  for (int i = 0; i < numRegions; i++) {
    double sum_g_new = 0.0;
    double sum_g_prev = 0.0;

    int eq_idx = eq_reg_list[i];
    double vol = mainRegions_vol[eq_idx];
    // printf("%i, %i \n", a, eq_idx);
    double fission_src_i = 0.0;
   

    for (int g = 0; g < eneG; g++) {
      fission_src_i += nuFiss_i[eq_idx][g] * phi[g][i] * vol;
      // printf("%.8f, %.8f, %.8f \n", nuFiss_i[eq_idx][g], phi[g][i], vol);
    }
    fiss_src[i] = fission_src_i;
  }

  return fiss_src;
}

double calculate_keff(
  double **phi_prev, double **phi_new, double *mainRegions_vol,
  int numRegions, int eneG, double keff_prev, double **nuFiss_i,  
  int *eq_reg_list
) {

  // printf("hello\n");
  // CALCULATE NUMERATOR: INTEGRATED FISSION SOURCE IN ENERGY (N+1)
  // CALCULATE DENOMINATOR: INTEGRATED FISSION SOURCE IN ENERGY (N)

  double *fission_src_prev = calculate_fission_src(
    numRegions, eneG, nuFiss_i, eq_reg_list, mainRegions_vol, phi_prev
  );
  
  double *fission_src_new = calculate_fission_src(
    numRegions, eneG, nuFiss_i, eq_reg_list, mainRegions_vol, phi_new
  );


  double new_dot_prod = 0.0;
  double prev_dot_prod = 0.0;
  for (int j = 0; j < numRegions; j++) {
    // printf("%.8f\n", fission_src_new[j]);
    new_dot_prod += fission_src_new[j] * fission_src_new[j];
    prev_dot_prod += fission_src_prev[j] * fission_src_prev[j];
  }

  double keff_new = keff_prev * sqrt(new_dot_prod / prev_dot_prod);

  free(fission_src_new);
  free(fission_src_prev);
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

