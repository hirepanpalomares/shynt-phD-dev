
import numpy as np














def getMatrixU_byNode_byGroup(coarse_nodes, energy_g, probabilities):
    # We need matrix U for the source
    matrixU_byNode_byGroup = { }
    
    
    for n_id, node in coarse_nodes.items():
        matrixU_byNode_byGroup[n_id] = {}

        surfaces_n = node.surface_ids
        surface_areas_n = node.surface_areas
        regions = node.fine_nodes_ids
        regions_volume = node.fine_nodes_volume
        
        for g in range(energy_g):
            mat_u_n = build_U(
                probabilities[n_id],
                surfaces_n,
                surface_areas_n,
                regions,
                regions_volume,
                g,
            )
            # print(mat_u_n)
            matrixU_byNode_byGroup[n_id][g] = mat_u_n
            
    # print(matrixU_byNode_byGroup)
    return matrixU_byNode_byGroup


def build_U(probabilities, surfaces, surface_areas, regions, regions_volume, g):
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


    cell_materials = ["fuel", "coolant"]

    for a in range(numSurf):
        surf_id = surfaces[a]
        area_a = surface_areas[surf_id]
        for i in range(numReg):
            region_id = regions[i]
            region_name = cell_materials[i]
            vol_i = regions_volume[region_id]
            p_i_a = probabilities[region_name]["surfaces"][surf_id][g]
            matrix_U_n[a][i] =  vol_i * p_i_a / area_a


    return matrix_U_n
