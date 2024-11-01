import numpy as np


def buildJsource(matrixU, source, energy_g):
  """
  This function calculates the  Jin_source vectors by energy group

        Jin_source = Ug x Qg

  (numberSurfaces, numberRegions) x (numberRegions) =  (numberSurfaces)
        
  J_in_source = {
    g0: array([Jin_s1, Jin_s2, ...., Jin_sA])
    g1: array([Jin_s1, Jin_s2, ...., Jin_sA])
    ...
    ...
  }
        
  Parameters
  ----------
  matrixU : dict
    Matrix U for all the system by energy group, it ahs a shape
    of (numberSurfaces, numberRegions)
  source : dict
    Source vectors Qg for all the system by energy group, it has 
    a shape of (numberRegions)
  energy_g : int
    Number of energy groups

  Returns
  -------
  j_source : dict

  """

  j_source = {}
  for g in range(energy_g):
    matU = matrixU[g]
    q_vector = source[g]
    j_s_matmul = np.matmul(matU, q_vector)
    j_source[g] = j_s_matmul

  return j_source

def get_source_sys(source):
  q_sys = []
  for g, src_g in source.items():
    for val_ in src_g:
      q_sys.append(val_)

  return np.array(q_sys)


def buildJsource_sys(matrixU, source, energy_g):
  """
    
  """ 
  source_sys = get_source_sys(source)
  j_source_sys = np.matmul(matrixU, source_sys)
  

  return j_source_sys


def buildJsourceTBT(energy_g, mesh_info, probabilities, xs, keff, phi):
  j_source = {}
  
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area
  regions_volume = mesh_info.all_regions_vol

  for g in range(energy_g):
    j_array = []
    for n_id in coarse_nodes:
      regions_n = coarse_nodes_regions[n_id]
      surfaces_n = coarse_nodes_surfaces[n_id]
      numRegions_n = len(regions_n)
      numSurfaces_n = len(surfaces_n)

      # Logic to calculate a term for a surface
      for s in range(numSurfaces_n):
        surf_id = surfaces_n[s]
        area_a = surface_areas[surf_id]
        j_val = 0
        for i in range(numRegions_n):
          # Calculate Fraction
          region_id = regions_n[i]
          vol_i = regions_volume[region_id]
          p_i_a = probabilities["regions"][region_id]["surfaces"][surf_id][g]
          frac = vol_i * p_i_a / area_a
          # Calculate Q
          phi_i = 1
          q_val = calculateQval(energy_g, xs[region_id], keff, g, phi_i)
          j_val += frac*q_val
        #append value to array of each energy group
        j_array.append(j_val)
    j_source[g] = j_array

  return j_source


def calculateQval(energy_g, xs, keff, g, phi_gp_i):
  q_val = 0
  for gp in range(energy_g):
    scatt_val = xs["scatter"][gp][g]
    fiss_val = xs["nuSigFission"][gp] * xs["chi"][g] / keff
    q_val += (scatt_val + fiss_val)*phi_gp_i

  return q_val




