import numpy as np
import scipy.sparse as sparse


def getM_matrix_easier(mesh_info, store_sparse=False):
  surface_twins = mesh_info.coarse_mesh.surface_twins
  all_surfaces = mesh_info.all_surfaces_order

  numSurfaces = len(all_surfaces)
  surfaces_indexes = {all_surfaces[s]: s for s in range(numSurfaces)}

  matrixM_shape = (numSurfaces, numSurfaces)

  matrixM = []

  sparse_row = []
  sparse_col = []
  sparse_val = []
  idx_row = 0
  idx_col = 0

  if not store_sparse:
    matrixM = np.zeros(matrixM_shape)

  for s_id in all_surfaces:
    s_id_idx = surfaces_indexes[s_id]
    twin_surf, nid = surface_twins[s_id]
    if twin_surf is not None:
      twin_surf_idx = surfaces_indexes[twin_surf]
      # print(s_id_idx, twin_surf_idx)
      if store_sparse:
        sparse_row.append(s_id_idx)
        sparse_col.append(twin_surf_idx)
        sparse_val.append(1.0)
        
      else:      
        matrixM[s_id_idx][twin_surf_idx] = 1
        matrixM[twin_surf_idx][s_id_idx] = 1
    else:
      if store_sparse:
        sparse_row.append(s_id_idx)
        sparse_col.append(s_id_idx)
        sparse_val.append(1.0)
      else:
        matrixM[s_id_idx][s_id_idx] = 1

  if store_sparse:
    # sparse_mM = sparse.csc_matrix(
    #   (sparse_val, (sparse_row, sparse_col)), 
    #   shape=matrixM_shape,
    #   dtype=np.double
      
    # )
    sparse_mM = (
      np.array(sparse_row, dtype=np.int64),
      np.array(sparse_col, dtype=np.int64),
      np.array(sparse_val),    
    )
    return sparse_mM, surface_twins
  else:
    return matrixM, surface_twins



def get_mM_system(mesh_info, energy_g):
  all_coarse_nodes_ids = mesh_info.coarse_order
  
  surface_twins = mesh_info.coarse_mesh.surface_twins
  all_surfaces = mesh_info.all_surfaces_order

  numSurfaces = len(all_surfaces)
  surfaces_indexes = {all_surfaces[s]: s for s in range(numSurfaces)}

  matrixM_shape = (numSurfaces*energy_g, numSurfaces*energy_g)
  matrixM = np.zeros(matrixM_shape)

  lookup_surface_to_node = mesh_info.get_lookup_surface_to_node()

  # Building map of indexes:
  indexes = {}
  idx = 0
  for n, nid in enumerate(all_coarse_nodes_ids):
    node_surfaces = mesh_info.coarse_mesh.coarse_nodes[nid].surfaces
    indexes[nid] = {}
    for g in range(energy_g):
      indexes[nid][g] = {}
      for sa in node_surfaces.keys():
        indexes[nid][g][sa] = idx
        idx += 1
        
  for n, nid in enumerate(all_coarse_nodes_ids):
    node_surfaces = mesh_info.coarse_mesh.coarse_nodes[nid].surfaces
    for g in range(energy_g):
      for sa_id in node_surfaces.keys():    
        sa_twin_id = surface_twins[sa_id]
        sa_id_index = indexes[nid][g][sa_id]
        if sa_twin_id is not None:
          node_twin = lookup_surface_to_node[sa_twin_id]
          twin_index = indexes[node_twin][g][sa_twin_id]
          matrixM[sa_id_index][twin_index] = 1
          matrixM[twin_index][sa_id_index] = 1

        else:
          matrixM[sa_id_index][sa_id_index] = 1

  return matrixM, indexes
  




























































"""
  Functions below are not used

"""



def getM_matrix(global_mesh, mesh_info):
  """
  Function to obtain the matrix M for the whole system
  The procedure to calculate this matrix will be different
  depending on the shape of the mesh.

  Should twins be provided before? In the creation of the 
  GlobalMesh for example 

  Parameters
  ----------
  global_mesh : GlobalMesh
    Global mesh class
  mesh_info : MeshInfo
    Mesh info class

  Returns
  -------
  matrixM : np.array()
    Matrix of the topological relationship between the surfaces
    of the gobal nodes is expressed
  twins : dict
    Dictionary with the surfaces that share two global nodes.

  """
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
  twins = {}
  for y in range(numRows):
    for x in range(numCols):
      n_id = coarse_nodes_map[y][x]
      if n_id != 0:
        node = coarse_nodes[n_id]

        # print(node.geometry_info["type"])
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
                  twins[surf_id] = tws
                  twins[tws] = surf_id
                  surface_checked[tws] = True
                else:
                  twins[surf_id] = surf_id
            if type_mesh == "square_pin_mesh":
              twin_surf = twin_surface_squared_lattice(
                n_id, coarse_nodes_map, 
                coarse_nodes, direction, 
                x, y, numRows, numCols
              )
              matrixM = write_one_perfect_square_mesh(surf_id, surfaces_indexes, matrixM, twin_surf)
        else:
          continue
  
  
  return matrixM, twins


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
  
  

