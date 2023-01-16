
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
                probabilities,
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

def getMatrixU_system_byGroup(mesh_info, energy_g, probabilities):
    # We need matrix U for the source
    
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
                probabilities,
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
            p_i_a = probabilities["regions"][region_id]["surfaces"][surf_id][g]
            matrix_U_n[a][i] =  vol_i * p_i_a / area_a
            # matrix_U_n[a][i] =  p_i_a / area_a


    return matrix_U_n
