
from Shynt.api_py.Mesh.coarse_node import CoarseNodeTriangularMesh
from Shynt.api_py.Mesh.coarse_mesh import CoarseMesh

# from Shynt.api_py.Geometry.universes import SquareLattice
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX
# from Shynt.api_py.Geometry.universes import Pin
# from Shynt.api_py.Geometry.universes import Universe

from Shynt.api_py.Geometry.cells import Cell


class TriangularMesh(CoarseMesh):
  """Class to represent a triangular coarse mesh in a hexagonal assembly.

  ...

  Attributes
  ----------
  __offset : float

  __map_pins : list
  
  __symmetry : dict

  clean_mesh_map : list

  points_mesh : list

  rectangles : list

  surface_twins : dict

  nodes_surfaces : dict

  num_surfaces : int

  equivalent_nodes : dict

  corse_nodes_regions : dict

  regions_coarse_node : dict

  coarse_nodes_regions_material : dict

  regions_volume : dict

  coarse_nodes : dict

  type_mesh : str

  hex_assembly : Universe

  map_nodes : list of list
  
  clean_map : list of list
  
  x_div : list
  
  y_div : list of list

  Methods
  -------
  __create_nodes_hex_assem()
  
  """
    
  def __init__(self, cell):
    super().__init__(cell)
    self.hex_assembly = super().cell.content
    self.points_mesh = {}
    self.mesh_rings = []
    self.coarse_nodes = {}
    self.type_nodes = {}
    self.nodes_surfaces = {}
    self.num_surfaces = 0
    self.surface_twins = {}
    self.surfaces = {}

    # self.calculate_nodes_coordinates()
    # self.calculate_nodes_surfaces()
    # self.calculate_surfaces_twins()
    
    self.map_pins = []
    self.symmetry = {}
    self.mesh_map = [] # mesh in rings


    self.equivalent_nodes = {}
    self.corse_nodes_regions = {}
    self.regions_coarse_node = {}
    self.coarse_nodes_regions_material = {}
    self.regions_volume = {}

    self.type_mesh = ""

    # self.map_nodes = self.__get_node_map()
    # self.clean_map = self.__get_clean_map()
    
  
  
  
  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    self.__create_nodes_points()
    coarse_nodes = {}
    surfaces = {}
    s_id = 0
    num_rings = len(self.mesh_rings)
    for r, ring in enumerate(self.mesh_rings):
      for n_id in ring:
        surface_points = self.points_mesh[n_id]
        
        node = CoarseNodeTriangularMesh(
          n_id, 'triangular', self.hex_assembly.pitch
        )
        surfs, s_id = node.calculate_surfaces(surface_points, s_id)
        surfaces.update(surfs)
        
        # "inner_triangle"
        # "corner_triangle"
        # "square_side"
        print(surface_points)
        if r < num_rings - 1:  node.type_coarse_node = "inner_triangle"
        else:
          num_points = len(surface_points)
          if num_points == 4: node.type_coarse_node = "square_side"
          elif num_points == 3: node.type_coarse_node = "corner_triangle"
          
        coarse_nodes[n_id] = node
    
    self.coarse_nodes = coarse_nodes
    self.nodes_surfaces = surfaces
    self.num_surfaces = s_id

  def __create_nodes_points(self):
    nodes_surfaces, nodes_map = self.__get_mesh_in_rings()

    self.points_mesh = nodes_surfaces
    self.mesh_rings = nodes_map


  def __get_mesh_in_rings(self):
    """
    The function __get_mesh_in_rings calculates the triangles and 
    triangle rings for a mesh based on the pin centers of an assembly.
    :return: three values: node_id, triangles, and triangle_rings.
    """
    nodes_surfaces = {}
    nodes_map = []
    assembly = self.cell.content
    pin_centers = assembly.pin_centers
    num_rings = assembly.num_rings
    pitch = assembly.pitch
    center = pin_centers[0][0] # first ring

    #First ring --------------
    node_id = 1
    nid_ring = []
    for p in range(-6,0):
      p1 = center
      p2 = pin_centers[1][p]
      p3 = pin_centers[1][p+1]
      nodes_surfaces[node_id] = (p1, p2, p3)
      nid_ring.append(node_id)
      node_id += 1
    nodes_map.append(nid_ring)

    # Other rings -------------
    num_pins_on_side = 1
    for r in range(2, num_rings):
      nid_ring = []
      prev_ring = pin_centers[r-1]
      prev_ring_idx = -len(prev_ring)
      num_pins = len(pin_centers[r])
      on_side_pins_counter = 0
      on_side = False
      for p in range(-num_pins,0):
        if on_side: # Pin is on one of the sides
          p1 = pin_centers[r][p]
          p2 = prev_ring[prev_ring_idx]
          p3 = prev_ring[prev_ring_idx+1]
          nodes_surfaces[node_id] = (p1, p2, p3)
          nid_ring.append(node_id)
          
          p1 = pin_centers[r][p]
          p2 = pin_centers[r][p+1]
          p3 = prev_ring[prev_ring_idx+1]
          nodes_surfaces[node_id+1] = (p1, p2, p3)
          nid_ring.append(node_id+1)

          node_id += 2
          on_side_pins_counter += 1
          prev_ring_idx += 1

        else: # Pin is in one of the corners
          p1 = pin_centers[r][p]
          p2 = pin_centers[r][p+1]
          p3 = prev_ring[prev_ring_idx]
          on_side = True

          nodes_surfaces[node_id] = (p1, p2, p3)
          nid_ring.append(node_id)

          node_id += 1

        if on_side_pins_counter == num_pins_on_side: 
          on_side = False
          on_side_pins_counter = 0
      nodes_map.append(nid_ring)
      num_pins_on_side += 1

    nsurfs_boundary, boundary_ring = self.__get_mesh_in_boundary(node_id)
    nodes_surfaces.update(nsurfs_boundary)
    nodes_map.append(boundary_ring)
    
    return nodes_surfaces, nodes_map

  def __get_mesh_in_boundary(self, node_id):
    from math import cos
    from math import sin
    from math import radians

    n_id = node_id

    assembly = self.cell.content
    pin_centers = assembly.pin_centers
    num_rings = assembly.num_rings
    pitch = assembly.pitch
    
    # Boundary ----------------
    wrapper = self.cell.region.surface
    wrapper_radius = wrapper.radius
    
    wrapper_last_pin_radius = (num_rings-1)*pitch
    wrapper_last_pin_hw = (
      wrapper_last_pin_radius**2 - wrapper_last_pin_radius**2/4
    )**0.5
    
    dptc = wrapper_radius - wrapper_last_pin_radius  # distance_pin_to_corner
    dpts = wrapper.half_width - wrapper_last_pin_hw  # distance_pin_to_side

    dx_dptc = dptc * cos(radians(30))
    dy_dptc = dptc * sin(radians(30))

    sides_dxdy = {
      'A': {
        'dx': 0,
        'dy': dpts,
        "dtc": +dptc
      },
      'B': {
        'dx': dpts * cos(radians(30)),
        'dy': dpts * sin(radians(30)),
        "dtc": +dptc
      },
      'C': {
        'dx': dpts * cos(radians(30)),
        'dy': -dpts * sin(radians(30)),
        "dtc": dptc
      },
      'D': {
        'dx': 0,
        'dy': -dpts,
        "dtc": dptc
      },
      'E': {
        'dx': -dpts * cos(radians(30)),
        'dy': -dpts * sin(radians(30)),
        "dtc": dptc
      },
      'F': {
        'dx': -dpts * cos(radians(30)),
        'dy': dpts * sin(radians(30)),
        "dtc": dptc
      }
    }
    dtc_dx_dy = {
      'A': {
        't1': {
          "dx": -dpts * cos(radians(30)),
          "dy":  dpts * sin(radians(30)),
          "dptc_dx": -dptc * cos(radians(60)),
          "dptc_dy":  dptc * sin(radians(60))

        },
        't2': {
          "dx":  0.0,
          "dy":  dpts,
          "dptc_dx": -dptc * cos(radians(60)),
          "dptc_dy": dptc * sin(radians(60))
        },
      },
      'B': {
        't1': {
          "dx":  0.0,
          "dy":  dpts,
          "dptc_dx": dptc * cos(radians(60)),
          "dptc_dy": dptc * sin(radians(60))
        },
        't2': {
          "dx":  dpts * cos(radians(30)),
          "dy":  dpts * sin(radians(30)),
          "dptc_dx": dptc * cos(radians(60)),
          "dptc_dy": dptc * sin(radians(60))
        },
      },
      'C': {
        't1': {
          "dx":  dpts * cos(radians(30)),
          "dy":  dpts * sin(radians(30)),
          "dptc_dx": dptc,
          "dptc_dy": 0.0
        },
        't2': {
          "dx":  dpts * cos(radians(30)),
          "dy":  -dpts * sin(radians(30)),
          "dptc_dx": dptc,
          "dptc_dy": 0.0
        },
      },
      'D': {
        't1': {
          "dx":  dpts * cos(radians(30)),
          "dy":  -dpts * sin(radians(30)),
          "dptc_dx": dptc * cos(radians(60)),
          "dptc_dy": -dptc * sin(radians(60))
        },
        't2': {
          "dx":  0.0,
          "dy":  -dpts,
          "dptc_dx": dptc * cos(radians(60)),
          "dptc_dy": -dptc * sin(radians(60))
        },
      },
      'E': {
        't1': {
          "dx":  0.0,
          "dy":  -dpts,
          "dptc_dx": -dptc * cos(radians(60)),
          "dptc_dy": -dptc * sin(radians(60))
        },
        't2': {
          "dx":  -dpts * cos(radians(30)),
          "dy":  -dpts * sin(radians(30)),
          "dptc_dx": -dptc * cos(radians(60)),
          "dptc_dy": -dptc * sin(radians(60))
        },
      },
      'F': {
        't1': {
          "dx": -dpts * cos(radians(30)),
          "dy": -dpts * sin(radians(30)),
          "dptc_dx": -dptc,
          "dptc_dy": 0
        },
        't2': {
          "dx": -dpts * cos(radians(30)),
          "dy":  dpts * sin(radians(30)),
          "dptc_dx": -dptc,
          "dptc_dy": 0
        },
      },
    }
    
    hexagon_sides =  ['F','A','B','C','D','E']
    
    corner_positions = [
      0,
      0+9,
      0+9+9,
      0+9+9+9,
      0+9+9+9+9,
      0+9+9+9+9+9,
    ]

    nodes = {}
    node_ring = []

    last_ring = pin_centers[-1]
    num_pins_last_ring = len(last_ring)
    
    side_idx = 0
    distance = 0.0
    for p in range(-num_pins_last_ring, 0):
      side = hexagon_sides[side_idx]
      
      # Corners first -----------------------------------
      if p+num_pins_last_ring in corner_positions:
        dx = round(dtc_dx_dy[side]['t1']['dx'], 8)
        dy = round(dtc_dx_dy[side]['t1']['dy'], 8)
        dptc_dx = round(dtc_dx_dy[side]['t1']['dptc_dx'], 8)
        dptc_dy = round(dtc_dx_dy[side]['t1']['dptc_dy'], 8)
        p1 = last_ring[p]
        p2 = (
          last_ring[p][0] + dptc_dx, 
          last_ring[p][1] + dptc_dy, 
        )
        p3 = (
          last_ring[p][0] + dx, 
          last_ring[p][1] + dy, 
        )

        nodes[n_id] = (p1, p2, p3)
        node_ring.append(n_id)

        dx = round(dtc_dx_dy[side]['t2']['dx'], 8)
        dy = round(dtc_dx_dy[side]['t2']['dy'], 8)
        dptc_dx = round(dtc_dx_dy[side]['t2']['dptc_dx'], 8)
        dptc_dy = round(dtc_dx_dy[side]['t2']['dptc_dy'], 8)

        p1 = last_ring[p]
        p2 = (
          last_ring[p][0] + dptc_dx, 
          last_ring[p][1] + dptc_dy, 
        )
        p3 = (
          last_ring[p][0] + dx, 
          last_ring[p][1] + dy, 
        )
        nodes[n_id+1] = [p1, p2, p3]
        node_ring.append(n_id+1)

        n_id += 2

      # Then sides -------------------------------------
      dx = round(sides_dxdy[side]['dx'], 8)
      dy = round(sides_dxdy[side]['dy'], 8)
      p1 = last_ring[p]
      
      p2 = (
        last_ring[p][0] + dx, 
        last_ring[p][1] + dy, 
      )
      p3 = (
        last_ring[p+1][0] + dx, 
        last_ring[p+1][1] + dy, 
      )
      p4 = last_ring[p+1]

      nodes[n_id] = (p1, p2, p3, p4)
      node_ring.append(n_id)
      n_id += 1
      


      distance += pitch
      # print(distance)
      if round(distance,8) == round(wrapper_last_pin_radius,8):
        side_idx += 1
        distance = 0.0
      
    return nodes, node_ring  

  def calculate_nodes_surfaces(self):
    nodes_surfaces = {}
    surfaces = {}
    s_id = 1
    for n_id, node_points in self.points_mesh.items():
      num_points = len(node_points)
      if num_points == 3: # triangle
        p1, p2, p3 = node_points
        surf1 = (p1,p2)
        surf2 = (p2,p3)
        surf3 = (p3,p1)
        nodes_surfaces[n_id] = {
          s_id: surf1, 
          s_id+1: surf2, 
          s_id+2: surf3
        }
        surfaces[s_id] = surf1
        surfaces[s_id+1] = surf2
        surfaces[s_id+2] = surf3

        s_id += 3
      elif num_points == 4: # rectangle
        p1, p2, p3, p4 = node_points
        surf1 = (p1,p2)
        surf2 = (p2,p3)
        surf3 = (p3,p4)
        surf4 = (p4,p1)

        nodes_surfaces[n_id] = {
          s_id: surf1, 
          s_id+1: surf2, 
          s_id+2: surf3,
          s_id+3: surf4
        }
        surfaces[s_id] = surf1
        surfaces[s_id+1] = surf2
        surfaces[s_id+2] = surf3
        surfaces[s_id+3] = surf4

        s_id += 4
    self.surfaces = surfaces
    self.nodes_surfaces = nodes_surfaces
    self.num_surfaces = s_id - 1
    
  def calculate_surfaces_twins(self):
    """Class method to extract the surface twins of every node. It sweeps all
    surfaces and then call the method  find_surface_twin()

    Returns
    -------
    surface_twins : dict

    """
    

    surf_checked = {s_idx: False for s_idx in range(1,self.num_surfaces+2)}
    surface_twins = {s_idx: None for s_idx in range(1,self.num_surfaces+2)}
    for ring_idx, ring in enumerate(self.mesh_rings):
      # print(ring)
      for n_id in ring:
        node = self.coarse_nodes[n_id]
        node_surfs = node.surfaces
      
        for s_id, points in node_surfs.items():
  
          if surf_checked[s_id]: continue
          rings = []
          if ring_idx == 0:
            rings = [ring_idx, ring_idx+1]
          elif ring_idx == len(self.mesh_rings)-1:
            rings = [ring_idx-1, ring_idx]
          else: 
            rings = [ring_idx-1, ring_idx, ring_idx+1]
          twin = self.__find_surface_twin(n_id, points, rings, s_id)
          # if n_id == 7: print(s_id, twin)
          if twin:
            surface_twins[s_id] = twin
            surface_twins[twin] = s_id
            surf_checked[twin] = True
            surf_checked[s_id] = True
    
    self.surface_twins = surface_twins
  
  def __find_surface_twin(self, n_id, points, rings, s_id):
    """Class method to find the surface twin of one surface. It sweeps all the
    surfaces and compare the points  in order to determine wether is a twin or
    not.
    
    Parameters
    ----------
    n_id : int

    points : tuple

    rings : list

    Returns
    -------
    surf_twin : int or None
    """
    p1, p2 = points
    p1 = (round(p1[0], 10), round(p1[1], 10))
    p2 = (round(p2[0], 10), round(p2[1], 10))

    p1x, p1y = p1
    p2x, p2y = p2

    # if n_id <= 6: print("surf: ", s_id, p1,p2, "searching -------------------------------------")
    surf_twin = None

    # print(rings)
    for ring_idx in rings:
      # print(ring_idx)
      ring = self.mesh_rings[ring_idx]
      # print(ring)
      # if n_id == 7: print(ring)
      for other_n_id in ring:
        if n_id == other_n_id: continue
        node = self.coarse_nodes[n_id]
        node_surfs = node.surfaces
        for s_id_other, points_other in node_surfs.items():
          p1_other, p2_other = points_other
          p1_other = (round(p1_other[0], 10), round(p1_other[1], 10))
          p2_other = (round(p2_other[0], 10), round(p2_other[1], 10)) 
          # if other_n_id == 24: print("surf: ", s_id_other, p1_other, p2_other)
          
          p1x_o, p1y_o = p1_other
          p2x_o, p2y_o = p2_other
          
          # if n_id == 1: print(p1,p2)
          if p1x == p1x_o and p1y == p1y_o and p2x == p2x_o and p2y == p2y_o:
            # surf_twin = s_id_other
            # if n_id <= 6: print("twin found:", s_id_other)
            return s_id_other
          
          if p1x == p2x_o and p1y == p2y_o and p2x == p1x_o and p2y == p1y_o:
            # if n_id <= 6: print("twin found:", s_id_other)
            
            # surf_twin = s_id_other
            return s_id_other
          
    # return surf_twin
  
  def find_equivalent_nodes(self):
    """Class method to calculate the equivalent nodes in the triangular mesh.
    
    For an hexagonal assembly with one pin_cell type there is only three types
    of nodes:
      - the triangular subchannel inside the hexagon
      - the triangular subchannel in the corner
      - the squared subchannel on the edges
    
    So the proccess, to find the equivalent nodes is simply to check the zone
    where the coarse node is. This is all nodes are the same contained in all
    rings, except for the last ring.  In the last ring the way to differentiate
    is the number of points to check if it is a square or a triangle.

    Parameters
    ----------

    Returns
    -------

    """
    
    equivalent_nodes = {
      1: [], 2: [], 3: []
    }
    
    # Assuming a single pin type inside the hexagonal assembly
    num_rings = len(self.mesh_rings)
    for r in range(num_rings-1):
      ring = self.mesh_rings[r]
      for n_id in ring:
        equivalent_nodes[1].append(n_id)

    last_ring = self.mesh_rings[-1]
    for n_id in last_ring:
      node_surfs = self.points_mesh[n_id]
      
      if len(node_surfs) == 3:
        equivalent_nodes[2].append(n_id)
      if len(node_surfs) == 4:
        equivalent_nodes[3].append(n_id)
    
    
    # print(equivalent_nodes[2])
    self.equivalent_nodes = {
      equivalent_nodes[1][0]: equivalent_nodes[1], # inner triangles
      equivalent_nodes[2][0]: equivalent_nodes[2], # corner triangles
      equivalent_nodes[3][0]: equivalent_nodes[3], # square sides
    }

    self.type_nodes = {
      "inner_triangle": equivalent_nodes[1],
      "corner_triangle": equivalent_nodes[2],
      "square_side": equivalent_nodes[3],
    }
    self.unique_nodes = list(self.equivalent_nodes.keys())
  
  def find_equivalent_nodes_symmetry(self):
    """Class method to calculate the equivalent nodes symmetry 
    in the triangular mesh.
    
    
      - the triangular subchannel inside the hexagon
      - the triangular subchannel in the corner
      - the squared subchannel on the edges
    
    For the inner triangles and for the squares the symmetry is the same,
    and for the corner triangles it is {"mirror" : "right"}

    #TODO Check if it is neccesary to change for the inner triangles to 
    #TODO mirror-down when it comes to region symmetry
    Parameters
    ----------

    Returns
    -------

    """
    nodes_symmetry = {}
    
    type_nodes_symmetry = {
      "inner_triangle": {"same": ""},
      "corner_triangle": {"mirror": "right"},
      "square_side": {"same": ""},
    }
    for ttype, eq_nodes_list in self.type_nodes.items():
      main_node = eq_nodes_list[0]
      nodes_symmetry[main_node] = {}
      for n_eq in eq_nodes_list:
        nodes_symmetry[main_node][n_eq] = type_nodes_symmetry[ttype]

    self.symmetry = nodes_symmetry
    









