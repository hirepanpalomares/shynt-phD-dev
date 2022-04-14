from Shynt.api_py.Probabilities.p_calc import calculate_probabilities
from Shynt.api_py.Serpent.detector_output import read_detector_file



def helper_get_probabilities(det_inputs, mesh_info, coarse_nodes, fine_nodes, energy_g):
    # Extract data from detectors -------------------------------------------------------------------
    """
        This section probably could be includdde in the file p_calc as a part of the 
        process of getting the neutrons counts
    """
    coarse_node_scores = {}
    detector_relation = {}
    for id_, inp in det_inputs.items():
        # id_ is a coarse node identifier
        coarse_node_scores[id_] = {}
        detector_relation[id_] = {}
        for file_ in inp:
            det_file_name = file_.name + "_det0.m"
            data_detector = read_detector_file(det_file_name) # This is data of the detectors
            coarse_node_scores[id_][file_.specific] = data_detector
            detector_relation[id_][file_.specific] = file_.detectors_relation
            # print(file_.detectors_relation.keys())
    
    # Calculate probabilities for each node of the coarse mesh -------------------
    probabilities = {}
    for id_ in det_inputs:
        prob_id = calculate_probabilities(
            coarse_node_scores[id_], 
            detector_relation[id_], 
            energy_g, id_, mesh_info, coarse_nodes, fine_nodes
        )
        probabilities[id_] = prob_id

    debugging_breakingPoint = True

    # return get_HY_probabilities()
    return probabilities


def get_probabilities_data(det_inputs, mesh_info, coarse_nodes, fine_nodes, energy_g):
    # Calculating probabilities
    
    probabilities_uniq_node = helper_get_probabilities(det_inputs, mesh_info, coarse_nodes, fine_nodes, energy_g)


    debugging_breakingPoint = True

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
        prob_id_eq = probabilities_uniq_node[id_eq]

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



    