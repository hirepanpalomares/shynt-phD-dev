
import numpy as np
import matplotlib.pyplot as plt


from Shynt.api_py.ResponseMatrix.global_problem import solveGlobalProblem_bg
from Shynt.api_py.ResponseMatrix.local_problem import solveLocalProblem_bg
from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix
from Shynt.api_py.ResponseMatrix.build_J_source import buildJsource
from Shynt.api_py.ResponseMatrix.build_matrix_M import (
  getM_matrix,
  getM_matrix_easier
)
from Shynt.api_py.ResponseMatrix.build_matrix_R import (
  getResponseMatrix_byGroup
)
from Shynt.api_py.ResponseMatrix.build_matrix_S import (
  getMatrixS_system_byGroup
)
from Shynt.api_py.ResponseMatrix.build_matrix_T import (
  getMatrixT_system_byGroup
)
from Shynt.api_py.ResponseMatrix.build_matrix_U import (
  getMatrixU_system_byGroup
)
from Shynt.api_py.ResponseMatrix.build_Phi_Source import buildPhiSource
from Shynt.api_py.ResponseMatrix.build_source_Q import SourceQ
from Shynt.api_py.Probabilities.propagation import propagate_prob_uncertainty



def solveKeff_byGroup(root, xs, probabilities, mesh_info, prob_sigma={}):
  """
  It solves the eigenvalue problem using the response matrix method (RMM)

  Parameters
  ----------
  root : Universe
    Root universe where the geometry is stored
  xs : dict
    Dictionary with cross sections for all the regions 
  probabilities : dict
    Dictionary with all the probabilities needed for the RMM
  mesh_info : MeshInfo
    Variable where useful information about the geometry is stored
  prob_sigma : dict, optional
    Dictionary where the uncertainties of the probabilities are stored
  
  Returns
  -------
  solution : dict
    Variable where the solution is stored. Keys of the stored variables are:
      - multiplication fator (keff)
      - escalar flux (phi)
      - escalar flux uncertainty (phi_sigma)
      - final convergence value for the multipication factor and flux 
        (keff_convergence, flux convergence)
      - number of iterations (iterations)
      - source contribution from scalar flux (phi_source)
      - neutron currents in and out from all the surfaces (j_in_sys, j_out_sys)

  """

  energy_g = root.energy_grid.energy_groups
  global_mesh = root.cell.global_mesh

  # Useful mesh information ---------------------------------------------------
  coarse_nodes_ids = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  all_regions = mesh_info.all_regions_order
  all_surfaces = mesh_info.all_surfaces_order
  numRegions = len(all_regions)
  numSurfaces = len(all_surfaces)
  print(f"Number of regions: {numRegions}")
  print(f"Number of surfaces: {numSurfaces}")


  # BUILDING MATRIXES ---------------------------------------------------------
  print("Building matrix S .......", end="")
  matrixS_bg = getMatrixS_system_byGroup(mesh_info, energy_g, xs, probabilities)
  print(matrixS_bg[0].shape)
  print("Building matrix U .......", end="")
  matrixU_bg = getMatrixU_system_byGroup(mesh_info, energy_g, probabilities) 
  print(matrixU_bg[0].shape)
  print("Building matrix T .......", end="")
  matrixT_bg = getMatrixT_system_byGroup(mesh_info, energy_g, xs, probabilities)
  print(matrixT_bg[0].shape)
  print("Building matrix R .......", end="")
  matrixR_bg = getResponseMatrix_byGroup(mesh_info, energy_g, probabilities) 
  print(matrixR_bg[0].shape)
  #print(matrixR_bg[7][:10,:10])
  print("Building matrix M .......", end="")
  matrixM, twin_surfs = getM_matrix_easier(mesh_info)  
  print(matrixM.shape)
  # plotting matrix sparsity --------------------------------------------------
  #plot_matrix_sparsity(matrixR_bg[7], "matrix R")
  #plot_matrix_sparsity(matrixS_bg[7], "matrix S")
  #plot_matrix_sparsity(matrixT_bg[7], "matrix T")
  #plot_matrix_sparsity(matrixU_bg[7], "matrix U")
  #plot_matrix_sparsity(matrixM, "matrix M")
  # plot_matrix_sparsity(fission_source, "fission source")

  #print(matrixM[:8,:8]) ------------------------------------------------------
  # surf_to_check = [0,1,2,3,4,5,6,7,8,9,10,11,83,84,85,86,87,88,89,90]
  # for sid in surf_to_check:
  #   one_idx = find_index_one(matrixM, sid)
  #   print(f"{sid}: {one_idx}")
  # ---------------------------------------------------------------------------

  print("Inverting (I - MxR)......")  
  inverse_IMR_bg = calculate_inverseIMR(matrixM, matrixR_bg, energy_g, numSurfaces)
  print(inverse_IMR_bg[0].shape)
  #raise SystemExit 
  
  # check matrix M ------------------------------------------------------------
  #checkMatrixM(matrixM, twin_surfs)

  # Building the initial source -----------------------------------------------
  print("Building initial source .......")
  systemSource = SourceQ( # scattering matrix and fission matrix per region
    coarse_nodes_ids, coarse_nodes_regions, energy_g, xs
  ) 
  fission_source = systemSource.buildFissionSource( # for power iteration
    coarse_nodes_ids, coarse_nodes_regions, mesh_info.all_regions_vol, 
    probabilities
  )

  
  # Initial guesses keff and phi ----------------------------------------------
  phi_guess = {g: np.ones(numRegions) for g in range(energy_g)}
  j_in_prev = {g: np.ones(numSurfaces) for g in range(energy_g)}
  keff_guess = 1
  keff_prev = keff_guess
  phi_prev = phi_guess
  tolerance = 1E-10
  k_converge = 1
  phi_converge = 1
  iteration = 1
  k_array = []
  phi_source_array = []

  while k_converge >= tolerance or phi_converge >= tolerance:
    print("-"*50)

    # Estimating the Source --------------------------------
    print("Estimating source ...")
    source_Q_vectors = systemSource.calculate_Qvector(
      keff_prev, phi_prev, all_regions, numRegions, fluxOrdered_bg=True
    )

    print("Estimating J source ...")
    j_source = buildJsource(matrixU_bg, source_Q_vectors, energy_g)
    print("Estimating Phi source ...")
    phi_source = buildPhiSource(matrixT_bg, source_Q_vectors, energy_g)
        
    # Solving the Global problem------------------------------
    print("Solving Global Problem ...")
    j_in_new = solveGlobalProblem_bg(
      energy_g, inverse_IMR_bg, matrixM, j_source
    )
    # Solving local problem: ---------------------------------
    print("Solving Local Problem ...")
    phi_new = solveLocalProblem_bg(matrixS_bg, j_in_new, phi_source, energy_g)

    # power iteration -----------------------------------------
    keff_new = power_iteration(
      phi_new, phi_prev, keff_prev, fission_source
    )    
    k_array.append(keff_new)
    phi_source_array.append(phi_source)

    # check convergence ------------------------------------
    k_converge, phi_converge, j_in_converge = check_convergence(
      keff_prev, keff_new, phi_prev, phi_new, j_in_prev, j_in_new, energy_g
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
  # phi_sys = create_long_vector_phi_sys(phi_new)
  # flux_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
  # phi_sys, j_in_sys)
  # current_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, 
  # phi_sys, j_in_sys)
  
  solution = {
    "keff": keff_new,
    "phi": phi_new,
    "phi_sigma": False,
    "keff_convergence": k_converge,
    "flux_convergence": phi_converge, 
    "iterations": iteration,
    "phi_source": phi_source_array,
    "j_in_sys": {}, #j_in_sys,
    "j_out_sys": {} #j_out_sys
  }

  return  solution

def find_index_one(mM,row_idx):
  for idx, val in enumerate(mM[row_idx]):
    if val == 1: return idx


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


def check_convergence(
  k_prev, k_new, phi_prev, phi_new, jin_prev, jin_new, energy_g
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
  k_converge = abs(k_new - k_prev)/k_new

  # max_phi_prev = np.zeros(energy_g)
  # max_phi_new = np.zeros(energy_g)
  # max_jin_prev = np.zeros(energy_g)
  # max_jin_new = np.zeros(energy_g)
  # for g in range(energy_g):
  #   max_phi_new[g] = phi_new[g].max()
  #   max_phi_prev[g] = phi_prev[g].max()
  #   max_jin_new[g] = jin_new[g].max()
  #   max_jin_prev[g] = jin_prev[g].max()
  # phi_converge = abs(max_phi_new - max_phi_prev) / max_phi_new 
  # jin_converge = abs(max_jin_new - max_jin_prev) / max_jin_new 

  phi_new = create_long_vector_flux(phi_new)
  phi_prev = create_long_vector_flux(phi_prev)
  jin_new = create_long_vector_jin(jin_new)
  jin_prev = create_long_vector_jin(jin_prev)
  phi_converge = (phi_new - phi_prev) / phi_prev
  jin_converge = (jin_new - jin_prev) / jin_prev

  return k_converge, phi_converge.max(), jin_converge.max()


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




def power_iteration(phi_new, phi_prev, keff_prev, fission_source):
  """
  
  Parameters
  ----------


  Returns
  -------


  """
    
  phi_new = create_long_vector_flux(phi_new)
  phi_prev = create_long_vector_flux(phi_prev)
  

  vector_prev = np.matmul(fission_source, phi_prev)
  vector_new = np.matmul(fission_source, phi_new)

  new_product = np.inner(vector_prev, vector_new)
  prev_product = np.inner(vector_prev, vector_prev)
  
  k_new = keff_prev * new_product / prev_product

  return k_new


def create_long_vector_flux(phi):
  """
  Function to create a long flux vector containing the flux for all the regions
  and all the energy groups. It is arranged in such a way that it can be multi-
  plied by the big fission source block matrix.

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

  phi_long = np.array([])
  for g, phi_g in phi.items():
    phi_long = np.concatenate((phi_long, phi_g), axis=0)
  return phi_long


def create_long_vector_jin(j_in):
  """
  Function to create a long j_in vector containing the j_in for all the 
  surfaces and all the energy groups. 

  jin = [
    jin_a1_g1 .. jin_a1_G .. jin_a2_g1 .. jin_a2_G .. jin_aA_g1 .. jin_aA_G
  ]

  Parameters
  ----------
  j_in : dict

  Returns
  -------
  jin_long : np.array()

  """

  jin_long = np.array([])
  for g, jin_g in j_in.items():
    jin_long = np.concatenate((jin_long, jin_g), axis=0)
  return jin_long


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
    
    
def plot_matrix_sparsity(matrix, name):
  plt.figure()
  plt.imshow(matrix, interpolation='none', cmap='jet')
  plt.title(name)
  plt.colorbar()
  plt.savefig(f"{name}.png")


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
    

