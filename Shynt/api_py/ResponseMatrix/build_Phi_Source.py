import numpy as np



def buildPhiSource(matrixT, source, energy_g):
  """
  This function calculates the Phi_source vectors for the
  system by energy group

        Phi_source = Tg x Qg

  (numberRegions, numberRegions) x (numberRegions) =  (numberRegions)
        
  
  phi_source = {
    g0: array([Phi_src_i1, Phi_src_i2, ...., Phi_src_iI]),
    g1: array([Phi_src_i1, Phi_src_i2, ...., Phi_src_iI]),
    :
    gG: array([Phi_src_i1, Phi_src_i2, ...., Phi_src_iI]),
  }
        
  Parameters
  ----------
  matrixT : dict
    Matrix T for all the system by energy group, it ahs a shape
    of (numberRegions, numberRegions)
  source : dict
    Source vectors Qg for all the system by energy group, it has 
    a shape of (numberRegions)
  energy_g : int
    Number of energy groups

  Returns
  -------
  phi_source : dict

  """
  phi_source = {}
  for g in range(energy_g):
    mT = matrixT[g]
    q_vector = source[g]
    phi_s = np.matmul(mT, q_vector)
    phi_source[g] = phi_s
    
  return phi_source


def buildPhiSource_sys(matrixT, source, energy_g):
  
  q_sys = []
  for g in range(energy_g):
      for val_ in source[g]:
          q_sys.append(val_)

  q_sys = np.array(q_sys)
  
  phi_source = np.matmul(matrixT, q_sys)

  return phi_source


def buildPhiSourceTBT(energy_g, mesh_info, probabilities, xs, keff, phi):
  phi_source = {}
  
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area
  regions_volume = mesh_info.all_regions_vol

  for g in range(energy_g):
      phi_array = []
      for n_id in coarse_nodes:
          regions_n = coarse_nodes_regions[n_id]
          surfaces_n = coarse_nodes_surfaces[n_id]
          numRegions_n = len(regions_n)
          numSurfaces_n = len(surfaces_n)
  
          # Logic to calculate a term for a surface
          for j in range(numRegions_n):
              reg_j_id = regions_n[j]
              phi_val = 0
              for i in range(numRegions_n):
                  # Calculate Fraction
                  reg_i_id = regions_n[i]
                  vol_i = regions_volume[reg_i_id]
                  p_i_j = probabilities["regions"][reg_i_id]["regions"][reg_j_id][g]
                  xsTot = xs[reg_j_id]["total"][g]
                  vol_j = regions_volume[reg_j_id]

                  frac = (vol_i * p_i_j)/(xsTot * vol_j)

                  # Calculate Q
                  phi_i = 1
                  q_val = calculateQval(energy_g, xs[reg_i_id], keff, g, phi_i)
                  phi_val += frac*q_val
              #append value to array of each energy group
              phi_array.append(phi_val)
      phi_source[g] = phi_array

  return phi_source


def calculateQval(energy_g, xs, keff, g, phi_gp_i):
  q_val = 0
  for gp in range(energy_g):
      scatt_val = xs["scatter"][gp][g]
      fiss_val = xs["nuSigFission"][gp] * xs["chi"][g] / keff
      q_val += (scatt_val + fiss_val)*phi_gp_i

  return q_val

