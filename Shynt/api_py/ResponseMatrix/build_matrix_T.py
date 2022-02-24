import numpy as np







def getMatrixT_byNode_byGroup(coarse_nodes, energy_g, xs, probabilities):
    matrix_T_byNode_byGroup = {}
    for n_id, node in coarse_nodes.items():
        matrix_T_byNode_byGroup[n_id] = {}
        regions = node.fine_nodes_ids
        regions_volume = node.fine_nodes_volume
        for g in range(energy_g):
            mT = build_T(
                xs[n_id],
                probabilities[n_id],
                regions,
                regions_volume,
                g
            )
            
            matrix_T_byNode_byGroup[n_id][g] = mT
    return matrix_T_byNode_byGroup





def build_T(xs, probabilities, regions, regions_volume, g):
    numRegions = len(regions)
    matrix_T = np.zeros((numRegions, numRegions))

    cell_materials = ["fuel", "coolant"]

    for j in range(numRegions):
        region_j_id = regions[j]
        vol_j = regions_volume[region_j_id]
        material_region_j = cell_materials[j]
        xsTotal_j = xs[region_j_id]["total"][g]
        for i in range(numRegions):
            region_i_id = regions[i]
            vol_i = regions_volume[region_i_id]
            material_region_i = cell_materials[i]
            p_i_j = probabilities[material_region_i][material_region_j][g]
            matrix_T[j][i] =  vol_i * p_i_j / (xsTotal_j * vol_j)
    
    return matrix_T