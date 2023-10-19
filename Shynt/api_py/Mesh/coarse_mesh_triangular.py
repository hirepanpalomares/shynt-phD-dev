
from Shynt.api_py.Mesh.global_coarse_mesh import GlobalMesh

from Shynt.api_py.Geometry.universes import SquareLattice
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX
from Shynt.api_py.Geometry.universes import Pin
from Shynt.api_py.Geometry.universes import Universe

from Shynt.api_py.Geometry.cells import Cell

from Shynt.api_py.Mesh.coarse_node import CoarseNode
from Shynt.api_py.Mesh.coarse_node import HexAssemCoarseNode
from Shynt.api_py.Mesh.coarse_node import SquarePinCoarseNode



import numpy as np


class TriangularMesh(GlobalMesh):
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
    
    
    self.__map_pins = []
    self.__symmetry = {}
    self.clean_mesh_map = []

    self.points_mesh = []
    self.rectangles = []
    self.surface_twins = {}
    self.nodes_surfaces = {}
    self.num_surfaces = 0
    self.equivalent_nodes = {}
    self.corse_nodes_regions = {}
    self.regions_coarse_node = {}
    self.coarse_nodes_regions_material = {}
    self.regions_volume = {}

    self.coarse_nodes = {}
    self.type_mesh = ""
    self.hex_assembly = super().cell.content

    self.triangles = self.get_triangles_coordinates()
    # self.map_nodes = self.__get_node_map()
    # self.clean_map = self.__get_clean_map()
    print("hola triangular mesh")
    
  
  def __create_nodes_switch(self, universe):
    coarse_nodes = None
    coarse_nodes_map = None
    try:
      assert isinstance(universe, HexagonalLatticeTypeX)
      coarse_nodes, coarse_nodes_map = self.__create_nodes_HexagonalLattice(universe)
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
  
  def get_triangles_coordinates(self):
    triangles = {}
    assembly = self.cell.content
    print(assembly.cell_centers)

    return triangles

  def get_cells(self, triangle_points, outer_surf, pin_radius, fuel_mat, coolant_mat):
    from math import pi
    from Shynt.api_py.Geometry.surfaces import CylinderPad, InfiniteRectangleCylinderZ, PlaneX

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
  