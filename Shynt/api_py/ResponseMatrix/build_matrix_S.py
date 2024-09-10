import numpy as np
import scipy.sparse as sparse

from Shynt.api_py.Geometry import surfaces
from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix



def getMatrixS_system_byGroup(mesh_info, energy_g, xs, probabilities, store_sparse=False):
  """
  Calculates the Matrix S of the system by energy group

    - matrix_S_system_byGroup = {
        g1: mS_system_g, g2: mS_system_g2, ..., gG: mS_system_gG 
      }
    - mS_system_g : Block matrix  of matrix S, one block is the 
      mS of each node
      
      mS_system_g = [
        [mS_1]    0     0     ...    0
           0   [mS_2]   0     ...    0 
           :      :     :.    ...    0
           0      0     0     ...  [mS_n]
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
  matrix_S_system_byGroup : dict

  """
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area
  regions_volume = mesh_info.all_regions_vol
  eq_nodes = mesh_info.coarse_mesh.equivalent_nodes_rel
  eq_regions = mesh_info.coarse_mesh.equivalent_regions
  eq_surfaces = mesh_info.coarse_mesh.equivalent_surfaces
  

  shape_mS = (
    len(mesh_info.all_regions_order), len(mesh_info.all_surfaces_order)
  )
  matrix_S_system_byGroup = {}
  for g in range(energy_g):
    sparse_row = []
    sparse_col = []
    sparse_val = []
    idx_row = 0
    idx_col = 0

    systemMatrixes = []
    for c_id in coarse_nodes:
      # for each coarse node
      regions = coarse_nodes_regions[c_id]
      surfaces = coarse_nodes_surfaces[c_id]
      numRegions = len(regions)
      numSurfaces = len(surfaces)

      xs_node = {r: xs[r] for r in regions}
      mS = build_S(  
        xs_node,
        probabilities,
        surfaces,
        surface_areas,
        regions,
        regions_volume,
        c_id,
        eq_nodes,
        eq_regions,
        eq_surfaces,
        g
      )
      if store_sparse:
        for r in range(numRegions):
          for c in range(numSurfaces):
            sparse_row.append(idx_row)
            sparse_col.append(idx_col + c)
            sparse_val.append(mS[r][c])
          idx_row += 1
        idx_col += numSurfaces  
      else:
        systemMatrixes.append(mS)

    if store_sparse:
      # mSg = sparse.csc_matrix(
      #   (sparse_val, (sparse_row, sparse_col)), shape=shape_mS, dtype=np.double
      # )
      mSg =  (
        np.array(sparse_row), 
        np.array(sparse_col), 
        np.array(sparse_val)
      )
    else:
      mSg = getBlockMatrix(systemMatrixes)

    matrix_S_system_byGroup[g] = mSg


  return matrix_S_system_byGroup



def getMatrixS_mainNodes(mesh_info, energy_g, xs, probabilities):
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
  matrix_S_system_byGroup : dict

  """
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area
  regions_volume = mesh_info.all_regions_vol
  eq_nodes = mesh_info.coarse_mesh.equivalent_nodes
  eq_nodes_rel = mesh_info.coarse_mesh.equivalent_nodes_rel

  eq_regions = mesh_info.coarse_mesh.equivalent_regions
  eq_surfaces = mesh_info.coarse_mesh.equivalent_surfaces
  
  matrix_S_bg_mainNodes = {}
  for g in range(energy_g):
    matrix_S_bg_mainNodes[g] = {}

    for c_id in eq_nodes.keys():
      # for each coarse node
      regions = coarse_nodes_regions[c_id]
      surfaces = coarse_nodes_surfaces[c_id]
  
      xs_node = {r: xs[r] for r in regions}
      mS = build_S(  
        xs_node,
        probabilities,
        surfaces,
        surface_areas,
        regions,
        regions_volume,
        c_id,
        eq_nodes_rel,
        eq_regions,
        eq_surfaces,
        g
      )
      matrix_S_bg_mainNodes[g][c_id] = mS


  return matrix_S_bg_mainNodes




def build_S(xs, probabilities, surfaces, surface_areas, regions, 
  regions_volume, node, eq_nodes, eq_regions, eq_surfaces, g
):
  """
  Builds the matrix S for a coarse node

  mS = [
    [S_{a1,j1}, S_{a2,j1}, ..., S_{An,j1}]
    [S_{a1,j2}, S_{a2,j2}, ..., S_{An,j2}],
    [   ...   ,    ...   , ...,    ...   ],
    [S_{a1,Jn}, S_{a2,Jn}, ..., S_{An,Jn}],
  ]

                    s_a * P_{g,a-->j}
  S_{An,Jn} =    ----------------------
                  v_j * \Sigma_{t,g,j}

                  
  s_a            : Area of surface "a"  [ cm^2 ]
  v_j            : Volume of region "j" [ cm^3 ]
  P_{g,a-->j}    : Probability from surface "a" to region "j"
                    in the energy group "g" [ ]
  \Sigma_{t,g,j} : Total cross section of region "j" in energy
                    group "g" [cm^-1] 

  Parameters
  ----------
  xs : dict

  probabilities : dict

  surfaces : list

  surfaces_areas : dict

  regions : list

  regions_volume : dict

  g : int

  Returns
  -------
  mS : np.array(number_of_regions, number_of_surfaces)
    
  """
  numReg = len(regions)
  numSurf = len(surfaces)
  eq_node = eq_nodes[node]
  
  matrix_S_shape = (numReg, numSurf)
  mS = np.zeros(matrix_S_shape)
  for j in range(numReg):
    region_j_id = regions[j]
    eq_rjd =  eq_regions[region_j_id]
    vol_j = regions_volume[region_j_id]
    xsTotal_j = xs[region_j_id]["total"][g]
    
    for a in range(numSurf):
      s_id = surfaces[a]
      eq_sid = eq_surfaces[s_id]
      
      area_a = surface_areas[s_id]

      # p_a_j = probabilities["surfaces"][s_id]["regions"][region_j_id][g]
      # print(eq_node, "surfaces", eq_sid, "regions", eq_rjd, g)
      p_a_j = probabilities[eq_node]["surfaces"][eq_sid]["regions"][eq_rjd][g]

      if xsTotal_j == 0.0:
        mS[j][a] = 0.0
      else:  
        mS[j][a] =  area_a * p_a_j / (xsTotal_j * vol_j)
  # if node == 1:
  #   print(mS)
  return mS



def getMatrixS_system_allG(mesh_info, energy_g, xs, probabilities):
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area
  regions_volume = mesh_info.all_regions_vol

  systemMatrixes = []

  for c_id in coarse_nodes:
    # for each coarse node
    regions = coarse_nodes_regions[c_id]
    surfaces = coarse_nodes_surfaces[c_id]
    xs_node = {r: xs[r] for r in regions}
    mS = build_S_allG(  
      xs_node,
      probabilities,
      surfaces,
      surface_areas,
      regions,
      regions_volume,
      energy_g
    )
    systemMatrixes.append(mS)
  big_matrix_S = getBlockMatrix(systemMatrixes)
  
  return big_matrix_S


def build_S_allG(xs, probabilities, surfaces, surface_areas, regions, 
  regions_volume, energy_g
):
  """
  Builds the matrix S for a coarse node using all the energy groups
  to use it in the calculations with the Big Phi vector

  # mS = [
  #   [S_{a1,j1,g1}, S_{a2,j1,g1}, ..., S_{An,j1,g1}],
  #   [S_{a1,j1,g2}, S_{a2,j1,g2}, ..., S_{An,j1,g2}],
  #   [   ...      ,    ...      , ...,      ...    ],
  #   [S_{a1,j1,gG}, S_{a2,j1,gG}, ..., S_{An,j1,gG}]

  #   [S_{a1,j2,g1}, S_{a2,j2,g1}, ..., S_{An,j2,g1}],
  #   [S_{a1,j2,g2}, S_{a2,j2,g2}, ..., S_{An,j2,g2}],
  #   [   ...      ,    ...      , ...,      ...    ],
  #   [S_{a1,j2,gG}, S_{a2,j2,gG}, ..., S_{An,j2,gG}],

  #   [S_{a1,Jn,g1}, S_{a2,Jn,g1}, ..., S_{An,Jn,g1}],
  #   [S_{a1,Jn,g2}, S_{a2,Jn,g2}, ..., S_{An,Jn,g2}],
  #   [   ...      ,    ...      , ...,      ...    ],
  #   [S_{a1,Jn,gG}, S_{a2,Jn,gG}, ..., S_{An,Jn,gG}],
  # ]

                    s_a * P_{g,a-->j}
  S_{An,Jn} =    ----------------------
                  v_j * \Sigma_{t,g,j}

                  
  s_a            : Area of surface "a"  [ cm^2 ]
  v_j            : Volume of region "j" [ cm^3 ]
  P_{g,a-->j}    : Probability from surface "a" to region "j"
                    in the energy group "g" [ ]
  \Sigma_{t,g,j} : Total cross section of region "j" in energy
                    group "g" [cm^-1] 

  Parameters
  ----------
  xs : dict

  probabilities : dict

  surfaces : list

  surfaces_areas : dict

  regions : list

  regions_volume : dict

  energy_g : int

  Returns
  -------
  mS : np.array(number_of_regions, number_of_surfaces)
  """
  numReg = len(regions)
  numSurf = len(surfaces)

  
  matrices_S = []  
  for g in range(energy_g):
    # matrix_Sg_shape = (numReg, numSurf)
    # mSg = np.zeros(matrix_Sg_shape)
    # for j in range(numReg):
    #   region_j_id = regions[j]
    #   vol_j = regions_volume[region_j_id]
    #   xsTotal_j = xs[region_j_id]["total"][g]
    #   # row_index = j * energy_g + g
    #   for a in range(numSurf):
    #     s_id = surfaces[a]
        
    #     area_a = surface_areas[s_id]
    #     p_a_j = probabilities["surfaces"][s_id]["regions"][region_j_id][g]

    #     mSg[j][a] =  area_a * p_a_j / (xsTotal_j * vol_j)
    mSg = build_S(
      xs,probabilities,surfaces,surface_areas, regions, regions_volume, g
    )
    matrices_S.append(mSg)
  big_mS = getBlockMatrix(matrices_S)
  return big_mS


def getMatrixS_byNode_byGroup(coarse_nodes, energy_g, xs, probabilities):
  matrix_S_byNode_byGroup = {}

  for c_id, node in coarse_nodes.items():
    # for each coarse node
    matrix_S_byNode_byGroup[c_id] = {}
    regions = node.fine_nodes_ids
    regions_volume = node.fine_nodes_volume
    surfaces_n = node.surface_ids
    surface_areas_n = node.surface_areas
    for g in range(energy_g):
      mS = build_S(  
          xs[c_id],
          probabilities[c_id]["surface"],
          surfaces_n,
          surface_areas_n,
          regions,
          regions_volume,
          g
      )
      
      matrix_S_byNode_byGroup[c_id][g] = mS   
      
  return matrix_S_byNode_byGroup


def getMatrixS_system(mesh_info, energy_g, xs, probabilities):
 
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  coarse_nodes_surfaces = mesh_info.coarse_surface_rel
  surface_areas = mesh_info.all_surfaces_area
  regions_volume = mesh_info.all_regions_vol

  matrix_S_system_byGroup = []
  for g in range(energy_g):
    systemMatrixes = []
    for c_id in coarse_nodes:
      regions = coarse_nodes_regions[c_id]
      surfaces = coarse_nodes_surfaces[c_id]
      # for each coarse node
      xs_node = {r: xs[r] for r in regions}

      mS = build_S(  
        xs_node,
        probabilities,
        surfaces,
        surface_areas,
        regions,
        regions_volume,
        g
      )
      systemMatrixes.append(mS)
    big_matrix_S = getBlockMatrix(systemMatrixes)
    matrix_S_system_byGroup.append(big_matrix_S)

  return getBlockMatrix(matrix_S_system_byGroup)




