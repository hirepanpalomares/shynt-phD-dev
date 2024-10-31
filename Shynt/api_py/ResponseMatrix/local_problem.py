from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix
import numpy as np


def solveLocalProblem_bg(matrixS_n, jin_system, phi_source_n, energy_g):
  """
  Function that solves the Local problem after solving the global problem
  i.e. the neutron currents exchanged in-between global nodes. 
  
                  phi = mS x Jin + phi_source

  This gives the solution of the flux by enery group as follows

  phi = {
    g0: array(numberRegions_length),
    g1: array(numberRegions_length),
    :
    gG: array(numberRegions_length)
  }

  Parameters
  ----------
  matrixS_n : dict
    S matrixes of the system by energy_group
  jin_system : dict
    Neutron in-currents of the system by energy_group
  phi_source_n : dict
    Source of neutron flux by energy group
  energy : int
    Number of energy groups

  Returns
  -------
  phi : dict
    Neutron flux in every region by energy group
  """
  phi = {}
  for g in range(energy_g):
    mS = matrixS_n[g]
    phi_source = phi_source_n[g]
    jin = jin_system[g]
    mS_x_jin = np.matmul(mS, jin)
    local_solution = mS_x_jin + phi_source
    phi[g] = local_solution
  return phi


def solveLocalProblem_sys(matrixS_sys, jin_sys, phi_source_sys):
  """
      
  """
  
  mS_x_jin = np.matmul(matrixS_sys, jin_sys)

  local_solution = mS_x_jin + phi_source_sys
  phi = local_solution
  
  return phi
