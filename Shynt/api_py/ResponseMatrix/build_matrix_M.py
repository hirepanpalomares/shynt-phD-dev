import numpy as np


def getM_matrix(coarse_nodes_map, coarse_nodes, surfaces):
    numSurfaces = len(surfaces)
    surfaces_indexes = {surfaces[s]: s for s in range(numSurfaces)}

    matrixM_shape = (numSurfaces, numSurfaces)
    matrixM = np.zeros(matrixM_shape)
    

    numRows, numCols = coarse_nodes_map.shape
    
    surface_checked = {s: False for s in surfaces}
    for y in range(numRows):
        for x in range(numCols):
            n_id = coarse_nodes_map[y][x]
            node = coarse_nodes[n_id]

            surface_directions = node.surface_directions
            surfaces_node =  node.surface_ids

            for surf_id in surfaces_node:
                if not surface_checked[surf_id]:
                    surface_checked[surf_id] = True
                    direction = surface_directions[surf_id]
                    twin_surf = twin_surface(n_id, coarse_nodes_map, coarse_nodes, direction, x, y, numRows, numCols)
                    matrixM = write_one(surf_id, twin_surf, surfaces_indexes, matrixM) # write 
                    if twin_surf:
                        surface_checked[twin_surf] = True

    return matrixM


def twin_surface(n_id, coarse_node_map, coarse_nodes, direction, x, y, numRows, numCols):
    if direction == "top":
        topwards_pos = (y - 1, x) # position format (row, col)
        new_y, new_x = topwards_pos
        if position_valid(topwards_pos, numRows, numCols):
            # find twin in node towards that direction
            contiguous_node_id = coarse_node_map[new_y][new_x]
            contiguous_node = coarse_nodes[contiguous_node_id]
            contiguous_node_surf_dir = contiguous_node.surface_directions
            twin = [s for s, dir_ in contiguous_node_surf_dir.items() if dir_ == "bottom"][0]
            return twin
        else:
            return None # is boundary
    elif direction == "right":
        rightwards_pos = (y, x + 1)
        new_y, new_x = rightwards_pos
        if position_valid(rightwards_pos, numRows, numCols):
            # find twin in node towards that direction
            contiguous_node_id = coarse_node_map[new_y][new_x]
            contiguous_node = coarse_nodes[contiguous_node_id]
            contiguous_node_surf_dir = contiguous_node.surface_directions
            twin = [s for s, dir_ in contiguous_node_surf_dir.items() if dir_ == "left"][0]
            return twin
        else:
            return None # is boundary
    elif direction == "bottom":
        bottomwards_pos = (y + 1, x)
        new_y, new_x = bottomwards_pos
        if position_valid(bottomwards_pos, numRows, numCols):
            # find twin in node towards that direction
            contiguous_node_id = coarse_node_map[new_y][new_x]
            contiguous_node = coarse_nodes[contiguous_node_id]
            contiguous_node_surf_dir = contiguous_node.surface_directions
            twin = [s for s, dir_ in contiguous_node_surf_dir.items() if dir_ == "top"][0]
            return twin
        else:
            return None # is boundary

    elif direction == "left":
        leftwards_pos = (y, x - 1)
        new_y, new_x = leftwards_pos
        if position_valid(leftwards_pos, numRows, numCols):
            # find twin in node towards that direction
            contiguous_node_id = coarse_node_map[new_y][new_x]
            contiguous_node = coarse_nodes[contiguous_node_id]
            contiguous_node_surf_dir = contiguous_node.surface_directions
            twin = [s for s, dir_ in contiguous_node_surf_dir.items() if dir_ == "right"][0]
            return twin
        else:
            return None # is boundary
    

def position_valid(pos, numRows, numCols):
    y, x = pos

    if x < 0 or y < 0:
        return False
    elif x >= numCols or y >= numRows:
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





