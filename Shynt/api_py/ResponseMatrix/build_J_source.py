import numpy as np


def buildJsource(coarse_nodes, matrixU, source, energy_g):
    """
        Calculate the vector J_source 


        returns
        ---------
        {
            g0: array([js1, js2, ...., jsA])
            g1: array([js1, js2, ...., jsA])
            ...
            ...
        }
    
    """
    j_source = {}
    for g in range(energy_g):
        matU = matrixU[g]
        q_vector = source[g]
        j_s = np.matmul(matU, q_vector)
        j_source[g] = j_s
    
    # print(total_j_source)
    # print(j_source)

    return j_source
    # return total_j_source