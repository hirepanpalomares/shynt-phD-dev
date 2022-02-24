import numpy as np


class SourcePhi:

    def __init__(self) -> None:
        pass



def buildPhiSource(matrixT, source, energy_g):
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
    # print(matrixT)
    for g in range(energy_g):
        systemPhi_vector = np.array([])
        for n_id in matrixT.keys():
            q_vector = source[n_id][g]
            mT = matrixT[n_id][g]
            phiSource = np.matmul(mT, q_vector)
            # To remove the following concatenate the mT should be in blovks and the q_vectors
            # with all the regions of the system, and not by eahch coarse node
            systemPhi_vector = np.concatenate((systemPhi_vector, phiSource), axis=0)
        phi_source[g] = systemPhi_vector
    
    # print(phi_source)
    return phi_source