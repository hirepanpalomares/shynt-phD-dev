import numpy as np

def solveGlobalProblem(energy_g, inverse_IMR, mM, j_source_byGroup):
    
    j_in = {}
    for g in range(energy_g):
        j_source = j_source_byGroup[g]
        inverse = inverse_IMR[g]
        inverse_x_mM = np.matmul(inverse, mM)
        j_in_vector = np.matmul(inverse_x_mM, j_source)
        j_in[g] = j_in_vector

    return j_in

def solveGlobalProblem_sys(energy_g, inverse_IMR, mM, j_source):
    inverse_x_mM = np.matmul(inverse_IMR, mM)
    j_in_vector = np.matmul(inverse_x_mM, j_source)

    return j_in_vector