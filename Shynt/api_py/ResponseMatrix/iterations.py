import numpy as np
import matplotlib.pyplot as plt
from Shynt.api_py import energy
from Shynt.api_py.ResponseMatrix.matrix_utilities import getInitializedPhi_system_byGroup


from Shynt.api_py.ResponseMatrix.build_J_source import buildJsource
from Shynt.api_py.ResponseMatrix.build_matrix_M import getM_matrix
from Shynt.api_py.ResponseMatrix.build_matrix_R import getResponseMatrix_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_S import getMatrixS_system_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_T import getMatrixT_system_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_U import getMatrixU_system_byGroup
from Shynt.api_py.ResponseMatrix.build_Phi_Source import buildPhiSource
from Shynt.api_py.ResponseMatrix.build_source_Q import SourceQ


def solveKeff(coarse_nodes, energy_g, xs, probabilities, mesh_info):

    # Useful mesh information ----------------------------------------------------
    coarse_nodes_order = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    all_surfaces = mesh_info.all_surfaces_order
    coarse_nodes_map = mesh_info.coarse_nodes_map
    all_regions_order = mesh_info.all_regions_order
    numRegions = len(all_regions_order)


    # Guessing of phi and k ------------------------------------------------------
    phi_guess = getInitializedPhi_system_byGroup(numRegions, energy_g)
    keff_guess = 1

    # Building the source
    systemSource = SourceQ(coarse_nodes_order, coarse_nodes_regions, energy_g, xs)
    fission_source = systemSource.buildFissionSource(mesh_info, probabilities) # for power iteration

    # Building matrixes -----------------------------------------------------------
    matrixU = getMatrixU_system_byGroup(mesh_info, energy_g, probabilities) # ready
    matrixT = getMatrixT_system_byGroup(mesh_info, energy_g, xs, probabilities) # ready

    matrixR = getResponseMatrix_byGroup(mesh_info, energy_g, probabilities) # ready
    matrixM = getM_matrix(coarse_nodes_map, coarse_nodes, all_surfaces) # ready 
    inverse_IMR = calculate_inverseIMR(matrixM, matrixR, energy_g)

    matrixS = getMatrixS_system_byGroup(mesh_info, energy_g, xs, probabilities) # ready
    
    


    # Guessing initial keff and phi

    keff_prev = keff_guess
    phi_prev = phi_guess

    tolerance = 1E-10
    k_converge = 1
    phi_converge = 1
    
    print() 
    iteration = 1
    k_array = []

    while k_converge >= tolerance and phi_converge >= tolerance:
        print("-"*50)

        # Estimating the Source 
        source_Q_vectors = systemSource.calculate_Qvector(keff_prev, phi_prev, all_regions_order) # checked
        j_source = buildJsource(coarse_nodes_order, matrixU, source_Q_vectors, energy_g)
        phi_source = buildPhiSource(coarse_nodes_order, matrixT, source_Q_vectors, energy_g)

        # Solving the Global problem
        j_in = solveGlobalProblem(energy_g, inverse_IMR, matrixM, j_source) 

        # Solving local problem:
        phi_new = solveLocalProblem(matrixS, j_in, phi_source, energy_g, all_regions_order, coarse_nodes_regions)
        
        
        # power iteration
        keff_new = power_iteration(phi_new, phi_prev, keff_prev, fission_source, all_regions_order, energy_g)    
        k_array.append(keff_new)
        print("keff: ", keff_new)

        # check convergence
        k_converge, phi_converge = check_convergence(keff_prev, keff_new, phi_prev, phi_new, energy_g)
        print("keff converge:", k_converge)
        print("phi converge:", phi_converge)
        print("iteration:", iteration)

        
        # update for the next iteration
        keff_prev = keff_new
        phi_prev = phi_new
        
        iteration += 1
        
        

    
    plt.plot(k_array)
    plt.savefig("k_convergence.png")


    return  {
        "keff": keff_new, 
        "phi": order_flux_output(phi_new, mesh_info, energy_g),
        "keff_convergence": k_converge,
        "flux_convergence": phi_converge, 
        "iterations": iteration
    }


def check_convergence(k_prev, k_new, phi_prev, phi_new, energy_g):
    k_converge = abs(k_new - k_prev)/k_new

    max_phi_prev = np.zeros(energy_g)
    max_phi_new = np.zeros(energy_g)

    for g in range(energy_g):
        max_phi_new[g] = phi_new[g].max()
        max_phi_prev[g] = phi_prev[g].max()

    max_phi_prev = max_phi_prev.max()
    max_phi_new = max_phi_new.max()
    phi_converge = abs(max_phi_new - max_phi_prev) / max_phi_new 

    return k_converge, phi_converge


def calculate_inverseIMR(matrixM, matrixR, energy_g):
    inv = {}
    mM = matrixM
    for g in range(energy_g):
        mR = matrixR[g]
        mM_x_mR = np.matmul(mM, mR)
        identityMatrix = np.identity(mM_x_mR.shape[0])
        matrix_to_invert = identityMatrix - mM_x_mR
        inverse = np.linalg.inv(matrix_to_invert)
        inv[g] = inverse
    return inv


def solveGlobalProblem(energy_g, inverse_IMR, mM, j_source_byGroup):
    
    j_in = {}
    for g in range(energy_g):
        j_source = j_source_byGroup[g]
        inverse = inverse_IMR[g]
        inverse_x_mM = np.matmul(inverse, mM)
        j_in_vector = np.matmul(inverse_x_mM, j_source)
        j_in[g] = j_in_vector

    return j_in


def solveLocalProblem(matrixS_n, jin_system, phi_source_n, energy_g, regions_order, coarse_nodes_regions):
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
    
    # order phi in a dictionary
    # region_phi = {}
    # numRegions = len(regions_order)
    # for r in range(numRegions):
    #     reg_id = regions_order[r]
    #     region_phi[reg_id] = []
    #     array = np.zeros(energy_g)
    #     for g in range(energy_g):
    #         array[g] = phi[g][r]    
    #     region_phi[reg_id] = array
    
    # ordered_phi = {
    #     n_id: {} for n_id in coarse_nodes_regions.keys()
    # }
    # for n_id, regions in coarse_nodes_regions.items():
    #     for r in regions:
    #         ordered_phi[n_id][r] = region_phi[r]

    return phi


def power_iteration(phi_new, phi_prev, keff_prev, fission_source, all_regions, energy_g):
    
    phi_new = create_long_vector_flux(phi_new, energy_g, all_regions)
    phi_prev = create_long_vector_flux(phi_prev, energy_g, all_regions)
    
    vector_prev = np.matmul(fission_source, phi_prev)
    vector_new = np.matmul(fission_source, phi_new)

    new_product = np.inner(vector_prev, vector_new)
    prev_product = np.inner(vector_prev, vector_prev)
    
    k_new = keff_prev * new_product / prev_product

    return k_new


def create_long_vector_flux(phi, energy_g, all_regions):
    numRegions = len(all_regions)
    vector = np.zeros(energy_g*numRegions)

    for r in range(numRegions):
        reg_id = all_regions[r]
        for g in range(energy_g):
            flux_val = phi[g][r]
            index = r * energy_g + g
            vector[index] = flux_val

    return vector


def order_flux_output(flux_group, mesh_info, energy_g):
    """
        This method orders the flux in a dictionary per coarse node
        and per region per energy group

        phi = {
            g0: {
                coarse_id : {
                    reg_1: <float_number>,
                    reg_2: <float_number>,
                    .
                    .
                    reg_n: <float_number>
                }
            },
            g1: { ... }
            .
            .
            gG: { ... }
        }

    """
    
    all_regions_order = mesh_info.all_regions_order
    coarse_order = mesh_info.coarse_order
    region_coarse_rel = mesh_info.region_coarse_rel
    
    phi_output = {
        g: {
            c_id: {} for c_id in coarse_order
        } for g in range(energy_g)
    }

    for g in range(energy_g):
        for r in range(len(all_regions_order)):
            region =  all_regions_order[r]
            coarse_id = region_coarse_rel[region]
            phi_output[g][coarse_id][region] = flux_group[g][r]
    
    return phi_output
    
    
    

