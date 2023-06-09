from .extractor_xs import get_cross_sections

def  get_xs_data(mesh_info, root, xs_inputs):
    energy_g = root.energy_grid.energy_groups
    model_cell = root.model_cell
    coarse_nodes = model_cell.global_mesh.coarse_nodes
    fine_nodes = model_cell.local_mesh.fine_nodes

    xs = get_cross_sections(energy_g, xs_inputs, fine_nodes)

    # filling probabilities to every similar node

    new_xs = {}
    for id_ in coarse_nodes.keys():
        # Filling XS

        id_eq = mesh_info.equal_nodes_rel[id_]
        xs_id_eq = xs[id_eq]
        type_regs = list(mesh_info.region_type_rel_switched[id_eq].keys())
        for r, reg_id in enumerate(mesh_info.coarse_region_rel[id_]):
            reg_eq = type_regs[r]
            new_xs[reg_id] = xs_id_eq[reg_eq]
    
    return new_xs

