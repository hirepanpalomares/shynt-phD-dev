// Function to multiply two sparse matrices in COO format
SparseMatrixCOO multiply_sparse_matrices(
  int *rowA, int *colA, double *valA, int nnzA,
  int *rowB, int *colB, double *valB, int nnzB, int size
) {
    // Estimate the maximum possible number of non-zero elements in the result
    int maxNnzC = nnzA * nnzB;
    
    // Allocate memory for the result matrix in COO format
    SparseMatrixCOO result;
    result.row = (int *)malloc(maxNnzC * sizeof(int));
    result.col = (int *)malloc(maxNnzC * sizeof(int));
    result.val = (double *)malloc(maxNnzC * sizeof(double));
    result.nnz = 0;

    // Temporary storage to accumulate results
    double *tempResult = (double *)calloc(size * size, sizeof(double));

    // Perform multiplication and accumulation
    for (int k = 0; k < nnzA; k++) {
      int i = rowA[k];
      int j = colA[k];
      double a_val = valA[k];

      for (int l = 0; l < nnzB; l++) {
        if (rowB[l] == j) {
          int jB = colB[l];
          double b_val = valB[l];
          tempResult[i * size + jB] += a_val * b_val;
        }
      }
    }

    // Transfer accumulated results to the result matrix in COO format
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        if (tempResult[i * size + j] != 0.0) {
          result.row[result.nnz] = i;
          result.col[result.nnz] = j;
          result.val[result.nnz] = tempResult[i * size + j];
          result.nnz++;
        }
      }
    }

    // Free temporary storage
    free(tempResult);

    return result;
}


SparseMatrixCOO substract_sparse_matrices(
  int *rowA, int *colA, double *valA, int nnzA,
  int *rowB, int *colB, double *valB, int nnzB
) {
  // Estimate the maximum possible number of non-zero elements in the result
  int maxNnzC = nnzA + nnzB;

  // Allocate memory for the result matrix in COO format
  SparseMatrixCOO result;
  result.row = (int *)malloc(maxNnzC * sizeof(int));
  result.col = (int *)malloc(maxNnzC * sizeof(int));
  result.val = (double *)malloc(maxNnzC * sizeof(double));
  result.nnz = 0;

  // Pointers to traverse the input matrices
  int i = 0, j = 0;

  // Merge and substract the non-zero elements
  while (i < nnzA && j < nnzB) {
      if (rowA[i] < rowB[j] || (rowA[i] == rowB[j] && colA[i] < colB[j])) {
          // Element from A goes into result
          result.row[result.nnz] = rowA[i];
          result.col[result.nnz] = colA[i];
          result.val[result.nnz] = valA[i];
          i++;
      } else if (rowA[i] > rowB[j] || (rowA[i] == rowB[j] && colA[i] > colB[j])) {
          // Element from B goes into result
          result.row[result.nnz] = rowB[j];
          result.col[result.nnz] = colB[j];
          result.val[result.nnz] = -1*valB[j];
          j++;
      } else {
          // Elements from A and B are at the same position
          result.row[result.nnz] = rowA[i];
          result.col[result.nnz] = colA[i];
          result.val[result.nnz] = valA[i] - valB[j];
          i++;
          j++;
      }
      result.nnz++;
  }

  // Add remaining elements from A
  while (i < nnzA) {
      result.row[result.nnz] = rowA[i];
      result.col[result.nnz] = colA[i];
      result.val[result.nnz] = valA[i];
      i++;
      result.nnz++;
  }

  // Add remaining elements from B
  while (j < nnzB) {
      result.row[result.nnz] = rowB[j];
      result.col[result.nnz] = colB[j];
      result.val[result.nnz] = valB[j];
      j++;
      result.nnz++;
  }

  return result;
}

SparseMatrixCOO sum_sparse_matrices(
  int *rowA, int *colA, double *valA, int nnzA,
  int *rowB, int *colB, double *valB, int nnzB) {
    // Estimate the maximum possible number of non-zero elements in the result
    int maxNnzC = nnzA + nnzB;

    // Allocate memory for the result matrix in COO format
    SparseMatrixCOO result;
    result.row = (int *)malloc(maxNnzC * sizeof(int));
    result.col = (int *)malloc(maxNnzC * sizeof(int));
    result.val = (double *)malloc(maxNnzC * sizeof(double));
    result.nnz = 0;

    // Pointers to traverse the input matrices
    int i = 0, j = 0;

    // Merge and sum the non-zero elements
    while (i < nnzA && j < nnzB) {
        if (rowA[i] < rowB[j] || (rowA[i] == rowB[j] && colA[i] < colB[j])) {
            // Element from A goes into result
            result.row[result.nnz] = rowA[i];
            result.col[result.nnz] = colA[i];
            result.val[result.nnz] = valA[i];
            i++;
        } else if (rowA[i] > rowB[j] || (rowA[i] == rowB[j] && colA[i] > colB[j])) {
            // Element from B goes into result
            result.row[result.nnz] = rowB[j];
            result.col[result.nnz] = colB[j];
            result.val[result.nnz] = valB[j];
            j++;
        } else {
            // Elements from A and B are at the same position
            result.row[result.nnz] = rowA[i];
            result.col[result.nnz] = colA[i];
            result.val[result.nnz] = valA[i] + valB[j];
            i++;
            j++;
        }
        result.nnz++;
    }

    // Add remaining elements from A
    while (i < nnzA) {
        result.row[result.nnz] = rowA[i];
        result.col[result.nnz] = colA[i];
        result.val[result.nnz] = valA[i];
        i++;
        result.nnz++;
    }

    // Add remaining elements from B
    while (j < nnzB) {
        result.row[result.nnz] = rowB[j];
        result.col[result.nnz] = colB[j];
        result.val[result.nnz] = valB[j];
        j++;
        result.nnz++;
    }

    return result;
}

