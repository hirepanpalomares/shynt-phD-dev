from unittest import removeResult
import numpy as np
import matplotlib.pyplot as plt

from Shynt.api_py import energy

from Shynt.api_py.ResponseMatrix.global_problem import solveGlobalProblem, solveGlobalProblem_sys
from Shynt.api_py.ResponseMatrix.local_problem import solveLocalProblem, solveLocalProblem_sys
from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix, getInitializedPhi_system, getInitializedPhi_system_byGroup
from Shynt.api_py.ResponseMatrix.build_J_source import buildJsource, buildJsource_sys, buildJsourceTBT
from Shynt.api_py.ResponseMatrix.build_matrix_M import getM_matrix
from Shynt.api_py.ResponseMatrix.build_matrix_R import getResponseMatrix_byGroup, getResponseMatrix_system
from Shynt.api_py.ResponseMatrix.build_matrix_S import getMatrixS_system, getMatrixS_system_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_T import getMatrixT_system, getMatrixT_system_byGroup
from Shynt.api_py.ResponseMatrix.build_matrix_U import getMatrixU_system, getMatrixU_system_byGroup
from Shynt.api_py.ResponseMatrix.build_Phi_Source import buildPhiSource, buildPhiSource_sys, buildPhiSourceTBT
from Shynt.api_py.ResponseMatrix.build_source_Q import SourceQ



def solveKeff(root, xs, probabilities, mesh_info):
    energy_g = root.energy_grid.energy_groups
    coarse_nodes = root.model_cell.global_mesh.coarse_nodes

    # Useful mesh information ----------------------------------------------------
    coarse_nodes_order = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    all_surfaces = mesh_info.all_surfaces_order
    coarse_nodes_map = mesh_info.coarse_nodes_map
    all_regions_order = mesh_info.all_regions_order
    numRegions = len(all_regions_order)


    # Guessing of phi and k ------------------------------------------------------
    # phi_guess = getInitializedPhi_system_byGroup(numRegions, energy_g)
    # keff_guess = 1

    # Building matrixes -----------------------------------------------------------
    # matrixS = getMatrixS_system_byGroup(mesh_info, energy_g, xs, probabilities) # ready
    # matrixU_bg = getMatrixU_system_byGroup(mesh_info, energy_g, probabilities) # ready
    # matrixT_bg = getMatrixT_system_byGroup(mesh_info, energy_g, xs, probabilities) # read
    # matrixR = getResponseMatrix_byGroup(mesh_info, energy_g, probabilities) # ready
    # matrixM = getM_matrix(coarse_nodes_map, coarse_nodes, all_surfaces, mesh_info.type_system) # ready 
    # inverse_IMR = calculate_inverseIMR(matrixM, matrixR, energy_g)
    

    matrixS = getMatrixS_system(mesh_info, energy_g, xs, probabilities) # ready 
    matrixU = getMatrixU_system(mesh_info, energy_g, probabilities) # ready
    matrixT = getMatrixT_system(mesh_info, energy_g, xs, probabilities) # read
    matrixR = getResponseMatrix_system(mesh_info, energy_g, probabilities) # ready    
    matrixM = getM_matrix(coarse_nodes_map, coarse_nodes, all_surfaces, mesh_info.type_system) # ready 
    matrixM_sys = [matrixM for g in range(energy_g)]
    matrixM_sys = getBlockMatrix(matrixM_sys)
    inverse_IMR = calculate_inverseIMR_sys(matrixM_sys, matrixR)
    

    # Building the source
    systemSource = SourceQ(coarse_nodes_order, coarse_nodes_regions, energy_g, xs) # scattering matrix and fission matrix per region
    fission_source = systemSource.buildFissionSource(mesh_info, probabilities) # for power iteration
    
    # Guessing initial keff and phi
    phi_guess = getInitializedPhi_system(numRegions, energy_g)
    # phi_guess = getInitializedPhi_system_byGroup(numRegions, energy_g)

    keff_guess = 1

    keff_prev = keff_guess
    phi_prev = phi_guess

    tolerance = 1E-10
    k_converge = 1
    phi_converge = 1
    
    print() 
    iteration = 1
    k_array = []
    phi_source_array = []
    print(matrixS)
    print(matrixT)
    print(matrixU) 
    print(matrixR)
    iii = input()
    while k_converge >= tolerance or phi_converge >= tolerance:
        print("-"*50)

        # Estimating the Source --------------------------------
        source_Q_vectors = systemSource.calculate_Qvector(keff_prev, phi_prev, all_regions_order) # checked


        # j_source = buildJsource(coarse_nodes_order, matrixU_bg, source_Q_vectors, energy_g)
        # phi_source = buildPhiSource(coarse_nodes_order, matrixT_bg, source_Q_vectors, energy_g)
        # j_sourceTBT = buildJsourceTBT(energy_g, mesh_info, probabilities, xs, keff_prev, phi_prev)
        # phi_sourceTBT = buildPhiSourceTBT(energy_g, mesh_info, probabilities, xs, keff_prev, phi_prev)
        
        # Solving the Global problem------------------------------
        # j_in = solveGlobalProblem(energy_g, inverse_IMR, matrixM, j_source) 
        # Solving local problem: ---------------------------------
        # phi_new = solveLocalProblem(matrixS, j_in, phi_source, energy_g)
        # ---------------------------------------------------------------------------------------

        j_source_sys = buildJsource_sys(matrixU, source_Q_vectors, energy_g)
        phi_source_sys = buildPhiSource_sys(matrixT, source_Q_vectors, energy_g)
        
        phi_source_array.append(phi_source_sys)

        j_in_sys = solveGlobalProblem_sys(energy_g, inverse_IMR, matrixM_sys, j_source_sys) 
        phi_new = solveLocalProblem_sys(matrixS, j_in_sys, phi_source_sys)

        # power iteration -----------------------------------------
        keff_new = power_iteration_sys(phi_new, phi_prev, keff_prev, fission_source, all_regions_order, energy_g)    
        # keff_new = power_iteration(phi_new, phi_prev, keff_prev, fission_source, all_regions_order, energy_g)    
        k_array.append(keff_new)



        print("keff: ", keff_new)
        # check convergence
        # k_converge, phi_converge = check_convergence(keff_prev, keff_new, phi_prev, phi_new, energy_g)
        k_converge, phi_converge = check_convergence_sys(keff_prev, keff_new, phi_prev, phi_new, energy_g)
        print(f"keff converge: {k_converge:.8E}")
        print(f"phi converge: {phi_converge:.8E}")
        print(f"convergence tolerance: {tolerance:.8E}")
        print("iteration:", iteration)
        print(phi_new)

        # update for the next iteration
        keff_prev = keff_new
        phi_prev = phi_new
        iteration += 1
        # inputtt = input()
        
    # phi_output = order_flux_output(phi_new, mesh_info, energy_g)
    phi_output = order_flux_output_sys(phi_new, mesh_info, energy_g)

    print(phi_output)
    flux_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, phi_new, j_in_sys)
    current_eq_proof(probabilities, source_Q_vectors, mesh_info, energy_g, xs, phi_new, j_in_sys)

    return  {
        "keff": keff_new,
        "phi": phi_output,
        "keff_convergence": k_converge,
        "flux_convergence": phi_converge, 
        "iterations": iteration,
        "phi_source": phi_source_array
    }


def flux_eq_proof(probabilities, source, mesh_info, energy_g, xs, flux, j_in):
    left =  []
    right = []
    
    all_regions = mesh_info.all_regions_order
    all_surfaces = mesh_info.all_surfaces_order

    numRegions = len(all_regions)
    numSurfaces = len(all_surfaces)
    for g in range(energy_g):
        vec_left = []
        vec_right = []
        for r, r_i in enumerate(all_regions):
            coarse_node = mesh_info.region_coarse_rel[r_i]
            coarse_node_regions = mesh_info.coarse_region_rel[coarse_node]
            coarse_node_surfaces = mesh_info.coarse_surface_rel[coarse_node]
            vol_i = mesh_info.all_regions_vol[r_i]
            
            index_flx = numRegions * g + r
            flux_val = flux[index_flx]
            left_side = xs[r_i]['total'][g] * vol_i * flux_val
            vec_left.append(left_side)
            right_sum = 0
            for r_j in coarse_node_regions:
                index_j = all_regions.index(r_j)
                vol_j = mesh_info.all_regions_vol[r_j]
                right_sum += probabilities["regions"][r_j]["regions"][r_i][g] * vol_j * source[g][index_j]
            for s_a in coarse_node_surfaces:
                index_a = all_surfaces.index(s_a)
                index_jin_a = numSurfaces * g + index_a
                right_sum += j_in[index_jin_a] * mesh_info.all_surfaces_area[s_a] * probabilities["surfaces"][s_a]["regions"][r_i][g]
            vec_right.append(right_sum)
        left.append(vec_left)
        right.append(vec_right)


    pass


def current_eq_proof(probabilities, source, mesh_info, energy_g, xs, flux, j_in):
    left =  []
    right = []
    
    all_regions = mesh_info.all_regions_order
    all_surfaces = mesh_info.all_surfaces_order

    numRegions = len(all_regions)
    numSurfaces = len(all_surfaces)
    for g in range(energy_g):
        vec_left = []
        vec_right = []
        for s, s_a in enumerate(all_surfaces):
            coarse_node = 1 # This does not apply for bigger systems than a pin cell
            coarse_node_regions = mesh_info.coarse_region_rel[coarse_node]
            coarse_node_surfaces = mesh_info.coarse_surface_rel[coarse_node]
            area_a = mesh_info.all_surfaces_area[s_a]

            index_a = all_surfaces.index(s_a)
            index_jout_a = numSurfaces * g + index_a
            jout_val = j_in[index_jout_a]

            left_side = jout_val * area_a
            vec_left.append(left_side)
            right_sum = 0
            for r_j in coarse_node_regions:
                index_j = all_regions.index(r_j)
                vol_j = mesh_info.all_regions_vol[r_j]
                right_sum += probabilities["regions"][r_j]["surfaces"][s_a][g] * vol_j * source[g][index_j]
            for s_b in coarse_node_surfaces:
                index_b = all_surfaces.index(s_b)
                index_jin_b = numSurfaces * g + index_b
                right_sum += j_in[index_jin_b] * mesh_info.all_surfaces_area[s_b] * probabilities["surfaces"][s_a]["surfaces"][s_b][g]
            vec_right.append(right_sum)
        left.append(vec_left)
        right.append(vec_right)


    pass


def check_convergence_sys(k_prev, k_new, phi_prev, phi_new, energy_g):
    k_converge = abs(k_new - k_prev)/k_new

    phi_converge = abs(phi_new - phi_prev) / phi_new
    
    return k_converge, phi_converge.max()


def check_convergence(k_prev, k_new, phi_prev, phi_new, energy_g):
    k_converge = abs(k_new - k_prev)/k_new

    max_phi_prev = np.zeros(energy_g)
    max_phi_new = np.zeros(energy_g)

    for g in range(energy_g):
        max_phi_new[g] = phi_new[g].max()
        max_phi_prev[g] = phi_prev[g].max()

    phi_converge = abs(max_phi_new.max() - max_phi_prev.max()) / max_phi_new.max() 
    new_converge = abs(max_phi_new - max_phi_prev) / max_phi_new 
    # print(phi_converge)
    # print(new_converge)
    return k_converge, new_converge.max()


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


def calculate_inverseIMR_sys(matrixM, matrixR):
    
    mM = matrixM
    mR = matrixR

    mM_x_mR = np.matmul(mM, mR)
    identityMatrix = np.identity(mM_x_mR.shape[0])
    matrix_to_invert = identityMatrix - mM_x_mR
    inverse = np.linalg.inv(matrix_to_invert)
    inv = inverse
    return inv


def power_iteration_sys(phi_new, phi_prev, keff_prev, fission_source, all_regions, energy_g):
    
    vector_prev = np.matmul(fission_source, phi_prev)
    vector_new = np.matmul(fission_source, phi_new)

    new_product = np.inner(vector_prev, vector_new)
    prev_product = np.inner(vector_prev, vector_prev)
    
    k_new = keff_prev * new_product / prev_product

    return k_new


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
    """
        The order of the long vector is the following:

        phi = [
            phi_r1_g1, phi_r1_g2, phi_r2_g1, phi_r2_g2
        ]
    """
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


def order_flux_output_sys(flux_system, mesh_info, energy_g):
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

    numRegions = len(all_regions_order)
    for g in range(energy_g):
        for r in range(numRegions):
            region =  all_regions_order[r]
            coarse_id = region_coarse_rel[region]
            idx = r + numRegions * g
            phi_output[g][coarse_id][region] = flux_system[idx]
    
    return phi_output
    
    
    
    

