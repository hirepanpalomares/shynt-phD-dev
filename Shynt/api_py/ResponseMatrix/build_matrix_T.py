import numpy as np

from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix







def getMatrixT_byNode_byGroup(mesh_info, energy_g, xs, probabilities):
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    coarse_nodes_surfaces = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area
    regions_volume = mesh_info.all_regions_vol


    matrix_T_byNode_byGroup = {}
    prob = { "regions": {}, "surfaces": {}}
    for n_id in coarse_nodes:
        matrix_T_byNode_byGroup[n_id] = {}
        regions = coarse_nodes_regions[n_id]

        prob["regions"] = {r: probabilities["regions"][r] for r in regions}
        xs_node = {r: xs[r] for r in regions}

        for g in range(energy_g):
            mT = build_T(
                xs_node,
                prob[n_id],
                regions,
                regions_volume,
                g
            )
            
            matrix_T_byNode_byGroup[n_id][g] = mT
    return matrix_T_byNode_byGroup

def getMatrixT_system(mesh_info, energy_g, xs, probabilities):
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    regions_volume = mesh_info.all_regions_vol


    matrix_T_system_byGroup = []
    for g in range(energy_g):
        systemMatrixes = []
        for n_id in coarse_nodes:
            regions = coarse_nodes_regions[n_id]

            xs_node = {r: xs[r] for r in regions}

            mT = build_T(
                xs_node,
                probabilities[n_id],
                regions,
                regions_volume,
                g
            )
            systemMatrixes.append(mT)
        big_matrix_T = getBlockMatrix(systemMatrixes)
        matrix_T_system_byGroup.append(big_matrix_T)
            
    return getBlockMatrix(matrix_T_system_byGroup)


def getMatrixT_system_wo_prob_byGroup(mesh_info, energy_g, xs):
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    regions_volume = mesh_info.all_regions_vol


    matrix_T_system_byGroup = {}
    for g in range(energy_g):
        systemMatrixes = []
        for n_id in coarse_nodes:
            regions = coarse_nodes_regions[n_id]

            xs_node = {r: xs[r] for r in regions}

            mT = build_T_wo_prob(
                xs_node,
                regions,
                regions_volume,
                g
            )
            systemMatrixes.append(mT)
        big_matrix_T = getBlockMatrix(systemMatrixes)
        matrix_T_system_byGroup[g] = big_matrix_T
            
    return matrix_T_system_byGroup



def getMatrixT_system_byGroup(mesh_info, energy_g, xs, probabilities):
  """
  Calculates the Matrix T of the system by energy group

  - matrix_T_system_byGroup = {
      g1: mT_system_g, g2: mT_system_g2, ..., gG: mT_system_gG 
    }
  - mT_system_g : Block matrix  of matrix T, one block is the 
    mT of each node
    
    mT_system_g = [
      [mT_1]    0     0     ...    0
          0   [mT_2]   0     ...    0 
          :      :     :.    ...    0
          0      0     0     ...  [mT_n]
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
    matrix_T_system_byGroup : dict

  """
  coarse_nodes = mesh_info.coarse_order
  coarse_nodes_regions = mesh_info.coarse_region_rel
  regions_volume = mesh_info.all_regions_vol


  matrix_T_system_byGroup = {}
  for g in range(energy_g):
    systemMatrixes = []
    for n_id in coarse_nodes:
      regions = coarse_nodes_regions[n_id]
      xs_node = {r: xs[r] for r in regions}
      mT = build_T(
        xs_node,
        probabilities,
        regions,
        regions_volume,
        g
      )
      systemMatrixes.append(mT)
    big_matrix_T = getBlockMatrix(systemMatrixes)
    matrix_T_system_byGroup[g] = big_matrix_T       
  return matrix_T_system_byGroup




def build_T(xs, probabilities, regions, regions_volume, g):
  """
  Builds the matrix T for a coarse node

  mT = [
      [T_{i1,j1}, T_{i2,j1}, ..., T_{In,j1}]
      [T_{i1,j2}, T_{i2,j2}, ..., T_{In,j2}],
      [   ...   ,    ...   , ...,    ...   ],
      [T_{i1,Jn}, T_{i2,Jn}, ..., T_{In,Jn}],
    ]

                    v_i * P_{g,i-->j}
  T_{In,Jn} =    ----------------------
                  v_j * \Sigma_{t,g,j}

                  
  v_i            :  Volume of region "j" [ cm^3 ]
  v_j            :  Volume of region "j" [ cm^3 ]
  P_{g,i-->j}    :  Probability from region "i" to region "j"
                    in the energy group "g" [ ]
  \Sigma_{t,g,j} :  Total cross section of region "j" in energy
                    group "g" [cm^-1] 

  Parameters
  ----------
  xs : dict

  probabilities : dict

  regions : list

  regions_volume : dict

  g : int

  Returns
  -------
  mT : np.array(number_of_regions, number_of_regions)
    
  """
  numRegions = len(regions)

  matrix_T_shape = (numRegions, numRegions)
  matrix_T = np.zeros(matrix_T_shape)

  for j in range(numRegions):
    region_j_id = regions[j]
    vol_j = regions_volume[region_j_id]
    
    xsTotal_j = xs[region_j_id]["total"][g]
    for i in range(numRegions):
      region_i_id = regions[i]
      vol_i = regions_volume[region_i_id]
      p_i_j = probabilities["regions"][region_i_id]["regions"][region_j_id][g]
      matrix_T[j][i] =  vol_i * p_i_j / (xsTotal_j * vol_j)
      
    
  return matrix_T



def build_T_wo_prob(xs, regions, regions_volume, g):
    numRegions = len(regions)

    matrix_T_shape = (numRegions, numRegions)
    matrix_T = np.zeros(matrix_T_shape)

    for j in range(numRegions):
        region_j_id = regions[j]
        vol_j = regions_volume[region_j_id]
        
        xsTotal_j = xs[region_j_id]["total"][g]
        for i in range(numRegions):
            region_i_id = regions[i]
            vol_i = regions_volume[region_i_id]
            matrix_T[j][i] =  vol_i / (xsTotal_j * vol_j)
    
    return matrix_T



