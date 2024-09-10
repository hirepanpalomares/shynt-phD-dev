#ifndef DATA_STRUCTS_H
#define DATA_STRUCTS_H

#include <stdlib.h>
#include <stdbool.h>


typedef struct {
  int numRows;
  int numCols;
  double ***matrix;
} MatrixEntry;


typedef struct {
  int numRows;
  int numCols;
  double **matrix;
} SrcMatrixEntry;

typedef struct {
  int from_surf;
  int to_surf;
  int to_node;
  double weight;
} TwinSurfaceInfo;

typedef struct {
  TwinSurfaceInfo *array;
  int twins_number;
} TwinSurfaceInfoArray;

typedef struct {
  int *regions;
  int *surfaces;
  
  int *equivalentRegions;
  int *equivalentSurfaces;

  int equivalent_coarse_node;

  TwinSurfaceInfoArray *twin_surfaces_info;


  int numRegions;
  int numSurfaces;
  int phi_idx;
  int jin_idx;

} CoarseNode;

typedef struct { // [main_node][g][rows][cols]
  MatrixEntry *mR_n; // array of mR for the different nodes 
  MatrixEntry *mS_n;
  MatrixEntry *mT_n;
  MatrixEntry *mU_n;

  SrcMatrixEntry *mFiss_i;
  SrcMatrixEntry *mScat_i;
  double **nuSigFiss_i;
} IcmMatrixes;

typedef struct {
  /* data */
  int max_iterations;
  double tolerance;
  int energyGr;
} ConvergenceData;

typedef struct {
  CoarseNode *coarse_nodes;
  CoarseNode *mainCoarseNodes_array;

  int *mainCoarseNodes;
  int *mainRegions;
  double *mainRegions_volume;

  int *mainSurfaces;

  int numCoarseNodes;
  int numSurfaces;
  int numRegions;
  int numMainNodes;
  bool bc; // reflective = True, void = False
} MeshData;

typedef struct {
  int numValues;
  double *vector;
} IcmOperationEntry;


typedef struct {
  // Vectors with the matrix operation for all the main nodes
  IcmOperationEntry *qsrc;
  IcmOperationEntry *mSJi;
  IcmOperationEntry *mTQ;
  IcmOperationEntry *mRJi;
  IcmOperationEntry *mUQ;
} IcmOperations;

typedef struct {
  // Vectors with the matrix operation for all the main nodes
  double ***qsrc;
  double ***mSJi;
  double ***mTQ;
  double ***mRJi;
  double ***mUQ;
} IcmOperationsParallel;

typedef struct {
  double *keff;
  double keff_convergence;
  double *phi;
  double *phi_convergence;
  int *transport_iterations;
  int power_iterations;
  double time_iterations;
  double *jin;
  double *jout;
} OutputData;
#endif
