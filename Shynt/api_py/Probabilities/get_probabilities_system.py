from Shynt.api_py.Probabilities.p_calc import calculate_probabilities_main_nodes
from Shynt.api_py.Serpent.detector_output import read_detectors_data

import numpy as np

def get_probabilities(det_inputs, mesh_info, root):
    model_cell = root.model_cell
    energy_g = root.energy_grid.energy_groups
    coarse_nodes = model_cell.global_mesh.coarse_nodes
    coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
    fine_nodes = model_cell.local_mesh.fine_nodes

    # Calculating probabilities
    
    coarse_node_scores, detector_relation = read_detectors_data(det_inputs)
    
    probabilities_unique_nodes = calculate_probabilities_main_nodes(
        det_inputs, 
        mesh_info, 
        coarse_nodes, 
        fine_nodes, 
        energy_g, 
        coarse_node_scores, 
        detector_relation
    )

    sum_prob_unique_nodes = calculate_sum_probabilities(probabilities_unique_nodes, energy_g)

    debugging_breakingPoint = True

    probs = fill_probabilities(coarse_nodes, mesh_info, probabilities_unique_nodes)

    return probs
    


def fill_probabilities(coarse_nodes, mesh_info, probabilities_unique_nodes):
    new_prob = {
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
        prob_id_eq = probabilities_unique_nodes[id_eq]

        # Filling probabilities to every similar node

        for reg in regions:
            type_region = mesh_info.region_type_rel_switched[id_][reg]
            reg_eq = mesh_info.region_type_rel[id_eq][type_region]
            # region to region
            for reg_p in regions:
                type_region_p = mesh_info.region_type_rel_switched[id_][reg_p]
                reg_p_eq = mesh_info.region_type_rel[id_eq][type_region_p]
                new_prob["regions"][reg]["regions"][reg_p] = prob_id_eq["regions"][reg_eq]["regions"][reg_p_eq]
            # region to surfaces
            for surf in surfaces:
                surf_eq = mesh_info.equivalence_surface_rel[surf]
                new_prob["regions"][reg]["surfaces"][surf] = prob_id_eq["regions"][reg_eq]["surfaces"][surf_eq]
    
        for surf in surfaces:
            surf_eq = mesh_info.equivalence_surface_rel[surf]
            # surface to region
            for reg in regions:
                type_region = mesh_info.region_type_rel_switched[id_][reg]
                reg_eq = mesh_info.region_type_rel[id_eq][type_region]
                new_prob["surfaces"][surf]["regions"][reg] = prob_id_eq["surfaces"][surf_eq]["regions"][reg_eq]
            # surface to surface
            for surf_p in surfaces:
                surf_p_eq = mesh_info.equivalence_surface_rel[surf_p]
                new_prob["surfaces"][surf]["surfaces"][surf_p] = prob_id_eq["surfaces"][surf_eq]["surfaces"][surf_p_eq]


    return  new_prob

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
    