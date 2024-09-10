#ifndef MATRIX_OPERATIONS
#define MATRIX_OPERATIONS

#include <stdlib.h>
#include <stdio.h>

void freeMatrix(int** matrix, int rows);
int** multiplyMatrices(
  int** matrix1, int rows1, int cols1, int** matrix2, int rows2, int cols2
);


void freeMatrix(int** matrix, int rows) {
  for (int i = 0; i < rows; i++) {
      free(matrix[i]);
  }
  free(matrix);
}

void multiplyMatrixVector(
  double** matrix, int rows_mat, int cols_mat, 
  double* vector, int rows_vec, int start_vec,
  double* result
) {
  
  for (int i = 0; i < rows_mat; i++) {
    // printf("i = %i \n", i);
    result[i] = 0.0;
    for (int k = 0; k < cols_mat; k++) {
      // printf("k = %i \n", k);
      
      result[i] += matrix[i][k] * vector[start_vec+k];
    }
  }
}

void sumVectors(
  double* vector1, int rows_vec1, 
  double* vector2, int rows_vec2, 
  double* result, int result_idx
) {
 
  for (int i = 0; i < rows_vec1; i++) {
    result[result_idx + i] = vector1[i] + vector2[i];
  }
  
}

void substractVectors(
  double* vector1, int rows_vec1, int v1_start_idx,
  double* vector2, int rows_vec2, int v2_start_idx,
  double* result, int result_idx
) {
 
  for (int i = 0; i < rows_vec1; i++) {
    result[result_idx + i] = vector1[v1_start_idx + i] - vector2[v2_start_idx + i];
  }
  
}


double vector_norm(double * vector, int rows_vector){
  double norm = 0.0;
  for (int i = 0; i < rows_vector; i++) { 
    norm += vector[i] * vector[i];
  }
  norm = sqrt(norm);

  return norm;
  
}

#endif