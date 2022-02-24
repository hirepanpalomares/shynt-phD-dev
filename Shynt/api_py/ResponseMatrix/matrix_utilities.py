import numpy as np


def getInitializedPhi_byNode(coarse_nodes, energy_g):
    phi_vectors = {}

    for node_id, node in coarse_nodes.items():
        phi_vectors[node_id] = {}
        regions = node.fine_nodes_ids
        for r in regions:
            phi_vectors[node_id][r] = {}
            for g in range(energy_g):
                phi_vectors[node_id][r][g] = 1.0
    return phi_vectors













def getRegRegProbabilityMatrix_system(probabilities, coarse_nodes, energyG, regions_vol):
    
    probabilityM_byGroup = []
    cells = ["fuel", "coolant"]
    for g in range(energyG):
        probabilityMg_byNode = []
        for n_id in coarse_nodes.keys():
            probabilities_n = probabilities[n_id]
            regions = coarse_nodes[n_id].fine_nodes_ids
            numRegions = len(regions)
            mP = np.zeros((numRegions, numRegions))
            for r in range(numRegions):
                cell_mat_r = cells[r]
                region_id = regions[r]
                for rp in range(numRegions):
                    cell_mat_rp = cells[rp]
                    vol_rp = regions_vol[regions[rp]]
                    mP[r][rp] = probabilities_n[cell_mat_r][cell_mat_rp][g] 
            probabilityMg_byNode.append(mP)
        
        # print(probabilityMg_byNode)
        probM_System_g = getBlockMatrix(probabilityMg_byNode)
        probabilityM_byGroup.append(probM_System_g)
    
    probM_system = getBlockMatrix(probabilityM_byGroup)

    # print(probM_system)
    

    return probM_system

def getRegRegProbabilityMatrix_byCoarse_byGroup(probabilities, coarse_nodes, energyG, regions_vol):
    
    probabilityM_byCoarse_byGroup = {}
    cells = ["fuel", "coolant"]
    for n_id in coarse_nodes.keys():
        probabilityM_byCoarse_byGroup[n_id] = {}
        
        regions = coarse_nodes[n_id].fine_nodes_ids
        probabilities_n = probabilities[n_id]
        numRegions = len(regions)
        for g in range(energyG):    
            mP = np.zeros((numRegions, numRegions))
            for i in range(numRegions):
                cell_mat_i = cells[i]
                region_id_i = regions[i]
                for j in range(numRegions):
                    cell_mat_j = cells[j]
                    mP[i][j] = probabilities_n[cell_mat_i][cell_mat_j][g] 
            probabilityM_byCoarse_byGroup[n_id][g] = mP
        

    return probabilityM_byCoarse_byGroup








def getBlockMatrix(matrixes):
    """
        Convert a tuple of matrixes into a one big block matrix
    """
    numMatrixes = len(matrixes)

    corner = (0,0)
    matrix_corners = []
    for matrix in matrixes:
        matrix_corners.append(corner)
        m_shape = matrix.shape
        corner = (
            corner[0] + m_shape[0], 
            corner[1] + m_shape[1]
        ) # The final value of the corner gives the Big matrix shape

    bigM = np.zeros(corner)
    for m in range(numMatrixes):
        matrix = matrixes[m]
        corner = matrix_corners[m]
        for r in range(len(matrix)):
            row = matrix[r]
            for c in range(len(row)):
                bigM[corner[0] + r][corner[1] + c] = matrix[r][c]
    return bigM