from Shynt.api_py.ResponseMatrix.build_matrix_R import get_dR_dPab_system
from Shynt.api_py.ResponseMatrix.build_matrix_U import get_dU_dPij_system
from Shynt.api_py.ResponseMatrix.build_J_source import get_source_sys

from Shynt.api_py.ResponseMatrix.build_matrix_S import getMatrixS_system_wo_prob_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_T import getMatrixT_system_wo_prob_byGroup


import numpy as np


def propagate_prob_uncertainty(phi_new, mesh_info, energy_g, sourceQ, xs, j_in_sys, prob_sigma):
  all_regions = mesh_info.all_regions_order
  all_surfaces = mesh_info.all_surfaces_order
  numRegions = len(all_regions)
  numSurfaces = len(all_surfaces)
  source_sys = get_source_sys(sourceQ)
  mS_byGroup = getMatrixS_system_wo_prob_byGroup(mesh_info, energy_g, xs)
  mT_byGroup = getMatrixT_system_wo_prob_byGroup(mesh_info, energy_g, xs)
  j_byGroup = {}
  for g in range(energy_g):
    j_g = []
    for s in range(numSurfaces):
      index_jin =  numSurfaces * g + s
      j_g.append(j_in_sys[index_jin])
    j_byGroup[g] = np.array(j_g)

  
  
  phi_sigma = []
  for g in range(energy_g):
    mS_x_jin = mS_byGroup[g] * j_byGroup[g]
    mT_x_Q = mT_byGroup[g] * sourceQ[g]

    mS_x_jin_square = np.power(mS_x_jin, 2)
    mT_x_Q_square = np.power(mT_x_Q, 2)
    for r in range(numRegions):
      r_j = all_regions[r]
      sigma_paj = get_sigma_Paj_vector(prob_sigma, mesh_info, g, r_j)
      sigma_pij = get_sigma_Pij_vector(prob_sigma, mesh_info, g, r_j)
      sigma_paj_square = np.power(sigma_paj, 2)
      sigma_pij_square = np.power(sigma_pij, 2)


      term_S = mS_x_jin_square[r] * sigma_paj_square
      term_T = mT_x_Q_square[r] * sigma_pij_square

      sqrt_val = np.sum(term_S) + np.sum(term_T)

      phi_sigma.append(np.sqrt(sqrt_val))




  # dJin_dPba = get_dJin_dPba(mesh_info, energy_g, matrixM, inverse_IMR, matrixU, source_sys)
  # dJin_dPij = get_dJin_dPij(mesh_info, energy_g, inverse_IMR, matrixM, source_sys)
  
  return np.array(phi_sigma)


def get_sigma_Paj_vector(prob_sigma, mesh_info, g, r_j):
  sigma_array = []
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  for c_id in coarse_nodes:
    # for each coarse node
    surfaces_n = coarse_nodes_surfaces[c_id]
    for a in surfaces_n:
      sigma_val = prob_sigma["surfaces"][a]["regions"][r_j][g]
      sigma_array.append(sigma_val)
  return np.array(sigma_array)


def get_sigma_Pij_vector(prob_sigma, mesh_info, g, r_j):
  sigma_array = []
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  for c_id in coarse_nodes:
    # for each coarse node
    regions = coarse_nodes_regions[c_id]
    for r_i in regions:
      sigma_val = prob_sigma["regions"][r_i]["regions"][r_j][g]
      sigma_array.append(sigma_val)
  return np.array(sigma_array)


def get_dJin_dPba(mesh_info, energy_g, matrixM, inverse_IMR, matrixU, sourceQ):
  dR_dPba = get_dR_dPab_system(mesh_info, energy_g)
  inverse_IMR_2 = inverse_IMR * inverse_IMR
  mM_x_dR = np.matmul(matrixM, dR_dPba)
  mult1 = np.matmul(mM_x_dR, inverse_IMR_2)
  mult2 = np.matmul(mult1, matrixM)
  mult3 = np.matmul(mult2, matrixU)

  return np.matmul(mult3, sourceQ)


def get_dJin_dPij(mesh_info, energy_g, inverse_IMR, matrixM, sourceQ):
  dU_dPij = get_dU_dPij_system(mesh_info, energy_g)
  mult1 = np.matmul(inverse_IMR, matrixM)
  mult2 = np.matmul(mult1, dU_dPij)

  return np.matmul(mult2, sourceQ)