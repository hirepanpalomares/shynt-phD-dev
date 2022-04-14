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
                prob,
                regions,
                regions_volume,
                g
            )
            
            matrix_T_byNode_byGroup[n_id][g] = mT
    return matrix_T_byNode_byGroup


def getMatrixT_system_byGroup(mesh_info, energy_g, xs, probabilities):
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    coarse_nodes_surfaces = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area
    regions_volume = mesh_info.all_regions_vol


    matrix_T_system_byGroup = {}
    prob = { "regions": {}, "surfaces": {}}
    for g in range(energy_g):
        systemMatrixes = []
        for n_id in coarse_nodes:
            regions = coarse_nodes_regions[n_id]

            prob["regions"] = {r: probabilities["regions"][r] for r in regions}
            xs_node = {r: xs[r] for r in regions}

            mT = build_T(
                xs_node,
                prob,
                regions,
                regions_volume,
                g
            )
            systemMatrixes.append(mT)
        big_matrix_T = getBlockMatrix(systemMatrixes)
        matrix_T_system_byGroup[g] = big_matrix_T
            
    return matrix_T_system_byGroup




def build_T(xs, probabilities, regions, regions_volume, g):
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