import numpy as np


def solveLocalProblem(matrixS_n, jin_system, phi_source_n, energy_g):
    """
        It gives the solution of the flux by enery group

        phi = {
            g0: array([]),
            g1: array([]),
            .
            .
            gG: array([])
        }

        Each array contains the scalar flux for all the regions 
        in the system
    """
    
    phi = {}
    
    for g in range(energy_g):
        mS = matrixS_n[g]
        phi_source = phi_source_n[g]
        jin = jin_system[g]
        mS_x_jin = np.matmul(mS, jin)

        local_solution = mS_x_jin + phi_source
        phi[g] = local_solution
    
    return phi
