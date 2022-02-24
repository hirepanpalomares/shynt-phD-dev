import numpy as np

from Shynt.api_py.ResponseMatrix.matrix_utilities import getInitializedPhi_byNode

from Shynt.api_py.ResponseMatrix.build_J_source import buildJsource
from Shynt.api_py.ResponseMatrix.build_matrix_M import getM_matrix
from Shynt.api_py.ResponseMatrix.build_matrix_R import getResponseMatrix_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_R import getResponseMatrix_system
from Shynt.api_py.ResponseMatrix.build_matrix_S import getMatrixS_byNode_byGroup, getMatrixS_system_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_T import getMatrixT_byNode_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_U import getMatrixU_byNode_byGroup
from Shynt.api_py.ResponseMatrix.build_Phi_Source import buildPhiSource
from Shynt.api_py.ResponseMatrix.build_source_Q import Source


def solveKeff(coarse_nodes, fine_nodes, energy_g, xs, probabilities, mesh_info):


    # Guessing of phi and k ------------------------------------------------------
    phi_guess = getInitializedPhi_byNode(coarse_nodes, energy_g)
    keff_guess = 1


    # Building matrixes and source -----------------------------------------------
    matrixU = getMatrixU_byNode_byGroup(coarse_nodes, energy_g, probabilities) # ready
    matrixR = getResponseMatrix_byGroup(coarse_nodes, energy_g, probabilities, mesh_info) # ready
    matrixM = getM_matrix(coarse_nodes, energy_g) # ready 
    matrixS = getMatrixS_system_byGroup(coarse_nodes, energy_g, xs, probabilities) # ready
    matrixT = getMatrixT_byNode_byGroup(coarse_nodes, energy_g, xs, probabilities) # ready
    

    systemSource = Source(
        coarse_nodes, 
        energy_g, 
        xs
    )


    # Guessing initial keff and phi

    keff_prev = keff_guess
    phi_prev = phi_guess

    tolerance = 0.000001
    difference = 1
    
    print("#"*100) 
    
    while difference >= tolerance:
        print("#"*100) 

        # Calculating the Source 
        source_Q = systemSource.calculate_Qvector(keff_prev, phi_prev) # checked
        print("source Q ", source_Q)
        


        # Solving the Global problem
        j_source_total = buildJsource(
            matrixU, source_Q, energy_g
        )
        print("j_source: ", j_source_total)

        # print("-"*100)
        # print("Global Problem")
        # print(j_source_byGroup)
        j_in = solveGlobalProblem(
            energy_g, matrixM, matrixR, j_source_total
        ) 
        print("j_in", j_in)


        # Solving local problem:
        phi_source_n = buildPhiSource(matrixT, source_Q, energy_g)

        print("phi source", phi_source_n)
        phi_new = solveLocalProblem(matrixS, j_in, phi_source_n, energy_g, coarse_nodes)
        print("phi_new", phi_new)
        raise SystemExit
        
        
        # power iteration
        # keff_new = power_iteration_value_by_value(
        #     keff_init, 
        #     phi_init, 
        #     phi_new, 
        #     energy_g, 
        #     coarse_nodes, 
        #     xs, 
        #     probabilities, 
        #     all_regions,
        #     coarse_fine_rel,
        #     regions_vol
        # )

        # raise SystemExit
        keff_new = power_iteration_matrixes(
            systemSource,
            keff_prev,
            phi_prev,
            phi_new,
            probabilities,
            coarse_nodes, 
            energy_g,
            mesh_info,
            xs
        )

        print("keff: ", keff_new)
        print("phi", phi_new)

        # error previous iteration
        difference = abs(keff_new - keff_prev)

        # update for the next iteration
        keff_prev = keff_new
        phi_prev = phi_new
        # break
        


    return  0


def solveGlobalProblem(energy_g, matrixM_system, matrixR_system, j_source_byGroup):
    # print(matrixM_system)
    # print(matrixR_system)
    # print(j_source_byGroup)
    j_in = {}
    mM = matrixM_system
    for g in range(energy_g):
        mR = matrixR_system[g]
        j_source = j_source_byGroup[g]
        # print("mR", mR)
        mM_x_mR = np.matmul(mM, mR)
        # print("multiplitic", mM_x_mR)
        identityMatrix = np.identity(mM_x_mR.shape[0])
        matrix_to_invert = identityMatrix - mM_x_mR
        # print("to invert: ", matrix_to_invert)
        inverse = np.linalg.inv(matrix_to_invert)
        # print("inverse: ", inverse)
        inverse_x_mM = np.matmul(inverse, mM)
        # print(inverse_x_mM)
        print(j_source)
        # print("mpor Jsource", mM_x_jsource)
        j_in_vector = np.matmul(inverse_x_mM, j_source)
        j_in[g] = j_in_vector
        print("*"*100)
    
    # mM = matrixM_system
    # mR = matrixR_system
    # j_source = j_source_byGroup

    # mM_x_mR = np.matmul(mM, mR)
    # identityMatrix = np.identity(mM_x_mR.shape[0])
    # matrix_to_invert = identityMatrix - mM_x_mR
    # inverse = np.linalg.inv(matrix_to_invert)
    
    # mM_x_jsource = np.matmul(mM, j_source)
    # j_in = np.matmul(inverse, mM_x_jsource)
    
    
    
    return j_in



def solveLocalProblem(matrixS_n, jin_system, phi_source_n, energy_g, coarse_nodes):
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
    



def power_iteration_value_by_value(k_prev, phi_prev, phi_new, energy_g, coarse_nodes, xs, probabilities, all_regions, coarse_fine_rel, regions_vol):
    
    

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

    print("222")
    print(phi_power_new)
    print(phi_power_prev)
    


    numerator_dot_product = np.inner(phi_power_prev, phi_power_new)
    denominator_dot_product = np.inner(phi_power_prev, phi_power_prev)
    k_new = k_prev * numerator_dot_product / denominator_dot_product


    return k_new


def power_iteration_matrixes(systemSource, keff_prev, phi_prev, phi_new, probabilities, coarse_nodes, energyG, mesh_info, xs):
    # print("¤"*100)
    regions_vol = mesh_info.all_regions_vol

    fission_source_prev = systemSource.buildFissionSource(phi_prev)
    fission_source_new = systemSource.buildFissionSource(phi_new)

    regions_vol_vector = np.array([regions_vol[r] for r in regions_vol])
    p_r_rp_matrix = getRegRegProbabilityMatrix_system(probabilities, coarse_nodes, energyG, regions_vol)

    phi_power_prev = np.matmul(p_r_rp_matrix, fission_source_prev)
    phi_power_new = np.matmul(p_r_rp_matrix, fission_source_new)
    print("new:  ", phi_power_new)
    print("prev: ", phi_power_prev)

    numerator_dot_product = np.inner(phi_power_prev, phi_power_new)
    denominator_dot_product = np.inner(phi_power_prev, phi_power_prev)
    # print(numerator_dot_product)
    # print(denominator_dot_product)

    k_new = keff_prev * numerator_dot_product / denominator_dot_product




    # -----------------------------------------------------------------------
    regions = mesh_info.all_regions_order
    regions_vol = mesh_info.all_regions_vol
    coarse_reg_rel = mesh_info.coarse_region_rel
    coarse_order = mesh_info.coarse_order

    
    vector_prev = []
    vector_new = []
    # print(phi_prev)
    p_i_j_byCoarse_byGroup = getRegRegProbabilityMatrix_byCoarse_byGroup(probabilities, coarse_nodes, energyG, regions_vol)
    # print(p_i_j_byCoarse_byGroup)
    for g in range(energyG):
        for n_id in coarse_order:
            regions = mesh_info.coarse_region_rel[n_id]
            numRegions = len(regions)
            for j in range(numRegions):
                # Sumation for each term starts -----------
                reg_j_id = regions[j]
                sum_i_prev = 0
                sum_i_new = 0
                for i in range(numRegions):
                    reg_i_id = regions[i]
                    
                    sum_gp_prev = 0
                    sum_gp_new = 0
                    xs_reg_i = xs[n_id][reg_i_id]
                    for gp in range(energyG):
                        nuFiss = xs_reg_i["nuSigFission"][gp]
                        flux_igp_prev = phi_prev[n_id][reg_i_id][gp]
                        flux_igp_new = phi_new[n_id][reg_i_id][gp]
                        sum_gp_prev += nuFiss * flux_igp_prev
                        sum_gp_new += nuFiss * flux_igp_new
                    vol_i = regions_vol[reg_i_id]
                    chi_g_i = xs_reg_i["chi"][g]
                    p_g_i_j = p_i_j_byCoarse_byGroup[n_id][g][i][j]
                    sum_i_new += vol_i * p_g_i_j * chi_g_i * sum_gp_new
                    sum_i_prev += vol_i * p_g_i_j * chi_g_i * sum_gp_prev
                vector_new.append(sum_i_new)
                vector_prev.append(sum_i_prev)

    vector_new = np.array(vector_new)
    vector_prev = np.array(vector_prev)
    print("new:  ", vector_new)
    print("prev: ", vector_prev) 

    numerator_dot_product = np.inner(vector_prev, vector_new)
    denominator_dot_product = np.inner(vector_prev, vector_prev)
    # print(numerator_dot_product)
    # print(denominator_dot_product)

    k_new = keff_prev * numerator_dot_product / denominator_dot_product




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