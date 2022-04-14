import numpy as np



def buildPhiSource(coarse_nodes, matrixT, source, energy_g):
    """
        This method builds the phi source vector of the system
        by energy group


        phi_source = {
            g0: array([]),
            g1: array([]),
            .
            .
            .
            gG: array([]),
        }
    """
    phi_source = {}
    for g in range(energy_g):
        mT = matrixT[g]
        q_vector = source[g]
        phi_s = np.matmul(mT, q_vector)
        phi_source[g] = phi_s
    
    # print(phi_source)
    return phi_source