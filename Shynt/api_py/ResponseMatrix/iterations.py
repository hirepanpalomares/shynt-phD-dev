
import numpy as np
import scipy.sparse as sprs
import ctypes
import psutil

import matplotlib.pyplot as plt
import time

from Shynt.api_py.ResponseMatrix.global_problem import solveGlobalProblem_bg
from Shynt.api_py.ResponseMatrix.local_problem import solveLocalProblem_bg
from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix
from Shynt.api_py.ResponseMatrix.build_J_source import buildJsource
from Shynt.api_py.ResponseMatrix.build_matrix_M import (
  getM_matrix,
  getM_matrix_easier,
  get_mM_system
)
from Shynt.api_py.ResponseMatrix.build_matrix_R import (
  getResponseMatrix_byGroup,
  getResponseMatrix_mainNodes
)
from Shynt.api_py.ResponseMatrix.build_matrix_S import (
  getMatrixS_system_byGroup,
  getMatrixS_mainNodes
)
from Shynt.api_py.ResponseMatrix.build_matrix_T import (
  getMatrixT_system_byGroup,
  getMatrixT_mainNodes
)
from Shynt.api_py.ResponseMatrix.build_matrix_U import (
  getMatrixU_system_byGroup,
  getMatrixU_mainNodes
)
from Shynt.api_py.ResponseMatrix.build_Phi_Source import buildPhiSource
from Shynt.api_py.ResponseMatrix.build_source_Q import SourceQ
# from Shynt.api_py.Probabilities.propagation import propagate_prob_uncertainty

from Shynt.api_py.ResponseMatrix.c_data_structures import (
  MatrixEntry,
  SrcMatrixEntry,
  IcmMatrixes,
  ConvergenceData,
  MeshData,
  TwinSurfaceInfo,
  TwinSurfaceInfoArray,
  CoarseNode,
  OutputData
)

class RmmSolution:

  def __init__(
    self, energy_g, mesh, xs, probabilities
  ):
    self.energy_g = energy_g
    self.mesh = mesh
    self.xs = xs
    self.probabilities = probabilities
    
    self.matrixS_bg = {}
    self.matrixU_bg = {}
    self.matrixT_bg = {}
    self.matrixR_bg = {}
    self.matrixM = []
    self.inverse_IMR_bg = {}
    self.systemSource = {}
    self.fission_source = {}


   
    self.solution_data = {}
    self.computing_time_cpu = 0.0 # Yet to implement
    self.computing_time_wall = 0.0 # Yet to implement

    self.time_elapsed_matrixes = 0.0 
    self.time_elapsed_pow_it = 0.0 


    # Useful mesh information -------------------------------------------------
    self.all_coarse_nodes = mesh.coarse_order
    self.all_regions = mesh.all_regions_order
    self.all_surfaces = mesh.all_surfaces_order

    self.numCoarseNodes = len(self.all_coarse_nodes)
    self.numRegions = len(self.all_regions)
    self.numSurfaces = len(self.all_surfaces)
    print(f"Number of coarse_nodes: {self.numCoarseNodes}")
    print(f"Number of regions: {self.numRegions}")
    print(f"Number of surfaces: {self.numSurfaces}")

 
 
  def build_source(self):
    start = time.time()

    print("Building initial source .......", end='')
    systemSource = SourceQ( 
      # It is initialized by building the scattering matrix and fission matrix 
      # per region in the main nodes
      self.mesh, self.energy_g, self.xs
    ) 
    # fission_source = systemSource.buildFissionSource( # for power iteration
    #   self.mesh, self.probabilities
    # )

    self.systemSource = systemSource
    # self.fission_source = fission_source
    print("OK")
    end = time.time()

    print(f'Built the scattering and fission source in: {end-start} sec.')
    
  
  def power_iteration(self, phi_new, phi_prev, keff_prev, fiss_src):
    """

    Parameters
    ----------

    Returns
    -------

    """
    if isinstance(phi_new, dict) and isinstance(phi_new, dict):
      phi_new = self.create_long_vector_flux(phi_new)
      phi_prev = self.create_long_vector_flux(phi_prev)
    

    vector_prev = []
    vector_new = []

    if fiss_src:
      vector_prev = np.matmul(fiss_src, phi_prev)
      vector_new = np.matmul(fiss_src, phi_new)
    else:
      vector_prev = phi_prev
      vector_new = phi_new

    new_product = np.inner(vector_prev, vector_new)
    prev_product = np.inner(vector_prev, vector_prev)
    
    
    k_new = keff_prev * new_product / prev_product

    return k_new

  def check_power_convergence(
    self, k_prev, k_new, phi_prev, phi_new
  ):
    """
    Function to check the convergence for the power iteration method, it checks
    the convergence in the k_eff, scalar flux, and the neutron currents 
    in-between the coarse nodes.

    For the convergence of neutron flux and neutron current it creates a long
    vector and performs the convergence opperations i.e. (new-prev)/prev and 
    takes the max value of the resultant vector.

    Parameters
    ----------
    k_prev : float

    k_new : float
    
    phi_prev : dict

    phi_new : dict

    jin_prev : dict

    jin_new : dict

    energy_g : int

    Returns
    -------
    k_converge : float

    new_converge.max() : float

    jin_converge.max() : float

    """
    k_converge = abs(abs(k_new) - k_prev)/k_prev

    if isinstance(phi_new, dict) and isinstance(phi_new, dict):
      phi_new = self.create_long_vector_flux(phi_new)
      phi_prev = self.create_long_vector_flux(phi_prev)

    max_phi_new = np.max(phi_new)
    max_phi_prev = np.max(phi_prev)

    phi_converge = (max_phi_new - max_phi_prev) / max_phi_prev

   
    return k_converge, phi_converge.max()

  def create_flux_dictionary_bg(self, phi_long_vector):
    coarse_nodes = self.mesh.coarse_order
    coarse_nodes_regions = self.mesh.coarse_region_rel
    
    # create indexes
    
    indexes = { g: {} for g in range(self.energy_g)}
        
    idx = 0
    for n_id in coarse_nodes:
      regions_node = coarse_nodes_regions[n_id]
      for g in range(self.energy_g):
        for r_id in regions_node:
          indexes[g][r_id] = idx
          idx += 1


    # print(indexes[0])
    phi_bg = {}
    for g in range(self.energy_g):
      # print('g: ', g)
      phi_g_array = []
      for r_id in self.mesh.all_regions_order:
        # print(r_id)
        idx_long = indexes[g][r_id]
        phi_g_array.append(phi_long_vector[idx_long])
      phi_bg[g] = np.array(phi_g_array)
    
    return phi_bg

  def create_long_vector_flux(self, phi, for_output=False):
    """
      Function to create a long flux vector containing the flux for all the 
      regions and all the energy groups. It is arranged in such a way that it 
      can be multiplied by the big fission source block matrix.

      phi = [
        phi_r1_g1 .. phi_r1_G .. phi_r2_g1 .. phi_r2_G .. phi_rI_g1 .. phi_rI_G
      ]

      Parameters
      ----------
      phi : dict

      Returns
      -------
      phi_long : np.array()
    """


    if for_output:
      phi_g = {}
      for g in phi:
        phi_long = np.array([])
        if isinstance(phi[g], dict):
          for nid, phi_g_nid in phi[g].items():
            phi_long = np.concatenate((phi_long, phi_g_nid), axis=0)
        phi_g[g] = phi_long
      return phi_g
    else:
      phi_long = np.array([])
      for g, phi_g in phi.items():
        
        if isinstance(phi[g], dict):
          for nid, phi_g_nid in phi_g.items():
            phi_long = np.concatenate((phi_long, phi_g_nid), axis=0)
        else:
          phi_long = np.concatenate((phi_long, phi_g), axis=0)
      return phi_long

  def plot_matrix_sparsity(self,matrix, name, log_scale=False):
    plt.figure()
    if log_scale:
      log_matrix = np.log10(matrix)
      plt.imshow(log_matrix, interpolation='none', cmap='jet', vmin=0)
    else:
      plt.imshow(matrix, interpolation='none', cmap='jet')
    plt.title(name)
    plt.colorbar()
    plt.savefig(f"{name}.png")

  def run_simplePI_factorized_long_phi_vector(
    self, max_iterations=1000, tolerance=1E-10
  ):
    """
      This method runs the simple problem as two parts:
        
      
    """
    start1 = time.time()
    
    # Initial guesses keff and phi --------------------------------------------


    phi_guess = np.ones(self.numRegions * self.energy_g)
  
    keff_guess = 1
    keff_prev = keff_guess
    phi_prev = phi_guess
    k_converge = 1
    phi_converge = 1
    iteration = 1
    k_array = []
    phi_source_array = []
    
    # input()
    # print(matrixS_bg[0])
    print("Inverting (I - MxR)......")  
    identityMatrix = np.identity(self.numSurfaces*self.energy_g)
    mM_x_mR = np.matmul(self.matrixM_sys, self.matrixR_sys)
    mI_mMxR = identityMatrix -mM_x_mR
    mInverse = None
    try:    
      mInverse = np.linalg.inv(mI_mMxR)
    except np.linalg.LinAlgError:
      mInverse = np.linalg.pinv(mI_mMxR)

    
    print(f'calculating matrix mA ...')
    mSK = np.matmul(self.matrixS_sys, mInverse)
    mSKM = np.matmul(
      mSK, self.matrixM_sys
    )
    mSKMU = np.matmul(mSKM, self.matrixU_sys)
    mA_sys = mSKMU + self.matrixT_sys
    
    identityMatrix2 = np.identity(self.numRegions*self.energy_g)
    print(f'calculating   mAF ...')
    mAF = np.matmul(mA_sys, self.matrixF_sys)

    print(f'calculating   I-AZ ...')
    mAZ = np.matmul(mA_sys, self.matrixZ_sys)
    mI_AZ = identityMatrix2 - mAZ

    print(f'calculating inverse  I-AZ ...')
    mI_AZ_inv = np.linalg.inv(mI_AZ)
    
    
    print(f'calculating matrix  mH ...')
    mH = np.matmul(mI_AZ_inv, mAF)

    

    

    # print(f'calculating inverse  mA ...')
    # mA_inverse = np.linalg.inv(mA_sys)
    
    # print(f'calculating matrix  mG ...')
    # mG = mA_inverse - self.matrixZ_sys

    # print(f'calculating inverse  mG ...')
    # mG_inverse = np.linalg.inv(mG)

    # print(f'calculating matrix  mG_inv x mF ...')
    # mGinv_x_mF = np.matmul(mG_inverse, self.matrixF_sys)

    end1 = time.time()
    print(f'Built G^-1*F in {end1-start1} sec.')

    # print(mA.shape)
    input()
    start2 = time.time()
    while (
      (k_converge >= tolerance or phi_converge >= tolerance) and
      iteration < max_iterations + 1
    ):
      print("-"*50)

      
      
      phi_new = np.matmul(mH,phi_prev) / keff_prev
      # phi_new = phi_new / keff_prev
      
        # print("phi_shape:",phi_g.shape)
     

      # power iteration -----------------------------------------
      keff_new = self.power_iteration(
        phi_new, phi_prev, keff_prev, fiss_src=self.matrixF_sys
      )    
      k_array.append(keff_new)
      phi_source_array.append([])

      
      # check convergence ------------------------------------
      k_converge, phi_converge = self.check_convergence(
        keff_prev, keff_new, phi_prev, phi_new
      )
      print("keff: ", keff_new)
      print(f"keff converge: {k_converge:.8E}")
      print(f"phi converge: {phi_converge:.8E}")
      print(f"convergence tolerance: {tolerance:.8E}")
      print("iteration:", iteration)



      # update for the next iteration ------------------------
      keff_prev = keff_new
      phi_prev = phi_new
      
      iteration += 1

      # return 0

    # j_in_sys = create_long_vector_jin(j_in_new)
    # j_out_sys = np.matmul(np.linalg.inv(matrixM_sys), j_in_sys)
    # phi_uncertainty = propagate_prob_uncertainty(phi_new, mesh_info, energy_g,
    # source_Q_vectors, xs, j_in_sys, prob_sigma)
    # phi_uncertainty = order_flux_output_sys(
    # phi_uncertainty, mesh_info, energy_g)
    # phi_sys = create_long_vector_phi_sys(phi_new)
    # flux_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
    # phi_sys, j_in_sys)
    # current_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
    # phi_sys, j_in_sys)
    
    end2 = time.time()
    print(f'Iterative process took {end2-start2} sec.')

    phi_new_bg = self.create_flux_dictionary_bg(phi_new)
    self.solution_data = {
      "keff": k_array,
      "phi": phi_new_bg,
      "phi_sigma": False,
      "keff_convergence": k_converge,
      "flux_convergence": phi_converge, 
      "iterations": iteration,
      "phi_source": phi_source_array,
      "j_in_sys": {}, #j_in_sys,
      "j_out_sys": {} #j_out_sys
    }
  
  def build_source_allG(self):
    import sys

    start = time.time()
    print("Building initial source .......")
    systemSource = SourceQ( # scattering matrix and fission matrix per region
      self.mesh, self.energy_g, self.xs
    )
    mZ = systemSource.build_big_scatt_matrix_blocks(self.mesh)
    mF = systemSource.build_big_fission_matrix_blocks(self.mesh)
    print(f'  Scattering matrix {mZ.shape} ({sys.getsizeof(mZ)/1e6} MB)')
    print(f'  Fission matrix {mF.shape} ({sys.getsizeof(mF)/1e6} MB)')
    self.matrixF_sys = mF
    self.matrixZ_sys = mZ
    print("OK")
    end = time.time()
    print(f'Built Scattering and Fission source in: {end-start} sec.')


class RmmSolution_inverse_operator(RmmSolution):
  
  def __init__(
    self, energy_g, mesh, xs, probabilities, sparse=False, c_calc=False
  ):
    super().__init__(energy_g, mesh, xs, probabilities)
    self.sparse = sparse
    self.c_calc = c_calc

  def build_matrices(self):
    import sys
   
    start = time.time()
    # BUILDING MATRIXES ------------------------------------------------------
    
    print("Building matrix S .......") # ------------------------------------
    matrixS_bg = getMatrixS_system_byGroup(
      self.mesh, self.energy_g, self.xs, self.probabilities, 
      store_sparse=self.sparse
    )
    print(f' {matrixS_bg[0].shape} ', end='\t')
    if self.sparse:
      print(f'({matrixS_bg[0].data.nbytes*self.energy_g/1e9} GB)')


    print("Building matrix U .......", ) # ------------------------------------
    matrixU_bg = getMatrixU_system_byGroup(
      self.mesh, self.energy_g, self.probabilities, 
      store_sparse=self.sparse
    )
    print(f' {matrixU_bg[0].shape} ', end='\t')
    if self.sparse:
      print(f'({matrixU_bg[0].data.nbytes*self.energy_g/1e9} GB)')
    else:
      print(f' ({sys.getsizeof(matrixU_bg[0])*self.energy_g/1e9} GB)')


    print("Building matrix T .......", ) # ------------------------------------
    matrixT_bg = getMatrixT_system_byGroup(
      self.mesh, self.energy_g, self.xs, self.probabilities, 
      store_sparse=self.sparse
    )
    print(f' {matrixT_bg[0].shape} ', end='\t')
    if self.sparse:
      print(f' ({matrixT_bg[0].data.nbytes*self.energy_g/1e9} GB)')


    print("Building matrix R .......", ) # ------------------------------------
    matrixR_bg = getResponseMatrix_byGroup(
      self.mesh, self.energy_g, self.probabilities, 
      store_sparse=self.sparse
    )
    print(f' {matrixR_bg[0].shape} ', end='\t')
    if self.sparse:
      print(f'({matrixR_bg[0].data.nbytes*self.energy_g/1e9} GB)')
    
    print(f' ({sys.getsizeof(matrixR_bg[0])*self.energy_g/1e9} GB)')


    print("Building matrix M .......", ) # ------------------------------------
    matrixM, twin_surfs = getM_matrix_easier(
      self.mesh, store_sparse=self.sparse
    ) 
    if self.sparse:
      print(f'{matrixM.shape} ({matrixM.data.nbytes*self.energy_g/1e9} GB)')
    else:
      print(f' {matrixM.shape} ({sys.getsizeof(matrixM)/1e9} GB)')


      
    self.matrixR_bg = matrixR_bg
    self.matrixS_bg = matrixS_bg
    self.matrixT_bg = matrixT_bg
    self.matrixU_bg = matrixU_bg
    self.matrixM = matrixM
    

    # Inverting the matrix ----------------------------------------------------
    print("Inverting (I - MxR)......")  
    
    inverse_IMR_bg = self.calculate_inverseIMR(
      matrixM, matrixR_bg, self.energy_g, self.numSurfaces, 
    )
    # self.plot_matrix_sparsity(
    #   inverse_IMR_bg[0]*10**10, 'inverse_g0', log_scale=True
    # )


    # Calculating matrix A ----------------------------------------------------
    self.matrixA_bg = self.calculate_matrixA(
      matrixS_bg, matrixR_bg, 
      inverse_IMR_bg, 
      matrixT_bg, matrixU_bg, 
      matrixM
    )
    
    # self.plot_matrix_sparsity(
    #   self.matrixA_bg[0]*10**10, 'mA_g0', log_scale=True
    # )

    end = time.time()
    self.time_elapsed_matrixes = end-start
    print(f'Built the matrixes in: {end-start} sec.')

  def calculate_inverseIMR_C(
    self, matrixM, matrixR, energy_g, numSurfaces, 
  ):
    """
    Calculates the inverse of the therm (I - MxR) in the response
    matrix method for each energy group

    Parameters
    ----------
    matrixM : np.array()
      Matrix M i.e. topological relation of the surfaces in the global 
      problem
    matrixR : dict
      Response matrix (matrix "R") dictionary where keys are the energy
      groups
    energy_g : int 
      Energy groups
    
    Returns
    -------
    inv : dict
      Dictionary with the inverse of the matrix (I - MxR) where the keys
      are the energy groups
    """
    inv = {}
    mM = matrixM
    identityMatrix = []
    
    mM_row_idxs = matrixM[0]
    mM_col_idxs = matrixM[1]
    mM_values = matrixM[2]
    numValuesM = mM_values.shape[0]
    print(mM_row_idxs.shape)
    print(mM_col_idxs.shape)
    print(mM_values.shape)
    print(numSurfaces)
    print(numValuesM)


    mM_row_idxs_ctype = (ctypes.c_int * numValuesM)(*mM_row_idxs)
    mM_col_idxs_ctype = (ctypes.c_int * numValuesM)(*mM_col_idxs)
    mM_values_ctype = (ctypes.c_double * numValuesM)(*mM_values)

    for g in range(energy_g):
      print(f"energy group {g+1} --------------------------------------------")
      mR_row_idxs = matrixR[g][0]
      mR_col_idxs = matrixR[g][1]
      mR_values = matrixR[g][2]
      numValues_mR = mR_row_idxs.shape[0]
      mR_row_idxs_ctype = (ctypes.c_int * numValues_mR)(*mR_row_idxs)
      mR_col_idxs_ctype = (ctypes.c_int * numValues_mR)(*mR_col_idxs)
      mR_values_ctype = (ctypes.c_double * numValues_mR)(*mR_values)
      print(f"types converted")
      
      c_matrix_lib.calculate_inverse_IMR(
        mM_row_idxs_ctype, mM_col_idxs_ctype, mM_values_ctype,
        mR_row_idxs_ctype, mR_col_idxs_ctype, mR_values_ctype,
        ctypes.c_int(numValuesM), ctypes.c_int(numValues_mR),
        ctypes.c_int(numSurfaces),
      )
      raise SystemExit
      mM_x_mR = []
      mI_MR = []
      inverse = []
      Hej,



      # return 0
      if self.sparse:
        
        # mM_x_mR = mM.dot(matrixR[g])
        # mI_MR = identityMatrix - mM_x_mR 
        # lu = sprs.linalg.splu(mI_MR)
        
        # for n in range(numSurfaces):
        #   sparse_vector_I = sprs.csc_matrix(
        #     ([1],([n], [0])), shape=(numSurfaces,1)
        #   ).toarray()
        #   xn = lu.solve(sparse_vector_I)
        #   print(xn)
        # inverse = mI_MR
        # inverse = sprs.linalg.inv(mI_MR)
        pass
      else:
        mM_x_mR = np.matmul(mM, matrixR[g])
      
        mI_MR = identityMatrix - mM_x_mR 
      
        try:    
          inverse = np.linalg.inv(mI_MR)
        except np.linalg.LinAlgError:
          inverse = np.linalg.pinv(mI_MR)


      # print(inverse)
      inv[g] = inverse
    # print(inv[0])
    return inv
  
  def calculate_inverseIMR(
    self, matrixM, matrixR, energy_g, numSurfaces, 
  ):
    """
    Calculates the inverse of the therm (I - MxR) in the response
    matrix method for each energy group

    Parameters
    ----------
    matrixM : np.array()
      Matrix M i.e. topological relation of the surfaces in the global 
      problem
    matrixR : dict
      Response matrix (matrix "R") dictionary where keys are the energy
      groups
    energy_g : int 
      Energy groups
    
    Returns
    -------
    inv : dict
      Dictionary with the inverse of the matrix (I - MxR) where the keys
      are the energy groups
    """
    inv = {}
    mM = matrixM
    identityMatrix = []
    if self.sparse:
      identityMatrix = sprs.identity(numSurfaces)
    else:
      identityMatrix = np.identity(numSurfaces)  # identity matrix
    np.set_printoptions(threshold=200)
    for g in range(energy_g):
      print(f"energy group {g+1}")
      
      mM_x_mR = []
      mI_MR = []
      inverse = []

      if self.sparse:
        mM_x_mR = mM.dot(matrixR[g])
        mI_MR = identityMatrix - mM_x_mR 
        
        inverse = sprs.linalg.inv(mI_MR)
      else:
        mM_x_mR = np.matmul(mM, matrixR[g])
        # self.plot_matrix_sparsity(mM_x_mR, 'mM_x_mR')
        mI_MR = identityMatrix - mM_x_mR 
        # self.plot_matrix_sparsity(mI_MR, 'I - MR')
        print("nnz MR", np.count_nonzero(mM_x_mR))
        print("nnz I-MR", np.count_nonzero(mI_MR))
        try:    
          inverse = np.linalg.inv(mI_MR)
        except np.linalg.LinAlgError:
          inverse = np.linalg.pinv(mI_MR)
        


      print(inverse)
      print("nnz inv(I-MR)", np.count_nonzero(inverse))
      inv[g] = inverse
    # print(inv[0])
    return inv

  def calculate_matrixA(
    self, matrixS_bg, matrixR_bg, 
    inverse_IMR_bg, 
    matrixT_bg, matrixU_bg, 
    matrixM
  ):
    mA_bg = {}
    for g in range(self.energy_g):

      print(f'calculating matrix A (g={g}) --- CPU utilization: {psutil.cpu_percent()}%')
      
      if self.sparse:
        mSK = matrixS_bg[g].dot(inverse_IMR_bg[g])
        mSKM = mSK.dot(matrixM)
        mSKMU = mSKM.dot(matrixU_bg[g])
        mA = mSKMU + matrixT_bg[g]
        mA_bg[g] = mA

      else:
        mSK = np.matmul(matrixS_bg[g], inverse_IMR_bg[g])
        mSKM = np.matmul(
          mSK, matrixM
        )
        mSKMU = np.matmul(mSKM, matrixU_bg[g])
        mA = mSKMU + matrixT_bg[g]
        mA_bg[g] = mA

      del mSK
      del mSKMU
      del (
        # matrixS_bg[g], 
        # matrixR_bg[g], 
        #inverse_IMR_bg[g], 
        # matrixT_bg[g], 
        # matrixU_bg[g]
      )
      # print(mA.shape)
    return mA_bg
  
  def run_simplePI_factorized_bg(
    self, max_iterations=1000, tolerance=1E-10
  ):
    
    """
      This method runs the simple problem as two parts:
        1. Calculate matrix A
        2. Calculate Phi
      
    """
    
    # Initial guesses keff and phi --------------------------------------------
    phi_guess = {g: np.ones(self.numRegions) for g in range(self.energy_g)}
    j_in_prev = {g: np.ones(self.numSurfaces) for g in range(self.energy_g)}
    keff_guess = 1
    keff_prev = keff_guess
    phi_prev = phi_guess
    k_converge = 1
    phi_converge = 1
    iteration = 1
    k_array = []
    phi_source_array = []
    
    # input()
    start2 = time.time()

    while (
      (k_converge >= tolerance or phi_converge >= tolerance) and
      iteration < max_iterations + 1
    ):
      print("-"*50)
      
      # Estimating the Source --------------------------------
      print("Estimating source ...")
      source_Q_vectors = self.systemSource.calculate_Qvector(
        keff_prev, phi_prev, self.all_regions, self.numRegions, 
        fluxOrdered_bg=True
      )
      # print(source_Q_vectors[1].shape)
      
      
      phi_new = {}
      for g in range(self.energy_g):
        if self.sparse:
          phi_g = self.matrixA_bg[g].dot(source_Q_vectors[g])
        else:
          phi_g = np.matmul(self.matrixA_bg[g],source_Q_vectors[g])
        # print(phi_g)
        phi_new[g] = phi_g
        # print("phi_shape:",phi_g.shape)
      print(phi_new[0][:5])
      print(phi_new[0][-5:])

      # power iteration -----------------------------------------
      keff_new = self.power_iteration(
        phi_new, phi_prev, keff_prev, fiss_src=self.fission_source
      )    
      k_array.append(keff_new)
      phi_source_array.append([])

      
      # check convergence ------------------------------------
      k_converge, phi_converge = self.check_power_convergence(
        keff_prev, keff_new, phi_prev, phi_new
      )
      print("keff: ", keff_new)
      print(f"keff converge: {k_converge:.8E}")
      print(f"phi converge: {phi_converge:.8E}")
      print(f"convergence tolerance: {tolerance:.8E}")
      print("iteration:", iteration)



      # update for the next iteration ------------------------
      keff_prev = keff_new
      phi_prev = phi_new
      
      iteration += 1

      
      
    end2 = time.time()
    self.time_elapsed_pow_it = end2 - start2
    print(f'Iterative method completed in {end2 - start2} sec')
    
    self.solution_data = {
      "keff": k_array,
      "phi": phi_new,
      "phi_sigma": False,
      "keff_convergence": k_converge,
      "flux_convergence": phi_converge, 
      "iterations": iteration,
      "phi_source": phi_source_array,
      'time_matrixes': self.time_elapsed_matrixes,
      'time_iterations': self.time_elapsed_pow_it,
      "j_in_sys": {}, #j_in_sys,
      "j_out_sys": {} #j_out_sys
    }
    return k_array, phi_new
  
  def run_chevyshev_PI_factorized_bg(
    self, max_iterations=1000, tolerance=1E-10
  ):
    
    """
      This method runs the simple problem as two parts:
        1. Calculate matrix A
        2. Calculate Phi
      
    """
    start = time.time()
    
    
    # input()
    # print(matrixS_bg[0])

    mA_bg = {}
    for g in range(self.energy_g):
      print(f'calculating matrix A (g={g})')
      mSK = np.matmul(self.matrixS_bg[g], self.inverse_IMR_bg[g])
      mSKM = np.matmul(
        mSK, self.matrixM
      )
      mSKMU = np.matmul(mSKM, self.matrixU_bg[g])
      mA = mSKMU + self.matrixT_bg[g]
      mA_bg[g] = mA
      # print(mA.shape)

    end = time.time()
    print(f'Built dictionary of mA_g in {end-start} sec.')

    # iiii = input('Press enter to continue')
    start2 = time.time()
    # Initial guesses keff and phi --------------------------------------------
    phi_guess = {g: np.ones(self.numRegions) for g in range(self.energy_g)}
    j_in_prev = {g: np.ones(self.numSurfaces) for g in range(self.energy_g)}
    keff_guess = 1
    keff_prev = keff_guess
    phi_prev = phi_guess
    k_converge = 1
    phi_converge = 1
    iteration = 1
    k_array = [keff_guess]
    phi_source_array = []
    phi_array= [phi_guess] # it saves all the phi_vectors from the iteration
    epsilon_array = [k_converge]
    dr_prev = 0
    dr_new = 1
    iteration_acceleration = 0
    alpha = 1
    beta = 0 
    chev_prev = 1
    chev_prev_prev = 1
    chev_new = 1
    acceleration = False
    while (
      (k_converge >= tolerance or phi_converge >= tolerance) and
      iteration < max_iterations + 1
    ):
      print("-"*50)
      # Estimating the Source --------------------------------
      print("Estimating source ...")
      source_Q_vectors = self.systemSource.calculate_Qvector(
        keff_prev, phi_prev, self.all_regions, self.numRegions, 
        fluxOrdered_bg=True
      )
      
      
      phi_new = {}

      if dr_new < 1 and abs(dr_new-dr_prev) < 0.01 or acceleration:
        # Acceleration
        acceleration = True
        print('Acceleration iteration:', iteration_acceleration)
        print('Dominance ratio', dr_new - dr_prev)
        dr_new = 0.8
        gamma_0 = 2/dr_new - 1
        print('Gamma_0', gamma_0)

        if iteration_acceleration == 1:
          print('hello acc1')
          chev_new = gamma_0
          alpha = 4*chev_prev/(dr_new*chev_new)
        elif iteration_acceleration >= 2:
          chev_new = 2*gamma_0*chev_prev - chev_prev_prev
          beta = chev_prev_prev / chev_new
          alpha = 4*chev_prev/(dr_new*chev_new)

        print('chev_prev:', chev_prev)
        print('chev_new:', chev_new)

        print('alpha:', alpha)
        print('beta:', beta)
        # Calculation of the flux ----------------------------------
        for g in range(self.energy_g):
          phi_AQ = np.matmul(mA_bg[g],source_Q_vectors[g])
          phi_g = alpha * phi_AQ + (1 - alpha + beta)*phi_array[-1][g] - beta*phi_array[-2][g]
          phi_new[g] = phi_g
        
        chev_prev_prev = chev_prev
        chev_prev = chev_new
        iteration_acceleration += 1

        # input()
      else:
        # Calculation of the flux ----------------------------------
        for g in range(self.energy_g):
          phi_g = np.matmul(mA_bg[g],source_Q_vectors[g])
          phi_new[g] = phi_g
          # print("phi_shape:",phi_g.shape)
        

     



      # power iteration -----------------------------------------
      keff_new = self.power_iteration(
        phi_new, phi_prev, keff_prev, fiss_src=self.fission_source
      )    
      k_array.append(keff_new)
      phi_array.append(phi_new)
      phi_source_array.append([])

      
      # check convergence ------------------------------------
      k_converge, phi_converge = self.check_convergence(
        keff_prev, keff_new, phi_prev, phi_new
      )
      epsilon_array.append(k_converge)

      if iteration > 3:
        dr_prev = epsilon_array[-2]/epsilon_array[-3]
        dr_new = epsilon_array[-1]/epsilon_array[-2]
      print("keff: ", keff_new)
      print(f"keff converge: {k_converge:.8E}")
      print(f"phi converge: {phi_converge:.8E}")
      print(f"convergence tolerance: {tolerance:.8E}")
      print(f'Dominance ratio: {epsilon_array[-1]/epsilon_array[-2]}')
      print("iteration:", iteration)



      # update for the next iteration ------------------------
      keff_prev = keff_new
      phi_prev = phi_new
      
      iteration += 1

      # return 0

    # j_in_sys = create_long_vector_jin(j_in_new)
    # j_out_sys = np.matmul(np.linalg.inv(matrixM_sys), j_in_sys)
    # phi_uncertainty = propagate_prob_uncertainty(phi_new, mesh_info, energy_g,
    # source_Q_vectors, xs, j_in_sys, prob_sigma)
    # phi_uncertainty = order_flux_output_sys(
    # phi_uncertainty, mesh_info, energy_g)
    # phi_sys = create_long_vector_phi_sys(phi_new)
    # flux_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
    # phi_sys, j_in_sys)
    # current_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
    # phi_sys, j_in_sys)
      
    end2 = time.time()
    print(f'Iterative method completed in {end2-start2} sec')
    
    self.solution_data = {
      "keff": k_array,
      "phi": phi_new,
      "phi_sigma": False,
      "keff_convergence": k_converge,
      "flux_convergence": phi_converge, 
      "iterations": iteration,
      "phi_source": phi_source_array,
      "j_in_sys": {}, #j_in_sys,
      "j_out_sys": {} #j_out_sys
    }
    
  def run_simplePI_bg(
    self, max_iterations=1000, tolerance=1E-10
  ):
    """
      This method runs the simple problem as two parts:
        1. Calculate Jin
        2. Calculate Phi
      
    """
    # Initial guesses keff and phi --------------------------------------------
    phi_guess = {g: np.ones(self.numRegions) for g in range(self.energy_g)}
    j_in_prev = {g: np.ones(self.numSurfaces) for g in range(self.energy_g)}
    keff_guess = 1
    keff_prev = keff_guess
    phi_prev = phi_guess
    tolerance = 1E-10
    k_converge = 1
    phi_converge = 1
    iteration = 1
    k_array = []
    phi_source_array = []
    
    # input()
    # print(matrixS_bg[0])
    while (
      (k_converge >= tolerance or phi_converge >= tolerance) and
      iteration < self.max_iterations + 1
    ):
      print("-"*50)

      # Estimating the Source --------------------------------
      print("Estimating source ...")
      source_Q_vectors = self.systemSource.calculate_Qvector(
        keff_prev, phi_prev, self.all_regions, self.numRegions, 
        fluxOrdered_bg=True
      )

      print("Estimating J source ...")
      j_source = buildJsource(self.matrixU_bg, source_Q_vectors, self.energy_g)
      print("Estimating Phi source ...")
      phi_source = buildPhiSource(
        self.matrixT_bg, source_Q_vectors, self.energy_g
      )

      # Solving the Global problem------------------------------
      print("Solving Global Problem ...")
      j_in_new = solveGlobalProblem_bg(
        self.energy_g, self.inverse_IMR_bg, self.matrixM, j_source
      )
      # Solving local problem: ---------------------------------
      print("Solving Local Problem ...")
      phi_new = solveLocalProblem_bg(
        self.matrixS_bg, j_in_new, phi_source, self.energy_g
      )

      # power iteration -----------------------------------------
      keff_new = self.power_iteration(
        phi_new, phi_prev, keff_prev, self.fission_source
      )    
      k_array.append(keff_new)
      phi_source_array.append(phi_source)

      # check convergence ------------------------------------
      k_converge, phi_converge, j_in_converge = self.check_convergence(
        keff_prev, keff_new, phi_prev, phi_new, jin_prev=j_in_prev, 
        jin_new=j_in_new
      )
      print("keff: ", keff_new)
      print(f"keff converge: {k_converge:.8E}")
      print(f"phi converge: {phi_converge:.8E}")
      print(f"j_in converge: {j_in_converge:.8E}")
      print(f"convergence tolerance: {tolerance:.8E}")
      print("iteration:", iteration)



      # update for the next iteration ------------------------
      keff_prev = keff_new
      phi_prev = phi_new
      j_in_prev = j_in_new
      iteration += 1


    # j_in_sys = create_long_vector_jin(j_in_new)
    # j_out_sys = np.matmul(np.linalg.inv(matrixM_sys), j_in_sys)
    # phi_uncertainty = propagate_prob_uncertainty(phi_new, mesh_info, energy_g,
    # source_Q_vectors, xs, j_in_sys, prob_sigma)
    # phi_uncertainty = order_flux_output_sys(
    # phi_uncertainty, mesh_info, energy_g)
    # phi_sys = self.create_long_vector_phi_sys(phi_new)
    # flux_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
    # phi_sys, j_in_sys)
    # current_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
    # phi_sys, j_in_sys)
    
    self.solution_data = {
      "keff": k_array,
      "phi": phi_new,
      "phi_sigma": False,
      "keff_convergence": k_converge,
      "flux_convergence": phi_converge, 
      "iterations": iteration,
      "phi_source": phi_source_array,
      "j_in_sys": {}, #j_in_sys,
      "j_out_sys": {} #j_out_sys
    }
    
  
class RmmSolution_transport_sweep(RmmSolution):

  def __init__(
    self, energy_g, mesh, xs, probabilities, c_calc=False, parallel=False,
    c_lib_path=''
  ):
    super().__init__(energy_g, mesh, xs, probabilities)
    self.c_calc = c_calc
    self.parallel = parallel
    self.c_lib = None
    
    if parallel and c_calc:
      print(c_lib_path)
      if c_lib_path == '':
        c_lib_path = '/home/hirepan/Documents/chalmers/Project/codes/Shynt'
        c_lib_path += '/repo/Shynt/src_cpp/icm_iterations_parallel.so'
      print("Parallel calculation in  C")
      # Load the shared library
      self.c_lib = ctypes.CDLL(c_lib_path)
      self.c_lib.power_iteration_with_transport_sweep.argtypes = (
        ctypes.Structure, ctypes.Structure,  ctypes.Structure, ctypes.c_int
      )
      self.c_lib.power_iteration_with_transport_sweep.restype = OutputData
    else:
      if c_lib_path == '':
        c_lib_path = '/home/hirepan/Documents/chalmers/Project/codes/Shynt'
        c_lib_path += '/repo/Shynt/src_cpp/icm_iterations.so'
      # Load the shared library
      self.c_lib = ctypes.CDLL(c_lib_path)
      self.c_lib.power_iteration_with_transport_sweep.argtypes = (
        ctypes.Structure, ctypes.Structure,  ctypes.Structure
      )
      self.c_lib.power_iteration_with_transport_sweep.restype = OutputData
    
    self.nuFiss_main_reg = None
    self.fission_src = None
    self.scattering_src = None
    self.matrixR_mn_ctype = None
    self.matrixS_mn_ctype = None
    self.matrixT_mn_ctype = None
    self.matrixU_mn_ctype = None

    self.matrixR_mainNodes = None
    self.matrixS_mainNodes = None
    self.matrixT_mainNodes = None
    self.matrixU_mainNodes = None

  def build_matrices(self):
  
    start = time.time()
    # BUILDING MATRIXES ------------------------------------------------------
    print("Building matrix R .......", )
    matrixR_bg_mainNodes = getResponseMatrix_mainNodes(
      self.mesh, self.energy_g, self.probabilities
    )
    print("Building matrix S .......")
    matrixS_bg_mainNodes = getMatrixS_mainNodes(
      self.mesh, self.energy_g, self.xs, self.probabilities
    )
    print("Building matrix T .......", )
    matrixT_bg_mainNodes = getMatrixT_mainNodes(
      self.mesh, self.energy_g, self.xs, self.probabilities
    )
    print("Building matrix U .......", )
    matrixU_bg_mainNodes = getMatrixU_mainNodes(
      self.mesh, self.energy_g, self.probabilities
    )
    

    self.matrixR_mainNodes = matrixR_bg_mainNodes
    self.matrixS_mainNodes = matrixS_bg_mainNodes
    self.matrixT_mainNodes = matrixT_bg_mainNodes
    self.matrixU_mainNodes = matrixU_bg_mainNodes

    if self.c_calc:
      self.matrixR_mn_ctype = self.convert_matrix_bg_to_ctypes(
        matrixR_bg_mainNodes
      )
      self.matrixS_mn_ctype = self.convert_matrix_bg_to_ctypes(
        matrixS_bg_mainNodes
      )
      self.matrixT_mn_ctype = self.convert_matrix_bg_to_ctypes(
        matrixT_bg_mainNodes
      )
      self.matrixU_mn_ctype = self.convert_matrix_bg_to_ctypes(
        matrixU_bg_mainNodes
      )
    
    end = time.time()
    self.time_elapsed_matrixes = end-start
    print(f'Built the matrixes in: {end-start} sec.')


  def build_source(self):
    start = time.time()

    print("Building initial source .......", end='')
    systemSource = SourceQ( 
      # It is initialized by building the scattering matrix and fission matrix 
      # per region in the main nodes
      self.mesh, self.energy_g, self.xs
    ) 
    self.systemSource = systemSource

    self.fission_src, self.nuFiss_main_reg = self.convert_src_matrixes_to_ctypes(
      systemSource.fissionMatrix
    )
    self.scattering_src, self.nuFiss_main_reg = self.convert_src_matrixes_to_ctypes(
      systemSource.scatteringMatrix
    )
    print(self.fission_src)
    print("OK")
    end = time.time()
    print(f'Built the scattering and fission source in: {end-start} sec.')
  
  def parse_data_to_ctypes(self):
    self.icm_matrixes_ctypes = IcmMatrixes(
      self.matrixR_mn_ctype, 
      self.matrixS_mn_ctype, 
      self.matrixT_mn_ctype, 
      self.matrixU_mn_ctype, 

      self.fission_src, 
      self.scattering_src,

      self.nuFiss_main_reg
    )
    # ------------------------------------------------------------------
    
    
    # ------------------------------------------------------------------
    self.mesh_data_ctypes = self.convert_mesh_data_for_c_api()
    
  
  def run_simplePI_transport_sweep_bg_cCalc(
    self, max_iterations=1000, tolerance=1E-10, omp=1
  ):
    convergence_ctypes = ConvergenceData(
      ctypes.c_int(max_iterations), ctypes.c_double(tolerance),
      ctypes.c_int(self.energy_g)
    )
    # return 0
    output = None
    if self.parallel:
      print("Num coarse nodes from python: ", self.mesh_data_ctypes.numCoarseNodes)
      output = self.c_lib.power_iteration_with_transport_sweep(
        self.icm_matrixes_ctypes, 
        convergence_ctypes, 
        self.mesh_data_ctypes, 
        ctypes.c_int(omp)
      )
    else:
      output = self.c_lib.power_iteration_with_transport_sweep(
        self.icm_matrixes_ctypes, 
        convergence_ctypes, 
        self.mesh_data_ctypes
      )
    # ------------------------------------------------------------------
    keff_array = np.ctypeslib.as_array(output.keff, shape=(max_iterations,))
    tr_iter = np.ctypeslib.as_array(output.transport_iterations, shape=((max_iterations,self.energy_g))) 
    phi_np = np.ctypeslib.as_array(output.phi, shape=(self.energy_g*self.numRegions,))
    phi_np = phi_np.reshape((self.energy_g,self.numRegions))

    jin_np = np.ctypeslib.as_array(output.jin, shape=(self.energy_g*self.numSurfaces,))
    jin_np = jin_np.reshape((self.energy_g,self.numSurfaces))
    jout_np = np.ctypeslib.as_array(output.jout, shape=(self.energy_g*self.numSurfaces,))
    jout_np = jout_np.reshape((self.energy_g,self.numSurfaces))

    phi_convergence = np.ctypeslib.as_array(output.phi_convergence, shape=((max_iterations,self.energy_g)))
    # phi_convergence = phi_convergence.reshape((self.energy_g,self.numRegions))

    self.solution_data = {
      "keff": keff_array,                # double *
      "phi":  phi_np,                    # double *
      "phi_convergence": phi_convergence,
      "transport_iterations": tr_iter,   # double *
      "keff_convergence": output.keff_convergence,
      "iterations": output.power_iterations,
      'time_matrixes': self.time_elapsed_matrixes,
      'time_iterations': output.time_iterations, 
      "omp": omp,
      "phi_sigma": False,                        
      "phi_source": False,                       
      "jin": jin_np,                            
      "jout": jout_np                            
    }

  def run_simplePI_transport_sweep_bg(
    self, max_iterations=1000, tolerance=1E-10
  ):
    import copy
    phi_prev = {
      g: {
        nid : np.ones(
          len(c_node.fine_mesh.regions)
        ) for nid, c_node in self.mesh.coarse_mesh.coarse_nodes.items()
      } for g in range(self.energy_g)
    }
    phi_new = {
      g: {
        nid : np.ones(
          len(c_node.fine_mesh.regions)
        ) for nid, c_node in self.mesh.coarse_mesh.coarse_nodes.items()
      } for g in range(self.energy_g)
    }

    keff_prev = 1

    print("Calculating transfer indexes for Jin ... ", end='')
    j_transfer_idxs = self.calculate_transfer_idxs()
    print("Completed")
    k_converge = 1
    phi_converge = 1
    iteration = 1
    k_array = []
    phi_source_array = []
    
    # input()
    start2 = time.time()
    iterations_info = open("iter_info.txt", 'w')

    while (
      (k_converge >= tolerance or phi_converge >= tolerance) and
      iteration < max_iterations + 1
    ):
      print("-"*50)
      j_converge = 1
      ji_prev = {
        g: {
          nid : np.ones(
            len(c_node.surfaces)
          ) for nid, c_node in self.mesh.coarse_mesh.coarse_nodes.items()
        } for g in range(self.energy_g)
      }
      ji_new = {
        g: {
          nid : np.ones(
            len(c_node.surfaces)
          ) for nid, c_node in self.mesh.coarse_mesh.coarse_nodes.items()
        } for g in range(self.energy_g)
      }
      jo_prev = {
        g: {
          nid : np.ones(
            len(c_node.surfaces)
          ) for nid, c_node in self.mesh.coarse_mesh.coarse_nodes.items()
        } for g in range(self.energy_g)
      }
      transport_iter = 1

      print("Beggining transport iterations ...")
      while j_converge >= tolerance:
        # print(f"{transport_iter},", end='')
        if transport_iter < 5:
          self.print_jin_or_phi(
            phi_new, f"tr{transport_iter}_power{iteration}_phi_new_py.txt", 1
          )
          self.print_jin_or_phi(
            jo_prev, f"tr{transport_iter}_power{iteration}_jout_prev_py.txt", 1
          )
          self.print_jin_or_phi(
            ji_new, f"tr{transport_iter}_power{iteration}_jin_new_py.txt", 1
          )

        for g in range(self.energy_g):
          for nid, c_node in self.mesh.coarse_mesh.coarse_nodes.items():
            eq_node = self.mesh.coarse_mesh.equivalent_nodes_rel[nid]
            regions_node = c_node.fine_mesh.regions

            # calculate phi_node_new
            mS = self.matrixS_mainNodes[g][eq_node]
            mT = self.matrixT_mainNodes[g][eq_node]
            qsrc_prev = self.systemSource.calculate_Qvector_node(
              keff_prev, phi_prev, regions_node, g, nid
            )
            
            phi_new[g][nid] = np.matmul(
              mS, ji_prev[g][nid]
            ) + np.matmul(mT, qsrc_prev)
            
            # ---- update currents -----
            mR = self.matrixR_mainNodes[g][eq_node]
            mU = self.matrixU_mainNodes[g][eq_node]
            
            jo_prev[g][nid] = np.matmul(
              mR, ji_prev[g][nid]
            ) + np.matmul(mU, qsrc_prev)
          # print(phi_new[g][2])
          
          # transfer jin  -------------------------------------------------
          for nid, c_node in self.mesh.coarse_mesh.coarse_nodes.items():
            
            surfaces_n = list(c_node.surfaces.keys())
            for sidx, sid in enumerate(surfaces_n):
              transfer_node, transfer_sidx = j_transfer_idxs[nid][sidx]
              ji_new[g][transfer_node][transfer_sidx] = jo_prev[g][nid][sidx]
          
          jout_prev_all = self.create_long_vector_flux(jo_prev[g])
          jin_new_all = self.create_long_vector_flux(ji_new[g])
          phi_new_all  = self.create_long_vector_flux(phi_new[g])
          # print("phi: ", phi_new_all[:4])
          # print("jin: ", jin_new_all[:4])
          # print("Jout ", jo_prev[0][1])
          # print("Jin transfered", ji_new[0][1])
          # return jout_prev_all, jin_new_all
          # break
          # --------------------------------------------------------------
        
      
        # Check J_in convergence:
        # print("ji_prev: ", id(ji_prev[0][1]))
        # print("ji_new : ", ji_new[0][1])

        
        j_converge = self.check_transport_convergence(ji_prev, ji_new)
        # print("j_converge", j_converge)
        ji_prev = copy.deepcopy(ji_new)
        transport_iter += 1
        # if (transport_iter == 4):
        #   break
      # power iteration -----------------------------------------
      if iteration < 5:
        self.print_jin_or_phi(
          ji_new, f'trConverged_power{iteration}_jin_new_py.txt', iteration
        )
        self.print_jin_or_phi(
          phi_new, f'trConverged_power{iteration}_phi_new_py.txt', iteration
        )

      keff_new = self.power_iteration(
        phi_new, phi_prev, keff_prev, fiss_src=self.fission_source
      )   
      
      k_array.append(keff_new)
      phi_source_array.append([])
      
      # check convergence ------------------------------------
      k_converge, phi_converge = self.check_power_convergence(
        keff_prev, keff_new, phi_prev, phi_new
      )
      print(f"keff: {keff_new:.15f}")
      print("# Transport iterations: ", transport_iter)
      print(f"Keff converge: {k_converge:.8E}")
      print(f"Phi converge: {phi_converge:.8E}")
      print(f"Convergence tolerance: {tolerance:.8E}")
      print("Power iteration:", iteration)

      iterations_info.write(f"keff: {keff_new:.15f}\n")
      iterations_info.write(f"# Transport iterations: {transport_iter}\n")
      iterations_info.write(f"Keff converge: {k_converge:.8E}\n")
      iterations_info.write(f"Phi converge: {phi_converge:.8E}\n")
      iterations_info.write(f"Convergence tolerance: {tolerance:.8E}\n")
      iterations_info.write(f"Power iteration: {iteration}\n")
      iterations_info.write("-----------------------------------\n")
      # update for the next iteration ------------------------
      keff_prev = keff_new
      phi_prev = copy.deepcopy(phi_new)
      
      iteration += 1
      # break

    iterations_info.close()
    
    end2 = time.time()
    self.time_elapsed_pow_it = end2 - start2
    print(f'Iterative method completed in {end2 - start2} sec')

    self.solution_data = {
      "keff": k_array,                                                  # double *
      "phi":  self.create_long_vector_flux(phi_new, for_output=True),   # double **

      "phi_sigma": False,                                               # double
      "keff_convergence": k_converge,                                   # double
      "flux_convergence": phi_converge,                                 # double
      "iterations": iteration,                                          # int
      "phi_source": phi_source_array,                                   # double ***
      'time_matrixes': self.time_elapsed_matrixes,                      # double
      'time_iterations': self.time_elapsed_pow_it,                      # double
      "j_in_sys": {},                                                   # double **
      "j_out_sys": {}                                                   # double **
    }
    return k_array, phi_new
       
  def print_jin_or_phi(self, dictionary, name, tr_iter):
    mode_file = 'w'
    # if tr_iter == 1:
    #   mode_file = 'w'
    
    with open(name, mode_file) as file_out:
      file_out.write("------------- Transport iter --------- \n")
      for g in range(self.energy_g):
        for nid, vector in dictionary[g].items():
          for val in vector:
            file_out.write(f"{val:.12f}\n")
    
  def convert_matrix_bg_to_ctypes(self, m_g_node):
    """
      m_g_node --> [energy group][main_node][row][col]

      ---
      Returns
      [main_node][energy group][row][col]
    """
    # mM_row_idxs_ctype = (ctypes.c_int * numValuesM)(*mM_row_idxs)
    # mM_col_idxs_ctype = (ctypes.c_int * numValuesM)(*mM_col_idxs)
    # mM_values_ctype = (ctypes.c_double * numValuesM)(*mM_values)
    
    # allocate matrix 4D

    main_nodes = list(self.mesh.coarse_mesh.equivalent_nodes.keys())
    num_mainNodes = len(main_nodes)

    mainNodesMatrixesArray = MatrixEntry * num_mainNodes

    mainNodes_matrixes = mainNodesMatrixesArray()

    DoublePtr = ctypes.POINTER(ctypes.c_double)
    DoublePtrPtr = ctypes.POINTER(DoublePtr)
    DoublePtrPtrPtr = ctypes.POINTER(DoublePtrPtr)


    for mnid, main_nid in enumerate(main_nodes):

      numRows, numCols = m_g_node[0][main_nid].shape
      # Allocate memory for the 3D array of matrixes per energy group
      # for each main node
      array_3d_ctypes = (DoublePtrPtr * self.energy_g)()
      # print(array_3d_ctypes)
      for g in range(self.energy_g):
        array_3d_ctypes[g] = (DoublePtr * numRows)()

        for row in range(numRows):
          array_3d_ctypes[g][row] = (ctypes.c_double * numCols)()

          for col in range(numCols):
            array_3d_ctypes[g][row][col] = ctypes.c_double(
              m_g_node[g][main_nid][row][col]
            )

      matrixEntry_struct_instance = MatrixEntry()
      matrixEntry_struct_instance.numRows = numRows
      matrixEntry_struct_instance.numCols = numCols
      matrixEntry_struct_instance.matrix = (
        DoublePtrPtr * self.energy_g
      )(*array_3d_ctypes)
      
      mainNodes_matrixes[mnid] = matrixEntry_struct_instance
    
    return mainNodes_matrixes

  def convert_src_matrixes_to_ctypes(self, src_matrx):

    """

      src_matrx  can be either fission or scattering
      each src_mtrx is a dictionary with regions as keys and 
      fission or scattering matrix as values. The size of the
      square matrix is GxG

    """
   
    

    main_regions = list(src_matrx.keys())
    num_mainRegions = len(main_regions)

    mainRegions_SrcMatrixArray = SrcMatrixEntry * num_mainRegions
    mainRegions_src_matrix = mainRegions_SrcMatrixArray()

    DoublePtr = ctypes.POINTER(ctypes.c_double)
    DoublePtrPtr = ctypes.POINTER(DoublePtr)

    nuFiss_array = (DoublePtr * num_mainRegions)()

    for mrid, main_rid in enumerate(main_regions):

      # Allocate memory for the 3D array of matrixes per energy group
      # for each main node
      array_2d_ctypes = (DoublePtr * self.energy_g)()
      # print("asasas", mrid, main_rid)
      # print(self.systemSource.nuSigFiss[main_rid])
      nuFiss_array[mrid] = (ctypes.c_double * self.energy_g)()
      nuFiss_i = self.systemSource.nuSigFiss[main_rid]
      for g in range(self.energy_g):

        nuFiss_array[mrid][g] = nuFiss_i[g]
        
        array_2d_ctypes[g] = (ctypes.c_double * self.energy_g)()
        for gp in range(self.energy_g):
          array_2d_ctypes[g][gp] = ctypes.c_double(
            src_matrx[main_rid][g][gp]
          )
      src_matrixEntry_struct_instance = SrcMatrixEntry(
        self.energy_g, self.energy_g, array_2d_ctypes
      )
      mainRegions_src_matrix[mrid] = src_matrixEntry_struct_instance
    
    return mainRegions_src_matrix, nuFiss_array

  def convert_mesh_data_for_c_api(self):
    coarse_node_list = self.mesh.coarse_order
    
    regions_list = []
    regions_by_coarse = []
    
    main_coarse_nodes = self.mesh.coarse_mesh.main_nodes
    main_surfaces = self.mesh.coarse_mesh.main_surfaces
    main_regions = self.mesh.coarse_mesh.main_regions
    main_regions_vol = self.mesh.coarse_mesh.main_regions_vol
    num_main_coarse_nodes = len(main_coarse_nodes)

    coarse_nodes_main_idx = {
      main_node: midx for midx, main_node in enumerate(main_coarse_nodes)
    }
    surfaces_main_idx = {
      main_surf: ms_idx for ms_idx, main_surf in enumerate(main_surfaces)
    }
    regions_main_idx = {
      main_reg: mr_idx for mr_idx, main_reg in enumerate(main_regions)
    }

    coarse_mesh = self.mesh.coarse_mesh
    coarse_nodes_array = CoarseNode * self.numCoarseNodes

    coarse_nodes = coarse_nodes_array()
    phi_idx = 0
    jin_idx = 0
    self.jin_transfer_idxs = self.calculate_transfer_idxs()
    for cid in coarse_node_list:
      # print(cid)
      eq_node = coarse_mesh.equivalent_nodes_rel[cid]
      eq_node_idx = coarse_nodes_main_idx[eq_node]
      regs_node = list(
        coarse_mesh.coarse_nodes[cid].fine_mesh.regions.keys()
      )
      surfs_node = list(
        coarse_mesh.coarse_nodes[cid].surfaces.keys()
      )
      
      num_regs_node = len(regs_node)
      num_surfs_node = len(surfs_node)

      equivalent_regions = [
        regions_main_idx[coarse_mesh.equivalent_regions[rid]] for rid in regs_node
      ]
      # print(equivalent_regions)
      equivalent_surfaces = [
        surfaces_main_idx[coarse_mesh.equivalent_surfaces[sid]] for sid in surfs_node
      ]
      
      
      # print(regs_node)
      regions_list += regs_node
      regions_by_coarse.append(regs_node)

      # -----------------------------------------------------
      # twins info 
      

      transfer_surfs = self.jin_transfer_idxs[cid]
      twin_data = { }
      for i, tr_data in enumerate(transfer_surfs):
        
        from_surf_idx, tr_nid, tr_sidx, tr_weight = tr_data

        tr_node_surfs = list(coarse_mesh.coarse_nodes[tr_nid].surfaces.keys())
        
        to_surf_id = tr_node_surfs[tr_sidx]
        from_surf_id = surfs_node[from_surf_idx] 
        
        twin_surf_info = TwinSurfaceInfo(
          ctypes.c_int(from_surf_id),
          ctypes.c_int(to_surf_id),
          ctypes.c_int(tr_nid),
          ctypes.c_double(tr_weight)
        )
        if from_surf_idx not in twin_data:
          twin_data[from_surf_idx] = [twin_surf_info]
        else:
          twin_data[from_surf_idx].append(twin_surf_info)

      
      
      for ss, array_of_twins in twin_data.items():
        num_of_twins = len(array_of_twins)
        array = TwinSurfaceInfo * num_of_twins
        array_twins = array()
        for t, twin in enumerate(array_of_twins):
          # print(twin)
          array_twins[t] = twin
        
        twin_surface_info_array = TwinSurfaceInfoArray(
          (TwinSurfaceInfo * num_of_twins)(*array_of_twins),
          ctypes.c_int(num_of_twins)
        )

        twin_data[ss] = twin_surface_info_array

      # print(twin_data)

      twin_surf_info_array_array = TwinSurfaceInfoArray * num_surfs_node
      node_surfs_twin_info = twin_surf_info_array_array()

      for ss, ss_id in enumerate(surfs_node):
        # print(ss_id, twin_data[ss])
        
        node_surfs_twin_info[ss] = twin_data[ss]

      # -----------------------------------------------------

      coarse_node = CoarseNode(
        (ctypes.c_int * num_regs_node)(*regs_node), 
        (ctypes.c_int * num_surfs_node)(*surfs_node), 

        (ctypes.c_int * num_regs_node)(*equivalent_regions),
        (ctypes.c_int * num_surfs_node)(*equivalent_surfaces),
        
        ctypes.c_int(eq_node_idx),

        (TwinSurfaceInfoArray * num_surfs_node)(*node_surfs_twin_info),

        ctypes.c_int(num_regs_node),
        ctypes.c_int(num_surfs_node),
        ctypes.c_int(phi_idx),
        ctypes.c_int(jin_idx),
      )
      coarse_nodes[cid - 1] = coarse_node
      phi_idx += num_regs_node
      jin_idx += num_surfs_node

    main_nodes_array = CoarseNode * num_main_coarse_nodes
    main_nodes = main_nodes_array()
    
    i = 0
    
    for mcid in main_coarse_nodes:
      main_nodes[i] = coarse_nodes[mcid]
      i += 1


    # -------------------------------------------------------------------------

    sys_bc = self.mesh.boundary_bc
    bc = True if sys_bc == "reflective" else False
    mesh_data = MeshData(
      coarse_nodes, # coarse_nodes
      main_nodes, # mainCoarseNodes_array

      (ctypes.c_int * len(main_coarse_nodes))(*main_coarse_nodes), # 
      (ctypes.c_int * len(main_regions))(*main_regions), # 
      (ctypes.c_double * len(main_regions))(*main_regions_vol), # 
      
      (ctypes.c_int * len(main_surfaces))(*main_surfaces), # 

      ctypes.c_int(self.numCoarseNodes), # numCoarseNodes
      ctypes.c_int(self.numSurfaces), # numSurfaces
      ctypes.c_int(self.numRegions), # numRegions
      ctypes.c_int(num_main_coarse_nodes), # numMainNodes
      ctypes.c_bool(bc)
    )

    return mesh_data

  def check_transport_convergence(self, jin_prev, jin_new):
    if isinstance(jin_prev, dict) and isinstance(jin_new, dict):
      jin_new = self.create_long_vector_flux(jin_new)
      jin_prev = self.create_long_vector_flux(jin_prev)
   
    jin_converge = (jin_new - jin_prev) / jin_prev
    jin_converge = np.abs(jin_converge)

    return np.max(jin_converge)
  
  def calculate_transfer_idxs(self):
    surface_twins = self.mesh.coarse_mesh.surface_twins
    coarse_nodes = self.mesh.coarse_mesh.coarse_nodes

    transfer_idxs = {}

    for nid, c_node in coarse_nodes.items():
    
      transfer_idxs[nid] = []
      surfaces_n = list(c_node.surfaces.keys())
      for sidx, s_id in enumerate(surfaces_n):
        twins = surface_twins[s_id]
        # print(twins)
        num_twins = len(twins)

        for twin_info in twins:
          # print(twin_info)
          twin_sid, twin_node, weight = twin_info
          if twin_sid == None: #it means it is a boundary
            # the boundary conditions will be treated in the iterative method 
            # when transfering Jout -> Jin 
            # weight = 1.0 for this case
            transfer_idxs[nid].append((sidx, nid, sidx, 1.0))
            continue

          # look for the index of the twin_sid ---------------------------
          other_node_surfaces = coarse_nodes[twin_node].surfaces
          for other_sid_idx, other_sid in enumerate(other_node_surfaces):
            if other_sid == twin_sid: 
              transfer_idxs[nid].append((sidx, twin_node, other_sid_idx, weight))
              break
        
        # --------------------------------------------------------------

    return transfer_idxs




def flux_eq_proof(probabilities, source, mesh_info, energy_g, xs, flux, j_in):
  left =  []
  right = []
  
  all_regions = mesh_info.all_regions_order
  all_surfaces = mesh_info.all_surfaces_order

  numRegions = len(all_regions)
  numSurfaces = len(all_surfaces)
  for g in range(energy_g):
    vec_left = []
    vec_right = []
    for r, r_i in enumerate(all_regions):
      coarse_node = mesh_info.region_coarse_rel[r_i]
      coarse_node_regions = mesh_info.coarse_region_rel[coarse_node]
      coarse_node_surfaces = mesh_info.coarse_surface_rel[coarse_node]
      vol_i = mesh_info.all_regions_vol[r_i]
      
      index_flx = numRegions * g + r
      flux_val = flux[index_flx]
      left_side = xs[r_i]['total'][g] * vol_i * flux_val
      vec_left.append(left_side)
      right_sum = 0
      for r_j in coarse_node_regions:
        index_j = all_regions.index(r_j)
        vol_j = mesh_info.all_regions_vol[r_j]
        right_sum += probabilities["regions"][r_j]["regions"][r_i][g] \
                     * vol_j * source[g][index_j]
      for s_a in coarse_node_surfaces:
        index_a = all_surfaces.index(s_a)
        index_jin_a = numSurfaces * g + index_a
        right_sum += j_in[index_jin_a] * mesh_info.all_surfaces_area[s_a] \
                     * probabilities["surfaces"][s_a]["regions"][r_i][g]
      vec_right.append(right_sum)
    left.append(vec_left)
    right.append(vec_right)

def current_eq_proof(
  probabilities, source, mesh_info, energy_g, xs, flux, j_in
):
  left =  []
  right = []
  
  all_regions = mesh_info.all_regions_order
  all_surfaces = mesh_info.all_surfaces_order

  numRegions = len(all_regions)
  numSurfaces = len(all_surfaces)
  for g in range(energy_g):
    vec_left = []
    vec_right = []
    for s, s_a in enumerate(all_surfaces):
      coarse_node = 1 # This doesn't apply for bigger systems than a pin
      coarse_node_regions = mesh_info.coarse_region_rel[coarse_node]
      coarse_node_surfaces = mesh_info.coarse_surface_rel[coarse_node]
      area_a = mesh_info.all_surfaces_area[s_a]

      index_a = all_surfaces.index(s_a)
      index_jout_a = numSurfaces * g + index_a
      jout_val = j_in[index_jout_a]

      left_side = jout_val * area_a
      vec_left.append(left_side)
      right_sum = 0
      for r_j in coarse_node_regions:
        index_j = all_regions.index(r_j)
        vol_j = mesh_info.all_regions_vol[r_j]
        right_sum += probabilities["regions"][r_j]["surfaces"][s_a][g] \
                      * vol_j * source[g][index_j]
      for s_b in coarse_node_surfaces:
        index_b = all_surfaces.index(s_b)
        index_jin_b = numSurfaces * g + index_b
        right_sum += j_in[index_jin_b]  \
                      * mesh_info.all_surfaces_area[s_b] \
                      * probabilities["surfaces"][s_a]["surfaces"][s_b][g]
      vec_right.append(right_sum)
    left.append(vec_left)
    right.append(vec_right)

def calculate_inverseIMR(matrixM, matrixR, energy_g, numSurfaces):
  """
  Calculates the inverse of the therm (I - MxR) in the response
  matrix method for each energy group

  Parameters
  ----------
  matrixM : np.array()
    Matrix M i.e. topological relation of the surfaces in the global 
    problem
  matrixR : dict
    Response matrix (matrix "R") dictionary where keys are the energy
    groups
  energy_g : int 
    Energy groups
  
  Returns
  -------
  inv : dict
    Dictionary with the inverse of the matrix (I - MxR) where the keys
    are the energy groups
  """
  inv = {}
  mM = matrixM
  identityMatrix = np.identity(numSurfaces)  # identity matrix
  np.set_printoptions(threshold=200)
  for g in range(energy_g):
    print(f"energy group {g+1}")
    mR = matrixR[g]
    
    mM_x_mR = np.matmul(mM, mR)
    #print(mM_x_mR)

    mI_MR = identityMatrix - mM_x_mR 
    #I_MR = identityMatrix - mR
    #print(mR[:4,:4])
    #print(mR[2280:,2280:])
    # det_IMR = np.linalg.det(mI_MR)
    
    # print(f"determinant = {det_IMR:.8f}")

    try:    
      inverse = np.linalg.inv(mI_MR)
    except np.linalg.LinAlgError:
      inverse = np.linalg.pinv(mI_MR)


    # print(inverse)
    inv[g] = inverse

  return inv

def calculate_inverseIMR_sys(matrixM, matrixR):

  mM = matrixM
  mR = matrixR

  mM_x_mR = np.matmul(mM, mR)
  identityMatrix = np.identity(mM_x_mR.shape[0])
  matrix_to_invert = identityMatrix - mM_x_mR
  inverse = np.linalg.inv(matrix_to_invert)
  inv = inverse
  return inv

def order_flux_output_sys(flux_system, mesh_info, energy_g):
  """This method orders the flux in a dictionary per coarse node
  and per region per energy group

  phi = {
      g0: {
          coarse_id : {
              reg_1: <float_number>,
              reg_2: <float_number>,
              .
              .
              reg_n: <float_number>
          }
      },
      g1: { ... }
      .
      .
      gG: { ... }
  }

  """
  
  all_regions_order = mesh_info.all_regions_order
  coarse_order = mesh_info.coarse_order
  region_coarse_rel = mesh_info.region_coarse_rel
  
  phi_output = {
      g: {
          c_id: {} for c_id in coarse_order
      } for g in range(energy_g)
  }

  numRegions = len(all_regions_order)
  for g in range(energy_g):
      for r in range(numRegions):
          region =  all_regions_order[r]
          coarse_id = region_coarse_rel[region]
          idx = r + numRegions * g
          phi_output[g][coarse_id][region] = flux_system[idx]
  
  return phi_output
    
def checkMatrixM(mM, equivalence):
  indexs = {
    0: 193, 1: 194, 2: 195, 3: 197,
    4: 199, 5: 200, 6: 201, 7: 202,
    8: 205, 9: 206, 10: 207, 11: 208,
    12: 212, 13: 213, 14: 214, 15: 216,
    16: 220, 17: 221, 18: 223,
    19: 225, 20: 226, 21: 227, 22: 228,
    23: 232, 24: 233, 25: 234, 26: 235,
    27: 240, 28: 241, 29: 242, 30: 243,
    31: 248, 32: 249, 33: 250, 34: 251,
    35: 257, 36: 258, 37: 260,
    38: 264, 39: 265, 40: 267, 
    41: 269, 42: 270, 43: 271, 44: 272,
    45: 276, 46: 277, 47: 278, 48: 279,
    49: 284, 50: 285, 51: 286, 52: 287,
    53: 292, 54: 293, 55: 294, 56: 295,
    57: 301, 58: 302, 59: 304,
    60: 307, 61: 308, 62: 309, 63: 311,
    64: 313, 65: 314, 66: 315, 67: 316,
    68: 319, 69: 320, 70: 321, 71: 322,
    72: 326, 73: 327, 74: 328, 75: 330,
  }
  indexs_inv = {
    193: 0, 194: 1, 195: 2, 197: 3,
    199: 4, 200: 5, 201: 6, 202: 7,
    205: 8, 206: 9, 207: 10, 208: 11,
    212: 12, 213: 13, 214: 14, 216: 15,
    220: 16, 221: 17, 223: 18,
    225: 19, 226: 20, 227: 21, 228: 22,
    232: 23, 233: 24, 234: 25, 235: 26,
    240: 27, 241: 28, 242: 29, 243: 30,
    248: 31, 249: 32, 250: 33, 251: 34,
    257: 35, 258: 36, 260: 37,
    264: 38, 265: 39, 267: 40,
    269: 41, 270: 42, 271: 43, 272: 44,
    276: 45, 277: 46, 278: 47, 279: 48,
    284: 49, 285: 50, 286: 51, 287: 52,
    292: 53, 293: 54, 294: 55, 295: 56,
    301: 57, 302: 58, 304: 59,
    307: 60, 308: 61, 309: 62, 311: 63,
    313: 64, 314: 65, 315: 66, 316: 67,
    319: 68, 320: 69, 321: 70, 322: 71,
    326: 72, 327: 73, 328: 74, 330: 75,
  }
  
  for r,row in enumerate(mM):
    numOnes = count_ones_array(row)
    assert len(numOnes) == 1
    one_index = numOnes[0][1]
    s = indexs[r]
    s_eq = equivalence[s]
    s_eq_index = indexs_inv[s_eq]
    assert one_index == s_eq_index

def count_ones_array(array):
  numOnes = []
  for i, num in enumerate(array):
    if num == 1:
      numOnes += [(num, i)]
  return numOnes
    

