from Shynt.api_py.Mesh.coarse_mesh import CoarseMesh
from Shynt.api_py.Mesh.coarse_node import (
  CoarseNodeSquarePinCell,
  CoarseNodeHexagonalPinCell
)

from Shynt.api_py.Geometry.universes import (
  SquareLattice, 
  Pin
)
from Shynt.api_py.Geometry.cells import Cell

from Shynt.api_py.Geometry.surfaces import (
  InfiniteHexagonalCylinderXtype,
  InfiniteSquareCylinderZ
)
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


