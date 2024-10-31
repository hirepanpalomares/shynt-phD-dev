#include <stdio.h>
#include <stdlib.h>

#include <suitesparse/umfpack.h>
#include <suitesparse/GraphBLAS.h>
#include <omp.h>

// Function to print a matrix
void print_matrix(double *matrix, int rows, int cols) {
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      printf("%f ", matrix[i * cols + j]);
    }
    printf("\n");
  }
}


// Define a structure to store the result in COO format
typedef struct {
  int *row;
  int *col;
  double *val;
  int nnz; // number of non-zero elements
} SparseMatrixCOO;

// Define a structure to store the result in CSC format
typedef struct {
  int *row;
  int *col_ptr;
  double *val;
  int nnz; // number of non-zero elements
} SparseMatrixCSC;



// Function to convert a sparse matrix from COO to CSC format
void coo_to_csc(
  int matrix_size, int num_nonzero, int *coo_row, 
  int *coo_col, double *coo_val,
  int *csc_row, int *csc_col_ptr, double *csc_val
) {
  
    int i, j, k;
    
    // Initialize column pointers
    for (i = 0; i <= matrix_size; i++) {
        csc_col_ptr[i] = 0;
    }

    // Count the number of entries in each column
    for (i = 0; i < num_nonzero; i++) {
        csc_col_ptr[coo_col[i] + 1]++;
    }

    // Cumulative sum of column pointers
    for (i = 0; i < matrix_size; i++) {
        csc_col_ptr[i + 1] += csc_col_ptr[i];
    }

    // Fill in the row indices and values
    for (i = 0; i < num_nonzero; i++) {
        j = coo_col[i];
        k = csc_col_ptr[j];
        csc_row[k] = coo_row[i];
        csc_val[k] = coo_val[i];
        csc_col_ptr[j]++;
    }

    // Restore column pointers
    for (i = matrix_size; i > 0; i--) {
        csc_col_ptr[i] = csc_col_ptr[i - 1];
    }
    csc_col_ptr[0] = 0;
}



// Function to print a sparse matrix in COO format
void print_sparse_matrix(SparseMatrixCOO matrix) {
  printf("row\tcol\tval\n");
  for (int i = 0; i < matrix.nnz; i++) {
    printf("%d\t%d\t%f\n", matrix.row[i], matrix.col[i], matrix.val[i]);
  }
}


void define_graphBLAS_sparse_matrix(){

}

// Function to extract a GraphBLAS matrix to CSC format
void extract_csc(
  GrB_Matrix M, int **Ap, int **Ai, double **Ax, int *nnz, int n
) {
  GrB_Index nvals;
  GrB_Matrix_nvals(&nvals, M);

  *nnz = nvals;
  *Ap = (int *) malloc((n + 1) * sizeof(int));
  *Ai = (int *) malloc(nvals * sizeof(int));
  *Ax = (double *) malloc(nvals * sizeof(double));

  int *Cp = *Ap;
  int *Ci = *Ai;
  double *Cx = *Ax;

  Cp[0] = 0;
  int idx = 0;
  for (GrB_Index j = 0; j < n; j++) {
    // int col_start = idx;
    for (GrB_Index i = 0; i < n; i++) {
      double value;
      if (GrB_Matrix_extractElement_FP64(&value, M, i, j) == GrB_SUCCESS) {
        int ii = i;
        Ci[idx] = ii;
        Cx[idx] = value;
        idx++;
        // nnz ++;
      }
    }
    int jj = j;
    Cp[jj + 1] = idx;
  }
}

void invert_matrix( ) {

}


void calculate_inverse_IMR(
  int *mM_row_idxs, int *mM_col_idxs, double *mM_values,
  int *mR_row_idxs, int *mR_col_idxs, double *mR_values,
  int numValuesM, int numValuesR, int numSurfaces
){
  // omp_set_num_threads(20);
  printf("Sparse matrix calculations with C\n");
  SparseMatrixCOO mM = {
    mM_row_idxs, mM_col_idxs, mM_values, numValuesM
  };
  SparseMatrixCOO mR = {
    mR_row_idxs, mR_col_idxs, mR_values, numValuesR
  };
  
  printf("Sparse COO allocation completed\n");
  // convert mR and mM to CSC format --------------------------------------
  int *csc_col_ptr_mM, *csc_row_mM, *csc_col_ptr_mR, *csc_row_mR;
  double *csc_val_mM, *csc_val_mR;

  // Allocate memory for CSC format
  // mM allocation
  csc_col_ptr_mM = (int *)malloc((numSurfaces+ 1) * sizeof(int));
  csc_row_mM = (int *)malloc(mM.nnz * sizeof(int));
  csc_val_mM = (double *)malloc(mM.nnz * sizeof(double));
  // mR allocation
  csc_col_ptr_mR = (int *)malloc((numSurfaces+ 1) * sizeof(int));
  csc_row_mR = (int *)malloc(mR.nnz * sizeof(int));
  csc_val_mR = (double *)malloc(mR.nnz * sizeof(double));
  printf("Sparse CSC allocation completed\n");

  // convert COO to CSC
  coo_to_csc(
    numSurfaces, mM.nnz, mM.row, mM.col, mM.val,
    csc_row_mM, csc_col_ptr_mM, csc_val_mM // Ap, Ai, Ax
  );

  coo_to_csc(
    numSurfaces, mR.nnz, mR.row, mR.col, mR.val,
    csc_row_mR, csc_col_ptr_mR, csc_val_mR // Ap, Ai, Ax
  );
  printf("Sparse COO->CSC completed\n");

  // ---------------------------------------------------------------------

  
  GrB_Info info; // start with GraphBLAS
  GrB_init(GrB_BLOCKING); // Initialize the GraphBLAS library
  GxB_Global_Option_set(GxB_NTHREADS, 10); // Set the number of threads for parallelism


  // Create two sparse matrices A and B in CSC format
  GrB_Index matrixDim = numSurfaces; // Define the dimensions of the matrices
  GrB_Matrix gr_mM, gr_mR, gr_mMxmR;
  GrB_Matrix_new(&gr_mM, GrB_FP64, matrixDim, matrixDim);
  GrB_Matrix_new(&gr_mR, GrB_FP64, matrixDim, matrixDim);
  GrB_Matrix_new(&gr_mMxmR, GrB_FP64, matrixDim, matrixDim);
  printf("GrB Matrixes instantiated\n");
  
  // Populate matrix gr_mM using CSC format

  for (int j = 0; j < matrixDim; j++) {
    for (int p = csc_col_ptr_mM[j]; p < csc_col_ptr_mM[j + 1]; p++) {
      GrB_Matrix_setElement_FP64(gr_mM, csc_val_mM[p], csc_row_mM[p], j);
    }
        
    for (int p = csc_col_ptr_mR[j]; p < csc_col_ptr_mR[j + 1]; p++) {
      GrB_Matrix_setElement_FP64(gr_mR, csc_val_mR[p], csc_row_mR[p], j);
    }    
  }

  printf("GraphBLAS matrixes gr_mM populated\n");
  printf("GraphBLAS matrixes gr_mR populated\n");

  // Perform the matrix multiplication C = A * B
  printf("Performing multiplication mM x mR: ");
  GrB_mxm(
    gr_mMxmR, GrB_NULL, GrB_NULL, GxB_PLUS_TIMES_FP64, gr_mM, gr_mR, GrB_NULL
  );
  printf("Matrix multiplication completed \n");


  // allocate identity matrix -------------------------------------------
  GrB_Matrix gr_mI;
  GrB_Matrix_new(&gr_mI, GrB_FP64, numSurfaces, numSurfaces);
  // Dynamically allocate the CSC format arrays for the identity matrix
  GrB_Index *Ap_I = (GrB_Index *)malloc((numSurfaces + 1) * sizeof(GrB_Index));
  GrB_Index *Ai_I = (GrB_Index *)malloc(numSurfaces * sizeof(GrB_Index));
  double *Ax_I = (double *)malloc(numSurfaces * sizeof(double));
  
  // Populate the CSC arrays for the identity matrix
  for (GrB_Index i = 0; i < numSurfaces; i++) {
    Ap_I[i] = i;
    Ai_I[i] = i;
    Ax_I[i] = 1.0;
  }
  Ap_I[numSurfaces] = numSurfaces;

  // Populate the identity matrix I
  for (GrB_Index j = 0; j < numSurfaces; j++) {
    for (GrB_Index p = Ap_I[j]; p < Ap_I[j + 1]; p++) {
      GrB_Matrix_setElement_FP64(gr_mI, Ax_I[p], Ai_I[p], j);
    }
  }

  // --------------------------------------------------------------------
  
  printf("Performing mI - mM x mR: ");
  // mI - mM_xmR
  GrB_Matrix gr_mI_mMmR;
  GrB_Matrix_new(&gr_mI_mMmR, GrB_FP64, numSurfaces, numSurfaces);
  // Subtract the matrices
  GrB_eWiseAdd(
    gr_mI_mMmR, GrB_NULL, GrB_NULL, GrB_MINUS_FP64, gr_mI, gr_mMxmR, GrB_NULL
  );
  printf("Completed\n");
  // Taking inverse ---------------------------------------------------
  // printf("Calculating inverse of mI - mM x mR ");

  // extract GrB_matrix in CSC 

  SparseMatrixCSC mI_mMmR_csc;
  extract_csc(
    gr_mI_mMmR, &mI_mMmR_csc.col_ptr, &mI_mMmR_csc.row, &mI_mMmR_csc.val, 
    &mI_mMmR_csc.nnz, numSurfaces
  );
  printf("CSC format of gr_mI_mMmR extracted from GraphBLAS\n");
  printf("Non zero elements of (I - MR): %i \n", mI_mMmR_csc.nnz);

  
  void *Symbolic, *Numeric;
  double *null = (double *) NULL ;
  int status;

  // // Perform LU decomposition using UMFPACK
  umfpack_di_symbolic(
    numSurfaces, numSurfaces, 
    mI_mMmR_csc.col_ptr, mI_mMmR_csc.row, mI_mMmR_csc.val, 
    &Symbolic, null, null
  );
  umfpack_di_numeric(
    mI_mMmR_csc.col_ptr, mI_mMmR_csc.row, mI_mMmR_csc.val, Symbolic, 
    &Numeric, null, null
  );

  umfpack_di_free_symbolic(&Symbolic);

  printf("Symbolic and numeric analysis carried out by UMFPACK\n");

  // Create identity matrix
  int *mI_colptr = (int *)malloc((numSurfaces + 1) * sizeof(int));
  int *mI_row_idx = (int *)malloc(numSurfaces * sizeof(int));
  double *mI_val = (double *)malloc(numSurfaces * sizeof(double));
  for (int i = 0; i < numSurfaces; i++) {
    mI_colptr[i] = i;
    mI_row_idx[i] = i;
    mI_val[i] = 1.0;
  }
  mI_colptr[numSurfaces] = numSurfaces;
  
  printf("Identity matrix created for calculating the inverse \n");

  int upper_bound_nnz = mI_mMmR_csc.nnz;

  int *Inv_colptr = (int *)calloc( (upper_bound_nnz*10)+1, sizeof(int));
  int *Inv_rowidx = (int *)malloc( upper_bound_nnz * 10 * sizeof(int));
  double *Inv_val = (double *)malloc( upper_bound_nnz * 10 * sizeof(double));

  // Solve each column of the identity matrix
  // int i;
  // omp_set_num_threads(20);
  // #pragma omp parallel for private(i) //schedule(static)
  // for (i = 0; i < numSurfaces; i++) {
  //   umfpack_di_solve(
  //     UMFPACK_A, mI_mMmR_csc.col_ptr, mI_mMmR_csc.row, mI_mMmR_csc.val, 
  //     &Inv[i * numSurfaces], &mI_val[i * numSurfaces], Numeric, null, null
  //   );
  // }


  umfpack_di_free_numeric(&Numeric);
  free(mI_colptr);
  free(mI_row_idx);
  free(mI_val);
  free(Inv_colptr);
  free(Inv_rowidx);
  free(Inv_val);

  
  printf("Completed\n");

  printf("\nControl dbg\n");
  // ----------------------------------------------------------

  GrB_Matrix_free(&gr_mM);
  GrB_Matrix_free(&gr_mR);
  GrB_Matrix_free(&gr_mMxmR);
  GrB_Matrix_free(&gr_mI);
  GrB_Matrix_free(&gr_mI_mMmR);
  
  GrB_finalize();
}

// Function to convert and print a matrix in dense form from COO format
void printDenseMatrixFromCOO(
  int rows, int cols, int nnz, int row_indices[], int col_indices[], 
  double values[]
) {
  printf("\n");
  // Initialize a dense matrix with zeros
  double denseMatrix[rows][cols];
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      denseMatrix[i][j] = 0.0;
    }
  }

  // Populate the dense matrix with non-zero values from COO format
  for (int i = 0; i < nnz; i++) {
    int row = row_indices[i];
    int col = col_indices[i];
    double value = values[i];
    denseMatrix[row][col] = value;
  }

  // Print the dense matrix
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        printf("%6.8f ", denseMatrix[i][j]);
    }
    printf("\n");
  }
}


// Function to convert and print a matrix in dense form from CSC format
void printDenseMatrixFromCSC(
  int rows, int cols, int nnz, double values[], int row_indices[], int col_ptr[]
) {
  // Initialize a dense matrix with zeros
  double denseMatrix[rows][cols];
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      denseMatrix[i][j] = 0.0;
    }
  }

  // Populate the dense matrix with non-zero values from CSC format
  for (int j = 0; j < cols; j++) {
    for (int i = col_ptr[j]; i < col_ptr[j+1]; i++) {
        int row = row_indices[i];
        denseMatrix[row][j] = values[i];
    }
  }

  // Print the dense matrix
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        printf("%6.8f ", denseMatrix[i][j]);
    }
    printf("\n");
  }
}