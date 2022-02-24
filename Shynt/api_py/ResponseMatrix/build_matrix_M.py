import numpy as np


def getM_matrix(coarse_nodes, energy_g):
    
    matrix_M = {}

    numTotalSurfaces = 0
    for n_id, node in coarse_nodes.items():
        surfaces_n = node.surface_ids
        numTotalSurfaces += len(surfaces_n)

    matrix_M_len = numTotalSurfaces
    matrix_M = np.identity(matrix_M_len)
    
    # print(matrix_M)
    return matrix_M