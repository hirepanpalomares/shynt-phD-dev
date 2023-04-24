from Shynt.api_py.Probabilities.p_calc import calculate_probabilities_main_nodes
from Shynt.api_py.Serpent.detector_output import read_detectors_data

import numpy as np

def get_probabilities(det_inputs, mesh_info, root, xs):
    model_cell = root.model_cell
    energy_g = root.energy_grid.energy_groups
    coarse_nodes = model_cell.global_mesh.coarse_nodes
    coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
    fine_nodes = model_cell.local_mesh.fine_nodes

    # Calculating probabilities
    
    coarse_node_scores, detector_relation = read_detectors_data(det_inputs)
    
    probabilities_unique_nodes, prob_uncertainty = calculate_probabilities_main_nodes(
        det_inputs, 
        mesh_info, 
        coarse_nodes, 
        fine_nodes, 
        energy_g, 
        coarse_node_scores, 
        detector_relation
    )

    # sum_prob_unique_nodes = calculate_sum_probabilities(probabilities_unique_nodes, energy_g)
    # print("Sum of probabilities: ")
    # print(sum_prob_unique_nodes)
    
    # reciprocity = check_reciprocity(probabilities_unique_nodes, xs, energy_g, mesh_info)
    # print("reciprocity --------------------------")
    # for n_id in reciprocity:
    #     print("regions " + "-"*100)
    #     for r_id in reciprocity[n_id]["regions"]:
    #         print(r_id, reciprocity[n_id]["regions"][r_id])
    #     print("surfaces " + "-"*100)
    #     for s_id in reciprocity[n_id]["surfaces"]:
    #         print(s_id, reciprocity[n_id]["surfaces"][s_id])


    debugging_breakingPoint = True

    probs, probs_sigma = fill_probabilities(coarse_nodes, mesh_info, probabilities_unique_nodes, prob_uncertainty)

    return probs, probs_sigma
    


def fill_probabilities(coarse_nodes, mesh_info, probabilities_unique_nodes, prob_uncertainty):
    """
        This method replicates the probabilities of the main nodes
        to those nodes that belong to the same type.

        TO do this, the method relies on the variables:
            - mesh_info.equivalence_region_rel
            - mesh_info.equivalence_surface_rel
    """
    new_prob = {
        "regions": {},
        "surfaces": {}
    }
    new_prob_sigma = {
        "regions": {},
        "surfaces": {}
    }
    
    for id_ in coarse_nodes.keys():
        regions = mesh_info.coarse_region_rel[id_]
        surfaces = mesh_info.coarse_surface_rel[id_]

        id_eq = mesh_info.equal_nodes_rel[id_]
        new_prob["regions"].update({
            r: {
                "regions": {},
                "surfaces": {}
            } for r in regions
        })
        new_prob["surfaces"].update({
            s: {
                "regions": {},
                "surfaces": {}
            } for s in surfaces
        })
        new_prob_sigma["regions"].update({
            r: {
                "regions": {},
                "surfaces": {}
            } for r in regions
        })
        new_prob_sigma["surfaces"].update({
            s: {
                "regions": {},
                "surfaces": {}
            } for s in surfaces
        })
        prob_id_eq = probabilities_unique_nodes[id_eq]
        prob_sigma_id_eq = prob_uncertainty[id_eq]
        # Filling probabilities to every similar node

        for r, reg_id in enumerate(regions):
            reg_eq = mesh_info.equivalence_region_rel[reg_id]
            # reg to reg
            for rp, regp_id in enumerate(regions):
                reg_p_eq = mesh_info.equivalence_region_rel[regp_id]
                new_prob["regions"][reg_id]["regions"][regp_id] = prob_id_eq["regions"][reg_eq]["regions"][reg_p_eq]
                new_prob_sigma["regions"][reg_id]["regions"][regp_id] = prob_sigma_id_eq["regions"][reg_eq]["regions"][reg_p_eq]
                
            # reg to surf
            for surf in surfaces:
                surf_eq = mesh_info.equivalence_surface_rel[surf]
                new_prob["regions"][reg_id]["surfaces"][surf] = prob_id_eq["regions"][reg_eq]["surfaces"][surf_eq]
                new_prob_sigma["regions"][reg_id]["surfaces"][surf] = prob_sigma_id_eq["regions"][reg_eq]["surfaces"][surf_eq]
    
        for surf in surfaces:
            surf_eq = mesh_info.equivalence_surface_rel[surf]
            # surface to region
            for r, reg_id in enumerate(regions):
                reg_eq_id = mesh_info.equivalence_region_rel[reg_id]
                new_prob["surfaces"][surf]["regions"][reg_id] = prob_id_eq["surfaces"][surf_eq]["regions"][reg_eq_id]
                new_prob_sigma["surfaces"][surf]["regions"][reg_id] = prob_sigma_id_eq["surfaces"][surf_eq]["regions"][reg_eq_id]

            # surface to surface
            for surf_p in surfaces:
                surf_p_eq = mesh_info.equivalence_surface_rel[surf_p]
                new_prob["surfaces"][surf]["surfaces"][surf_p] = prob_id_eq["surfaces"][surf_eq]["surfaces"][surf_p_eq]
                new_prob_sigma["surfaces"][surf]["surfaces"][surf_p] = prob_sigma_id_eq["surfaces"][surf_eq]["surfaces"][surf_p_eq]


    return  new_prob, new_prob_sigma

def calculate_sum_probabilities(probabilities_unique_nodes, energy_g):
    sum_prob_unique_nodes = {}

    for id_ in probabilities_unique_nodes.keys():
        sum_prob_unique_nodes[id_] = {
            "regions": {}, "surfaces": {}
        }
        regions = list(probabilities_unique_nodes[id_]["regions"].keys()) 
        surfaces = list(probabilities_unique_nodes[id_]["surfaces"].keys()) 
        for r in regions:
            sum_prob_r = np.zeros(energy_g)
            for rp in regions:
                sum_prob_r += probabilities_unique_nodes[id_]["regions"][r]["regions"][rp]
            for sp in surfaces:
                sum_prob_r += probabilities_unique_nodes[id_]["regions"][r]["surfaces"][sp]
            sum_prob_unique_nodes[id_]["regions"][r] = sum_prob_r
        for s in surfaces:
            sum_prob_s = np.zeros(energy_g)
            for rp in regions:
                sum_prob_s += probabilities_unique_nodes[id_]["surfaces"][s]["regions"][rp]
            for sp in surfaces:
                sum_prob_s += probabilities_unique_nodes[id_]["surfaces"][s]["surfaces"][sp]
            sum_prob_unique_nodes[id_]["surfaces"][s] = sum_prob_s
    return sum_prob_unique_nodes



def check_reciprocity(probabilities, xs, energy_g, mesh_info):
    reciprocity = {}
    for n_id, prob_n in probabilities.items():
        reciprocity[n_id] = {
            "regions": {},
            "surfaces": {}
        }
        for r_i in prob_n["regions"]:
            # checking region to region
            reciprocity[n_id]["regions"][r_i] = {
                "regions": {},
                "surfaces": {}
            }
            for r_j in prob_n["regions"][r_i]["regions"]:
                reciprocity[n_id]["regions"][r_i]["regions"][r_j] = np.zeros(energy_g)
                for g in range(energy_g):
                    prob_j_i = prob_n["regions"][r_j]["regions"][r_i][g]
                    prob_i_j_rec = xs[r_j]["total"][g] * mesh_info.all_regions_vol[r_j] * prob_j_i
                    prob_i_j_rec /= (xs[r_i]["total"][g] * mesh_info.all_regions_vol[r_i])

                    prob_i_j = prob_n["regions"][r_i]["regions"][r_j][g]
                    diff = ( prob_i_j - prob_i_j_rec ) * 100 / prob_i_j
                    reciprocity[n_id]["regions"][r_i]["regions"][r_j][g] = diff
            # checking region to surface
            for s_a in prob_n["regions"][r_i]["surfaces"]:
                radius_wigner = mesh_info.all_surfaces_area[s_a] / np.sqrt(np.pi) # because pitch is equal to surface area in this case
                reciprocity[n_id]["regions"][r_i]["surfaces"][s_a] = np.zeros(energy_g)
                for g in range(energy_g):
                    prob_a_i = prob_n["surfaces"][s_a]["regions"][r_i][g]

                    prob_i_a_rec = 2 * np.pi * radius_wigner * prob_a_i / 4
                    prob_i_a_rec /= (4 * mesh_info.all_regions_vol[r_i] * xs[r_i]["total"][g])

                    prob_i_a = prob_n["regions"][r_i]["surfaces"][s_a][g]
                    diff = ( prob_i_a - prob_i_a_rec ) * 100 / prob_i_a
                    reciprocity[n_id]["regions"][r_i]["surfaces"][s_a][g] = diff
        
        for s_a in prob_n["surfaces"]:
            radius_wigner = mesh_info.all_surfaces_area[s_a] / np.sqrt(np.pi) # because pitch is equal to surface area in this case
            reciprocity[n_id]["surfaces"][s_a] = {
                "regions": {},
                "surfaces": {}
            }
            # checking surface to region
            for r_j in prob_n["surfaces"][s_a]["regions"]:
                reciprocity[n_id]["surfaces"][s_a]["regions"][r_j] = np.zeros(energy_g)
                for g in range(energy_g):
                    prob_j_a = prob_n["regions"][r_j]["surfaces"][s_a][g]
                    prob_a_j_rec = 4 * mesh_info.all_regions_vol[r_j] * xs[r_j]["total"][g] * prob_j_a
                    prob_a_j_rec /= (2 * np.pi * radius_wigner / 4)

                    prob_a_j = prob_n["surfaces"][s_a]["regions"][r_j][g]
                    diff = ( prob_a_j - prob_a_j_rec ) * 100 / prob_a_j
                    reciprocity[n_id]["surfaces"][s_a]["regions"][r_j][g] = diff
            # checking surface to surface
            pass
        
        
    
    return reciprocity

                
