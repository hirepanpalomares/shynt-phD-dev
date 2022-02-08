from platform import node
from threading import local
from urllib.parse import _NetlocResultMixinStr
import numpy as np


def getMatrixS_byGlobalNode(coarse_nodes, fine_nodes, surf_area_relation, energy_g, xs, probabilities):
    matrixes_S = {}
    for node_id in coarse_nodes.keys():
        # for each coarse node
        mS = build_S(
            fine_nodes[node_id], 
            surf_area_relation[node_id], 
            energy_g, 
            xs[node_id],
            probabilities[node_id]["surface"]
        )
        matrixes_S[node_id] = mS   
    return matrixes_S

def getMatrixT_byGlobalNode(coarse_nodes, fine_nodes, energy_g, xs, probabilities):
    matrixes_T = {}
    for node_id in coarse_nodes.keys():
        # for each coarse node
        mT = build_T(
            fine_nodes[node_id], 
            energy_g, 
            xs[node_id],
            probabilities[node_id]
        )
        matrixes_T[node_id] = mT
    return matrixes_T

def getResponseMatrix_system(coarse_nodes, surf_area_relation, energy_g, probabilities):
    responseMatrix_byNode = { }
    
    responseMatrix_system_rows = 0  # Just in case the number of surfaces of the all the coarse nodes is not the same
    responseMatrix_system_cols = 0  # Just in case the number of surfaces of the all the coarse nodes is not the same
    matrix_corners = {}
    corner = (0,0) # Postion of the left upper corner of the matrix in the RM of the system

    for n_id in coarse_nodes.keys():
        matrix_corners[n_id] = corner
        rm_n, rm_n_shape = build_R(
            surf_area_relation[n_id],
            energy_g,
            probabilities[n_id]["surface"]
        ) 
        responseMatrix_byNode[n_id] = rm_n
        
        next_corner_row = corner[0] + rm_n_shape[0]
        next_corner_col = corner[1] + rm_n_shape[1]
        corner = (next_corner_row, next_corner_col)

        responseMatrix_system_rows += len(rm_n)     # Just in case the number of surfaces of the all the coarse nodes is not the same
        responseMatrix_system_cols += len(rm_n[0])  # Just in case the number of surfaces of the all the coarse nodes is not the same


    responseMatrix_system_shape = (responseMatrix_system_rows, responseMatrix_system_cols)
    responseMatrix_system = np.zeros(responseMatrix_system_shape)


    for n_id in coarse_nodes.keys():
        corner = matrix_corners[n_id]
        resp_n = responseMatrix_byNode[n_id]
        for r in range(resp_n.shape[0]):
            for c in range(resp_n.shape[1]):
                responseMatrix_system[corner[0] + r][corner[1] + c] = resp_n[r][c]
                

    return responseMatrix_system

def getUMatrix_system(coarse_nodes, fine_nodes, surf_area_relation, energy_g, probabilities):
    matrix_U_byNode = { }
    
    matrix_U_system_rows = 0  # Just in case the number of surfaces of the all the coarse nodes is not the same
    matrix_U_system_cols = 0  # Just in case the number of surfaces of the all the coarse nodes is not the same
    matrix_corners = {}
    corner = (0,0) # Postion of the left upper corner of the matrix in the RM of the system

    for n_id in coarse_nodes.keys():
        matrix_corners[n_id] = corner
        mat_u_n, mat_u_n_shape = build_U(
            fine_nodes[n_id],
            surf_area_relation[n_id],
            energy_g,
            probabilities[n_id]
        ) 
        matrix_U_byNode[n_id] = mat_u_n
        
        next_corner_row = corner[0] + mat_u_n_shape[0]
        next_corner_col = corner[1] + mat_u_n_shape[1]
        corner = (next_corner_row, next_corner_col)

        matrix_U_system_rows += len(mat_u_n)     # Just in case the number of surfaces of the all the coarse nodes is not the same
        matrix_U_system_cols += len(mat_u_n[0])  # Just in case the number of surfaces of the all the coarse nodes is not the same


    matrix_U_system_shape = (matrix_U_system_rows, matrix_U_system_cols)
    matrix_U_system = np.zeros(matrix_U_system_shape)


    for n_id in coarse_nodes.keys():
        corner = matrix_corners[n_id]
        resp_n = matrix_U_byNode[n_id]
        for r in range(resp_n.shape[0]):
            for c in range(resp_n.shape[1]):
                matrix_U_system[corner[0] + r][corner[1] + c] = resp_n[r][c]
                
    return matrix_U_system

def getPhiVector_byGlobalNode(coarse_nodes, fine_nodes, energy_g):
    phi_vectors = {}
    for node_id in coarse_nodes.keys():
        phi = build_phi(fine_nodes[node_id], energy_g)
        phi_vectors[node_id] = phi
    return phi_vectors

def getSource_byGllobalNode(coarse_nodes, fine_nodes, energy_g, xs, keff, phi):
    """
        It returns a dictionary with the source terms in it

    """
    
    source_Q_byGlobalNode = {}
    for n_id in coarse_nodes.keys():
        numReg = len(fine_nodes[n_id])
        source_Q = buildSourceVector(numReg, energy_g, fine_nodes[n_id], xs[n_id], keff, phi[n_id])
        source_Q_byGlobalNode[n_id] = source_Q

    return source_Q_byGlobalNode

def getJinVector_byNode(coarse_nodes, surf_area_relation, energy_g):
    j_vectors = {}
    for node_id in coarse_nodes.keys():
        j = build_phi(surf_area_relation[node_id], energy_g, )
        j_vectors[node_id] = j
    return j_vectors

def getJinVector_global(surf_relation):
    total_surfaces = 0 
    for relation in surf_relation.values():
        total_surfaces += len(relation)
    return np.ones(total_surfaces)

def build_S(local_cells, surface_relation, energy_g, xs, probabilities):
   
    _J = len(local_cells)
    _A = len(surface_relation)
    matrix_S = np.zeros((_J*energy_g, _A))

    surface_ids = list(surface_relation.keys())
    surface_areas = [surface_relation[s] for s in surface_ids]

    cell_ids = [cell.id for cell in local_cells]
    cell_materials = ["fuel", "coolant"]

    
    
    for g in range(energy_g):
        for j in range(len(cell_ids)):
            cell_id = cell_ids[j]
            vol_j = local_cells[j].volume
            region_j = cell_materials[j]
            xsTotal_j = xs[cell_id]["total"][g]
            row_index = j + g * _J
            for a in range(len(surface_ids)):
                area_a = surface_areas[a]
                s_id = surface_ids[a]
                p_a_j = probabilities[s_id][region_j][g]
                matrix_S[row_index][a] =  area_a * p_a_j / (xsTotal_j * vol_j)
    
    return matrix_S

def build_R(surf_area_relation, energy_g, probabilities):
    surface_ids = list(surf_area_relation.keys())
    _A = len(surface_ids)
    
    _B = len(surface_ids)

    surface_areas = [surf_area_relation[s] for s in surface_ids]

    responseMatrix_shape = (_A*energy_g, _B)
    
    responseMatrix_n = np.zeros(responseMatrix_shape)

    for g in range(energy_g):
        for a in range(_A):
            area_a = surface_areas[a]
            row_index = a + g * _A
            surf_a_id = surface_ids[a]
            for b in range(len(surface_ids)):
                surf_b_id = surface_ids[b]
                area_b = surface_areas[b]
                p_b_a = probabilities[surf_a_id]["surfaces"][surf_b_id][g]
                responseMatrix_n[row_index][b] =  area_b * p_b_a / area_a


    return responseMatrix_n, responseMatrix_shape

def build_T(local_cells, energy_g, xs, probabilities):
    _J = len(local_cells)
    _I = len(local_cells)
    
    matrix_T = np.zeros((_J*energy_g, _I))

    cell_ids = [cell.id for cell in local_cells]
    cell_materials = ["fuel", "coolant"]

    for g in range(energy_g):
        for j in range(len(cell_ids)):
            cell_id = cell_ids[j]
            vol_j = local_cells[j].volume
            region_j = cell_materials[j]
            xsTotal_j = xs[cell_id]["total"][g]
            row_index = j + g * _J
            for i in range(len(cell_ids)):
                vol_i = local_cells[i].volume
                region_i = cell_materials[i]
                p_i_j = probabilities[region_i][region_j][g]
                matrix_T[row_index][i] =  vol_i * p_i_j / (xsTotal_j * vol_j)
    
    return matrix_T

def build_U(local_cells, surf_area_relation, energy_g, probabilities):
    surface_ids = list(surf_area_relation.keys())
    _A = len(surface_ids)
    
    _I = len(local_cells)

    surface_areas = [surf_area_relation[s] for s in surface_ids]

    matrix_U_shape = (_A*energy_g, _I)
    matrix_U_n = np.zeros(matrix_U_shape)

    cell_materials = ["fuel", "coolant"]

    for g in range(energy_g):
        for a in range(_A):
            area_a = surface_areas[a]
            row_index = a + g * _A
            surf_a_id = surface_ids[a]
            for i in range(len(local_cells)):
                vol_i = local_cells[i].volume
                region_i = cell_materials[i]
                p_i_a = probabilities[region_i]["surfaces"][surf_a_id][g]
                matrix_U_n[row_index][i] =  vol_i * p_i_a / area_a


    return matrix_U_n, matrix_U_shape

def build_M(surf_relation, energy_g):
    print()
    numSurfaces = 0
    for n_id in surf_relation.keys():
        numSurfaces += len(surf_relation[n_id].keys())

    matrix_M_len = numSurfaces*energy_g
    matrix_M = np.zeros((matrix_M_len, matrix_M_len))
    for m in range(matrix_M_len):
        matrix_M[m][m] = 1
        # for c in range(matrix_M_len): # this is changing for the implenetation with more surfaces and contiguous cells
        #     pass

    return matrix_M

def build_phi(fine_nodes, energy_g):
    numRegions = len(fine_nodes)
    return np.ones(numRegions*energy_g)

def build_j(surfaces, energy_g):
    numSurfaces = len(surfaces.keys())
    return np.ones(numSurfaces*energy_g)

def buildSourceVector(numReg, energy_g, fine_nodes, xs, keff, phi):
    """
        It returns a vector with the source terms

        Q_g,i = [Q_g,1  Q_g,2  Q_g,3 ... Q_g,I]^T

    """
    _I = len(fine_nodes)
    
    cell_ids = [cell.id for cell in fine_nodes]

    source_Q = np.zeros(numReg*energy_g)
    
    for i in range(len(cell_ids)):
        cell_id = cell_ids[i]
        nuFiss = xs[cell_id]["nuSigFission"]
        chi = xs[cell_id]["chi"]
        scatterMatrix = xs[cell_id]["scatter"]
        for g in range(energy_g):
            row_index = i + g * _I # Index for the  Q vector according to the region and energy group
            q_value = 0
            for gp in range(energy_g):
                #sumation in gp
                row_index_p = i + gp * _I # Index for the phi value
                q_value += (scatterMatrix[gp][g] + chi[gp] * nuFiss[gp] / keff) * phi[row_index_p]
            source_Q[row_index] = q_value / (4 * np.pi)

    return source_Q

def buildJsource(matrixU, qVector):
    j_source = []
    print(qVector)
    numSurf, numReg = matrixU.shape
    
    print(matrixU)


    return j_source

