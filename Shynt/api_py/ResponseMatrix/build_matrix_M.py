import numpy as np


def getM_matrix(coarse_nodes_map, coarse_nodes, surfaces, type_system):
    numSurfaces = len(surfaces)
    surfaces_indexes = {surfaces[s]: s for s in range(numSurfaces)}

    matrixM_shape = (numSurfaces, numSurfaces)
    matrixM = np.zeros(matrixM_shape)
    

    numRows, numCols = coarse_nodes_map.shape
    
    surface_checked = {s: False for s in surfaces}
    for y in range(numRows):
        for x in range(numCols):
            n_id = coarse_nodes_map[y][x]
            if n_id is not None:
                node = coarse_nodes[n_id]

                surface_directions = node.surface_directions
                surfaces_node =  node.surface_ids
                dbPoint = True
                for surf_id in surfaces_node:
                    if not surface_checked[surf_id]:
                        surface_checked[surf_id] = True
                        twin_surf = None
                        direction = surface_directions[surf_id]
                        if type_system == "square":
                            twin_surf = twin_surface_squared_lattice(
                                n_id, coarse_nodes_map, 
                                coarse_nodes, direction, 
                                x, y, numRows, numCols
                            )
                        elif type_system == "hexagonal":
                            twin_surf = twin_surface_hexagonal_lattice_x(
                                n_id, coarse_nodes_map, 
                                coarse_nodes, direction, 
                                x, y, numRows, numCols
                            )
                        # elif type_system == "hexagonal_y":
                        #     twin_surf = twin_surface_hexagonal_lattice_y(
                        #         n_id, coarse_nodes_map, 
                        #         coarse_nodes, direction, 
                        #         x, y, numRows, numCols
                        #     )
                        
                        matrixM = write_one(surf_id, twin_surf, surfaces_indexes, matrixM) # write 
                        if twin_surf:
                            surface_checked[twin_surf] = True
            else:
                continue
    number_of_ones = 0
    for x in range(numSurfaces):
        for y in range(numSurfaces):
            if matrixM[x][y] == 1.0:
                number_of_ones += 1
    
    return matrixM


def twin_surface_squared_lattice(n_id, coarse_node_map, coarse_nodes, direction, x, y, numRows, numCols):
    """
        Procedure to find a twin surface:

            1. Check direction
            2. Calculate next cell position in the map towards such direction
            3a. If the position is valid (not out of the map indexes):
                4a. Get the id of the contiguous coarse node
                4b. Get the coarse corresponding coarse node
                4c. Get directions of the corresponding corse node
                4d. Get the twin surface id based on the direction towrds the original node
            3b. Else:
                4b. return None (This mens that the direction corresponds to a boundary of the system)
    """
    new_position_transformations = {
        "top": (y-1, x),
        "right": (y, x+1),
        "bottom": (y+1, x),
        "left": (y, x-1),
    }
    direction_mirror = {
        "top": "bottom",
        "right": "left",
        "bottom": "top",
        "left": "right",
    }
    
    new_pos = new_position_transformations[direction] # position format (row, col)
    new_y, new_x = new_pos
    if position_valid(new_pos, numRows, numCols, coarse_node_map):
        # find twin in node towards that direction
        contiguous_node_id = coarse_node_map[new_y][new_x]
        contiguous_node = coarse_nodes[contiguous_node_id]
        contiguous_node_surf_dir = contiguous_node.surface_directions
        twin = [s for s, dir_ in contiguous_node_surf_dir.items() if dir_ == direction_mirror[direction]][0]
        return twin
    else:
        return None # is boundary

   
    
def twin_surface_hexagonal_lattice_x(n_id, coarse_node_map, coarse_nodes, direction, x, y, numRows, numCols):
    """
    Procedure to find a twin surface:

        1. Check direction
        2. Calculate next cell position in the map towards such direction
        3a. If the position is valid (not out of the map indexes):
            4a. Get the id of the contiguous coarse node
            4b. Get the coarse corresponding coarse node
            4c. Get directions of the corresponding corse node
            4d. Get the twin surface id based on the direction towrds the original node
        3b. Else:
            4b. return None (This mens that the direction corresponds to a boundary of the system)
    """
    new_position_transformations = {
        "A": (y-1, x+1),
        "B": (y, x+1),
        "C": (y+1, x),
        "D": (y+1, x-1),
        "E": (y, x-1),
        "F": (y-1, x)
    }
    direction_mirror = {
        "A": "D",
        "B": "E",
        "C": "F",
        "D": "A",
        "E": "B",
        "F": "C"
    }

    new_pos = new_position_transformations[direction] # position format (row, col)
    new_y, new_x = new_pos
    if position_valid(new_pos, numRows, numCols, coarse_node_map):
        # find twin in node towards that direction
        contiguous_node_id = coarse_node_map[new_y][new_x]
        contiguous_node = coarse_nodes[contiguous_node_id]
        contiguous_node_surf_dir = contiguous_node.surface_directions
        twin = [s for s, dir_ in contiguous_node_surf_dir.items() if dir_ == direction_mirror[direction]][0]
        return twin
    else:
        return None # is boundary
    

def twin_surface_hexagonal_lattice_y(n_id, coarse_node_map, coarse_nodes, direction, x, y, numRows, numCols):
    print("Matrix M generation not implemented for Hexagonal lattice type Y")
    raise SystemError
    

def position_valid(pos, numRows, numCols, coarse_node_map):
    y, x = pos

    if x < 0 or y < 0 :
        return False
    elif x >= numCols or y >= numRows:
        return False
    elif coarse_node_map[y][x] is None:
        return False
    return True
    
def write_one(surf, twin_surf, surfaces_indexes, mM):
    if twin_surf:
        surf_index = surfaces_indexes[surf]
        twin_surf_index = surfaces_indexes[twin_surf]
        mM[surf_index][twin_surf_index] = 1
        mM[twin_surf_index][surf_index] = 1
    else:
        surf_index = surfaces_indexes[surf]
        mM[surf_index][surf_index] = 1
    return mM





