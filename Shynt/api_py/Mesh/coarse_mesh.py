
from Shynt.api_py.Mesh.coarse_node import (
  CoarseNodeTriangularMesh_InnerTriangle,
  CoarseNodeTriangularMesh_SquareSubChanell,
  CoarseNodeTriangularMesh_TriangleCorner,
  CoarseNodeSquarePinCell,
  CoarseNodeHexagonalPinCell
)

from Shynt.api_py.Geometry.universes import (
  SquareLattice,
  HexagonalLatticeTypeX,
  Pin
)
from Shynt.api_py.Geometry.surfaces import (
  InfiniteSquareCylinderZ
)

from Shynt.api_py.Geometry.cells import Cell


class CoarseMesh():

  def __init__(self, cell: Cell) -> None:
    super().__init__()
    self.__cell = cell
  

  
  def calculate_surfaces_twins(self):
    """Class method to extract the surface twins of every node. It sweeps all
    surfaces and then call the method  find_surface_twin()

    Returns
    -------
    surface_twins : dict

    """

    num_coarse_nodes = len(self.coarse_nodes)
    print(f"Calculating surface twins for {num_coarse_nodes} coarse_nodes ...")

    surf_checked = {s_idx: False for s_idx in range(1,self.num_surfaces+2)}
    surface_twins = {s_idx: None for s_idx in range(1,self.num_surfaces+2)}
    for n_id, coarse_node in self.coarse_nodes.items():
      print(n_id, end=",")
      if n_id % 20 == 0: print()
      
      node_surfs = coarse_node.surfaces
      for s_id, points in node_surfs.items():
        if surf_checked[s_id]: continue
        twin = self.__find_surface_twin(n_id, points, s_id)
        # if n_id == 7: print(s_id, twin)
        if twin:
          surface_twins[s_id] = twin
          surface_twins[twin] = s_id
          surf_checked[twin] = True
          surf_checked[s_id] = True
    print()
    self.surface_twins = surface_twins
  
  def __find_surface_twin(self, n_id, points, s_id):
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

    # if n_id <= 6: print("surf: ", s_id, p1,p2, "searching -----------")
    surf_twin = None

    # print(rings)
    
    for other_n_id, coarse_node in self.coarse_nodes.items():
      if n_id == other_n_id: continue      
      node_surfs = coarse_node.surfaces
      for s_id_other, points_other in node_surfs.items():
        p1_other, p2_other = points_other
        p1_other = (round(p1_other[0], 10), round(p1_other[1], 10))
        p2_other = (round(p2_other[0], 10), round(p2_other[1], 10)) 

        p1x_o, p1y_o = p1_other
        p2x_o, p2y_o = p2_other
        
        if p1x == p1x_o and p1y == p1y_o and p2x == p2x_o and p2y == p2y_o:
          return s_id_other
        
        if p1x == p2x_o and p1y == p2y_o and p2x == p1x_o and p2y == p1y_o:
          return s_id_other


  @property
  def cell(self) -> Cell:
    return self.__cell


class PinCellMesh(CoarseMesh):
  """Class to represent  a pin cell mesh only used in a square lattice.
  Each coarse node is a pin cell, so different coarse nodes be differentiate
  by type of pin.
  Steps to generate the coarse_mesh:
    1. Calculate the nodes coordinates (points of the mesh) and the 
      map of nodes
    2. With each set of points generate instance CoarseNode
      2.a Generate surfaces (only a set of two points)
      2.b Count surfaces ids and calculate surface twins
    4. Calculate equivalent coarse nodes or provide them

  Attributes
  ----------

  Methods
  -------
  """
    
  def __init__(self, cell):
    try:
      if isinstance(cell.content, SquareLattice):
        pass
      elif isinstance(cell.content, Pin):
        pass
      else:
        raise AssertionError
    except AssertionError:
      print(" ************ Error ************ ")
      print("PinCellMesh only supported for SquareLattice or Pin")
      raise SystemExit
    
    super().__init__(cell)
    self.__isPin = False
    if isinstance(cell.content, Pin):
      self.__isPin = True

    self.type_mesh = ""
    self.lattice = super().cell.content
    self.points_mesh = {}
    self.coarse_nodes_map = []
    self.coarse_nodes = {}
    self.num_surfaces = 0
    self.surfaces = {}
    self.surface_twins = {}

    self.unique_nodes = []
    self.equivalent_nodes = {}
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}

  
  
    
  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    coarse_nodes = {}
    surfaces = {}
    nodes_map = []
    s_id = 0
    n_id = 1
    if self.__isPin:
      # check surface
      pin_universe = super().cell.content
      print(pin_universe)
      pin_cell_wrapper = super().cell.region.surface
      if isinstance(pin_cell_wrapper, InfiniteSquareCylinderZ):
        node = CoarseNodeSquarePinCell(
          n_id, 'pin_cell_mesh', pin_cell_wrapper.half_width,
          pin_cell_wrapper.center
        )
        s_id = node.calculate_surfaces(s_id)
        surfaces.update(node.surfaces)
        coarse_nodes[1] = node
      else:
        # hexagonal cell
        node = CoarseNodeHexagonalPinCell(
          n_id, 'pin_cell_mesh', pin_cell_wrapper
        )
        s_id = node.calculate_surfaces(s_id)
        node.universe = pin_universe 
        surfaces.update(node.surfaces)
        coarse_nodes[1] = node
      
    else:
      pin_centers = self.lattice.pin_centers
      half_pitch = self.lattice.pitch / 2
      
      for i, row in enumerate(pin_centers):
        row_node = []
        for j, center in enumerate(row):
          pin_universe = self.lattice.array[i][j]

          node = CoarseNodeSquarePinCell(
            n_id, 'pin_cell_mesh', half_pitch, center
          )
          s_id = node.calculate_surfaces(s_id)
          surfaces.update(node.surfaces)
          node.universe = pin_universe 
          coarse_nodes[n_id] = node

          row_node.append(n_id)
          n_id += 1
        nodes_map.append(row_node)
        
    self.surfaces = surfaces
    self.coarse_nodes_map = nodes_map
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id


  def find_equivalent_nodes(self):
    """Class method to calculate the equivalent nodes in the square lattice.
    It takes the name of every pin to differentiate from other pins

    Parameters
    ----------

    Returns
    -------

    """
    equivalent_nodes = {}

    if self.__isPin:
      equivalent_nodes[1] = [1]
    else:
      array = self.lattice.array
      pin_types = {

      }
      for i, row in enumerate(array):
        for j, pin in enumerate(row):
          node_id = self.coarse_nodes_map[i][j]
          try:
            pin_types[pin.name].append(node_id)
          except KeyError:
            pin_types[pin.name] = [node_id]
      
      for pin_name, array in pin_types.items():
        equivalent_nodes[array[0]] = array
    
    self.equivalent_nodes = equivalent_nodes
    self.unique_nodes = list(equivalent_nodes.keys())

  def find_equivalent_nodes_symmetry(self):
    """Class method to find the equivalent nodes symmetry. For
    This mesh all the nodes have "same" symmetry
    
    Parameters
    ----------

    Returns
    -------

    """

    nodes_symmetry = {}
    for n_id in self.unique_nodes:
      nodes_symmetry[n_id] = {}
      for n_eq in self.equivalent_nodes[n_id]:
        nodes_symmetry[n_id][n_eq] = {"same": ""}
    self.symmetry = nodes_symmetry

  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      # print(regs_main_node)
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]

    self.equivalent_regions = regions_eq

  def find_eq_surfaces(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the dictionary
    since the surfaces are declared in the same order.

    Parameters
    ----------

    Returns
    -------
    
    """
    surfaces_eq = {}

    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      for surf in surfs_main_node:
        surfaces_eq[surf] = surf
      for eq_node in eq_nodes:
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s, s_p in enumerate(surfs_eq_node):
          surfaces_eq[s_p] = surfs_main_node[s]
    self.equivalent_surfaces = surfaces_eq

  
  @property
  def nodes_surfaces(self):
    nodes_surfaces = {}
    for n_id, coarse_node in self.coarse_nodes.items():
      nodes_surfaces[n_id] = coarse_node.surfaces
    return nodes_surfaces
  

  def __create_nodes_SquareLattice__deprecated(self, universe):
    map_nodes = []
    coarse_nodes = {}
    node_counter = 1
    for y in range(universe.ny):
      map_row = []
      for x in range(universe.nx):
        pin_cell_id = universe.array[y][x]
        map_row.append(node_counter)
        pin_cell = universe.cells[pin_cell_id]
        coarse_node_cells, geometry_info = self.__get_pin_cell_coarse_node(pin_cell)

        # Now with these cells create a universe 
        square_universe = Universe(name=f"rectangle_coarse_node_cell_{node_counter}")
        square_universe.cells = coarse_node_cells

        # Fill a rectangular cell with these universe
        # surf_rectangle = InfiniteRectangleCylinderZ(x1,x2,y1,y2)
        surf_square = geometry_info["square_surf"]
        square_cell = Cell(
            fill=square_universe, 
            region=-surf_square, 
            name=f"coarse_node_cell_{node_counter}"
        )
        coarse_node = SquarePinCoarseNode(square_cell, geometry_info)
        coarse_node.id = node_counter
        coarse_nodes[node_counter] = coarse_node
        node_counter += 1
      map_nodes.append(map_row)
    return coarse_nodes, np.array(map_nodes)

  def __create_nodes_SquarePin__deprecated(self):
    map_nodes = []
    coarse_nodes = {}
    node_counter = 1
    pin_cell = super().cell
    coarse_node_cells, geometry_info = self.__get_pin_cell_coarse_node(pin_cell)

    # Now with these cells create a universe 
    square_universe = Universe(name=f"rectangle_coarse_node_cell_{node_counter}")
    square_universe.cells = coarse_node_cells

    # Fill a rectangular cell with these universe
    surf_square = geometry_info["square_surf"]
    square_cell = Cell(
        fill=square_universe, 
        region=-surf_square, 
        name=f"coarse_node_cell_{node_counter}"
    )
    coarse_node = SquarePinCoarseNode(square_cell, geometry_info)
    coarse_node.id = node_counter
    coarse_nodes[node_counter] = coarse_node
    
    return coarse_nodes, np.array([[1]])

  def __get_pin_cell_coarse_node__deprecated(self, pin_cell):
    
    def find_fuel_cell(cells):
      fuel_cells = {}
      for cell in cells.values():
        if cell.content.isFuel:
          fuel_cells[cell.id] = cell
      return fuel_cells
        
    cells = pin_cell.content.cells
    fuel_cells = find_fuel_cell(cells)
    non_fuel_cells = {c_id: c for c_id, c in cells.items() if c_id not in fuel_cells}
    fuel_surface = list(fuel_cells.values())[0].region.surface
    square_surf = pin_cell.region.surface
    half_width = square_surf.half_width
    square_length = half_width * 2
    num_fuel_cells = len(list(fuel_cells.keys()))
    num_nonfuel_cells = len(list(non_fuel_cells.keys()))
    num_fine_nodes = num_fuel_cells + num_nonfuel_cells

    type_node = f"square_pin_{num_fine_nodes}"
    for c_id, cell in fuel_cells.items():
      type_node += f"_{cell.content.name}"
    for c_id, cell in non_fuel_cells.items():
      type_node += f"_{cell.content.name}"

    surfaces_for_detectors = {
      "fuel": {
        fuel_surface.id: f"surf {fuel_surface.id} cyl 0.0 0.0 {fuel_surface.radius}",
      },
      "boundary": {
        square_surf.surf_left.id: f"surf {square_surf.surf_left.id} px {-half_width}\n",
        square_surf.surf_top.id: f"surf {square_surf.surf_top.id} py {half_width}\n",
        square_surf.surf_right.id: f"surf {square_surf.surf_right.id} px {half_width}\n",
        square_surf.surf_bottom.id: f"surf {square_surf.surf_bottom.id} py {-half_width}\n",
      },
      "boundary_guide": {
        "top": square_surf.surf_top.id,
        "right": square_surf.surf_right.id,
        "bottom": square_surf.surf_bottom.id,
        "left": square_surf.surf_left.id
      },
      "boundary_guide_inv": {
        square_surf.surf_top.id : "top",
        square_surf.surf_right.id : "right",
        square_surf.surf_bottom.id : "bottom",
        square_surf.surf_left.id: "left",
      },
      "boundary_surfaces": {
        square_surf.surf_left.id: square_surf.surf_left,
        square_surf.surf_top.id: square_surf.surf_top,
        square_surf.surf_right.id: square_surf.surf_right,
        square_surf.surf_bottom.id: square_surf.surf_bottom,
      },
      "boundary_surfaces_areas": {
        square_surf.surf_top.id: square_length,
        square_surf.surf_right.id: square_length,
        square_surf.surf_bottom.id: square_length,
        square_surf.surf_left.id: square_length,

      },
      "current_directions": {
        fuel_surface.id: {"inward": "-1", "outward": "1"},
        square_surf.surf_left.id: {"inward": "1", "outward": "-1"},
        square_surf.surf_top.id: {"inward": "-1", "outward": "1"},
        square_surf.surf_right.id: {"inward": "-1", "outward": "1"},
        square_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
      }
    }

    geometry_info =  {
      "half_width": square_surf.half_width,
      "radius": fuel_surface.radius,
      "square_surf": square_surf,
      "fuel_relation": {
        "fuel": list(fuel_cells.keys()),
        "non_fuel": list(non_fuel_cells.keys()),
      },
      "cells": cells,
      "surfaces_for_detectors": surfaces_for_detectors,
      "type": type_node
    } 

    return cells, geometry_info


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
        node = None
        if r < num_rings - 1:
          node = CoarseNodeTriangularMesh_InnerTriangle(
            n_id, self.hex_assembly, surface_points
          )
        else:
          num_points = len(surface_points)
          if num_points == 4: 
            node = CoarseNodeTriangularMesh_SquareSubChanell(
              n_id, self.hex_assembly, surface_points
            )
          elif num_points == 3: 
            node = CoarseNodeTriangularMesh_TriangleCorner(
              n_id, self.hex_assembly, surface_points
            )
            
        surfs, s_id = node.calculate_surfaces(s_id)
        surfaces.update(surfs)
        
        
          
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
      1: [], # inner triangle
      2: [], # corner triangles
      3: []  # square sides
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
    
    for ttype, eq_nodes_list in self.type_nodes.items():
      main_node = eq_nodes_list[0]
      nodes_symmetry[main_node] = {}
      for n, n_eq in enumerate(eq_nodes_list):
        if ttype == 'inner_triangle':
          nodes_symmetry[main_node][n_eq] = {'same': ''}
        elif ttype == 'corner_triangle':
          if n%2 == 0: 
            nodes_symmetry[main_node][n_eq] = {'same': ''}
          else:
            nodes_symmetry[main_node][n_eq] = {'mirror': 'right'}
        elif ttype == 'square_side':
          nodes_symmetry[main_node][n_eq] = {'same': ''}
          

    self.symmetry = nodes_symmetry
    
  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]


    self.equivalent_regions = regions_eq
    
  def find_eq_surfaces(self):
    """Class method to find the equivalent surfaces of nodes of the same type
    with respect to the main node. The criteria is the symmetry of the node

    Parameters
    ----------

    Returns
    -------
    
    """
   

    surfaces_eq = {}
    mirror_right = {'mirror': 'right'}
    mirror_down = {'mirror': 'down'}
    mirror_right_down = {'mirror': 'right_down'}



    for n_id, eq_nodes in self.equivalent_nodes.items():
      # print(n_id, eq_nodes)
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      # print(surfs_main_node)
      for surf in surfs_main_node: surfaces_eq[surf] = surf 
        

      for eq_node in eq_nodes:
        node_symmetry = self.symmetry[n_id][eq_node]
        # print(eq_node, node_symmetry)
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s_eq, s_m in zip(surfs_eq_node, surfs_main_node):
          surfaces_eq[s_eq] = s_m 
    self.equivalent_surfaces = surfaces_eq


class SquareGridHexPin(CoarseMesh):
  """Class to represent  a square grid mesh only used in a hexagonal pin.
  Each coarse node is a quarter of the hexagonal pin

  
  Attributes
  ----------

  Methods
  -------
  """
    
  def __init__(self, cell):
    try:
      assert(isinstance(cell.content, Pin))
        
    except AssertionError:
      print(" ************ Error ************ ")
      print("SquareGridHexPin only supported for Pin universe")
      raise SystemExit
    
    super().__init__(cell)

    self.type_mesh = ""
    self.lattice = super().cell.content
    self.points_mesh = {}
    self.coarse_nodes_map = []
    self.coarse_nodes = {}
    self.num_surfaces = 0
    self.surfaces = {}
    self.surface_twins = {}

    self.unique_nodes = []
    self.equivalent_nodes = {}
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}

  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype
    from Shynt.api_py.Mesh.coarse_node import CoarseNodeSquareGridHexPin
    coarse_nodes = {}
    surfaces = {}
    nodes_map = []
    s_id = 0
    n_id = 1
    
    # check surface
    pin_universe = super().cell.content
    pin_cell_wrapper = super().cell.region.surface
    if isinstance(pin_cell_wrapper, InfiniteHexagonalCylinderXtype):
      #Hexagonal Pin type X
      nodes_positions = ["top_left", "top_right", "lower_right", "lower_left"]
      for p, position in enumerate(nodes_positions):
        node = CoarseNodeSquareGridHexPin(
          n_id, 'square_grid_hex_pin', pin_cell_wrapper.half_width,
          pin_cell_wrapper.radius, position, pin_cell_wrapper.center
        )
        node.universe = pin_universe
        s_id = node.calculate_surfaces(s_id)
        surfaces.update(node.surfaces)
        coarse_nodes[p+1] = node
    else:
      #Hexagonal Pin type Y
      raise NotImplementedError
      
     
    self.surfaces = surfaces
    self.coarse_nodes_map = nodes_map
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id


  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      # print(regs_main_node)
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]

    self.equivalent_regions = regions_eq

  def find_eq_surfaces(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the dictionary
    since the surfaces are declared in the same order.

    Parameters
    ----------

    Returns
    -------
    
    """
    surfaces_eq = {}

    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      for surf in surfs_main_node:
        surfaces_eq[surf] = surf
      for eq_node in eq_nodes:
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s, s_p in enumerate(surfs_eq_node):
          surfaces_eq[s_p] = surfs_main_node[s]
    self.equivalent_surfaces = surfaces_eq

  def __find_surface_twin(self, n_id, points, s_id):
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

    # if n_id <= 6: print("surf: ", s_id, p1,p2, "searching -----------")
    surf_twin = None

    # print(rings)
    
    for other_n_id, coarse_node in self.coarse_nodes.items():
      if n_id == other_n_id: continue      
      node_surfs = coarse_node.surfaces
      for s_id_other, points_other in node_surfs.items():
        p1_other, p2_other = points_other
        p1_other = (round(p1_other[0], 10), round(p1_other[1], 10))
        p2_other = (round(p2_other[0], 10), round(p2_other[1], 10)) 

        p1x_o, p1y_o = p1_other
        p2x_o, p2y_o = p2_other
        
        if p1x == p1x_o and p1y == p1y_o and p2x == p2x_o and p2y == p2y_o:
          return s_id_other
        
        if p1x == p2x_o and p1y == p2y_o and p2x == p1x_o and p2y == p1y_o:
          return s_id_other

  @property
  def nodes_surfaces(self):
    nodes_surfaces = {}
    for n_id, coarse_node in self.coarse_nodes.items():
      nodes_surfaces[n_id] = coarse_node.surfaces
    return nodes_surfaces
  

class SquareGridHexAssembly(CoarseMesh):
  """Class to represent a square grid coarse mesh where the coarse nodes
  surfaces are shared totally with the contiguous coarse node, i.e. there
  is no splitting of outward neutron currents between two coarse nodes.

  For the mesh to work the following parameters have to be provided hardcoded
  and externally:
    - Unique nodes
    - the surfaces of the nodes that have a diagonal (done in fix boundaries)
    - equivalent nodes
    - equivalent nodes symmetry
    - coarse_nodes_regions
    - coarse_nodes_regions_materials
    - regions_coarse_node
    - regions volume
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
  __create_nodes_hex_assem() :

  __get_node_map() :

  __get_clean_map() :

  __get_x_div() :

  __get_y_div() :
  
  """

  def __init__(self, cell, offset=0.075):
    super().__init__(cell)
    self.__offset = offset
    self.hex_assembly = cell.content
    self.hex_wrapper = cell.region.surface
    self.coarse_nodes_map = []
    self.node_types = {}
    self.node_quadrants = {}

    self.x_div = []
    self.y_div = []
    self.points_mesh = []
    self.rectangles = []

    self.nodes_surfaces = {}
    self.num_surfaces = 0
    self.surface_twins = {}
    
    
    self.coarse_nodes = {}

    self.unique_nodes = []
    self.equivalent_nodes = {}
    self.equivalent_nodes_lookup = {}

    
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}

    self.corse_nodes_regions = {}
    self.regions_coarse_node = {}
    self.coarse_nodes_regions_material = {}
    self.type_mesh = "square_grid"

  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """

    coarse_nodes = {}
    surfaces = {}
    nodes_surfaces = {}
    s_id = 0
    
    pin_centers = self.hex_assembly.pin_centers
    half_pitch = self.hex_assembly.pitch / 2

    # self.calculate_rectangles()
    
    for i, row in enumerate(self.coarse_nodes_map):
      row_node = []
      for j, n_id in enumerate(row):
        if n_id == 0: continue
        node_type = ""
        quadrant = ""
        try:
          node_type = self.node_types[n_id]
          quadrant = self.node_quadrants[n_id]
        except KeyError:
          pass
        coarse_node_class = grid_coarse_node_manager(node_type)
        # print(coarse_node_class)
        node = coarse_node_class(
          n_id, 'pin_cell_mesh', half_pitch, quadrant, self.hex_wrapper
        )

        rectangle_points = self.rectangles[n_id-1]
        s_id = node.calculate_surfaces(s_id, rectangle_points)
        surfaces.update(node.surfaces)
        nodes_surfaces[n_id] = node.surfaces
        coarse_nodes[n_id] = node

        row_node.append(n_id)
        
    self.surfaces = surfaces
    self.nodes_surfaces = nodes_surfaces
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id

  def calculate_rectangles(self):
    x_div = self.calculate_x_div()
    y_div = self.calculate_y_div(x_div)
    self.x_div = x_div
    self.y_div = y_div

    rectangles = self.get_rectangles_from_mesh_coord(x_div, y_div)
    print(len(rectangles))

  def calculate_x_div(self):
    x_div = []
    pins_array = self.hex_assembly.array
    middle_idx = len(pins_array) // 2
    
    first_row = pins_array[0]
    middle_row = pins_array[middle_idx]
    # hex_wrapper = super().cell.region.surface

    
    central_x_div = [
      self.hex_wrapper.center[0] - self.hex_wrapper.radius
    ]
    pitch = self.hex_assembly.pitch
    limit1 = first_row[0].center[0]
    limit2 = first_row[-1].center[0]

    for pin in middle_row:
      cx, cy = pin.center

      if cx < limit1:
        central_x_div.append(round(cx - self.__offset,8))
        if round(cx + pitch/2,8) == limit1:
          central_x_div.append(round(cx + pitch/2,8))
        else:
          central_x_div.append(round(cx - self.__offset + pitch/2,8))
        
      elif cx + pitch > limit1 and cx + pitch < limit2:
        if cx + pitch/2 == limit1:
          central_x_div.append(cx - self.__offset)
          central_x_div.append(cx + pitch/2)
        else:
          central_x_div.append(cx)
          central_x_div.append(cx + pitch/2)
      elif cx + pitch > limit2:
        if cx + pitch/2 == limit2:
          central_x_div.append(cx)
          central_x_div.append(cx + pitch/2)
        else:
          central_x_div.append(cx + self.__offset)
          central_x_div.append(cx + self.__offset + pitch/2)
    
    central_x_div[-1] = self.hex_wrapper.center[0] + self.hex_wrapper.radius
    
    x_div.append(central_x_div.copy()) 
    x_div.append(central_x_div.copy()) 

    last_row = central_x_div.copy()
    for i in range(9):
      new_row = last_row[1:-1]
      x_div.append(new_row)
      x_div = [new_row] + x_div

      last_row = new_row
        
  
    return x_div

  def calculate_y_div(self, x_div):
    y_div = [
      self.hex_wrapper.half_width
    ]
    for row in x_div:
      x_value = row[0]
      new_y = round(
        self.hex_wrapper.surf_F.useFunction(x_value, given="x"),8
      )
      y_div.append(new_y)
    
      if new_y == self.hex_wrapper.center[1]:
        break
    
    
    half_y_div = []
    for i in range(-2, -len(y_div)-1, -1):
      # print(i)
      
      half_y_div.append(y_div[i]*-1)
      
    y_div += half_y_div
  
   
    return y_div
    
  def get_rectangles_from_mesh_coord(self, x_div, y_div):
    self.x_div = x_div
    self.y_div = y_div

    mesh = []
    node_counter = 1
    row_x = 0
    num_y_div = len(y_div)
    
    for y in range(1, num_y_div):
      y_t = y_div[y-1]
      y_b = y_div[y]

      num_x_div = len(x_div[row_x])
      for x in range(1,num_x_div):
        x_l = x_div[row_x][x-1]
        x_r = x_div[row_x][x]
        rectangle = ((x_l,x_r),(y_b,y_t))
        
        mesh.append(rectangle)
        node_counter += 1

      row_x += 1
  
    self.rectangles = mesh
    return mesh

  def generate_fine_mesh_regions(self, unique_regions):
    from Shynt.api_py.Geometry.cells import Cell
    from Shynt.api_py.Mesh.local_mesh_material import MaterialMesh
    
    print('creating fine mesh ...')
    for n_id in  self.coarse_nodes:
      eq_node = self.equivalent_nodes_lookup[n_id]
      fine_regs = {}
      for reg in unique_regions[eq_node]:
        new_fine_reg = (Cell(fill=reg['material'], volume=reg['volume'])) 
        fine_regs[new_fine_reg.id] = new_fine_reg 
        # print(new_fine_reg.volume)
      new_fine_mesh = MaterialMesh(
        coarse_node=self.coarse_nodes[n_id],
        type_coarse_mesh=self.type_mesh
      )
      new_fine_mesh.regions = fine_regs
      self.coarse_nodes[n_id].fine_mesh = new_fine_mesh
        
  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]


    self.equivalent_regions = regions_eq
    
  def find_eq_surfaces(self):
    """Class method to find the equivalent surfaces of nodes of the same type
    with respect to the main node. The criteria is the symmetry of the node

    Parameters
    ----------

    Returns
    -------
    
    """
   

    surfaces_eq = {}

    same = {'same': ''}
    mirror_right = {'mirror': 'right'}
    mirror_down = {'mirror': 'down'}
    mirror_right_down = {'mirror': 'right_down'}



    for n_id, eq_nodes in self.equivalent_nodes.items():

      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      for surf in surfs_main_node:
        surfaces_eq[surf] = surf
      for eq_node in eq_nodes:
        node_symmetry = self.symmetry[n_id][eq_node]
        # print(node_symmetry)
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        
        if node_symmetry == mirror_right:
          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
          elif len(surfs_main_node) == 4:

            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[3]
        elif node_symmetry == mirror_down:

          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[1]
          elif len(surfs_main_node) == 4:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[3]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[1]
        elif node_symmetry == mirror_right_down:

          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[1]
          elif len(surfs_main_node) == 4:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[3]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[1]
        else:
          # same
          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
          elif len(surfs_main_node) == 4:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[3]
          
    self.equivalent_surfaces = surfaces_eq


def grid_coarse_node_manager(node_type):
  from Shynt.api_py.Mesh.coarse_node import (
    CoarseNodeSquareGridHexAssembly,
    CoarseNodeSquareGridHexAssembly_Inside1,
    CoarseNodeSquareGridHexAssembly_Inside2,
    CoarseNodeSquareGridHexAssembly_TrapezoidCorner,
    CoarseNodeSquareGridHexAssembly_SideEdge,
    CoarseNodeSquareGridHexAssembly_TriangleCorner
  )
  if node_type == 'trapezoid_corner':
    return CoarseNodeSquareGridHexAssembly_TrapezoidCorner
  elif node_type == 'inside1':
    return CoarseNodeSquareGridHexAssembly_Inside1
  elif node_type == 'inside2':
    return CoarseNodeSquareGridHexAssembly_Inside2
  elif node_type == 'side_edge':
    return CoarseNodeSquareGridHexAssembly_SideEdge
  elif node_type == 'triangle_corner':
    return CoarseNodeSquareGridHexAssembly_TriangleCorner
  else:
    return CoarseNodeSquareGridHexAssembly



