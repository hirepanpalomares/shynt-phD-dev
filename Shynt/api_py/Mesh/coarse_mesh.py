import numpy as np
import math

from Shynt.api_py.Geometry.surfaces import CylinderPad, PlaneX, PlaneY
from Shynt.api_py.Geometry.surfaces import InfiniteCylinderZ
from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderYtype
from Shynt.api_py.Geometry.surfaces import InfiniteRectangleCylinderZ

from Shynt.api_py.Geometry.regions import SurfaceSide

from Shynt.api_py.Geometry.universes import SquareLattice
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX
from Shynt.api_py.Geometry.universes import Pin
from Shynt.api_py.Geometry.universes import Universe


from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.utilities_geometry import change_boundary_guide

from Shynt.api_py.Mesh.coarse_node import CoarseNode
from Shynt.api_py.Mesh.coarse_node import HexAssemCoarseNode
from Shynt.api_py.Mesh.coarse_node import SquarePinCoarseNode


from Shynt.api_py.materials import Material

from Shynt.api_py.Serpent.global_nodes_geometry import hexagonal_assembly



class CoarseMesh():

  def __init__(self, cell):
    super().__init__()
    self.__cell = cell
    self.coarse_nodes_map = []
    self.coarse_nodes = {}

  
  @property
  def cell(self):
    return self.__cell



class PinCellMesh(CoarseMesh):
    
  def __init__(self, cell):
    super().__init__(cell)
    universe = cell.content
    self.coarse_nodes = {}
    self.coarse_nodes_map = []
    self.type_mesh = "square_pin_mesh"
    if isinstance(universe, SquareLattice):
      self.coarse_nodes, self.coarse_nodes_map = self.__create_nodes_SquareLattice(universe)
    elif isinstance(universe, HexagonalLatticeTypeX):
      self.coarse_nodes, self.coarse_nodes_map = self.__create_nodes_HexagonalLattice(universe)
    elif isinstance(universe, Pin):
      self.coarse_nodes, self.coarse_nodes_map = self.__create_nodes_SquarePin()
    else:
        print("*** Error Trying to build coarse mesh no Lattice nor Pin universe provided *** ")
        raise SystemExit
  
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


class SquareGridMesh(CoarseMesh):
    

  def __init__(self, cell):
    super().__init__(cell)
    self.__map_pins = []
    self.__symmetry = {}
    self.clean_mesh_map = []
    self.points_mesh = []
    self.coarse_nodes = {}
    self.type_mesh = ""
    self.universe = super().cell.content
    if isinstance(self.universe, HexagonalLatticeTypeX):
      self.__create_nodes_hex_assem()
    elif isinstance(self.universe, Pin):
      self.__create_nodes_hex_pin()      
      
  def __create_nodes_hex_assem(self):

    self.type_mesh = "square_hex_assembly"
    # Getting node map --------------------------------------------------------
    map_pins = self.__get_node_map()
    
    clean_map = self.__get_clean_map()
    # print_map_node = [print(row) for row in map_pins]
    # print("-"*100)
    # print_map_node = [print(row) for row in clean_map]
    first_pin_id = clean_map[1][1][0]
    first_pin = self.universe.cells[first_pin_id]
    self.__hexagon_width = first_pin.region.surface.half_width

    fuel, no_fuel = first_pin.content.find_fuel_cells()

    fuel_mat = fuel[0].content
    radius_fuel = fuel[0].region.surface.radius
    coolant_mat = no_fuel[0].content
    
    outer_hex = super().cell.region.surface    

    x_div, y_div = self.__calculate_square_mesh_coord_hex_assem(outer_hex, clean_map)
    self.points_mesh = self.__get_rectangles_from_mesh_coord(x_div, y_div)#, outer_hex, clean_map)
    self.coarse_nodes_map = self.__get_map_mesh(clean_map)
    print("self.coarse_nodes_map: ")
    print(self.coarse_nodes_map)
    # print("-"*100)
    # print(self.coarse_nodes_map)
    self.__symmetry = self.__get_symmetry_hex_assem()
    self.coarse_nodes = self.__get_coarse_nodes_hex_assem(fuel_mat, coolant_mat, radius_fuel)

  def __create_nodes_hex_pin(self):
    self.type_mesh = "square_hex_pin"
    outer_hex = super().cell.region.surface
    self.__hexagon_width = outer_hex.half_width
    x_div, y_div = self.__calculate_square_mesh_coord_hex_pin(outer_hex)
    self.points_mesh = self.__get_rectangles_from_mesh_coord(x_div, y_div)
    self.coarse_nodes_map = np.array([
      [1,2],
      [3,4]
    ])

    self.__symmetry = {
      1: {
        1: {"same": ""},
        2: {"mirror":"right"},
        3: {"mirror":"right_down"},
        4: {"mirror":"down"},
        # 2: {"same": ""},
        # 3: {"same": ""},
        # 4: {"same": ""},
      }
    }
    fuel_mat = self.universe.cells[1].content
    radius_fuel = self.universe.cells[1].region.surface.radius
    cool_mat = self.universe.cells[2].content
    self.coarse_nodes = self.__get_coarse_nodes_hex_pin(fuel_mat, cool_mat, radius_fuel, outer_hex)

  def __get_node_map(self):
    universe = super().cell.content
    node_counter = 1
    map_pins = []
    for y in range(universe.ny):
      map_nodes_row = []
      cell_counter = 0
      for x in range(universe.nx):
          pin_cell_id = universe.array[y][x]
          if pin_cell_id is None:
              map_nodes_row.append(None)
          else:
              
              map_nodes_row.append(node_counter)
              node_counter += 1
      
      map_pins.append(map_nodes_row)
    return map_pins
  
  def __get_clean_map(self):
    universe = super().cell.content
    
    clean_map = [
      [
        col for col in row if col is not None
      ] for row in universe.array
    ]
    clean_map = [
      [
        col for col in row
      ] for row in clean_map if len(row) != 0
    ]
    return clean_map

  def __get_symmetry_hex_assem(self):
    self.__clean_mesh_map = [
      [
        col for col in row if col != 0
      ] for row in self.coarse_nodes_map
    ]
    print_clean_mesh_map = [print(row) for row in self.__clean_mesh_map]

    type_1 = self.__clean_mesh_map[0][0]
    type_2 = self.__clean_mesh_map[0][1]
    type_3 = self.__clean_mesh_map[1][0]
    type_4 = self.__clean_mesh_map[1][1]
    
    symmetry = {
      type_1: {
        self.__clean_mesh_map[0][0]: {"same": ""},
        self.__clean_mesh_map[0][-1]: {"mirror":"right"},
        self.__clean_mesh_map[-1][0]: {"mirror":"down"},
        self.__clean_mesh_map[-1][-1]: {"mirror":"right_down"},
        # self.__clean_mesh_map[0][-1]: {"same": ""},
        # self.__clean_mesh_map[-1][0]: {"same": ""},
        # self.__clean_mesh_map[-1][-1]: {"same": ""},
      }, 
      type_2: {
        self.__clean_mesh_map[0][1]: {"same": ""},
      }, 
      type_3: {
        self.__clean_mesh_map[1][0]: {"same": ""},
      }, 
      type_4: {
        self.__clean_mesh_map[1][1]: {"same": ""},
      }, 
    }

    middle_point = len(self.__clean_mesh_map)/2
    for x in range(1, len(self.__clean_mesh_map[0])-1):
      if (x+1)%2 == 0:
        symmetry[type_2][self.__clean_mesh_map[0][x]] =  {"same":""}
        symmetry[type_2][self.__clean_mesh_map[-1][x]] =  {"mirror":"down"}
        # symmetry[type_2][self.__clean_mesh_map[-1][x]] =  {"same":""}
      else:
        symmetry[type_2][self.__clean_mesh_map[0][x]] =  {"mirror":"right"}
        symmetry[type_2][self.__clean_mesh_map[-1][x]] =  {"mirror":"right_down"}
        # symmetry[type_2][self.__clean_mesh_map[0][x]] =  {"same":""}
        # symmetry[type_2][self.__clean_mesh_map[-1][x]] =  {"same":""}
    
    symmetry[type_3][self.__clean_mesh_map[1][-1]] =  {"mirror":"right"}
    # symmetry[type_3][self.__clean_mesh_map[1][-1]] =  {"same":""}

    for y in range(1, len(self.__clean_mesh_map)-1):
      if y > 1 and (y+1) <= middle_point:
        symmetry[type_3][self.__clean_mesh_map[y][0]] =  {"same":""}
        symmetry[type_3][self.__clean_mesh_map[y][-1]] =  {"mirror":"right"}
        # symmetry[type_3][self.__clean_mesh_map[y][-1]] =  {"same":""}

      elif (y+1) > middle_point:
        symmetry[type_3][self.__clean_mesh_map[y][0]] =  {"mirror":"down"}
        symmetry[type_3][self.__clean_mesh_map[y][-1]] =  {"mirror":"right_down"}
        # symmetry[type_3][self.__clean_mesh_map[y][0]] =  {"same":""}
        # symmetry[type_3][self.__clean_mesh_map[y][-1]] =  {"same":""}
      for x in range(1,len(self.__clean_mesh_map[y])-1):
        node_id = self.__clean_mesh_map[y][x]
        if node_id in symmetry:
          continue
        if (y+1) < middle_point:
          if (x+1)%2 == 0:
            symmetry[type_4][self.__clean_mesh_map[y][x]] = {"same":""}
          else:
            symmetry[type_4][self.__clean_mesh_map[y][x]] = {"mirror":"right"}
            # symmetry[type_4][self.__clean_mesh_map[y][x]] = {"same":""}
        else:
          if (x+1)%2 == 0:
            symmetry[type_4][self.__clean_mesh_map[y][x]] = {"mirror":"right"}
            # symmetry[type_4][self.__clean_mesh_map[y][x]] = {"same":""}
          else:
            symmetry[type_4][self.__clean_mesh_map[y][x]] = {"same":""}
        

    return symmetry

  def __calculate_square_mesh_coord_hex_assem(self, outer_hex, clean_map):
    universe = super().cell.content
    y_coords = [] 
    x_coords = []
    last_y_coord = None
    y_checked = []
    num_y = len(clean_map)
    for y in range(1,num_y-1):
      row = clean_map[y]
      y_coord = universe.cells[row[0][0]].center[1]
      last_row = clean_map[y-1]
      last_y_coord = universe.cells[last_row[0][0]].center[1]

      y_coords.append(y_coord)
      x_div_row = []
      if y_coord in y_checked: continue
      num_x = len(clean_map[y])
      for x in range(1,num_x-2):
        pin_id, type_pin = clean_map[y][x]
        x_coord = universe.cells[pin_id].center[0]
        hw = universe.cells[pin_id].region.surface.half_width
        if x == 1 and y_coord < 0.0: 
          x_div_row.append(x_coord - hw)
        x_div_row.append(x_coord)
        x_div_row.append(x_coord + hw)
      last_pin = clean_map[y][-2][0]
      last_pin_x_coord = universe.cells[last_pin].center[0]
      last_pin_hw = universe.cells[last_pin].region.surface.half_width
      if y_coord < 0:
        x_div_row.append(last_pin_x_coord)
        x_div_row.append(last_pin_x_coord + last_pin_hw)
        x_start = round(outer_hex.surf_E.useFunction(last_y_coord, given="y"),8)
        x_end = round(outer_hex.surf_C.useFunction(last_y_coord, given="y"),8)
      else:
        x_div_row.append(last_pin_x_coord)
        x_start = round(outer_hex.surf_F.useFunction(y_coord, given="y"),8)
        x_end = round(outer_hex.surf_B.useFunction(y_coord, given="y"),8)
      x_div_row = [x_start] + x_div_row
      x_div_row.append(x_end)

      if y_coord == 0.0: 
        x_coords.append(x_div_row)
        x_coords.append(x_div_row)
        y_checked.append(y_coord)
        y_checked.append(universe.cells[clean_map[y+1][0][0]].center[1])
      else:        
        x_coords.append(x_div_row)
        y_checked.append(y_coord)

    y_coords = [outer_hex.surf_A.y0] + y_coords
    y_coords.append(outer_hex.surf_D.y0)
    x_coords.append(x_coords[0])
    return x_coords, y_coords
  
  def __calculate_square_mesh_coord_hex_pin(self, outer_hex):
    """
      Calculates the coordinates of the coarse mesh for a  square mesh
      in a simple hexagonal pin (4 squares). Only using a Hexagon-x_Type:

        - 3 values of x
        - 3 values of y
    """
    center_x, center_y = outer_hex.center
    left_x = center_x - outer_hex.half_width
    right_x = center_x + outer_hex.half_width
    bottom_y = center_y - outer_hex.radius
    top_y = center_y + outer_hex.radius
    
    coord_x = [
      [left_x, center_x, right_x],
      [left_x, center_x, right_x],
      [left_x, center_x, right_x],
    ]
    coord_y = [
      top_y, center_y, bottom_y
    ]

    return coord_x, coord_y

  def __get_rectangles_from_mesh_coord(self, x_div, y_div):
    
    mesh = {}
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
        mesh[node_counter] = rectangle
        node_counter += 1
        
      row_x += 1

    return mesh
  
  def __get_map_mesh(self, clean_map):
    
    map_mesh = []
    node_counter = 1
    middle_clean_map = len(clean_map) 
    for r, row in enumerate(clean_map):
      map_mesh_row = []
      for id_, pin in row:
        if pin == "inside":
          map_mesh_row.append(node_counter)
          map_mesh_row.append(node_counter+1)
          node_counter += 2
      if len(map_mesh_row) > 0:
        if r == len(clean_map) // 2:
          map_mesh.append(map_mesh_row)
          another_middle_row = []
          for val_ in map_mesh_row:
            another_middle_row.append(node_counter)
            node_counter += 1
          map_mesh.append(another_middle_row)
        else:
          map_mesh.append(map_mesh_row)
    number_zeros = 1
    middle = len(map_mesh) // 2
    idx_up = middle - 1
    idx_bottom = middle
    while idx_up >= 0:
      map_row_bottom = map_mesh[idx_bottom]
      map_row_up = map_mesh[idx_up]
      for z in range(number_zeros):
        map_row_bottom = [0] + map_row_bottom
        map_row_bottom.append(0)
        map_row_up = [0] + map_row_up
        map_row_up.append(0)
      map_mesh[idx_bottom] = list(map_row_bottom)
      map_mesh[idx_up] = list(map_row_up)
      idx_up -= 1
      idx_bottom += 1
      number_zeros += 1

    
    return np.array(map_mesh)

  def __get_cells_from_square(self, square):
      """
        ! NOT IMPLEMENTED
      """
      x1,x2 = square[0]
      y1,y2 = square[1]
      points = [(x1,y1), (x2,y1), (x2,y2), (x1,y2)]
      # 1. find  hexagonal cells 
      cells_with_square = []
      cells_center_with_square = []
      hexagonal_assem = self.__cell.content
      for point in points:
          
          for c_id, cell in hexagonal_assem.cells.items():
              if cell.isPointInside(point) and cell.center not in cells_center_with_square:
                  cells_center_with_square.append(cell.center)
                  cells_with_square.append(cell)
                  
          pass
          # 2. check if the boundary traverses the square

          # 3. Find individual cells that are formed within the square

      return cells_with_square

  def __get_coarse_nodes_hex_pin(self, fuel_mat, coolant_mat, radius, outer_hex):
    coarse_nodes = {}

    for y, row in enumerate(self.coarse_nodes_map):
      for x, node_id in enumerate(row):
        rectangle = self.points_mesh[node_id]
        x1, x2 = rectangle[0]
        y1, y2 = rectangle[1]

        rectangle_cells, geometry_info = self.__get_rectangle_content_hex_pin(x1, x2, y1, y2, coolant_mat, fuel_mat, radius, outer_hex)
        geometry_info["symmetry"] = {
          1: self.__symmetry[1][node_id]
        }

        new_guide = change_boundary_guide(
          geometry_info["surfaces_for_detectors"]["boundary_guide"], geometry_info["symmetry"][1]
        )
        new_guide_inv = {
          s_id: s_dir for s_dir, s_id in new_guide.items() if s_id is not None
        }
        geometry_info["surfaces_for_detectors"]["boundary_guide"] = new_guide
        geometry_info["surfaces_for_detectors"]["boundary_guide_inv"] = new_guide_inv

        print(node_id, geometry_info["surfaces_for_detectors"]["boundary_guide"])
        print(node_id, geometry_info["surfaces_for_detectors"]["boundary_surfaces_areas"])
        print()

        # Now with these cells create a universe ----
        rectangle_universe = Universe(name=f"rectangle_coarse_node_cell_{node_id}")
        rectangle_universe.cells = rectangle_cells
        # Fill a rectangular cell with these universe ----
        surf_rectangle = geometry_info["rectangle_surf"]
        rectangle_cell = Cell(
            fill=rectangle_universe, 
            region=-surf_rectangle, 
            name=f"coarse_node_cell_{node_id}"
        )
        coarse_node = HexAssemCoarseNode(rectangle_cell, geometry_info)
        coarse_node.id = node_id
        coarse_nodes[node_id] = coarse_node

    return coarse_nodes
    
  def __get_coarse_nodes_hex_assem(self, fuel_mat, coolant_mat, radius):
    coarse_nodes = {}
    for y, row in enumerate(self.coarse_nodes_map):
      for x, node_id in enumerate(row):
        if node_id != 0:
          # each rectangle corresponds to a cell
          rectangle = self.points_mesh[node_id]
          x1, x2 = rectangle[0]
          y1, y2 = rectangle[1]

          get_cells, type_, node_type_id = self.__type_of_rectangle_cell_switch(row, x ,y)
          # print(type_, node_type_id)
          rectangle_cells, geometry_info = get_cells(x1, x2, y1, y2, coolant_mat, fuel_mat, radius)
          geometry_info["type"] = type_
          geometry_info["symmetry"] = {
            node_type_id: self.__symmetry[node_type_id][node_id]
          }
          new_guide = change_boundary_guide(
            geometry_info["surfaces_for_detectors"]["boundary_guide"], geometry_info["symmetry"][node_type_id]
          )
          new_guide_inv = {
            s_id: s_dir for s_dir, s_id in new_guide.items() if s_id is not None
          }
          geometry_info["surfaces_for_detectors"]["boundary_guide"] = new_guide
          geometry_info["surfaces_for_detectors"]["boundary_guide_inv"] = new_guide_inv

          print(node_id, geometry_info["surfaces_for_detectors"]["boundary_guide"])
          print(node_id, geometry_info["surfaces_for_detectors"]["boundary_surfaces_areas"])
          print()

          # print(geometry_info)
          # Now with these cells create a universe 
          rectangle_universe = Universe(name=f"rectangle_coarse_node_cell_{node_id}")
          rectangle_universe.cells = rectangle_cells
          # Fill a rectangular cell with these universe
          # surf_rectangle = InfiniteRectangleCylinderZ(x1,x2,y1,y2)
          surf_rectangle = geometry_info["rectangle_surf"]
          rectangle_cell = Cell(
              fill=rectangle_universe, 
              region=-surf_rectangle, 
              name=f"coarse_node_cell_{node_id}"
          )
          coarse_node = HexAssemCoarseNode(rectangle_cell, geometry_info)
          coarse_node.id = node_id
          coarse_nodes[node_id] = coarse_node
    return coarse_nodes
  
  def __type_of_rectangle_cell_switch(self, row, x, y):
    # * CASES -------------------------------------------------------
    if y == 0 or y == len(self.coarse_nodes_map) - 1:
      if row[x-1] == 0 or row[x+1] == 0:
        # * top/bottom corner
        return self.__get_rectangle_content_side_edge, "corner", self.__clean_mesh_map[0][0]
      else:
        # * top/bottom edge
        return self.__get_rectangle_content_top_edge, "top_edge", self.__clean_mesh_map[0][1]
    else:
      if row[x-1] == 0 or row[x+1] == 0:
        # * side edge
        return self.__get_rectangle_content_side_edge, "side_edge", self.__clean_mesh_map[1][0]
      else:
        # * inside
        return self.__get_rectangle_content_inside, "inside", self.__clean_mesh_map[1][1]

  def __get_rectangle_content_top_edge(self, x1, x2, y1, y2, coolant_mat, fuel_mat, radius):
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad = CylinderPad(0.0,0.0,0.0,radius,270,360)
    vol_fuel = circle_pad.volume
    vol_coolant = rectangle_surf.volume - vol_fuel
    region_coolant = -rectangle_surf & +circle_pad
    region_fuel = -circle_pad
    coolant_cell = Cell(
      name="coolant_top_type_hexagonal_square_mesh", 
      fill=coolant_mat,
      volume=vol_coolant,
      region=region_coolant
    )
    fuel_cell = Cell(
      name="fuel_top_type_hexagonal_square_mesh", 
      fill=fuel_mat,
      volume=vol_fuel,
      region=region_fuel
    )
    cells = {
      coolant_cell.id: coolant_cell,
      fuel_cell.id: fuel_cell
    }
    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "x1_x2_top": (x1, x2),
      "x1_x2_bottom": (x1, x2),
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "fuel_relation": {
        "fuel": fuel_cell.id,
        "non_fuel": coolant_cell.id
      },
      "cells": cells,
      "surfaces_for_detectors": {
        "fuel":{
          circle_pad.id: f"surf {circle_pad.id} pad 0.0 0.0 0.0 {radius} 270 360",
        },
        "boundary": {
          rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
          rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
          rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
          rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n"
        },
        "boundary_guide": {
        "left": rectangle_surf.surf_left.id,
        "top": rectangle_surf.surf_top.id,
        "right": rectangle_surf.surf_right.id,
        "bottom": rectangle_surf.surf_bottom.id,
        },
        "boundary_guide_inv": {
          rectangle_surf.surf_left.id : "left",
          rectangle_surf.surf_top.id: "top",
          rectangle_surf.surf_right.id : "right",
          rectangle_surf.surf_bottom.id : "bottom",
        },
        "boundary_surfaces": {
          rectangle_surf.surf_left.id: rectangle_surf.surf_left,
          rectangle_surf.surf_top.id: rectangle_surf.surf_top,
          rectangle_surf.surf_right.id: rectangle_surf.surf_right,
          rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
        },
        "boundary_surfaces_areas": {
          rectangle_surf.surf_left.id: rectangle_height,
          rectangle_surf.surf_top.id: rectangle_width,
          rectangle_surf.surf_right.id: rectangle_height,
          rectangle_surf.surf_bottom.id: rectangle_width,
        },
        "current_directions": {
          circle_pad.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
          rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"}
        }

      }

    } 
    return cells, geometry_info
  
  def __get_rectangle_content_side_edge(
    self, x1, x2, y1, y2, coolant_mat, fuel_mat, radius
  ):
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad = CylinderPad(rectangle_width,0,0,radius,90,180)
    plane = PlaneX(x1)
    plane.rotate(angle=-30, ref_point=(x1, y1))
    distance_to_plane = plane.useFunction(y2, given="y") - x1

    x1_t = x1
    x2_t = x2
    x1_b = x1
    x2_b = x2

    if y2 > 0:
      #? ------------------------- upper half
      if x1 > 0:
        x2_t -= distance_to_plane
      else:
        x1_t += distance_to_plane
    else:
      #? ------------------------- lower half
      if x1 > 0:
        x2_b -= distance_to_plane
      else:
        x1_b += distance_to_plane


    x1_x2_top = (x1_t, x2_t)
    x1_x2_bottom = (x1_b, x2_b)
        
    plane_area = math.sqrt(distance_to_plane * distance_to_plane + rectangle_height * rectangle_height)
    volume_void = distance_to_plane * rectangle_height / 2
    volume_fuel = circle_pad.volume
    volume_coolant = rectangle_surf.volume - volume_fuel - volume_void

    region_void = -rectangle_surf & +plane
    region_coolant = -rectangle_surf & -plane & +circle_pad
    region_fuel = -circle_pad

    void_cell = Cell(
      name="void_side_edge_type_hexagonal_square_mesh", 
      fill=Material("void"),
      volume=volume_void,
      region=region_void
    )
    coolant_cell = Cell(
      name="coolant_side_edge_type_hexagonal_square_mesh", 
      fill=coolant_mat,
      volume=volume_coolant,
      region=region_coolant
    )
    fuel_cell = Cell(
      name="fuel_side_edge_type_hexagonal_square_mesh", 
      fill=fuel_mat,
      volume=volume_fuel,
      region=region_fuel
    )

    cells = {
      # void_cell.id: void_cell,
      coolant_cell.id: coolant_cell,
      fuel_cell.id: fuel_cell
    }

    surfaces_for_detectors = {
      "fuel": {
        circle_pad.id: f"surf {circle_pad.id} pad {rectangle_width} 0.0 0.0 {radius} 180 270",
      },
      "boundary": {
        # rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
        rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
        rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
        rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n",
        plane.id: f"surf {plane.id} px 0.00\ntrans s {plane.id} 0.0 0.0 0.0 0.0 0.0 30\n\n\n"
      },
      "boundary_guide": {
        "left": plane.id,
        "top": rectangle_surf.surf_top.id,
        "right": rectangle_surf.surf_right.id,
        "bottom": rectangle_surf.surf_bottom.id,
        # "left": rectangle_surf.surf_left.id
      },
      "boundary_guide_inv": {
        plane.id : "left",
        rectangle_surf.surf_top.id : "top",
        rectangle_surf.surf_right.id : "right",
        rectangle_surf.surf_bottom.id : "bottom",
        # rectangle_surf.surf_left.id: "left",
      },
      "boundary_surfaces": {
        plane.id: plane,
        # rectangle_surf.surf_left.id: rectangle_surf.surf_left,
        rectangle_surf.surf_top.id: rectangle_surf.surf_top,
        rectangle_surf.surf_right.id: rectangle_surf.surf_right,
        rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
      },
      "boundary_surfaces_areas": {
        plane.id: plane_area,
        rectangle_surf.surf_top.id: rectangle_width - distance_to_plane,
        rectangle_surf.surf_right.id: rectangle_height,
        rectangle_surf.surf_bottom.id: rectangle_width,
        # rectangle_surf.surf_left.id: rectangle_height,

      },
      "current_directions": {
        circle_pad.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"},
        rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
        plane.id: {"inward": "1", "outward": "-1"}
      }
    }

    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "x1_x2_top": x1_x2_top,
      "x1_x2_bottom": x1_x2_bottom,
      "distance_to_plane": distance_to_plane,
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "fuel_relation": {
        "fuel": fuel_cell.id,
        "non_fuel": coolant_cell.id,
        # "void": void_cell
      },
      "plane_void_id": plane.id,
      "cells": cells,
      "surfaces_for_detectors": surfaces_for_detectors,
      # "detectors": hexagonal_assembly.edge_with_void_detectors
    } 

    return cells, geometry_info

  def __get_rectangle_content_inside(self, 
    x1, x2, y1, y2, coolant_mat, fuel_mat, radius
  ):
    coolant_mat_1 = coolant_mat
    coolant_mat_2 = coolant_mat
    fuel_mat_1 = fuel_mat
    fuel_mat_2 = fuel_mat
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2, radius)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad1 = CylinderPad(x1,y1,0,radius,0,90)
    circle_pad2 = CylinderPad(x2,y2,0,radius,180,270)

    plane = PlaneX(x1)
    plane.rotate(angle=-30, ref_point=(x1, self.__hexagon_width))

    volume_fuel1 = circle_pad1.volume
    volume_fuel2 = circle_pad2.volume
    volume_cool1 = (rectangle_surf.volume - volume_fuel1 - volume_fuel2) / 2
    volume_cool2 = (rectangle_surf.volume - volume_fuel1 - volume_fuel2) / 2
    
    region_fuel1 = -circle_pad1
    region_fuel2 = -circle_pad2
    region_cool1 = -rectangle_surf & +circle_pad1 & -plane
    region_cool2 = -rectangle_surf & +circle_pad2 & +plane

    coolant_cell_1 = Cell(
      name="coolant1_corner_type_hexagonal_square_mesh", 
      fill=coolant_mat_1,
      volume=volume_cool1,
      region=region_cool1
    )
    fuel_cell_1 = Cell(
      name="fuel1_corner_type_hexagonal_square_mesh", 
      fill=fuel_mat_1,
      volume=volume_fuel1,
      region=region_fuel1
    )
    coolant_cell_2 = Cell(
      name="coolant2_corner_type_hexagonal_square_mesh", 
      fill=coolant_mat_2,
      volume=volume_cool2,
      region=region_cool2
    )
    fuel_cell_2 = Cell(
      name="fuel2_corner_type_hexagonal_square_mesh", 
      fill=fuel_mat_2,
      volume=volume_fuel2,
      region=region_fuel2
    )
    cells = {
      coolant_cell_1.id: coolant_cell_1,
      fuel_cell_1.id: fuel_cell_1,
      coolant_cell_2.id: coolant_cell_2,
      fuel_cell_2.id: fuel_cell_2
    }
    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "x1_x2_top": (x1, x2),
      "x1_x2_bottom": (x1, x2),
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "hexagon_radius": self.__hexagon_width,
      "fuel_relation": {
        "fuel1": fuel_cell_1.id,
        "fuel2": fuel_cell_2.id,
        "non_fuel1": coolant_cell_1.id,
        "non_fuel2": coolant_cell_2.id,
      },
      "cells": cells,
      "surfaces_for_detectors": {
        "fuel": {
          circle_pad1.id: f"surf {circle_pad1.id} pad 0.0 0.0 0.0 {radius} 270 360",
          circle_pad2.id: f"surf {circle_pad2.id} pad {rectangle_width} {rectangle_height} 0.0 {radius} 90  180",
        },
        "boundary": {
          rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
          rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
          rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
          rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n"
        },
        "boundary_guide": {
          "left": rectangle_surf.surf_left.id,
          "top": rectangle_surf.surf_top.id,
          "right": rectangle_surf.surf_right.id,
          "bottom": rectangle_surf.surf_bottom.id,
        },
        "boundary_guide_inv": {
          rectangle_surf.surf_left.id : "left",
          rectangle_surf.surf_top.id : "top",
          rectangle_surf.surf_right.id : "right",
          rectangle_surf.surf_bottom.id : "bottom",
        },
        "boundary_surfaces": {
          rectangle_surf.surf_left.id: rectangle_surf.surf_left,
          rectangle_surf.surf_top.id: rectangle_surf.surf_top,
          rectangle_surf.surf_right.id: rectangle_surf.surf_right,
          rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
        },
        "boundary_surfaces_areas": {
          rectangle_surf.surf_left.id: rectangle_height,
          rectangle_surf.surf_top.id: rectangle_width,
          rectangle_surf.surf_right.id: rectangle_height,
          rectangle_surf.surf_bottom.id: rectangle_width,
        },
        "current_directions": {
          circle_pad1.id: {"inward": "-1", "outward": "1"},
          circle_pad2.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
          rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"}
        }
      }
    } 
    return cells, geometry_info

  def __get_rectangle_content_hex_pin(self, 
    x1, x2, y1, y2, coolant_mat, fuel_mat, radius, outer_hex
  ):
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad = CylinderPad(0,0,0,radius,90,180)
    plane = PlaneY(y2)
    plane.rotate(angle=30, ref_point=(x2, y2))
    
    plane_area = rectangle_height

    volume_void = rectangle_surf.volume - outer_hex.volume / 4
    volume_fuel = circle_pad.volume
    volume_coolant = outer_hex.volume / 4 - volume_fuel

    region_void = -rectangle_surf & +plane
    region_coolant = -rectangle_surf & -plane & +circle_pad
    region_fuel = -circle_pad

    void_cell = Cell(
      name="void_side_edge_type_hexagonal_square_mesh", 
      fill=Material("void"),
      volume=volume_void,
      region=region_void
    )
    coolant_cell = Cell(
      name="coolant_side_edge_type_hexagonal_square_mesh", 
      fill=coolant_mat,
      volume=volume_coolant,
      region=region_coolant
    )
    fuel_cell = Cell(
      name="fuel_side_edge_type_hexagonal_square_mesh", 
      fill=fuel_mat,
      volume=volume_fuel,
      region=region_fuel
    )

    cells = {
      # void_cell.id: void_cell,
      coolant_cell.id: coolant_cell,
      fuel_cell.id: fuel_cell
    }

    surfaces_for_detectors = {
      "fuel": {
        circle_pad.id: f"surf {circle_pad.id} pad 0.0 0.0 0.0 {radius} 180 270",
      },
      "boundary": {
        rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px {-rectangle_width}\n",
        plane.id: f"surf {plane.id} py {rectangle_width}\ntrans s {plane.id} 0.0 0.0 0.0 0.0 0.0 -30\n\n\n",
        # rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
        rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px 0.00000\n",
        rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n",
      },
      "boundary_guide": {
        "left": rectangle_surf.surf_left.id,
        "top": plane.id,
        "right": rectangle_surf.surf_right.id,
        "bottom": rectangle_surf.surf_bottom.id,
      },
      "boundary_guide_inv": {
        rectangle_surf.surf_left.id : "left",
        plane.id : "top",
        rectangle_surf.surf_right.id : "right",
        rectangle_surf.surf_bottom.id : "bottom",
      },
      "boundary_surfaces": {
        rectangle_surf.surf_left.id: rectangle_surf.surf_left,
        plane.id: plane,
        rectangle_surf.surf_right.id: rectangle_surf.surf_right,
        rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
      },
      "boundary_surfaces_areas": {
        rectangle_surf.surf_left.id: rectangle_height / 2,
        plane.id: plane_area,
        rectangle_surf.surf_right.id: rectangle_height,
        rectangle_surf.surf_bottom.id: rectangle_width,
      },
      "current_directions": {
        circle_pad.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"},
        rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
        plane.id: {"inward": "-1", "outward": "1"}
      }
    }

    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": rectangle_width,
      "rectangle_height": rectangle_height,
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "fuel_relation": {
        "fuel": fuel_cell.id,
        "non_fuel": coolant_cell.id,
        # "void": void_cell
      },
      "type": "corner_in_pin",
      "plane_void_id": plane.id,
      "cells": cells,
      "surfaces_for_detectors": surfaces_for_detectors,
      # "detectors": hexagonal_assembly.edge_with_void_detectors
    } 

    return cells, geometry_info


class SquareGridMesh_no_J_share(CoarseMesh):
    

  def __init__(self, cell):
    super().__init__(cell)
    self.__map_pins = []
    self.__symmetry = {}
    self.clean_mesh_map = []
    self.points_mesh = []
    self.coarse_nodes = {}
    self.type_mesh = ""
    self.universe = super().cell.content
    if isinstance(self.universe, HexagonalLatticeTypeX):
      self.__create_nodes_hex_assem()
    
    
  def __create_nodes_hex_assem(self):

    self.type_mesh = "square_hex_assembly"
    # Getting node map --------------------------------------------------------
    map_pins = self.__get_node_map()
    
    clean_map = self.__get_clean_map()
    # print_map_node = [print(row) for row in map_pins]
    # print("-"*100)
    # print_map_node = [print(row) for row in clean_map]
    first_pin_id = clean_map[1][1][0]
    first_pin = self.universe.cells[first_pin_id]
    self.__hexagon_width = first_pin.region.surface.half_width

    fuel, no_fuel = first_pin.content.find_fuel_cells()

    fuel_mat = fuel[0].content
    radius_fuel = fuel[0].region.surface.radius
    coolant_mat = no_fuel[0].content
    
    outer_hex = super().cell.region.surface    
    # a = [print(row) for row in clean_map]
    # print("--"*70)
    third_pin_id = clean_map[2][1][0]
    third_pin = self.universe.cells[third_pin_id]
    # print("----------------------:   ",third_pin.region.surface.center)
    # x_div, y_div = self.__calculate_square_mesh_coord_hex_assem(outer_hex, clean_map)
    y_div = [1.4182465, 0.8509479, 0.0, -0.8509479, -1.4182465]
    x_div = [
      [-1.146355, -0.491295, 0.0, 0.491295, 1.146355], 
      [-1.63765, -1.146355, -0.491295, 0.0, 0.491295, 1.146355, 1.63765], 
      [-1.63765, -1.146355, -0.491295, 0.0, 0.491295, 1.146355, 1.63765], 
      [-1.146355, -0.491295, 0.0, 0.491295, 1.146355]
    ]
    self.points_mesh = self.__get_rectangles_from_mesh_coord(x_div, y_div)#, outer_hex, clean_map)
    self.coarse_nodes_map = self.__get_map_mesh(clean_map)
    # print("self.coarse_nodes_map: ")
    # print(self.coarse_nodes_map)
    # print("--"*70)

    # print(self.coarse_nodes_map)
    self.__symmetry = self.__get_symmetry_hex_assem()
    
    self.coarse_nodes = self.__get_coarse_nodes_hex_assem(fuel_mat, coolant_mat, radius_fuel)

  
  def __get_node_map(self):
    universe = super().cell.content
    node_counter = 1
    map_pins = []
    for y in range(universe.ny):
      map_nodes_row = []
      cell_counter = 0
      for x in range(universe.nx):
          pin_cell_id = universe.array[y][x]
          if pin_cell_id is None:
              map_nodes_row.append(None)
          else:
              
              map_nodes_row.append(node_counter)
              node_counter += 1
      
      map_pins.append(map_nodes_row)
    return map_pins
  
  def __get_clean_map(self):
    universe = super().cell.content
    
    clean_map = [
      [
        col for col in row if col is not None
      ] for row in universe.array
    ]
    clean_map = [
      [
        col for col in row
      ] for row in clean_map if len(row) != 0
    ]
    return clean_map

  def __get_symmetry_hex_assem(self):
    self.__clean_mesh_map = [
      [
        col for col in row if col != 0
      ] for row in self.coarse_nodes_map
    ]
    # print("--"*70)
    # print("self.__clean_mesh_map")
    # print_clean_mesh_map = [print(row) for row in self.__clean_mesh_map]
    # print("--"*70)
    type_1 = self.__clean_mesh_map[0][0]  # 1
    type_2 = self.__clean_mesh_map[0][1]  # 2
    type_3 = self.__clean_mesh_map[1][0]  # 5
    type_4 = self.__clean_mesh_map[1][1]  # 6
    type_5 = self.__clean_mesh_map[1][2]  # 7
    
    symmetry = {
      type_1: {
        type_1: {"same": ""},
        4: {"mirror":"right"},
        17: {"mirror":"down"},
        20: {"mirror":"right_down"},
        # self.__clean_mesh_map[0][-1]: {"same": ""},
        # self.__clean_mesh_map[-1][0]: {"same": ""},
        # self.__clean_mesh_map[-1][-1]: {"same": ""},
      }, 
      type_2: {
        type_2: {"same": ""},
        3: {"mirror":"right"},
        18: {"mirror":"down"},
        19: {"mirror":"right_down"}
      }, 
      type_3: {
        type_3: {"same": ""},
        10: {"mirror":"right"},
        11: {"mirror":"down"},
        16: {"mirror":"right_down"},
      }, 
      type_4: {
        type_4: {"same": ""},
        9: {"mirror":"right"},
        12: {"mirror":"down"},
        15: {"mirror":"right_down"}
      }, 
      type_5: {
        type_5: {"same": ""},
        8: {"mirror":"right"},
        13: {"mirror":"down"},
        14: {"mirror":"right_down"}
      }
    }

    return symmetry

  def __get_rectangles_from_mesh_coord(self, x_div, y_div):
    
    mesh = {}
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
        mesh[node_counter] = rectangle
        node_counter += 1
      row_x += 1

    return mesh
  
  def __get_map_mesh(self, clean_map):
    
    map_mesh = []
    node_counter = 1
    middle_clean_map = len(clean_map) 
    for r, row in enumerate(clean_map):
      map_mesh_row = []
      for id_, pin in row:
        if pin == "inside":
          map_mesh_row.append(node_counter)
          map_mesh_row.append(node_counter+1)
          node_counter += 2
      if len(map_mesh_row) > 0:
        if r == len(clean_map) // 2:
          map_mesh.append(map_mesh_row)
          another_middle_row = []
          for val_ in map_mesh_row:
            another_middle_row.append(node_counter)
            node_counter += 1
          map_mesh.append(another_middle_row)
        else:
          map_mesh.append(map_mesh_row)
    number_zeros = 1
    middle = len(map_mesh) // 2
    idx_up = middle - 1
    idx_bottom = middle
    while idx_up >= 0:
      map_row_bottom = map_mesh[idx_bottom]
      map_row_up = map_mesh[idx_up]
      for z in range(number_zeros):
        map_row_bottom = [0] + map_row_bottom
        map_row_bottom.append(0)
        map_row_up = [0] + map_row_up
        map_row_up.append(0)
      map_mesh[idx_bottom] = list(map_row_bottom)
      map_mesh[idx_up] = list(map_row_up)
      idx_up -= 1
      idx_bottom += 1
      number_zeros += 1

    
    return np.array(map_mesh)

  def __get_coarse_nodes_hex_assem(self, fuel_mat, coolant_mat, radius):
    coarse_nodes = {}
    for y, row in enumerate(self.coarse_nodes_map):
      for x, node_id in enumerate(row):
        if node_id != 0:
          # each rectangle corresponds to a cell
          rectangle = self.points_mesh[node_id]
          x1, x2 = rectangle[0]
          y1, y2 = rectangle[1]

          get_cells, type_, node_type_id = self.__type_of_rectangle_cell_switch(row, x ,y)
          # print(type_, node_type_id)
          rectangle_cells, geometry_info = get_cells(x1, x2, y1, y2, coolant_mat, fuel_mat, radius)
          geometry_info["type"] = type_
          geometry_info["symmetry"] = {
            node_type_id: self.__symmetry[node_type_id][node_id]
          }
          new_guide = change_boundary_guide(
            geometry_info["surfaces_for_detectors"]["boundary_guide"], geometry_info["symmetry"][node_type_id]
          )
          new_guide_inv = {
            s_id: s_dir for s_dir, s_id in new_guide.items() if s_id is not None
          }
          geometry_info["surfaces_for_detectors"]["boundary_guide"] = new_guide
          geometry_info["surfaces_for_detectors"]["boundary_guide_inv"] = new_guide_inv


          # print(node_id, geometry_info["surfaces_for_detectors"]["boundary_guide"])
          # print(node_id, geometry_info["surfaces_for_detectors"]["boundary_surfaces_areas"])
          # print()
          # Now with these cells create a universe 
          rectangle_universe = Universe(name=f"rectangle_coarse_node_cell_{node_id}")
          rectangle_universe.cells = rectangle_cells
          # Fill a rectangular cell with these universe
          # surf_rectangle = InfiniteRectangleCylinderZ(x1,x2,y1,y2)
          surf_rectangle = geometry_info["rectangle_surf"]
          rectangle_cell = Cell(
              fill=rectangle_universe, 
              region=-surf_rectangle, 
              name=f"coarse_node_cell_{node_id}"
          )
          coarse_node = HexAssemCoarseNode(rectangle_cell, geometry_info)
          coarse_node.id = node_id
          coarse_nodes[node_id] = coarse_node
    return coarse_nodes
  

  def __type_of_rectangle_cell_switch(self, row, x, y):
    # * CASES -------------------------------------------------------
    if y == 0 or y == len(self.coarse_nodes_map) - 1:
      if row[x-1] == 0 or row[x+1] == 0:
        # * top/bottom corner
        return self.__get_rectangle_content_side_edge, "corner", self.__clean_mesh_map[0][0]
      else:
        # * top/bottom edge
        return self.__get_rectangle_content_top_edge, "top_edge", self.__clean_mesh_map[0][1]
    else:
      if row[x-1] == 0 or row[x+1] == 0:
        # * side edge
        return self.__get_rectangle_content_side_edge_no_offset, "offset_side_edge", self.__clean_mesh_map[1][0]
      else:
        # * inside
        if row[x-2] == 0 or row[x+2] == 0:
          return self.__get_rectangle_content_inside_no_offset, "offset_inside", self.__clean_mesh_map[1][1]
        else:
          return self.__get_rectangle_content_inside, "inside", self.__clean_mesh_map[1][2]

  def __get_rectangle_content_side_edge(self, x1, x2, y1, y2, coolant_mat, fuel_mat, radius):
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad = CylinderPad(rectangle_width,0,0,radius,90,180)
    plane = PlaneX(x1)
    plane.rotate(angle=-30, ref_point=(x1, y1))
    
    distance_to_plane = plane.useFunction(y2, given="y") - x1
    plane_area = math.sqrt(distance_to_plane * distance_to_plane + rectangle_height * rectangle_height)
    volume_void = distance_to_plane * rectangle_height / 2
    volume_fuel = circle_pad.volume
    volume_coolant = rectangle_surf.volume - volume_fuel - volume_void

    region_void = -rectangle_surf & +plane
    region_coolant = -rectangle_surf & -plane & +circle_pad
    region_fuel = -circle_pad

    void_cell = Cell(
      name="void_side_edge_type_hexagonal_square_mesh", 
      fill=Material("void"),
      volume=volume_void,
      region=region_void
    )
    coolant_cell = Cell(
      name="coolant_side_edge_type_hexagonal_square_mesh", 
      fill=coolant_mat,
      volume=volume_coolant,
      region=region_coolant
    )
    fuel_cell = Cell(
      name="fuel_side_edge_type_hexagonal_square_mesh", 
      fill=fuel_mat,
      volume=volume_fuel,
      region=region_fuel
    )

    cells = {
      # void_cell.id: void_cell,
      coolant_cell.id: coolant_cell,
      fuel_cell.id: fuel_cell
    }


    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "x1_x2_top": (x1, x2),
      "x1_x2_bottom": (x1, x2),
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "fuel_relation": {
        "fuel": fuel_cell.id,
        "non_fuel": coolant_cell.id,
        # "void": void_cell
      },
      "plane_void_id": plane.id,
      "cells": cells,
      "surfaces_for_detectors": {
        "fuel": {
          circle_pad.id: f"surf {circle_pad.id} pad {rectangle_width} 0.0 0.0 {radius} 180 270",
        },
        "boundary": {
          # rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
          rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
          rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
          rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n",
          plane.id: f"surf {plane.id} px 0.00\ntrans s {plane.id} 0.0 0.0 0.0 0.0 0.0 30\n\n\n"
        },
        "boundary_guide": {
          "left": plane.id,
          "top": rectangle_surf.surf_top.id,
          "right": rectangle_surf.surf_right.id,
          "bottom": rectangle_surf.surf_bottom.id,
          # "left": rectangle_surf.surf_left.id
        },
        "boundary_guide_inv": {
          plane.id : "left",
          rectangle_surf.surf_top.id : "top",
          rectangle_surf.surf_right.id : "right",
          rectangle_surf.surf_bottom.id : "bottom",
          # rectangle_surf.surf_left.id: "left",
        },
        "boundary_surfaces": {
          # rectangle_surf.surf_left.id: rectangle_surf.surf_left,
          rectangle_surf.surf_top.id: rectangle_surf.surf_top,
          rectangle_surf.surf_right.id: rectangle_surf.surf_right,
          rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
          plane.id: plane,
        },
        "boundary_surfaces_areas": {
          # rectangle_surf.surf_left.id: rectangle_height,
          rectangle_surf.surf_top.id: rectangle_width - distance_to_plane,
          rectangle_surf.surf_right.id: rectangle_height,
          rectangle_surf.surf_bottom.id: rectangle_width,
          plane.id: plane_area,

        },
        "current_directions": {
          circle_pad.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"},
          rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
          plane.id: {"inward": "1", "outward": "-1"}
        }
      },
      # "detectors": hexagonal_assembly.edge_with_void_detectors
    } 

    return cells, geometry_info

  def __get_rectangle_content_top_edge(self, x1, x2, y1, y2, coolant_mat, fuel_mat, radius):
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad = CylinderPad(0.0,0.0,0.0,radius,270,360)
    vol_fuel = circle_pad.volume
    vol_coolant = rectangle_surf.volume - vol_fuel
    region_coolant = -rectangle_surf & +circle_pad
    region_fuel = -circle_pad
    coolant_cell = Cell(
      name="coolant_top_type_hexagonal_square_mesh", 
      fill=coolant_mat,
      volume=vol_coolant,
      region=region_coolant
    )
    fuel_cell = Cell(
      name="fuel_top_type_hexagonal_square_mesh", 
      fill=fuel_mat,
      volume=vol_fuel,
      region=region_fuel
    )
    cells = {
      coolant_cell.id: coolant_cell,
      fuel_cell.id: fuel_cell
    }
    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "x1_x2_top": (x1, x2),
      "x1_x2_bottom": (x1, x2),
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "fuel_relation": {
        "fuel": fuel_cell.id,
        "non_fuel": coolant_cell.id
      },
      "cells": cells,
      "surfaces_for_detectors": {
        "fuel":{
          circle_pad.id: f"surf {circle_pad.id} pad 0.0 0.0 0.0 {radius} 270 360",
        },
        "boundary": {
          rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
          rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
          rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
          rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n"
        },
        "boundary_guide": {
          "left": rectangle_surf.surf_left.id,
          "top": rectangle_surf.surf_top.id,
          "right": rectangle_surf.surf_right.id,
          "bottom": rectangle_surf.surf_bottom.id,
        },
        "boundary_guide_inv": {
          rectangle_surf.surf_left.id : "left",
          rectangle_surf.surf_top.id: "top",
          rectangle_surf.surf_right.id : "right",
          rectangle_surf.surf_bottom.id : "bottom",
        },
        "boundary_surfaces": {
          rectangle_surf.surf_left.id: rectangle_surf.surf_left,
          rectangle_surf.surf_top.id: rectangle_surf.surf_top,
          rectangle_surf.surf_right.id: rectangle_surf.surf_right,
          rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
        },
        "boundary_surfaces_areas": {
          rectangle_surf.surf_left.id: rectangle_height,
          rectangle_surf.surf_top.id: rectangle_width,
          rectangle_surf.surf_right.id: rectangle_height,
          rectangle_surf.surf_bottom.id: rectangle_width,
        },
        "current_directions": {
          circle_pad.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
          rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"}
        }

      }

    } 
    return cells, geometry_info
  
  def __get_rectangle_content_side_edge_no_offset(self, x1, x2, y1, y2, coolant_mat, fuel_mat, radius, offset=0.163765):
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad = CylinderPad(rectangle_width,0,0,radius,90,180)
    plane = PlaneX(x1)
    plane.rotate(angle=-30, ref_point=(x1, y1))
    
    plane_area = math.sqrt(rectangle_width * rectangle_width + rectangle_height * rectangle_height)

    # Calculate distance to chord
    chord_length = 2 * math.sqrt(radius * radius - offset * offset)
    angle_segment = math.degrees(math.asin(chord_length/(2*radius))) * 2
    segment_area = math.pi * radius * radius * (angle_segment / 360)
    triangle_area = chord_length * offset / 2
    chord_area = segment_area - triangle_area
  
    volume_fuel = chord_area / 2
    volume_void = rectangle_width * rectangle_height / 2
    volume_coolant = rectangle_surf.volume - volume_fuel - volume_void

    region_void = -rectangle_surf & +plane
    region_coolant = -rectangle_surf & -plane & +circle_pad
    region_fuel = -circle_pad

    void_cell = Cell(
      name="void_side_edge_type_hexagonal_square_mesh", 
      fill=Material("void"),
      volume=volume_void,
      region=region_void
    )
    coolant_cell = Cell(
      name="coolant_side_edge_type_hexagonal_square_mesh", 
      fill=coolant_mat,
      volume=volume_coolant,
      region=region_coolant
    )
    fuel_cell = Cell(
      name="fuel_side_edge_type_hexagonal_square_mesh", 
      fill=fuel_mat,
      volume=volume_fuel,
      region=region_fuel
    )

    cells = {
      # void_cell.id: void_cell,
      coolant_cell.id: coolant_cell,
      fuel_cell.id: fuel_cell
    }

    surfaces_for_detectors = {
      "fuel": {
        circle_pad.id: f"surf {circle_pad.id} pad {rectangle_width} 0.0 0.0 {radius} 180 270",
      },
      "boundary": {
        # rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
        # rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
        rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
        rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n",
        plane.id: f"surf {plane.id} px 0.00\ntrans s {plane.id} 0.0 0.0 0.0 0.0 0.0 30\n\n\n",
      },
      "boundary_guide": {
        # "left": rectangle_surf.surf_left.id
        "top": None,
        "right": rectangle_surf.surf_right.id,
        "bottom": rectangle_surf.surf_bottom.id,
        "left": plane.id,
      },
      "boundary_guide_inv": {
        # rectangle_surf.surf_left.id: "left",
        None : "top",
        rectangle_surf.surf_right.id : "right",
        rectangle_surf.surf_bottom.id : "bottom",
        plane.id : "left",
      },
      "boundary_surfaces": {
        # rectangle_surf.surf_left.id: rectangle_surf.surf_left,
        # rectangle_surf.surf_top.id: rectangle_surf.surf_top,
        rectangle_surf.surf_right.id: rectangle_surf.surf_right,
        rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
        plane.id: plane,
      },
      "boundary_surfaces_areas": {
        # rectangle_surf.surf_left.id: rectangle_height,
        # rectangle_surf.surf_top.id: rectangle_width,
        rectangle_surf.surf_right.id: rectangle_height,
        rectangle_surf.surf_bottom.id: rectangle_width,
        plane.id: plane_area,
      },
      "current_directions": {
        circle_pad.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"},
        rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
        rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
        plane.id: {"inward": "1", "outward": "-1"}
      }
    }

    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "x1_x2_top": (x1, x2),
      "x1_x2_bottom": (x1, x2),
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "fuel_relation": {
        "fuel": fuel_cell.id,
        "non_fuel": coolant_cell.id,
        # "void": void_cell
      },
      "plane_void_id": plane.id,
      "cells": cells,
      "surfaces_for_detectors": surfaces_for_detectors,
      # "detectors": hexagonal_assembly.edge_with_void_detectors
    } 

    return cells, geometry_info

  def __get_rectangle_content_inside(self, x1, x2, y1, y2, coolant_mat, fuel_mat, radius):
    coolant_mat_1 = coolant_mat
    coolant_mat_2 = coolant_mat
    fuel_mat_1 = fuel_mat
    fuel_mat_2 = fuel_mat
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2, radius)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad1 = CylinderPad(x1,y1,0,radius,0,90)
    circle_pad2 = CylinderPad(x2,y2,0,radius,180,270)

    plane = PlaneX(x1)
    plane.rotate(angle=-30, ref_point=(x1, self.__hexagon_width))

    volume_fuel1 = circle_pad1.volume
    volume_fuel2 = circle_pad2.volume
    volume_cool1 = (rectangle_surf.volume - volume_fuel1 - volume_fuel2) / 2
    volume_cool2 = (rectangle_surf.volume - volume_fuel1 - volume_fuel2) / 2
    
    region_fuel1 = -circle_pad1
    region_fuel2 = -circle_pad2
    region_cool1 = -rectangle_surf & +circle_pad1 & -plane
    region_cool2 = -rectangle_surf & +circle_pad2 & +plane

    coolant_cell_1 = Cell(
      name="coolant1_corner_type_hexagonal_square_mesh", 
      fill=coolant_mat_1,
      volume=volume_cool1,
      region=region_cool1
    )
    fuel_cell_1 = Cell(
      name="fuel1_corner_type_hexagonal_square_mesh", 
      fill=fuel_mat_1,
      volume=volume_fuel1,
      region=region_fuel1
    )
    coolant_cell_2 = Cell(
      name="coolant2_corner_type_hexagonal_square_mesh", 
      fill=coolant_mat_2,
      volume=volume_cool2,
      region=region_cool2
    )
    fuel_cell_2 = Cell(
      name="fuel2_corner_type_hexagonal_square_mesh", 
      fill=fuel_mat_2,
      volume=volume_fuel2,
      region=region_fuel2
    )
    cells = {
      coolant_cell_1.id: coolant_cell_1,
      fuel_cell_1.id: fuel_cell_1,
      coolant_cell_2.id: coolant_cell_2,
      fuel_cell_2.id: fuel_cell_2
    }
    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "x1_x2_top": (x1, x2),
      "x1_x2_bottom": (x1, x2),
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "hexagon_radius": self.__hexagon_width,
      "fuel_relation": {
        "fuel1": fuel_cell_1.id,
        "fuel2": fuel_cell_2.id,
        "non_fuel1": coolant_cell_1.id,
        "non_fuel2": coolant_cell_2.id,
      },
      "cells": cells,
      "surfaces_for_detectors": {
        "fuel": {
          circle_pad1.id: f"surf {circle_pad1.id} pad 0.0 0.0 0.0 {radius} 270 360",
          circle_pad2.id: f"surf {circle_pad2.id} pad {rectangle_width} {rectangle_height} 0.0 {radius} 90  180",
        },
        "boundary": {
          rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
          rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
          rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
          rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n"
        },
        "boundary_guide": {
          "left": rectangle_surf.surf_left.id,
          "top": rectangle_surf.surf_top.id,
          "right": rectangle_surf.surf_right.id,
          "bottom": rectangle_surf.surf_bottom.id,
        },
        "boundary_guide_inv": {
          rectangle_surf.surf_left.id : "left",
          rectangle_surf.surf_top.id : "top",
          rectangle_surf.surf_right.id : "right",
          rectangle_surf.surf_bottom.id : "bottom",
        },
        "boundary_surfaces": {
          rectangle_surf.surf_left.id: rectangle_surf.surf_left,
          rectangle_surf.surf_top.id: rectangle_surf.surf_top,
          rectangle_surf.surf_right.id: rectangle_surf.surf_right,
          rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
        },
        "boundary_surfaces_areas": {
          rectangle_surf.surf_left.id: rectangle_height,
          rectangle_surf.surf_top.id: rectangle_width,
          rectangle_surf.surf_right.id: rectangle_height,
          rectangle_surf.surf_bottom.id: rectangle_width,
        },
        "current_directions": {
          circle_pad1.id: {"inward": "-1", "outward": "1"},
          circle_pad2.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
          rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"}
        }
      }
    } 
    return cells, geometry_info

  def __get_rectangle_content_inside_no_offset(self, x1, x2, y1, y2, coolant_mat, fuel_mat, radius, offset=0.163765):
    coolant_mat_1 = coolant_mat
    coolant_mat_2 = coolant_mat
    fuel_mat_1 = fuel_mat
    fuel_mat_2 = fuel_mat
    rectangle_surf = InfiniteRectangleCylinderZ(x1, x2, y1, y2, radius)
    rectangle_height = y2 - y1
    rectangle_width = x2 - x1
    circle_pad1 = CylinderPad(x1+offset,y1,0,radius,0,180)
    circle_pad2 = CylinderPad(x2,y2,0,radius,180,270)


    # only one coolant region to not mess with the volumes --------------------
    # plane = PlaneX(x1)
    # plane.rotate(angle=-30, ref_point=(x1, self.__hexagon_width))
    chord_length = 2 * math.sqrt(radius * radius - offset * offset)
    angle_segment = math.degrees(math.asin(chord_length/(2*radius))) * 2
    segment_area = math.pi * radius * radius * (angle_segment / 360)
    triangle_area = chord_length * offset / 2
    chord_area = segment_area - triangle_area
    
   
    
    volume_fuel1 = math.pi * radius * radius / 2 - chord_area / 2
    volume_fuel2 = circle_pad2.volume
    volume_cool = rectangle_surf.volume - volume_fuel1 - volume_fuel2
   
    
    region_fuel1 = -circle_pad1
    region_fuel2 = -circle_pad2
    region_cool1 = -rectangle_surf & +circle_pad1 & +circle_pad2

    coolant_cell = Cell(
      name="coolant1_corner_type_hexagonal_square_mesh", 
      fill=coolant_mat_1,
      volume=volume_cool,
      region=region_cool1
    )
    fuel_cell_1 = Cell(
      name="fuel1_corner_type_hexagonal_square_mesh", 
      fill=fuel_mat_1,
      volume=volume_fuel1,
      region=region_fuel1
    )
    fuel_cell_2 = Cell(
      name="fuel2_corner_type_hexagonal_square_mesh", 
      fill=fuel_mat_2,
      volume=volume_fuel2,
      region=region_fuel2
    )
    cells = {
      coolant_cell.id: coolant_cell,
      fuel_cell_1.id: fuel_cell_1,
      fuel_cell_2.id: fuel_cell_2
    }
    geometry_info =  {
      "rectangle_x1": x1,
      "rectangle_x2": x2,
      "rectangle_width": x2 - x1,
      "rectangle_height": y2 - y1,
      "x1_x2_top": (x1, x2),
      "x1_x2_bottom": (x1, x2),
      "radius": radius,
      "rectangle_surf": rectangle_surf,
      "hexagon_radius": self.__hexagon_width,
      "fuel_relation": {
        "fuel1": fuel_cell_1.id,
        "fuel2": fuel_cell_2.id,
        "non_fuel": coolant_cell.id,
      },
      "cells": cells,
      "surfaces_for_detectors": {
        "fuel": {
          circle_pad1.id: f"surf {circle_pad1.id} pad {0.0+offset} 0.0 0.0 {radius} 180 360",
          circle_pad2.id: f"surf {circle_pad2.id} pad {rectangle_width} {rectangle_height} 0.0 {radius} 90  180",
        },
        "boundary": {
          rectangle_surf.surf_left.id: f"surf {rectangle_surf.surf_left.id} px 0.00000\n",
          rectangle_surf.surf_top.id: f"surf {rectangle_surf.surf_top.id} py {rectangle_height}\n",
          rectangle_surf.surf_right.id: f"surf {rectangle_surf.surf_right.id} px {rectangle_width}\n",
          rectangle_surf.surf_bottom.id: f"surf {rectangle_surf.surf_bottom.id} py 0.00000\n"
        },
        "boundary_guide": {
          "left": rectangle_surf.surf_left.id,
          "top": rectangle_surf.surf_top.id,
          "right": rectangle_surf.surf_right.id,
          "bottom": rectangle_surf.surf_bottom.id,
        },
        "boundary_guide_inv": {
          rectangle_surf.surf_left.id : "left",
          rectangle_surf.surf_top.id : "top",
          rectangle_surf.surf_right.id : "right",
          rectangle_surf.surf_bottom.id : "bottom",
        },
        "boundary_surfaces": {
          rectangle_surf.surf_left.id: rectangle_surf.surf_left,
          rectangle_surf.surf_top.id: rectangle_surf.surf_top,
          rectangle_surf.surf_right.id: rectangle_surf.surf_right,
          rectangle_surf.surf_bottom.id: rectangle_surf.surf_bottom,
        },
        "boundary_surfaces_areas": {
          rectangle_surf.surf_left.id: rectangle_height,
          rectangle_surf.surf_top.id: rectangle_width,
          rectangle_surf.surf_right.id: rectangle_height,
          rectangle_surf.surf_bottom.id: rectangle_width,
        },
        "current_directions": {
          circle_pad1.id: {"inward": "-1", "outward": "1"},
          circle_pad2.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_top.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_right.id: {"inward": "-1", "outward": "1"},
          rectangle_surf.surf_bottom.id: {"inward": "1", "outward": "-1"},
          rectangle_surf.surf_left.id: {"inward": "1", "outward": "-1"}
        }
      }
    } 
    return cells, geometry_info


