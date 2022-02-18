
from platform import node
import numpy as np

from Shynt.api_py.ResponseMatrix.build_matrix import Source, buildJsource, buildPhiSource

def solveKeff(k_guess, phi_guess, coarse_nodes, fine_nodes, energy_g, xs, matrixes, node_order, probabilities):

    matrixS_byNode = matrixes["S"]  # Ordered by node and by energy group
    matrixT_byNode = matrixes["T"]  # Ordered by node and by energy group
    matrixU_byNode = matrixes["U"]  # Ordered by node and by energy group
    matrixR_system = matrixes["R"]  # system ready by group
    matrixM_system = matrixes["M"]  # system ready 



    all_regions = []
    coarse_fine_rel = {}
    coarse_surf_rel = {}
    regions_vol = {}
    all_surfaces = []
    for n_id in node_order:
        regions = coarse_nodes[n_id].fine_nodes_ids
        surfaces = coarse_nodes[n_id].surface_ids
        vols = coarse_nodes[n_id].fine_nodes_volume
        regions_vol.update(vols)
        all_regions += regions
        all_surfaces += surfaces
        for r in regions:
            coarse_fine_rel[r] = n_id
        for s in surfaces:
            coarse_surf_rel[s] = n_id


    keff_init = k_guess
    phi_init = phi_guess

    
    tolerance = 0.000001
    difference = 1
    
    print("#"*100) 
    systemSource = Source(
        coarse_nodes, 
        energy_g, 
        xs, 
        keff_init, 
        phi_init
    )
    while difference >= tolerance:
        print("#"*100) 

        # Calculating the Source 
        

        # Solving the Global problem
        source_Q = systemSource.calculate_Qvector(keff_init, phi_init)
        print("source ", source_Q)

        j_source_byGroup = buildJsource(
            matrixU_byNode, source_Q, energy_g
        )
        j_in = solveGlobalProblem(
            energy_g, matrixM_system, matrixR_system, j_source_byGroup
        )
        print(j_in)
        raise SystemExit

        j_in_n = splitJin(
            j_in, node_order, coarse_nodes, energy_g
        )


        # Solving local problem:
        phi_source_n = buildPhiSource(matrixT_byNode, source_Q, energy_g)
        phi_new = solveLocalProblem(matrixS_byNode, j_in_n, phi_source_n, energy_g, coarse_nodes)
        
        # power iteration
        keff_new = power_iteration(
            keff_init, 
            phi_init, 
            phi_new, 
            energy_g, 
            coarse_nodes, 
            xs, 
            probabilities, 
            all_regions,
            coarse_fine_rel,
            regions_vol
        )

        print("keff: ", keff_new)
        print("phi", phi_new)

        # error previous iteration
        difference = abs(keff_new - keff_init)

        # update for the next iteration
        keff_init = keff_new
        phi_init = phi_new
        # break
        


    return  0


def solveGlobalProblem(energy_g, matrixM_system, matrixR_system, j_source_byGroup):
    j_in = {}
    mM = matrixM_system
    for g in range(energy_g):
        mR = matrixR_system[g]
        j_source = j_source_byGroup[g]
        mM_x_mR = np.matmul(mM, mR)
        identityMatrix = np.identity(mM_x_mR.shape[0])
        matrix_to_invert = identityMatrix - mM_x_mR
        inverse = np.linalg.inv(matrix_to_invert)
        mM_x_jsource = np.matmul(mM, j_source)
        j_in_vector = np.matmul(inverse, mM_x_jsource)
        j_in[g] = j_in_vector

    
    
    return j_in



def solveLocalProblem(matrixS_n, j_in_n, phi_source_n, energy_g, coarse_nodes):
    phi = {}
    
    for n_id, node in coarse_nodes.items():
        mS_byG = matrixS_n[n_id]
        phi[n_id] = {}
        regions_n = node.fine_nodes_ids
        for r in regions_n:
            phi[n_id][r] = {}
        for g in range(energy_g):
            mS = mS_byG[g]
            phi_source = phi_source_n[g][n_id]
            jin = j_in_n[g][n_id]
            
            mS_x_jin = np.matmul(mS, jin)

            local_solution = mS_x_jin + phi_source

            for r in range(len(regions_n)):
                phi[n_id][regions_n[r]][g] = local_solution[r]

    return phi
    


def splitJin(j_in, node_order, coarse_nodes, energy_g):
    """
        This method splits the vector of the current in each coarse node
        including each one the currents in the corresponding coarse node


    """
    j_in_splitted = {}

    for g in range(energy_g):
        j_in_splitted[g] = {}

        start_index = 0
        for n_id in node_order:
            vector_ = []
            node = coarse_nodes[n_id]
            num_surfaces = len(node.surface_ids)
            end_index = start_index + num_surfaces
            for i in range(start_index, end_index):
                vector_.append(j_in[g][i])
            j_in_splitted[g][n_id] = np.array(vector_)

            start_index = end_index
        
    return j_in_splitted


def power_iteration(k_prev, phi_prev, phi_new, energy_g, coarse_nodes, xs, probabilities, all_regions, coarse_fine_rel, regions_vol):
    
    

    # initializing vectors
    
    numRegions = len(all_regions)
    phi_power_prev = np.zeros(numRegions * energy_g)
    phi_power_new = np.zeros(numRegions * energy_g)

    # filling vectors
    # print(phi_new)
    # print(phi_prev)
    for j in range(numRegions):
        for g in range(energy_g):
            index_ = numRegions * g + j
            phi_power_prev[index_] = calculate_power_vector_term(
                coarse_fine_rel,
                all_regions,
                regions_vol,
                energy_g,
                j, g,
                probabilities,
                xs,
                phi_prev
            )
            phi_power_new[index_] = calculate_power_vector_term(
                coarse_fine_rel,
                all_regions,
                regions_vol,
                energy_g,
                j, g,
                probabilities,
                xs,
                phi_new
            )

    # print(phi_power_new)
    # print(phi_power_prev)
    


    numerator_dot_product = np.inner(phi_power_prev, phi_power_new)
    denominator_dot_product = np.inner(phi_power_prev, phi_power_prev)
    k_new = k_prev * numerator_dot_product / denominator_dot_product


    return k_new


def calculate_power_vector_term(coarse_fine_rel, regions, regions_vol, energy_g, j, g, probabilities, xs, flux):
    region_materials = ["fuel", "coolant"]

    
    numRegions = len(regions)
    term = 0
    for i in range(numRegions):
        region_i_id = regions[i]
        coarse_id = coarse_fine_rel[region_i_id]
        mat_j = region_materials[j]
        mat_i = region_materials[i]
        vol_i = regions_vol[region_i_id]
        chi = xs[coarse_id][region_i_id]["chi"][g]
        p_i_j = probabilities[coarse_id][mat_i][mat_j][g]
        sumation_energy = 0
        
        for gp in range(energy_g):
            nuFiss = xs[coarse_id][region_i_id]["nuSigFission"][gp]
            phi = flux[coarse_id][region_i_id][gp]
            sumation_energy += nuFiss * phi
        term += vol_i * p_i_j * chi * sumation_energy

    return term