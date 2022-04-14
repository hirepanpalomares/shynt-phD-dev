from .extractor_xs import get_cross_sections

def get_xs_data(mesh_info, coarse_nodes, fine_nodes, energy_g, xs_inputs):
    xs = get_cross_sections(energy_g, xs_inputs, fine_nodes)

    # filling probabilities to every similar node

    new_xs = {}
    for id_ in coarse_nodes.keys():
        # Filling XS
        regions = mesh_info.coarse_region_rel[id_]

        id_eq = mesh_info.equal_nodes_rel[id_]
        xs_id_eq = xs[id_eq]
        for reg in regions:
            type_region = mesh_info.region_type_rel_switched[id_][reg]
            reg_eq = mesh_info.region_type_rel[id_eq][type_region]
            new_xs[reg] = xs_id_eq[reg_eq]
    
    return new_xs

