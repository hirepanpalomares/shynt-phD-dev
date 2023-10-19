import numpy as np

def solveGlobalProblem_bg(energy_g, inverse_IMR, mM, j_source_byGroup):
  """
  Function that solves the Global problem i.e.the neutron currents exchanged 
  in-between global nodes. 
  
                  Jin = (I - M x R)^-1 x M x J_source

  This gives the solution of the neutron currents by enery group as follows

  J_in = {
    g0: array(numberSurfaces_length),
    g1: array(numberSurfaces_length),
    :
    gG: array(numberSurfaces_length)
  }

  Parameters
  ----------
  energy : int
    Number of energy groups
  inverse_IMR : dict
    (I - M x R)^-1 matrixes of the system by energy_group
  mM : np.array()
    Matrix M of the system
  j_source_by_Group : dict
    Source neutron currents by energy group

  Returns
  -------
  j_in : dict
    Neutron currents in every surface by energy group
  """
  j_in = {}
  for g in range(energy_g):
    j_source = j_source_byGroup[g]
    inverse = inverse_IMR[g]
    inverse_x_mM = np.matmul(inverse, mM)
    j_in_vector = np.matmul(inverse_x_mM, j_source)
    j_in[g] = j_in_vector
  return j_in

def solveGlobalProblem_sys(energy_g, inverse_IMR, mM, j_source):
  inverse_x_mM = np.matmul(inverse_IMR, mM)
  j_in_vector = np.matmul(inverse_x_mM, j_source)

  return j_in_vector