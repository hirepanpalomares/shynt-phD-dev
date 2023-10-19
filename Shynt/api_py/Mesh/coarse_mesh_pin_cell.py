
from Shynt.api_py.Mesh.global_coarse_mesh import GlobalMesh

from Shynt.api_py.Geometry.universes import SquareLattice, HexagonalLatticeTypeX, Pin, Universe
from Shynt.api_py.Geometry.cells import Cell

from Shynt.api_py.Mesh.coarse_node import CoarseNode, HexAssemCoarseNode, SquarePinCoarseNode


import numpy as np

class PinCellMesh(GlobalMesh):
    
  def __init__(self, cell):
    super().__init__(cell)
    self.coarse_nodes = None
    self.coarse_nodes_map = None
    self.type_mesh = "square_pin_mesh"
    universe = cell.content

    self.__create_nodes_switch(universe)
    
  
  def __create_nodes_switch(self, universe):
    coarse_nodes = None
    coarse_nodes_map = None
    if isinstance(universe, SquareLattice):
      coarse_nodes, coarse_nodes_map = self.__create_nodes_SquareLattice(universe)
    elif isinstance(universe, HexagonalLatticeTypeX):
      coarse_nodes, coarse_nodes_map = self.__create_nodes_HexagonalLattice(universe)
    elif isinstance(universe, Pin):
      coarse_nodes, coarse_nodes_map = self.__create_nodes_SquarePin()
    else:
        print("*** Error Trying to build coarse mesh no Lattice nor Pin universe provided *** ")
        raise SystemExit
    
    self.coarse_nodes = coarse_nodes
    self.coarse_nodes_map = coarse_nodes_map


  def __create_nodes_SquareLattice(self, universe):
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

  def __create_nodes_SquarePin(self):
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

  def __create_nodes_HexagonalLattice(self, universe):
    map_nodes = []
    coarse_nodes = {}
    node_counter = 1
    for y in range(universe.ny):
      map_row = []
      for x in range(universe.nx):
        pin_cell_id = universe.array[y][x]
        if pin_cell_id is None:
          map_row.append(None)
          continue
        map_row.append(node_counter)
        pin_cell = universe.cells[pin_cell_id]
        coarse_node = CoarseNode(pin_cell)
        coarse_node.id = node_counter
        coarse_nodes[node_counter] = coarse_node
        node_counter += 1
      map_nodes.append(map_row)
    return coarse_nodes, np.array(map_nodes)
  
  def __get_pin_cell_coarse_node(self, pin_cell):
    
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


