import ctypes

# C Data structures ----------------------------------------------
class MatrixEntry(ctypes.Structure):
  _fields_ = [
    ("numRows", ctypes.c_int),
    ("numCols", ctypes.c_int),
    (
      "matrix", 
      ctypes.POINTER(
        ctypes.POINTER( 
          ctypes.POINTER(ctypes.c_double) 
        )
      )
    )
  ]

class SrcMatrixEntry(ctypes.Structure):
  _fields_ = [
    ("numRows", ctypes.c_int),
    ("numCols", ctypes.c_int),
    ("matrix", ctypes.POINTER(ctypes.POINTER(ctypes.c_double)))
  ]

class IcmMatrixes(ctypes.Structure):
  _fields_ = [
    ("mR_n", ctypes.POINTER(MatrixEntry)),
    ("mS_n", ctypes.POINTER(MatrixEntry)),
    ("mT_n", ctypes.POINTER(MatrixEntry)),
    ("mU_n", ctypes.POINTER(MatrixEntry)),
    ("mFiss_i", ctypes.POINTER(SrcMatrixEntry)),
    ("mScat_i", ctypes.POINTER(SrcMatrixEntry)),
    ("nuSigFiss_i", ctypes.POINTER(ctypes.POINTER(ctypes.c_double)))
  ]

class ConvergenceData(ctypes.Structure):
  _fields_ = [
    ("max_iterations", ctypes.c_int),
    ("tolerance", ctypes.c_double),
    ("energyGr", ctypes.c_int)
  ]

class TwinSurfaceInfo(ctypes.Structure):
  _fields_ = [
    ("from_surf", ctypes.c_int),
    ("to_surf", ctypes.c_int),
    ("to_node", ctypes.c_int),
    ("weight", ctypes.c_double),
  ]

class TwinSurfaceInfoArray(ctypes.Structure):
  _fields_ = [
    ("array", ctypes.POINTER(TwinSurfaceInfo)),
    ("twins_number", ctypes.c_int)
  ]

class CoarseNode(ctypes.Structure):
  _fields_ = [
    ("regions", ctypes.POINTER(ctypes.c_int)),
    ("surfaces", ctypes.POINTER(ctypes.c_int)),
    
    ("equivalentRegions", ctypes.POINTER(ctypes.c_int)),
    ("equivalentSurfaces", ctypes.POINTER(ctypes.c_int)),
    
    ("equivalent_coarse_node", ctypes.c_int),
    
    ("twin_surfaces_info", ctypes.POINTER(TwinSurfaceInfoArray)),
    
    ("numRegions", ctypes.c_int),
    ("numSurfaces", ctypes.c_int),
    ("phi_idx", ctypes.c_int),
    ("jin_idx", ctypes.c_int),
  ]


class MeshData(ctypes.Structure):
  _fields_ = [
    ("coarse_nodes", ctypes.POINTER(CoarseNode)),
    ("mainCoarseNodes_array", ctypes.POINTER(CoarseNode)),

    ("mainCoarseNodes", ctypes.POINTER(ctypes.c_int)),
    ("mainRegions", ctypes.POINTER(ctypes.c_int)),
    ("mainRegions_volume", ctypes.POINTER(ctypes.c_double)),

    ("mainSurfaces", ctypes.POINTER(ctypes.c_int)),
    

    ("numCoarseNodes", ctypes.c_int),
    ("numSurfaces", ctypes.c_int),
    ("numRegions", ctypes.c_int),
    ("numMainNodes", ctypes.c_int),
    ("bc", ctypes.c_bool)
  ]

class OutputData(ctypes.Structure):
  _fields_ = [
    ("keff", ctypes.POINTER(ctypes.c_double)),
    ("keff_convergence", ctypes.c_double),

    ("phi", ctypes.POINTER(ctypes.c_double)),

    ("phi_convergence", ctypes.POINTER(ctypes.c_double)),

    ("transport_iterations", ctypes.POINTER(ctypes.c_int)),
    ("power_iterations", ctypes.c_int),
    ("time_iterations", ctypes.c_double),
    ("jin", ctypes.POINTER(ctypes.c_double)),
    ("jout", ctypes.POINTER(ctypes.c_double)),
    
    
  ]
# -----------------------------------------------------------------
