
import numpy as np

from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix



def getMatrixU_byNode_byGroup(mesh_info, energy_g, probabilities):
    # We need matrix U for the source
    
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    coarse_nodes_surfaces = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area
    regions_volume = mesh_info.all_regions_vol

    matrixU_byNode_byGroup = { }
    for n_id in coarse_nodes:
        matrixU_byNode_byGroup[n_id] = {}
        regions = coarse_nodes_regions[n_id]
        surfaces_n = coarse_nodes_surfaces[n_id]
        
        for g in range(energy_g):
            mat_u_n = build_U(
                probabilities[n_id],
                surfaces_n,
                surface_areas,
                regions,
                regions_volume,
                g,
            )
            matrixU_byNode_byGroup[n_id][g] = mat_u_n
            
    return matrixU_byNode_byGroup

def getMatrixU_system(mesh_info, energy_g, probabilities):
    # We need matrix U for the source
    
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    coarse_nodes_surfaces = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area
    regions_volume = mesh_info.all_regions_vol

    matrixU_system_byGroup = []
    for g in range(energy_g):
        systemMatrixes = []
        for n_id in coarse_nodes:
            regions = coarse_nodes_regions[n_id]
            surfaces_n = coarse_nodes_surfaces[n_id]

            mat_u_n = build_U(
                probabilities[n_id],
                surfaces_n,
                surface_areas,
                regions,
                regions_volume,
                g,
            )
            systemMatrixes.append(mat_u_n)
        big_matrix_U = getBlockMatrix(systemMatrixes)
        matrixU_system_byGroup.append(big_matrix_U)
            
    return getBlockMatrix(matrixU_system_byGroup)


def get_dU_dPij_system(mesh_info, energy_g):
    # We need matrix U for the source
    
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    coarse_nodes_surfaces = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area
    regions_volume = mesh_info.all_regions_vol

    matrixU_system_byGroup = []
    for g in range(energy_g):
        systemMatrixes = []
        for n_id in coarse_nodes:
            regions = coarse_nodes_regions[n_id]
            surfaces_n = coarse_nodes_surfaces[n_id]

            mat_u_n = build_dU_dPij(
                surfaces_n,
                surface_areas,
                regions,
                regions_volume
            )
            systemMatrixes.append(mat_u_n)
        big_matrix_U = getBlockMatrix(systemMatrixes)
        matrixU_system_byGroup.append(big_matrix_U)
            
    return getBlockMatrix(matrixU_system_byGroup)



def getMatrixU_system_byGroup(mesh_info, energy_g, probabilities):
  """
  Calculates the Matrix U of the system by energy group

    - matrix_U_system_byGroup = {
        g1: mU_system_g, g2: mU_system_g2, ..., gG: mU_system_gG 
      }
    - mU_system_g : Block matrix  of matrix U, one block is the 
      mU of each node
      
      mU_system_g = [
        [mU_1]    0     0     ...    0
           0   [mU_2]   0     ...    0 
           :      :     :.    ...    0
           0      0     0     ...  [mU_n]
      ]

  Parameters
  ----------
  mesh_info : MeshInfo

  energy_g : int
  Number of energy groups
  xs : dict

  probabilities : dict

  Returns
  -------
  matrix_U_system_byGroup : dict

  """
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area
  regions_volume = mesh_info.all_regions_vol

  matrixU_system_byGroup = { }
  for g in range(energy_g):
      systemMatrixes = []
      for n_id in coarse_nodes:
          regions = coarse_nodes_regions[n_id]
          surfaces_n = coarse_nodes_surfaces[n_id]

          mat_u_n = build_U(
              probabilities[n_id],
              surfaces_n,
              surface_areas,
              regions,
              regions_volume,
              g,
          )
          systemMatrixes.append(mat_u_n)
      big_matrix_U = getBlockMatrix(systemMatrixes)
      matrixU_system_byGroup[g] = big_matrix_U
          
  return matrixU_system_byGroup


def build_U(probabilities, surfaces, surface_areas, regions, regions_volume, g):
  """
  Builds the matrix U for a coarse node

  mU = [
      [U_{i1,a1}, U_{i2,a1}, ..., U_{In,a1}]
      [U_{i1,a2}, U_{i2,a2}, ..., U_{In,a2}],
      [   ...   ,    ...   , ...,    ...   ],
      [U_{i1,An}, U_{i2,An}, ..., U_{In,An}],
    ]

                    v_i * P_{g,i-->a}
  U_{In,An} =    ----------------------
                          s_a

                  
  s_a            : Area of surface "a"  [ cm^2 ]
  v_i            : Volume of region "i" [ cm^3 ]
  P_{g,i-->a}    : Probability from region "i" to surface "a"
                   in the energy group "g" [ ]

  Parameters
  ----------
  probabilities : dict

  surfaces : list

  surfaces_areas : dict

  regions : list

  regions_volume : dict

  g : int

  Returns
  -------
  mU : np.array(number_of_regions, number_of_surfaces)
    
  """
  numReg = len(regions)
  numSurf = len(surfaces)
  
  mU_shape = (numSurf, numReg)
  mU = np.zeros(mU_shape)

  for a in range(numSurf):
    surf_id = surfaces[a]
    area_a = surface_areas[surf_id]
    for i in range(numReg):
      region_id = regions[i]
      vol_i = regions_volume[region_id]
      p_i_a = probabilities["regions"][region_id]["surfaces"][surf_id][g]
      mU[a][i] =  vol_i * p_i_a / area_a
  return mU


def build_dU_dPij(surfaces, surface_areas, regions, regions_volume):
    """
        surfaces:   Array with the surfaces_ids of the corresponding coarse node, ex:
                    [3, 4, 5, 6]

        regions:    Array with the regions_ids of the corresponding coarse node, ex:
                    [1, 2, 3, 4]
    """
    numReg = len(regions)
    numSurf = len(surfaces)
    
    matrix_U_shape = (numSurf, numReg)
    matrix_U_n = np.zeros(matrix_U_shape)

    for a in range(numSurf):
        surf_id = surfaces[a]
        area_a = surface_areas[surf_id]
        for i in range(numReg):
            region_id = regions[i]
            vol_i = regions_volume[region_id]
            matrix_U_n[a][i] =  vol_i / area_a
            # matrix_U_n[a][i] =  p_i_a / area_a


    return matrix_U_n