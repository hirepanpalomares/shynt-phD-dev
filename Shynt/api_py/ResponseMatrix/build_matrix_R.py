import numpy as np

from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix

def getResponseMatrix_system(mesh_info, energy_g, probabilities):
    coarse_nodes = mesh_info.coarse_order
    surfaces_rel = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area

    responseMatrix_byGroup = []
    for g in range(energy_g):
        responseMatrix_byCoarse = []
        for n_id in coarse_nodes:
            surfaces = surfaces_rel[n_id]

            rm_n = build_R(
                probabilities[n_id],
                surfaces,
                surface_areas,
                g
            )
            responseMatrix_byCoarse.append(rm_n)
        rm_g = getBlockMatrix(responseMatrix_byCoarse)
        responseMatrix_byGroup.append(rm_g)
    
            
    return getBlockMatrix(responseMatrix_byGroup)


def get_dR_dPab_system(mesh_info, energy_g):
    coarse_nodes = mesh_info.coarse_order
    surfaces_rel = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area

    responseMatrix_byGroup = []
    for g in range(energy_g):
        responseMatrix_byCoarse = []
        for n_id in coarse_nodes:
            surfaces = surfaces_rel[n_id]

            rm_n = build_dR_dPab(
                surfaces,
                surface_areas
            )
            responseMatrix_byCoarse.append(rm_n)
        rm_g = getBlockMatrix(responseMatrix_byCoarse)
        responseMatrix_byGroup.append(rm_g)
    
            
    return getBlockMatrix(responseMatrix_byGroup)


def getResponseMatrix_byGroup(mesh_info, energy_g, probabilities):
  """
  Builds the Response Matrix (mR) for the system for each energy group


  - matrix_R_system_byGroup = {
      g1: mR_system_g, g2: mR_system_g2, ..., gG: mR_system_gG 
    }
  - mR_system_g : Block matrix  of matrix R, one block is Rhe 
    mR of each node
    
    mR_system_g = [
      [mR_1]    0     0     ...    0
          0   [mR_2]   0     ...    0 
          :      :     :.    ...    0
          0      0     0     ...  [mR_n]
    ]

  ParameRers
  ----------
  mesh_info : MeshInfo

  energy_g : int
    Number of energy groups
  probabilities : dict

  Returns
  -------
  responseMatrix_byGroup : dict
    
  """
  coarse_nodes = mesh_info.coarse_order
  surfaces_rel = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area

  responseMatrix_byGroup = {}
  for g in range(energy_g):
    responseMatrix_byCoarse = []
    for n_id in coarse_nodes:
      surfaces = surfaces_rel[n_id]
      rm_n = build_R(
        probabilities,
        surfaces,
        surface_areas,
        g
      )
      responseMatrix_byCoarse.append(rm_n)
    rm_g = getBlockMatrix(responseMatrix_byCoarse)
    responseMatrix_byGroup[g] = rm_g
          
  return responseMatrix_byGroup




def build_R(probabilities, surfaces, surface_areas, g):
  """
  Builds the response matrix R for a coarse node

  mR = [
      [R_{b1,a1}, R_{b2,a1}, ..., R_{Bn,a1}]
      [R_{b1,a2}, R_{b2,a2}, ..., R_{Bn,a2}],
      [   ...   ,    ...   , ...,    ...   ],
      [R_{b1,An}, R_{b2,An}, ..., R_{Bn,An}],
    ]

                    s_b * P_{g,b-->a}
  R_{Bn,An} =    ----------------------
                          s_a

                  
  s_a            : Area of surface "a"  [ cm^2 ]
  s_b            : Area of surface "b"  [ cm^2 ]
  P_{g,b-->a}    : Probability from surface "b" to surface "a"
                   in the energy group "g" [ ]

  Parameters
  ----------
  probabilities : dict

  surfaces : list

  surfaces_areas : dict

  g : int

  Returns
  -------
  mR : np.array(number_of_surfaces, number_of_surfaces)
    
  """
  numSurf = len(surfaces)
  mR_shape = (numSurf, numSurf)
  mR = np.zeros(mR_shape)
  for a in range(numSurf):
    surf_a_id = surfaces[a]
    area_a = surface_areas[surf_a_id]
    for b in range(numSurf):
      surf_b_id = surfaces[b]
      area_b = surface_areas[surf_b_id]
      p_b_a = probabilities["surfaces"][surf_b_id]["surfaces"][surf_a_id][g]
      mR[a][b] =  area_b * p_b_a / area_a

  return mR

def build_dR_dPab(surfaces, surface_areas):
    """
        surfaces:   Array with the surfaces_ids of the corresponding coarse node, ex:
                    [3, 4, 5, 6]

        regions:    Array with the regions_ids of the corresponding coarse node, ex:
                    [1, 2, 3, 4]
    """
    numSurf = len(surfaces)
    responseMatrix_shape = (numSurf, numSurf)
    responseMatrix_n = np.zeros(responseMatrix_shape)
    for a in range(numSurf):
        surf_a_id = surfaces[a]
        area_a = surface_areas[surf_a_id]
        for b in range(numSurf):
            surf_b_id = surfaces[b]
            area_b = surface_areas[surf_b_id]
            responseMatrix_n[a][b] =  area_b / area_a

    return responseMatrix_n