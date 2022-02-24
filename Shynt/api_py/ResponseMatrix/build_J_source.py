import numpy as np


class SourceJ:

    def __init__(self) -> None:
        pass



def buildJsource(matrixU, source, energy_g):
    j_source = {}
    print(matrixU)
    

    total_j_source = np.array([])
    for g in range(energy_g):
        system_vector = np.array([])
        for n_id, values in matrixU.items():
            q_vector = source[n_id][g]
            
            j_s = np.matmul(matrixU[n_id][g], q_vector)
            system_vector = np.concatenate((system_vector, j_s), axis=0)
            # print(system_vector)
        # print()
        total_j_source = np.concatenate((total_j_source, system_vector), axis=0)
        j_source[g] = system_vector
    
    # print(total_j_source)
    # print(j_source)

    return j_source
    # return total_j_source