import numpy as np

from Shynt.api_py.Geometry import surfaces
from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix


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


def getMatrixS_system_byGroup(mesh_info, energy_g, xs, probabilities):
 
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    coarse_nodes_surfaces = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area
    regions_volume = mesh_info.all_regions_vol

    matrix_S_system_byGroup = {}
    prob = { "regions": {}, "surfaces": {}}
    for g in range(energy_g):
        systemMatrixes = []
        for c_id in coarse_nodes:
            regions = coarse_nodes_regions[c_id]
            surfaces = coarse_nodes_surfaces[c_id]
            # for each coarse node
            xs_node = {r: xs[r] for r in regions}
            prob = {s: probabilities["surfaces"][s] for s in surfaces}

            mS = build_S(  
                xs_node,
                prob,
                surfaces,
                surface_areas,
                regions,
                regions_volume,
                g
            )
            systemMatrixes.append(mS)
        big_matrix_S = getBlockMatrix(systemMatrixes)
        matrix_S_system_byGroup[g] = big_matrix_S

    return matrix_S_system_byGroup



def build_S(xs, probabilities, surfaces, surface_areas, regions, regions_volume, g):
    numReg = len(regions)
    numSurf = len(surfaces)

    matrix_S_shape = (numReg, numSurf)
    mS = np.zeros(matrix_S_shape)

    cell_materials = ["fuel", "coolant"]

    for j in range(numReg):
        region_j_id = regions[j]
        vol_j = regions_volume[region_j_id]
        xsTotal_j = xs[region_j_id]["total"][g]
        for a in range(numSurf):
            s_id = surfaces[a]
            area_a = surface_areas[s_id]
            p_a_j = probabilities[s_id]["regions"][region_j_id][g]
            mS[j][a] =  area_a * p_a_j / (xsTotal_j * vol_j)
    
            
    
    return mS
