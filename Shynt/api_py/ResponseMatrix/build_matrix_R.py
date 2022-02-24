import numpy as np

from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix




def getResponseMatrix_system(coarse_nodes, energy_g, probabilities, mesh_info):
    coarse_node_order = mesh_info.coarse_order
    
    responseMatrix_byGroup = []
    for g in range(energy_g):
        responseMatrix_byCoarse = []
        for n_id in coarse_node_order:
            node = coarse_nodes[n_id]
            surfaces_n = node.surface_ids
            surface_areas_n = node.surface_areas
            
            rm_n = build_R(
                probabilities[n_id]["surface"],
                surfaces_n,
                surface_areas_n,
                g
            )
            responseMatrix_byCoarse.append(rm_n)
        rm_g = getBlockMatrix(responseMatrix_byCoarse)
        responseMatrix_byGroup.append(rm_g)
            
    responseMatrix_system = getBlockMatrix(responseMatrix_byGroup)
    return responseMatrix_system


def getResponseMatrix_byGroup(coarse_nodes, energy_g, probabilities, mesh_info):
    coarse_node_order = mesh_info.coarse_order

    
    responseMatrix_byGroup = {}
    for g in range(energy_g):
       
        responseMatrix_byCoarse = []
        for n_id in coarse_node_order:
            node = coarse_nodes[n_id]
            surfaces_n = node.surface_ids
            surface_areas_n = node.surface_areas
            
            rm_n = build_R(
                probabilities[n_id]["surface"],
                surfaces_n,
                surface_areas_n,
                g
            )
            responseMatrix_byCoarse.append(rm_n)
        rm_g = getBlockMatrix(responseMatrix_byCoarse)
        responseMatrix_byGroup[g] = rm_g
            
    return responseMatrix_byGroup



def build_R(probabilities, surfaces, surface_areas, g):
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
            p_b_a = probabilities[surf_b_id]["surfaces"][surf_a_id][g]
            responseMatrix_n[a][b] =  area_b * p_b_a / area_a

    return responseMatrix_n