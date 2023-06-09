import numpy as np


def getM_matrix(global_mesh, mesh_info):
  coarse_nodes = global_mesh.coarse_nodes
  all_surfaces = mesh_info.all_surfaces_order
  coarse_nodes_map = mesh_info.coarse_nodes_map
  type_mesh = global_mesh.type_mesh

  numSurfaces = len(all_surfaces)
  surfaces_indexes = {all_surfaces[s]: s for s in range(numSurfaces)}

  matrixM_shape = (numSurfaces, numSurfaces)
  matrixM = np.zeros(matrixM_shape)
  

  numRows, numCols = coarse_nodes_map.shape
  
  surface_checked = {s: False for s in all_surfaces}
  for y in range(numRows):
    for x in range(numCols):
      n_id = coarse_nodes_map[y][x]
      if n_id != 0:
        node = coarse_nodes[n_id]

        print(node.geometry_info["type"])
        surface_directions = node.surface_directions
        surfaces_node =  node.surface_ids
        dbPoint = True
        for surf_id in surfaces_node:
          if not surface_checked[surf_id]:
            surface_checked[surf_id] = True
            twin_surf = None
            direction = surface_directions[surf_id]
            if type_mesh == "square_hex_pin":
              twin_surf = twin_surface_squared_lattice(
                n_id, coarse_nodes_map, 
                coarse_nodes, direction, 
                x, y, numRows, numCols
              )
              matrixM = write_one_perfect_square_mesh(surf_id, surfaces_indexes, matrixM, twin_surf)
            elif type_mesh == "square_hex_assembly":
              twin_surfs, contiguous_nodes = twin_surface_hexagonal_lattice_x_SquareMesh(
                n_id, coarse_nodes_map, 
                coarse_nodes, direction, 
                x, y, numRows, numCols, node.geometry_info["type"]
              )
              matrixM = write_one_hex_square_mesh(surf_id, n_id, twin_surfs, surfaces_indexes, matrixM, contiguous_nodes, coarse_nodes, direction) # write 
              for tws in twin_surfs:
                if tws:
                  surface_checked[tws] = True
        else:
          continue
  
  
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


def twin_surface_hexagonal_lattice_x_SquareMesh(n_id, coarse_node_map, coarse_nodes, direction, x, y, numRows, numCols, type_node):
    """
      Procedure to find a twin surface in a square global mesh:

      1. Check direction
      2. Calculate next cell position in the map towards such direction
      3a. If the position is valid (not out of the map indexes):
        4a. Get the id of the contiguous coarse node
        4b. Get the coarse corresponding coarse node
        4c. Get directions of the corresponding corse node
        4d. Get the twin surface id based on the direction towrds the original node
      3b. Else:
        4b. return None (This mens that the direction corresponds to a boundary of the system)

      The current has to be splitted in the following cases:
        - corner: bottom direction
        - side-edge: top/bottom direction
        - side-edge+1: top direction
          
    """
    new_position_transformations = {
        "top": [(y-1, x)],
        "right": [(y, x+1)],
        "bottom": [(y+1, x)],
        "left": [(y, x-1)],
    }
    direction_mirror = {
        "top": "bottom",
        "right": "left",
        "bottom": "top",
        "left": "right",
    }

    # ? Check y
    new_pos = ()
    if y < numRows / 2:
      # ? --------------------------------- above and middle-top
      if type_node == "corner":
        if x < numCols/2: new_position_transformations["bottom"].append((y+1,x-1))
        else: new_position_transformations["bottom"].append((y+1,x+1))
      elif type_node == "top_edge":
        #! stays the same
        pass
      elif type_node == "side_edge":
        if x < numCols/2: 
          new_position_transformations["top"] = [(y-1,x+1)]
          if y != numRows/2-1:
            # other than exact middle
            new_position_transformations["bottom"].append((y+1,x-1))          
        else: 
          new_position_transformations["top"] = [(y-1,x-1)]
          if y != numRows/2-1:
            # other than exact middle
            new_position_transformations["bottom"].append((y+1,x+1))
      elif type_node == "inside":
        # stays the same
        pass
    else:
      # elif y == numRows / 2 and type_node == "side_edge":
      #   # ? --------------------------------- middle-bottom
      #   if x < numCols/2: new_position_transformations["bottom"] = []
      #   else: new_position_transformations["bottom"] = []
      # elif y == numRows/2+1 and type_node == "side_edge":
      #   # ? ---------------------------------
      #   if x < numCols/2: new_position_transformations["bottom"] = [(y+1,x+1)]
      #   else: new_position_transformations["bottom"] = [(y+1,x-1)]
      # ? ---------------------------------
      if type_node == "corner":
        if x < numCols/2: new_position_transformations["top"].append((y-1,x-1))
        else: new_position_transformations["top"].append((y-1,x+1))
      elif type_node == "top_edge":
        pass
        #! stays the same
      elif type_node == "side_edge":
        new_position_transformations["bottom"] = []
        if x < numCols/2: 
          new_position_transformations["top"].append((y-1,x-1))
          # new_position_transformations["bottom"] = [(y+1,x+1)]
        else: 
          new_position_transformations["top"].append((y-1,x+1))
          # new_position_transformations["bottom"] = [(y+1,x-1)]
      elif type_node == "inside":
        new_position_transformations["bottom"] = []
        
      

    new_positions = new_position_transformations[direction] # position format (row, col)
    twins = []
    contiguous_nodes = []
    for new_pos in new_positions:
      new_y, new_x = new_pos
      if position_valid_hex_lattice_square_mesh(new_pos, numRows, numCols, coarse_node_map):
        # find twin in node towards that direction
        contiguous_node_id = coarse_node_map[new_y][new_x]
        contiguous_node = coarse_nodes[contiguous_node_id]
        contiguous_node_surf_dir = contiguous_node.surface_directions
        twin = [s for s, dir_ in contiguous_node_surf_dir.items() if dir_ == direction_mirror[direction]]
        twins += twin
        contiguous_nodes += [contiguous_node_id]
      else:
        return [None], [] # is boundary
    return twins, contiguous_nodes
    
  
def twin_surface_hexagonal_lattice_x_HexagonalMesh(n_id, coarse_node_map, coarse_nodes, direction, x, y, numRows, numCols):
    """
    Procedure to find a twin surface in a hexagonal global mesh:

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
    

def position_valid_hex_lattice_square_mesh(pos, numRows, numCols, coarse_node_map):
  y, x = pos
  if x < 0 or y < 0:
    return False
  elif x >= numCols or y >= numRows:
    return False
  elif coarse_node_map[y][x] == 0:
    return False
  return True


def position_valid_hex_lattice(pos, numRows, numCols, coarse_node_map):
  y, x = pos
  # node_in_pos = coarse_node_map[y][x]
  if y < 0 or y >= numRows:
    return False
  elif y <= numRows/2:
    if coarse_node_map[y][x] == 0 or coarse_node_map[y][x] == 0:
      #! is on the edge 

      pass
    if coarse_node_map[y][x-1] == 0 or coarse_node_map[y][x+1]:
        pass
  elif coarse_node_map[y][x] is None:
      return False
  return True
    

def position_valid(pos, numRows, numCols, coarse_node_map):
    y, x = pos

    if x < 0 or y < 0 :
        return False
    elif x >= numCols or y >= numRows:
        return False
    elif coarse_node_map[y][x] is None:
        return False
    return True
    

def write_one_hex_square_mesh(surf, n_id, twin_surfaces, surfaces_indexes, mM, contiguous_nodes, coarse_nodes, direction):
  coarse_node = coarse_nodes[n_id]
  def x1x2_tw_dir(dir_):
    if dir_ == "top":
      return "bottom"
    elif dir_ == "bottom":
      return "top"
  for s, tws in enumerate(twin_surfaces):
    if tws:
      if direction == "top" or direction == "bottom":
        coarse_node_twin = coarse_nodes[contiguous_nodes[s]]
        x1_tw_n, x2_tw_n = coarse_node_twin.x1_x2(face=x1x2_tw_dir(direction))
        x1_n, x2_n = coarse_node.x1_x2(face=direction)
        s_to_stw, stw_to_s = calculate_surf_to_surf_tw_proportion(x1_n, x2_n, x1_tw_n, x2_tw_n)
        surf_index = surfaces_indexes[surf]
        twin_surf_index = surfaces_indexes[tws]

        mM[surf_index][twin_surf_index] = stw_to_s
        mM[twin_surf_index][surf_index] = s_to_stw
      else:
        surf_index = surfaces_indexes[surf]
        twin_surf_index = surfaces_indexes[tws]
        mM[surf_index][twin_surf_index] = 1
        mM[twin_surf_index][surf_index] = 1
    else:
      surf_index = surfaces_indexes[surf]
      mM[surf_index][surf_index] = 1
  return mM


def write_one_perfect_square_mesh(surf, surfaces_indexes, mM, tws):
  if tws:
    surf_index = surfaces_indexes[surf]
    twin_surf_index = surfaces_indexes[tws]
    mM[surf_index][twin_surf_index] = 1
    mM[twin_surf_index][surf_index] = 1
  else:
    surf_index = surfaces_indexes[surf]
    mM[surf_index][surf_index] = 1
  return mM



def calculate_surf_to_surf_tw_proportion(x1_n, x2_n, x1_tw_n, x2_tw_n):
  """
    Check Klee's Algorithm
  """
  points = [
    (x1_n, True),
    (x2_n, False),
    (x1_tw_n, True),
    (x2_tw_n, False)
  ]

  matching_segment = calculate_matching_segment(points)
  stw_length = x2_tw_n - x1_tw_n
  s_length = x2_n - x1_n

  s_to_stw = matching_segment / s_length
  stw_to_s = matching_segment / stw_length

  # if stw_to_s == 1:
  #   s_to_stw = 1
  # if s_to_stw < 0.5:
  #   s_to_stw = 0
  #   stw_to_s = 0 
  return (s_to_stw, stw_to_s)



def calculate_matching_segment(points):
  """
    Check Klee's Algorithm
  """
  # Sort the points (bubble sort) -------
  n = len(points)
  for i in range(n):
    for j in range(0, n-i-1):
      if points[j][0] > points[j+1][0]:
        points[j], points[j+1] = points[j+1], points[j]

  # Check the order --------
  start = points[0]
  end = None
  for p in range(1,n):
    end = points[p]
    if start[1] and not end[1]:
      break
    start = end
  
  segment_length = end[0] - start[0]
  return segment_length
  
  

