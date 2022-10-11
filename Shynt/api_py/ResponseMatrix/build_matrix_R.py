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
                probabilities,
                surfaces,
                surface_areas,
                g
            )
            responseMatrix_byCoarse.append(rm_n)
        rm_g = getBlockMatrix(responseMatrix_byCoarse)
        responseMatrix_byGroup.append(rm_g)
    
            
    return getBlockMatrix(responseMatrix_byGroup)


def getResponseMatrix_byGroup(mesh_info, energy_g, probabilities):
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
            p_b_a = probabilities["surfaces"][surf_b_id]["surfaces"][surf_a_id][g]
            responseMatrix_n[a][b] =  area_b * p_b_a / area_a

    return responseMatrix_n