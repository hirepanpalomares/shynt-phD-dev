
import numpy as np
import scipy.sparse as sparse

from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix




def getMatrixU_system_byGroup(mesh_info, energy_g, probabilities, store_sparse=False):
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

  eq_nodes = mesh_info.coarse_mesh.equivalent_nodes_rel
  eq_regions = mesh_info.coarse_mesh.equivalent_regions
  eq_surfaces = mesh_info.coarse_mesh.equivalent_surfaces

  shape_mU = (
    len(mesh_info.all_surfaces_order), len(mesh_info.all_regions_order)
  )
  matrixU_system_byGroup = { }
  for g in range(energy_g):
    systemMatrixes = []

    sparse_row = []
    sparse_col = []
    sparse_val = []
    idx_row = 0
    idx_col = 0
    for n_id in coarse_nodes:
      surfaces = coarse_nodes_surfaces[n_id]
      regions = coarse_nodes_regions[n_id]

      numSurf = len(surfaces)      
      numReg = len(regions)
      mU = build_U(
        probabilities,
        surfaces,
        surface_areas,
        regions,
        regions_volume,
        n_id,
        eq_nodes,
        eq_regions,
        eq_surfaces,
        g,
      )
     
      if store_sparse:
        for r in range(numSurf):
          for c in range(numReg):
            sparse_row.append(idx_row)

            sparse_col.append(idx_col + c)
            # print(r,c, idx_row, idx_col+c)
            sparse_val.append(mU[r][c])
          idx_row += 1
        idx_col += numReg  
      else:
        systemMatrixes.append(mU)

    if store_sparse:
      # mUg = sparse.csc_matrix(
      #   (sparse_val, (sparse_row, sparse_col)), shape=shape_mU, dtype=np.double
      # )
      mUg =  (
        np.array(sparse_row), 
        np.array(sparse_col), 
        np.array(sparse_val)
      )
    else:
      mUg = getBlockMatrix(systemMatrixes)
    
    # print(mUg)
    # print(sparse_row[:50])
    # print(sparse_col[:50])
    # print(sparse_val[:50])

    # raise SystemExit
    matrixU_system_byGroup[g] = mUg
    # big_matrix_U = getBlockMatrix(systemMatrixes)

    # if store_sparse:
    #   sparse_mUg = sparse.csc_matrix(big_matrix_U)
    #   matrixU_system_byGroup[g] = sparse_mUg
    # else:
    #   matrixU_system_byGroup[g] = big_matrix_U

          
  return matrixU_system_byGroup



def getMatrixU_mainNodes(mesh_info, energy_g, probabilities):
  """

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

  eq_nodes = mesh_info.coarse_mesh.equivalent_nodes
  eq_nodes_rel = mesh_info.coarse_mesh.equivalent_nodes_rel

  eq_regions = mesh_info.coarse_mesh.equivalent_regions
  eq_surfaces = mesh_info.coarse_mesh.equivalent_surfaces

 
  matrixU_bg_mainNodes = { }
  for g in range(energy_g):
    matrixU_bg_mainNodes[g] = {}

    for n_id in eq_nodes.keys():
      surfaces = coarse_nodes_surfaces[n_id]
      regions = coarse_nodes_regions[n_id]

      mU = build_U(
        probabilities,
        surfaces,
        surface_areas,
        regions,
        regions_volume,
        n_id,
        eq_nodes_rel,
        eq_regions,
        eq_surfaces,
        g,
      )

      matrixU_bg_mainNodes[g][n_id] = mU
  

          
  return matrixU_bg_mainNodes




def build_U(
  probabilities, surfaces, surface_areas, regions, regions_volume,
  node, eq_nodes, eq_regions, eq_surfaces, g
):
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
  eq_node = eq_nodes[node]
  
  mU_shape = (numSurf, numReg)
  mU = np.zeros(mU_shape)

  for a in range(numSurf):
    surf_id = surfaces[a]
    eq_sa_id = eq_surfaces[surf_id]

    area_a = surface_areas[surf_id]
    for i in range(numReg):
      region_id = regions[i]
      eq_ri_id =  eq_regions[region_id]

      vol_i = regions_volume[region_id]
      # p_i_a = probabilities["regions"][region_id]["surfaces"][surf_id][g]
      p_i_a = probabilities[eq_node]["regions"][eq_ri_id]["surfaces"][eq_sa_id][g]

      mU[a][i] =  vol_i * p_i_a / area_a
  return mU




def getMatrixU_system_allG(mesh_info, energy_g, probabilities):
  """
  # Calculates the Matrix U of the system by energy group

  #   - matrix_U_system_byGroup = {
  #       g1: mU_system_g, g2: mU_system_g2, ..., gG: mU_system_gG 
  #     }
  #   - mU_system_g : Block matrix  of matrix U, one block is the 
  #     mU of each node
      
  #     mU_system_g = [
  #       [mU_1]    0     0     ...    0
  #         0   [mU_2]   0     ...    0 
  #         :      :     :.    ...    0
  #         0      0     0     ...  [mU_n]
  #     ]

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

  
  systemMatrixes = []
  for n_id in coarse_nodes:
    regions = coarse_nodes_regions[n_id]
    surfaces_n = coarse_nodes_surfaces[n_id]

    matrices_Ug = []
    for g in range(energy_g):
      mU_g = build_U(
        probabilities, surfaces_n, surface_areas, regions, regions_volume, g
      )
      matrices_Ug.append(mU_g)
    big_mU_n = getBlockMatrix(matrices_Ug)
    systemMatrixes.append(big_mU_n)
  big_matrix_U = getBlockMatrix(systemMatrixes)
      
  return big_matrix_U













































"""
  Functions below are not used

"""

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