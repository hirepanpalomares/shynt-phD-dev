

def is_pin_in_array(pin, arr, global_nodes, local_nodes):
    """
        Function that tells if a pin is in an array 
        returns True if in the array exist a similar pin
        and False if it does not

        Parameters
        ---------------------------------
        
        pin     :   <class Cell> and it hast be filled with the Pin universe
        arr     :   <class list> array of cells
        
        ---------------------------------
    """
    for other in arr:
        # check number of total local problems
        num_local_other = len(local_nodes[other])
        num_local_pin = len(local_nodes[pin])
        if num_local_other == num_local_pin:
            # check that the pin is the same
            pin_array = global_nodes[other].cell.content
            pin_compare = global_nodes[pin].cell.content
            if pin_array == pin_compare:
                return True
    
    return False


def get_equal_nodes(global_nodes, local_nodes):
    """
    
        Ways that could be used to check if are different:
            
            - Amount of local problems
            - Material of local problems 
            - Shape of local problems (surface)
            - Size of the local problems

        ****************************************************************

            At the moment it only works when the global cells are
            cells with a Pin universe as content
        
        ****************************************************************
    """

    bins = []
    for id_, cell in global_nodes.items():
        # sweep cells
        found = False
        for b in range(len(bins)):
            # sweep bins
            if is_pin_in_array(id_, bins[b], global_nodes, local_nodes):
                bins[b].append(id_)
                found = True
                break
        if not found:
            # add new bin
            bins.append([id_])
    
    
    return bins


def get_surface_equality(node, node_base):
    """
        returns the relation of which surfaces correspond to one
        equal node
    """
    node_cell = node.cell
    node_base_cell = node_base.cell

    surface_cell = node_cell.region.surface
    surface_base_cell = node_base_cell.region.surface

    rel = {
        surface_cell.surf_top.id: surface_base_cell.surf_top.id,
        surface_cell.surf_right.id: surface_base_cell.surf_right.id,
        surface_cell.surf_bottom.id: surface_base_cell.surf_bottom.id,
        surface_cell.surf_left.id: surface_base_cell.surf_left.id,
    }
    return rel