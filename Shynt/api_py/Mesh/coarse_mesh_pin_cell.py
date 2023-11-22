from Shynt.api_py.Mesh.coarse_mesh import CoarseMesh
from Shynt.api_py.Mesh.coarse_node import CoarseNodeSquarePinCell

from Shynt.api_py.Geometry.universes import SquareLattice
from Shynt.api_py.Geometry.cells import Cell

import numpy as np



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
      assert isinstance(cell.content, SquareLattice)
    except AssertionError:
      print(" ************ Error ************ ")
      print("PinCellMesh only supported for SquareLattice")
      raise SystemExit
    super().__init__(cell)
    self.type_mesh = ""
    self.lattice = super().cell.content
    self.points_mesh = {}
    self.coarse_nodes_map = []
    self.coarse_nodes = {}
    self.num_surfaces = 0
    self.surface_twins = {}

    self.unique_nodes = []
    self.equivalent_nodes = {}
    self.symmetry = {}
  
  def __check_lattice(self):
    message = "Type of lattice not supported in square pin cell coarse mesh"
    try:
      print(self.lattice)
      assert isinstance(self.lattice, SquareLattice)
    except AssertionError:
      print(message)
      raise NotImplementedError
  
  def calculate_nodes_coordinates(self):
    """Class method to calculate the points of the coarse nodes 
    starting from the lower-left point following a clock-wise sense
    to number the points.
    
    """
    squares = {}
    # print(self.lattice.left_bottom)
    pin_centers = self.lattice.pin_centers
    half_pitch = self.lattice.pitch / 2

    n_id = 1
    nodes_map = []
    for i, row in enumerate(pin_centers):
      row_node = []
      for j, center in enumerate(row):
        cx, cy = center
        # print(center)
        p1 = (cx-half_pitch, cy-half_pitch) # lower-left
        p2 = (cx-half_pitch, cy+half_pitch) # upper-left
        p3 = (cx+half_pitch, cy+half_pitch) # upper-right
        p4 = (cx+half_pitch, cy-half_pitch) # lower-right
        squares[n_id] = (p1, p2, p3, p4)
        row_node.append(n_id)
        n_id += 1
      nodes_map.append(row_node)
    

    self.coarse_nodes_map = nodes_map
    self.points_mesh = squares
    
  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    coarse_nodes = {}
    s_id = 1
    for i, row in enumerate(self.coarse_nodes_map):
      for j, n_id in enumerate(row):
        surface_points = self.points_mesh[n_id]
        pin_universe = self.lattice.array[i][j]
        node = CoarseNodeSquarePinCell(
          n_id, surface_points, 'pin_cell_mesh', self.lattice.pitch
        )
        node.universe = pin_universe 

        s_id = node.calculate_node_surfaces(s_id)
        coarse_nodes[n_id] = node
    
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id

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
    
    self.surface_twins = surface_twins

  def find_equivalent_nodes(self):
    """Class method to calculate the equivalent nodes in the square lattice.
    It takes the name of every pin to differentiate from other pins

    Parameters
    ----------

    Returns
    -------

    """
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
    
    equivalent_nodes = {}
    unique_nodes = {}
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


