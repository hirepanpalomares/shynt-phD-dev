
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
    self.nodes_surfaces = {}
    self.surfaces = {}
    self.num_surfaces = 0
    self.surface_twins = {}

    # self.calculate_nodes_coordinates()
    # self.calculate_nodes_surfaces()
    # self.calculate_surfaces_twins()
    
    self.map_pins = []
    self.symmetry = {}
    self.clean_mesh_map = []


    self.equivalent_nodes = {}
    self.corse_nodes_regions = {}
    self.regions_coarse_node = {}
    self.coarse_nodes_regions_material = {}
    self.regions_volume = {}

    self.coarse_nodes = {}
    self.type_mesh = ""

    # self.map_nodes = self.__get_node_map()
    # self.clean_map = self.__get_clean_map()
    
  
  def __create_nodes_switch(self, universe):
    coarse_nodes = None
    coarse_nodes_map = None
    try:
      assert isinstance(universe, HexagonalLatticeTypeX)
      coarse_nodes, coarse_nodes_map = self.__create_nodes_HexagonalLattice(
        universe
      )
    except AssertionError:
      print("type of mesh not supported for cell")
      raise NotImplementedError
    
    self.coarse_nodes = coarse_nodes
    self.coarse_nodes_map = coarse_nodes_map


  def __create_nodes_HexagonalLattice(self, universe):
    map_nodes = []
    coarse_nodes = {}
    node_counter = 1
    triangle_coords = self.get_triangules_coordinates()

    self.points_mesh = triangle_coords
    self.__symmetry = {
      1: {
        1: {"same": ""},
        2: {"mirror": "right"},
        3: {"same": ""},
        4: {"mirror": "right"},
        5: {"same": ""},
        6: {"mirror": "right"},
        7: {"same": ""},
        8: {"mirror": "right"},
        9: {"same": ""},
        10: {"mirror": "right"},
        11: {"same": ""},
        12: {"mirror": "right"},
      }  
    }

    for n_id, triangle_points in triangle_coords.items():
      triangle_cells, geometry_info = self.get_cells()
  
  def calculate_nodes_coordinates(self):
    triangles = {}
    coarse_node_mesh_rings = []

    n_id, nodes_points_inside, mesh_rings = self.__get_mesh_in_rings()
    triangles.update(nodes_points_inside)
    coarse_node_mesh_rings += mesh_rings

    n_id, nodes_points_boundary, mesh_rings = self.__get_mesh_in_boundary(n_id)
    triangles.update(nodes_points_boundary)

    coarse_node_mesh_rings += [mesh_rings]

    self.points_mesh = triangles
    self.mesh_rings = coarse_node_mesh_rings

  def __get_mesh_in_rings(self):
    triangles = {}
    triangle_rings = []
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
      triangles[node_id] = (p1, p2, p3)
      nid_ring.append(node_id)
      node_id += 1
    triangle_rings.append(nid_ring)

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
          triangles[node_id] = (p1, p2, p3)
          nid_ring.append(node_id)
          
          p1 = pin_centers[r][p]
          p2 = pin_centers[r][p+1]
          p3 = prev_ring[prev_ring_idx+1]
          triangles[node_id+1] = (p1, p2, p3)
          nid_ring.append(node_id+1)

          node_id += 2
          on_side_pins_counter += 1
          prev_ring_idx += 1

        else: # Pin is in one of the corners
          p1 = pin_centers[r][p]
          p2 = pin_centers[r][p+1]
          p3 = prev_ring[prev_ring_idx]
          on_side = True

          triangles[node_id] = (p1, p2, p3)
          nid_ring.append(node_id)

          node_id += 1

        if on_side_pins_counter == num_pins_on_side: 
          on_side = False
          on_side_pins_counter = 0
      triangle_rings.append(nid_ring)
      num_pins_on_side += 1

    return node_id, triangles, triangle_rings
  
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
      
    return node_id, nodes, node_ring  

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

        node_surfs = self.nodes_surfaces[n_id]
      
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
        node_surfs = self.nodes_surfaces[other_n_id]
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
  

  def get_cells(self, 
    triangle_points, outer_surf, pin_radius, fuel_mat, coolant_mat
  ):
    from math import pi
    from Shynt.api_py.Geometry.surfaces import (
      CylinderPad, InfiniteRectangleCylinderZ, PlaneX
    )

    p1, p2, p3 = triangle_points
    height = outer_surf.half_width
    base = outer_surf.radius / 2
    hypotenuse = outer_surf.radius
    rectangle_height = height
    rectangle_width = base
    triangle_volume = base * height / 2
    center_fuel2 = (-1, 1)

    x1, y2 = p1
    x2 = p2[0]
    y1 = p3[0]

    # center_fuel2 = (None,None)
    fuel1_surf = CylinderPad(0.0, 0.0, 0.0, pin_radius, 90, 120)
    fuel2_surf = CylinderPad(center_fuel2[0], center_fuel2[1], 0.0, pin_radius, 300, 120)
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2, pin_radius)
    hypotenuse_plane = PlaneX(x1)
    hypotenuse_plane.rotate(angle=-30, ref_point=(x1, y1))
    
    region_fuel1 = -fuel1_surf
    region_fuel2 = -fuel2_surf
    region_coolant = +hypotenuse_plane & +fuel1_surf & +fuel2_surf

    vol_circ = pi * pin_radius* pin_radius
    
    vol_fuel1 = vol_circ / 12
    vol_fuel2 = vol_circ / 2
    vol_cool = triangle_volume - vol_fuel1 - vol_fuel2

    coolant_cell = Cell(
      name="coolant_trianglular_mesh_hexagonal_assembly", 
      fill=coolant_mat,
      volume=vol_cool,
      region=region_coolant
    )
    fuel1_cell = Cell(
      name="fuel1_trianglular_mesh_hexagonal_assembly", 
      fill=fuel_mat,
      volume=vol_fuel1,
      region=region_fuel1
    )
    fuel2_cell = Cell(
      name="fuel2_trianglular_mesh_hexagonal_assembly", 
      fill=fuel_mat,
      volume=vol_fuel2,
      region=region_fuel2
    )
    cells = {
      coolant_cell.id: coolant_cell,
      fuel1_cell.id: fuel1_cell,
      fuel2_cell.id: fuel2_cell,
    }
    surfaces_for_detectors = {
      "fuel": {
        fuel1_surf.id: f"surf {fuel1_surf.id} pad 0.0 0.0 0.0 {pin_radius} 270 360",
        fuel2_surf.id: f"surf {fuel1_surf.id} pad {center_fuel2[0]} {center_fuel2[1]} 0.0 {pin_radius} 270 360"
      },
      "boundary": {
        rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
        rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
        hypotenuse_plane.id: f"surf {hypotenuse_plane.id} px 0.00\ntrans s {hypotenuse_plane.id} 0.0 0.0 0.0 0.0 0.0 30\n\n\n",
      },
      "boundary_guide": {
        "left": hypotenuse_plane.id,
        "top": rectangle_surf.surf_top.id,
        "right": rectangle_surf.surf_right.id,
      },
      "boundary_guide_inv": {
        hypotenuse_plane.id : "left",
        rectangle_surf.surf_top.id : "top",
        rectangle_surf.surf_right.id : "right",
      },
      "boundary_surfaces": {
        hypotenuse_plane.id: hypotenuse_plane,
        rectangle_surf.surf_top.id: rectangle_surf.surf_top,
        rectangle_surf.surf_right.id: rectangle_surf.surf_right,
      },
      "boundary_surfaces_areas": {
        hypotenuse_plane.id: hypotenuse,
        rectangle_surf.surf_top.id: rectangle_width,
        rectangle_surf.surf_right.id: rectangle_height,
      },
      "current_directions": {
        fuel1_surf.id: {"inward": "-1", "outward": "1"},
        fuel2_surf.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
        hypotenuse_plane.id: {"inward": "1", "outward": "-1"}
      }
    }

    geometry_info = {
      "surfaces_for_detectors": surfaces_for_detectors
    }

    return cells, geometry_info
    pass
  