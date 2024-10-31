
#include <stdio.h>
#include <stdlib.h>

// Define a structure to store the result in COO format
typedef struct {
    int *row;
    int *col;
    double *val;
    int nnz; // number of non-zero elements
} SparseMatrix;

// Function to multiply two sparse matrices in COO format
SparseMatrix multiply_sparse_matrices(
  int *rowA, int *colA, double *valA, int nnzA,
  int *rowB, int *colB, double *valB, int nnzB, int size
) {
    // Estimate the maximum possible number of non-zero elements in the result
    int maxNnzC = nnzA * nnzB;
    
    // Allocate memory for the result matrix in COO format
    SparseMatrix result;
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

// Function to print a sparse matrix in COO format
void print_sparse_matrix(SparseMatrix matrix) {
    printf("row\tcol\tval\n");
    for (int i = 0; i < matrix.nnz; i++) {
        printf("%d\t%d\t%f\n", matrix.row[i], matrix.col[i], matrix.val[i]);
    }
}

// Main function
int main() {
    // Example matrices in COO format
    int rowA[] = {0, 1, 2};
    int colA[] = {0, 1, 2};
    double valA[] = {1.0, 2.0, 3.0};
    int nnzA = 3;

    int rowB[] = {0, 1, 2};
    int colB[] = {0, 1, 2};
    double valB[] = {4.0, 5.0, 6.0};
    int nnzB = 3;

    int size = 3; // Assuming matrices are 3x3

    // Perform sparse matrix multiplication
    SparseMatrix result = multiply_sparse_matrices(
      rowA, colA, valA, nnzA, rowB, colB, valB, nnzB, size
    );

    // Print the result
    print_sparse_matrix(result);

    // Free allocated memory
    free(result.row);
    free(result.col);
    free(result.val);

    return 0;
}
