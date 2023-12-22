
from Shynt.api_py.Mesh.coarse_mesh import CoarseMesh

from Shynt.api_py.Geometry.universes import (
  HexagonalLatticeTypeX,
  Pin,
  Universe
)

import numpy as np



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
  


class SquareGridMeshHexAssembly_deprecated(CoarseMesh):
  """#!DO NOT USE
  Deprecated class
  """
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
    # Getting node map -----------------------------------------------------------------
    map_pins = self.__get_node_map()
    
    clean_map = self.__get_clean_map()
    # print_map_node = [print(row) for row in map_pins]
    print("-"*100)
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
    print("-"*100)
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

  def __get_coarse_nodes_hex_pin(self, 
  fuel_mat, coolant_mat, radius, outer_hex):
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

  def __get_rectangle_content_top_edge(self, 
  x1, x2, y1, y2, coolant_mat, fuel_mat, radius):
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
  
  def __get_rectangle_content_side_edge(self, 
  x1, x2, y1, y2, coolant_mat, fuel_mat, radius):
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
  x1, x2, y1, y2, coolant_mat, fuel_mat, radius):
    from Shynt.api_py.Geometry.surfaces import (
      InfiniteRectangleCylinderZ,
      CylinderPad,
      PlaneX
    )
    from Shynt.api_py.Geometry.cells import Cell

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
  x1, x2, y1, y2, coolant_mat, fuel_mat, radius, outer_hex):
    from Shynt.api_py.Geometry.surfaces import (
      InfiniteRectangleCylinderZ,
      CylinderPad,
      PlaneY
    )
    from Shynt.api_py.Geometry.cells import Cell
    from Shynt.api_py.materials import Material

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


class SquareGridMeshHexAssembly(CoarseMesh):
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
    self.hex_assembly = super().cell.content
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
    
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}

    self.type_mesh = ""

    
  

  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    from Shynt.api_py.Mesh.coarse_node import CoarseNodeSquareGridHexAssembly

    coarse_nodes = {}
    surfaces = {}

    s_id = 0
    
    pin_centers = self.hex_assembly.pin_centers
    half_pitch = self.hex_assembly.pitch / 2
    hex_wrapper = super().cell.region.surface
    for i, row in enumerate(self.coarse_nodes_map):
      row_node = []
      for j, n_id in enumerate(row):
        if n_id == 0: continue
        node_type = self.node_types[n_id]
        quadrant = self.node_quadrants[n_id]
        coarse_node_class = grid_coarse_node_manager(node_type)
        node = coarse_node_class(
          n_id, 'pin_cell_mesh', half_pitch, quadrant, hex_wrapper
        )

        rectangle_points = self.rectangles[n_id-1]
        s_id = node.calculate_surfaces(s_id, rectangle_points)
        surfaces.update(node.surfaces)
        
        coarse_nodes[n_id] = node

        row_node.append(n_id)
        n_id += 1

    self.surfaces = surfaces
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id

  def __get_x_div(self):
    """Class private method that calculate the x-coordinate divisions for the
    square grid. 

    How these values are calculated is as follows. First it localizes where the
    pin is in the hexagonal assembly acoording to the x-coordinate value of 
    its center. Second, it applies the offset to the center or not depending
    on its position in the assembly. Last, it adds a second value using offset
    or not and a length equal to the half of the assembly pitch

    Returns
    -------
    x_div : list of list
    """
    pin_centers = self.hex_assembly.get_fuel_pins_centers()
    
    p = self.hex_assembly.pitch
    x_div = []
    top_first_pin_center_x = pin_centers[0][0][0]
    top_last_pin_center_x = pin_centers[0][-1][0]

    middle_idx = len(pin_centers) // 2

    for r in range(middle_idx+1):
      row = pin_centers[r]
      x_div_row = []
      last_pin_cx = row[-1][0]
      for c, pin_center in enumerate(row):
        xcoor = pin_center[0]

        # --------------------------------------------------------------------
        if xcoor < top_first_pin_center_x: 
          x_div_row.append(xcoor - self.__offset)
          if r >= 1 and xcoor + p/2 == top_first_pin_center_x: 
            x_div_row.append(top_first_pin_center_x)
          else:
            x_div_row.append(xcoor - self.__offset + p/2)

        # --------------------------------------------------------------------
        elif xcoor == top_first_pin_center_x:
          x_div_row.append(top_first_pin_center_x)
          x_div_row.append(xcoor + p/2)

        # --------------------------------------------------------------------
        elif xcoor > top_first_pin_center_x and xcoor < top_last_pin_center_x:
          x_div_row.append(xcoor)
          x_div_row.append(xcoor + p/2)

        # --------------------------------------------------------------------
        elif xcoor == top_last_pin_center_x:
          x_div_row.append(xcoor)
          if r > 1: x_div_row.append(xcoor + self.__offset + p/2)
        
        # --------------------------------------------------------------------
        elif xcoor == last_pin_cx:
          x_div_row.append(xcoor + self.__offset)

        # --------------------------------------------------------------------
        elif xcoor > top_last_pin_center_x:
          x_div_row.append(xcoor + self.__offset)
          if r >= 3:
            x_div_row.append(xcoor + p/2 + self.__offset)

        # --------------------------------------------------------------------
        elif xcoor == top_last_pin_center_x:
          x_div_row.append(xcoor)
          x_div_row.append(xcoor + p/2 + self.__offset)
        
      x_div.append(x_div_row)  

    # mirror for the bottom part
    for r in range(middle_idx,-1,-1):
      # Copy to be able to modified and not have conflicts in memory
      x_div.append(x_div[r].copy()) 
    
    return x_div
  
  def __get_y_div(self):
    """Class private method that calculate the y-coordinate divisions for the
    square grid. 
    
    How these values are calculated is as follows. First it starts form 
    the center of the assembly. Next, it takes the first x-value of the row and
    calculates its intersection with the face of the hexagon that crosses
    a vertical line from this x-value and that is the second value. Finally,
    it replicates this value in the other side of the hexagon.

    Returns
    -------
    y_div : list of float
    """
    from math import sqrt
    hexagon = super().cell.region.surface
    half_width = hexagon.half_width
    x0,y_center = hexagon.center
    top_limit = y_center + half_width
    p = self.hex_assembly.pitch
    
    pin_centers = self.hex_assembly.get_fuel_pins_centers()

    # print(pin_centers)
    # print(len(self.x_div))
    y_div = [y_center*1.0]
    y_coord = y_center
    # middle_y = len(self.x_div) // 2
    middle_y = len(pin_centers) // 2

    
    first_x_middle = self.x_div[middle_y][0]
    y_intersection = hexagon.surf_F.useFunction(first_x_middle, given="x")
    dy_to_side = round(y_intersection - y_center, 8)
    # Calculating start and end values of x in the central row
    start_x = hexagon.surf_F.useFunction(y_center, given="y")
    end_x = hexagon.surf_B.useFunction(y_center, given="y")
    # adding starting and ending x_value above the center

    
    self.x_div[middle_y].append(end_x) 
    self.x_div[middle_y] = [start_x] + self.x_div[middle_y]
    self.x_div[middle_y+1].append(end_x) 
    self.x_div[middle_y+1] = [start_x] + self.x_div[middle_y+1]
   

    # Loop starting from the center +/- 1
    above_idx = middle_y - 1
    below_idx = middle_y + 2
    while True:
      
      if y_coord + dy_to_side >= top_limit: break
      # print(below_idx)
      # using the first x value in that row to calculate the next y_val
      first_x = self.x_div[above_idx+1][1] 
      y_intersection = hexagon.surf_F.useFunction(first_x, given="x")
      y_above = y_intersection
      y_below = -1*y_intersection
      y_div.append(y_below)     # adding y_value bellow the center
      y_div = [y_above] + y_div # adding y_value above the center
      
      # Calculating start and end values of x in each row
      start_x = hexagon.surf_F.useFunction(y_above, given="y")
      end_x = hexagon.surf_B.useFunction(y_above, given="y")
      # adding starting and ending x_value above the center

      self.x_div[above_idx].append(end_x) 
      self.x_div[above_idx] = [start_x] + self.x_div[above_idx]
      self.x_div[below_idx].append(end_x) 
      self.x_div[below_idx] = [start_x] + self.x_div[below_idx]
      
      above_idx -= 1
      below_idx += 1
      y_coord = y_intersection            # updating the y_value

    if top_limit not in y_div:
      y_div.append(top_limit*-1)
      y_div = [top_limit] + y_div

    return y_div
    

  def get_rectangles_from_mesh_coord(self, x_div, y_div):
    
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

  def generate_fine_mesh_regions(self, unique_regions):
    from Shynt.api_py.Geometry.cells import Cell
    from Shynt.api_py.Mesh.local_mesh_material import MaterialMesh
    
    print('creating fine mesh ...')
    for n_id in  self.unique_nodes:
      eq_nodes = self.equivalent_nodes[n_id]
      for neq in eq_nodes:
        fine_regs = {}
        for reg in unique_regions[n_id]:
          new_fine_reg = (Cell(fill=reg['material'], volume=reg['volume'])) 
          fine_regs[new_fine_reg.id] = new_fine_reg 
        
        new_fine_mesh = MaterialMesh(coarse_node=self.coarse_nodes[neq])
        new_fine_mesh.regions = fine_regs
        self.coarse_nodes[neq].fine_mesh = new_fine_mesh
        
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

  

def grid_coarse_node_manager(node_type):
  from Shynt.api_py.Mesh.coarse_node import (
    CoarseNodeSquareGridHexAssembly_Inside,
    CoarseNodeSquareGridHexAssembly_TrapezoidCorner,
    CoarseNodeSquareGridHexAssembly_SideEdge,
    CoarseNodeSquareGridHexAssembly_TriangleCorner
  )
  if node_type == 'trapezoid_corner':
    return CoarseNodeSquareGridHexAssembly_TrapezoidCorner
  elif node_type == 'inside':
    return CoarseNodeSquareGridHexAssembly_Inside
  elif node_type == 'side_edge':
    return CoarseNodeSquareGridHexAssembly_SideEdge
  elif node_type == 'triangle_corner':
    return CoarseNodeSquareGridHexAssembly_TriangleCorner
  else:
    print(f"node type '{node_type}' not implemented")
    raise NotImplemented
  






























  
    

def fix_boundaries(self, nodes_surfaces):
  """Fixes the diagonal in the nodes on the boundary that are in the 
  diagonal of the hexagon 
  HARDCODED
  Nodes to fix:
    top_bottom_corners = [1,20,561,580]
    sides = [
      21,43,67,93,121,151,183,217,253,291,329,365,399,431,461,489,515,539,
      42,66,92,120,150,182,216,252,290,328,364,398,430,460,488,514,538,560
    ]

  Basically the function calculates from the points of the diagonal surface
  """

  n_surf = nodes_surfaces.copy()
  top_bottom_corners = [
    1,20,561,580
  ]
  sides = [
    21,43,67,93,121,151,183,217,253,291,329,365,399,431,461,489,515,539,
    42,66,92,120,150,182,216,252,290,328,364,398,430,460,488,514,538,560
  ]
  hexagon = super().cell.region.surface
  
  # ---------------------------------------------------
  #                   CORNERS
  # ---------------------------------------------------
  x1,y1 = n_surf[1]["top"]["points"][0]
  x2,y2 = n_surf[1]["top"]["points"][1]
  x1_new = hexagon.surf_F.useFunction(y1, given="y")
  n_surf[1]["top"]["points"] = ((x1_new,y1), (x2,y2))
  x1,y1 = n_surf[1]["left"]["points"][0]
  x2,y2 = n_surf[1]["left"]["points"][1]
  n_surf[1]["left"]["points"] = ((x1,y1), (x1_new,y2))
  # ----------------------------------------------
  x1,y1 = n_surf[20]["top"]["points"][0]
  x2,y2 = n_surf[20]["top"]["points"][1]
  x2_new = hexagon.surf_B.useFunction(y1, given="y")
  n_surf[20]["top"]["points"] = ((x1,y1), (x2_new,y2))
  x1,y1 = n_surf[20]["right"]["points"][0]
  x2,y2 = n_surf[20]["right"]["points"][1]
  n_surf[20]["right"]["points"] = ((x1,y1), (x2_new,y2))
  # ----------------------------------------------
  x1,y1 = n_surf[561]["bottom"]["points"][0]
  x2,y2 = n_surf[561]["bottom"]["points"][1]
  x1_new = hexagon.surf_E.useFunction(y1, given="y")
  n_surf[561]["bottom"]["points"] = ((x1_new,y1), (x2,y2))
  x1,y1 = n_surf[561]["left"]["points"][0]
  x2,y2 = n_surf[561]["left"]["points"][1]
  n_surf[561]["left"]["points"] = ((x1_new,y1), (x2,y2))
  # ----------------------------------------------
  x1,y1 = n_surf[580]["bottom"]["points"][0]
  x2,y2 = n_surf[580]["bottom"]["points"][1]
  x2_new = hexagon.surf_C.useFunction(y1, given="y")
  n_surf[580]["bottom"]["points"] = ((x1,y1), (x2_new,y2))
  x1,y1 = n_surf[580]["right"]["points"][0]
  x2,y2 = n_surf[580]["right"]["points"][1]
  n_surf[580]["right"]["points"] = ((x2_new,y1), (x2,y2))
  
  # ---------------------------------------------------
  #                   SIDES
  # ---------------------------------------------------
  
  def get_position_in_hexagon(point):
    """Mini function to find the place of the node in the hexagon
    giving a point of the top side of the rectangle
    """
    x, y = point
    if x < 0.0 and y > 0.0: return "upper_left"
    if x > 0.0 and y > 0.0: return "upper_right"
    if x < 0.0 and y <= 0.0: return "lower_left"
    if x > 0.0 and y <= 0.0: return "lower_right"

  surf_to_fix = {
    "upper_left": "left",
    "upper_right": "right",
    "lower_left": "left",
    "lower_right": "right"    
  }
  surf_to_remove = {
    "upper_left": "top",
    "upper_right": "top",
    "lower_left": "bottom",
    "lower_right": "bottom"    
  }
  surf_for_p1 = {
    "upper_left": "left",
    "upper_right": "right",
    "lower_left": "right",
    "lower_right": "left"    
  }
  surf_for_p2 = {
    "upper_left": "right",
    "upper_right": "left",
    "lower_left": "left",
    "lower_right": "right"    
  }

  for n_id in sides:
    random_top_point = n_surf[n_id]["top"]["points"][0]
    position = get_position_in_hexagon(random_top_point)
    s_fix = surf_to_fix[position]
    s_rem = surf_to_remove[position]
    new_p1 = n_surf[n_id][surf_for_p1[position]]["points"][0]
    new_p2 = n_surf[n_id][surf_for_p2[position]]["points"][1]
    
    n_surf[n_id][s_fix]["points"] = (new_p1,new_p2)
    n_surf[n_id][s_rem] = None

  return n_surf




def find_equivalent_nodes(self):
  """Hardcoded function to get the nodes that are similar or equivalent

  """
  equivalent_nodes = {
    1: [1,20,561,580],
    2: list(range(2,19+1)) + list(range(562,579+1)),
    21: [
      21,42,43,66,67,92,93,120,121,150,151,182,183,216,217,252,
      329,364,365,398,399,430,431,460,461,488,489,514,515,538,539,560
    ],
    22: [
      22, 22+19,
      70, 70+19,
      126, 126+19,
      190, 190+19,
      372, 372+19,
      436, 436+19,
      492, 492+19,
      540, 540+19,

    ],
    23: [],
    44: [],
    45: [
      45, 45+19,
      97, 97+19,
      157, 157+19,
      225, 225+19,
      337, 337+19,
      405, 405+19,
      465, 465+19,
      517, 517+19,
    ],
    69: [],
    253: [253,290,291,328],
    254: [],
    255: [],
    262: [262,281,300,319],
    263: list(range(263,280+1)) + list(range(301,318+1)),
  }

  # -----------------------------------------------------
  equivalent_nodes[23] += list(range(23,23+17+1))
  equivalent_nodes[23] += list(range(46,46+17+1))
  equivalent_nodes[23] += list(range(71,71+17+1))
  equivalent_nodes[23] += list(range(98,98+17+1))
  equivalent_nodes[23] += list(range(127,127+17+1))
  equivalent_nodes[23] += list(range(158,158+17+1))
  equivalent_nodes[23] += list(range(191,191+17+1))
  equivalent_nodes[23] += list(range(226,226+17+1))

  equivalent_nodes[23] += list(range(338,338+17+1))
  equivalent_nodes[23] += list(range(373,373+17+1))
  equivalent_nodes[23] += list(range(406,406+17+1))
  equivalent_nodes[23] += list(range(437,437+17+1))
  equivalent_nodes[23] += list(range(466,466+17+1))
  equivalent_nodes[23] += list(range(493,493+17+1))
  equivalent_nodes[23] += list(range(518,518+17+1))
  equivalent_nodes[23] += list(range(541,541+17+1))
  # -----------------------------------------------------
  equivalent_nodes[44] += [44,65,68,91]
  equivalent_nodes[44] += list(range(94,96+1,2))
  equivalent_nodes[44] += list(range(117,119+1,2)) 
  equivalent_nodes[44] += list(range(122,124+1,2))
  equivalent_nodes[44] += list(range(147,149+1,2))
  equivalent_nodes[44] += list(range(152,156+1,2))
  equivalent_nodes[44] += list(range(177,181+1,2))
  equivalent_nodes[44] += list(range(184,188+1,2))
  equivalent_nodes[44] += list(range(211,215+1,2))
  equivalent_nodes[44] += list(range(218,224+1,2))
  equivalent_nodes[44] += list(range(245,251+1,2))
  equivalent_nodes[44] += list(range(330,336+1,2))
  equivalent_nodes[44] += list(range(357,363+1,2))
  equivalent_nodes[44] += list(range(366,370+1,2))
  equivalent_nodes[44] += list(range(393,397+1,2))
  equivalent_nodes[44] += list(range(400,404+1,2))
  equivalent_nodes[44] += list(range(425,429+1,2))
  equivalent_nodes[44] += list(range(432,434+1,2))
  equivalent_nodes[44] += list(range(457,459+1,2))
  equivalent_nodes[44] += list(range(462,464+1,2))
  equivalent_nodes[44] += list(range(485,487+1,2))
  equivalent_nodes[44] += [490,513,516,537]
  # -----------------------------------------------------
  equivalent_nodes[69] += [69,90,95,118]
  equivalent_nodes[69] += list(range(123,125+1,2))
  equivalent_nodes[69] += list(range(146,148+1,2))
  equivalent_nodes[69] += list(range(153,155+1,2))
  equivalent_nodes[69] += list(range(178,180+1,2))
  equivalent_nodes[69] += list(range(185,189+1,2))
  equivalent_nodes[69] += list(range(210,214+1,2))
  equivalent_nodes[69] += list(range(219,223+1,2))
  equivalent_nodes[69] += list(range(246,250+1,2))

  equivalent_nodes[69] += list(range(331,335+1,2))
  equivalent_nodes[69] += list(range(358,362+1,2))
  equivalent_nodes[69] += list(range(367,371+1,2))
  equivalent_nodes[69] += list(range(392,396+1,2))
  equivalent_nodes[69] += list(range(401,403+1,2))
  equivalent_nodes[69] += list(range(426,428+1,2))
  equivalent_nodes[69] += list(range(433,435+1,2))
  equivalent_nodes[69] += list(range(456,458+1,2))
  equivalent_nodes[69] += [463,486,491,512]


  # -----------------------------------------------------
  equivalent_nodes[254] += list(range(254,260+1,2))
  equivalent_nodes[254] += list(range(283,289+1,2))
  equivalent_nodes[254] += list(range(292,298+1,2))
  equivalent_nodes[254] += list(range(321,327+1,2))
  # -----------------------------------------------------
  equivalent_nodes[255] += list(range(255,261+1,2))
  equivalent_nodes[255] += list(range(282,288+1,2))
  equivalent_nodes[255] += list(range(293,299+1,2))
  equivalent_nodes[255] += list(range(320,326+1,2))

  self.equivalent_nodes = equivalent_nodes
  return equivalent_nodes


def find_equivalent_nodes_symmetry(self):
  """Hardcoded function to get the simmetry relation of the twin
  nodes
    
    1: {
      1: {"same": ""},
      2: {"mirror":"right"},
      3: {"mirror":"right_down"},
      4: {"mirror":"down"},
    },
    ...
  """
  symmetry = {
    n_id: {
      n_id_eq: {} for n_id_eq in self.equivalent_nodes[n_id]
    } for n_id in self.equivalent_nodes.keys()
  }
  # Symmetry node 1 ---------------------------------------
  symmetry[1][1] = {"same": ""}
  symmetry[1][20] = {"mirror": "right"}
  symmetry[1][580] = {"mirror": "right_down"}
  symmetry[1][561] = {"mirror": "down"}
  # Symmetry node 2 ---------------------------------------
  for n_id_eq in symmetry[2]:
    symm = {}
    if n_id_eq < 561: 
      if n_id_eq % 2 == 0:
        symm = {"same": ""}
      else:
        symm = {"mirror": "right"}

    elif n_id_eq > 561: 
      if n_id_eq % 2 == 0:
        symm = {"mirror": "down"}
      else:
        symm = {"mirror": "right_down"}
    symmetry[2][n_id_eq] = symm

  # Symmetry 21  --------------------------------------------
  for idx,n_id_eq in enumerate(self.equivalent_nodes[21]):
    symm = {}
    if n_id_eq < 328: 
      if idx % 2 == 0:
        symm = {"same": ""}
      else:
        symm = {"mirror": "right"}
    
    elif n_id_eq > 328: 
      if idx % 2 == 0:
        symm = {"mirror": "down"}
      else:
        symm = {"mirror": "right_down"}
    symmetry[21][n_id_eq] = symm
  
  # Symmetry 22  --------------------------------------------
  for idx, n_id_eq in enumerate(self.equivalent_nodes[22]):
    symm = {}
    if n_id_eq < 371: 
      if idx % 2 == 0:
        symm = {"same": ""}
      else:
        symm = {"mirror": "right"}
    
    elif n_id_eq > 371: 
      if idx % 2 == 0:
        symm = {"mirror": "down"}
      else:
        symm = {"mirror": "right_down"}
    symmetry[22][n_id_eq] = symm

  # Symmetry 23  --------------------------------------------
  
  for idx, n_id_eq in enumerate(self.equivalent_nodes[23]):
    symm = {}
    if n_id_eq < 336: 
      if (idx//18)%2 == 0 :
        if idx % 2 == 0:
          symm = {"same": ""}
        else:
          symm = {"mirror": "right"}

      else:
        if idx % 2 == 0:
          symm = {"mirror": "right"}
        else:
          symm = {"same": ""}

    elif n_id_eq > 336: 
      if (idx//18)%2 == 0:
        if idx % 2 == 0:
          symm = {"mirror": "right_down"}
        else:
          symm = {"mirror": "down"}

      else:
        if idx % 2 == 0:
          symm = {"mirror": "down"}
        else:
          symm = {"mirror": "right_down"}
    symmetry[23][n_id_eq] = symm

  # Symmetry 44  --------------------------------------------
  for idx, n_id_eq in enumerate(self.equivalent_nodes[44]):
    symm = {}
    rectangle = self.rectangles[n_id_eq-1]
    x1 = rectangle[0][0]
    if n_id_eq < 329: 
      if x1 < 0:
        symm = {"same": ""}
      else:
        symm = {"mirror": "right"}
    
    elif n_id_eq > 329: 
      if x1 < 0:
        symm = {"mirror": "down"}
      else:
        symm = {"mirror": "right_down"}
    symmetry[44][n_id_eq] = symm

  # Symmetry 45  --------------------------------------------
  for idx, n_id_eq in enumerate(self.equivalent_nodes[45]):
    symm = {}
    if n_id_eq < 336: 
      if idx % 2 == 0:
        symm = {"same": ""}
      else:
        symm = {"mirror": "right"}
    
    elif n_id_eq > 336: 
      if idx % 2 == 0:
        symm = {"mirror": "down"}
      else:
        symm = {"mirror": "right_down"}
    symmetry[45][n_id_eq] = symm

  # Symmetry 69  --------------------------------------------
  for idx, n_id_eq in enumerate(self.equivalent_nodes[69]):
    symm = {}
    rectangle = self.rectangles[n_id_eq-1]
    x1 = rectangle[0][0]
    if n_id_eq < 330: 
      if x1 < 0:
        symm = {"same": ""}
      else:
        symm = {"mirror": "right"}
    
    elif n_id_eq > 330: 
      if x1 < 0:
        symm = {"mirror": "down"}
      else:
        symm = {"mirror": "right_down"}
    symmetry[69][n_id_eq] = symm
  # Symmetry node 253 ---------------------------------------
  symmetry[253][253] = {"same": ""}
  symmetry[253][290] = {"mirror": "right"}
  symmetry[253][291] = {"mirror": "down"}
  symmetry[253][328] = {"mirror": "right_down"}
  
  # Symmetry node 254 ---------------------------------------
  for idx, n_id_eq in enumerate(self.equivalent_nodes[254]):
    symm = {}
    if n_id_eq < 283: 
        symm = {"same": ""}
    elif n_id_eq > 260 and n_id_eq < 292: 
        symm = {"mirror": "right"}
    elif n_id_eq > 289 and n_id_eq < 320: 
        symm = {"mirror": "down"}
    elif n_id_eq > 320: 
        symm = {"mirror": "right_down"}
    symmetry[254][n_id_eq] = symm

  # Symmetry node 255 ---------------------------------------
  for idx, n_id_eq in enumerate(self.equivalent_nodes[255]):
    symm = {}
    if n_id_eq < 282: 
        symm = {"same": ""}
    elif n_id_eq > 261 and n_id_eq < 293: 
        symm = {"mirror": "right"}
    elif n_id_eq > 292 and n_id_eq < 320: 
        symm = {"mirror": "down"}
    elif n_id_eq > 319: 
        symm = {"mirror": "right_down"}
    symmetry[255][n_id_eq] = symm
  
  # Symmetry node 262 ---------------------------------------
  symmetry[262][262] = {"same": ""}
  symmetry[262][281] = {"mirror": "right"}
  symmetry[262][300] = {"mirror": "down"}
  symmetry[262][319] = {"mirror": "right_down"}

  # Symmetry node 263 ---------------------------------------
  for idx, n_id_eq in enumerate(self.equivalent_nodes[263]):
    symm = {}
    if n_id_eq < 300: 
      if idx % 2 == 0:
        symm = {"same": ""}
      else:
        symm = {"mirror": "right"}
    
    elif n_id_eq > 300: 
      if idx % 2 == 0:
        symm = {"mirror": "down"}
      else:
        symm = {"mirror": "right_down"}
    symmetry[263][n_id_eq] = symm

  return symmetry


def fill_regions(self):
  regions_ids = {
    1: [("fuel", 1),("na_coolant", 2)],
    2: [("fuel", 1),("na_coolant", 2)],
    21: [("fuel", 1),("na_coolant", 2)],
    22: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    23: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    44: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    45: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    69: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    253: [("fuel", 1),("na_coolant", 2)],
    254: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    255: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    262: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
    263: [("fuel", 1),("fuel", 2),("na_coolant", 3)],
  }
  coarse_nodes_regions = {}
  regions_coarse_node = {}
  coarse_nodes_regions_material = {}

  for nid, eq_array in self.equivalent_nodes.items():

    for eq_nid in eq_array:
      coarse_nodes_regions[eq_nid] = []

      for region in regions_ids[nid]:
        r_id = f"{eq_nid}_{region[1]}"
        coarse_nodes_regions[eq_nid].append(r_id)
        coarse_nodes_regions_material[r_id] = region[0]
        regions_coarse_node[r_id] = eq_nid
      # print(coarse_nodes_regions[eq_nid])
  
  self.coarse_nodes_regions = coarse_nodes_regions
  self.coarse_nodes_regions_material = coarse_nodes_regions_material
  self.regions_coarse_node = regions_coarse_node
  return coarse_nodes_regions


def __get_symmetry_hex_assem(self):
  self.__clean_mesh_map = [
    [
      col for col in row if col != 0
    ] for row in self.coarse_nodes_map
  ]
  print("--"*70)
  print("self.__clean_mesh_map")
  print_clean_mesh_map = [print(row) for row in self.__clean_mesh_map]
  print("--"*70)
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




