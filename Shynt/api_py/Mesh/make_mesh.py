
from Shynt.api_py.Mesh.local_mesh import (
  MaterialMesh, 
  CellMesh, 
  PieMesh
)

from Shynt.api_py.Mesh.coarse_mesh_pin_cell import PinCellMesh
from Shynt.api_py.Mesh.coarse_mesh_triangular import TriangularMesh
from Shynt.api_py.Mesh.coarse_mesh_square_grid import SquareGridMeshHexAssembly

from Shynt.api_py.Geometry.cells import Cell




class Mesh():
  """Class used to represent a mesh, it creates:
    - coarse mesh (Every coarse node)
    - the fine mesh for every coarse node
    - probably the map
    - a list of coarse nodes
  
    Every coarse Node should have as attributes:
      - fine mesh
      - The serpent syntax to simulate that coarse node

  ...

  Attributes
  ----------
  cell :

  global_mesh_type :

  local_mesh_type :

  coarse_mesh :

  coarse_nodes :

  coarse_nodes_map :

  fine_mesh :

  fine_nodes :

  Methods
  -------
  create_coarse_mesh()

  create_fine_mesh()
  """

  def __init__(
  self, cell: Cell, global_mesh_type: str, local_mesh_type: str, offset=0.0
  ) -> None:
    self.cell = cell
    self.global_mesh_type = global_mesh_type
    self.local_mesh_type = local_mesh_type
    self.offset = offset
    
    self.coarse_mesh = None
    self.coarse_nodes = None
    self.coarse_nodes_map = None
    self.fine_mesh = None
    self.fine_nodes = None

    self.create_coarse_mesh()
    self.create_fine_mesh()


  def create_coarse_mesh(self) -> None:
    """Helper method to create the coarse mesh,
    It chooses between different meshes depending on the attribute 
    global_mesh_type. Types available:
      - pin_cell
      - square_grid
      - square_mesh_pin_no_share
    
    """
    coarse_mesh = None
    if self.global_mesh_type == "pin_cell":    
      coarse_mesh =  PinCellMesh(self.cell)
    elif self.global_mesh_type == "square_grid":
      coarse_mesh =  SquareGridMeshHexAssembly(
        self.cell, offset=self.offset
      )
    elif self.global_mesh_type == "triangular":
      coarse_mesh =  TriangularMesh(self.cell)

    self.coarse_mesh = coarse_mesh
    self.coarse_nodes = coarse_mesh.coarse_nodes
    self.coarse_nodes_map = coarse_mesh.coarse_nodes_map

  def create_fine_mesh(self) -> None:
    pass



# def __create_nodes_hex_assem(self):

#     first_pin_id = self.clean_map[1][1][0]
#     first_pin = self.universe.cells[first_pin_id]
#     self.__hexagon_width = first_pin.region.surface.half_width

#     fuel, no_fuel = first_pin.content.find_fuel_cells()

#     fuel_mat = fuel[0].content
#     radius_fuel = fuel[0].region.surface.radius
#     coolant_mat = no_fuel[0].content
    
#     outer_hex = super().cell.region.surface    
    
#     third_pin_id = self.clean_map[2][1][0]
#     third_pin = self.universe.cells[third_pin_id]
#     # print("----------------------:   ",third_pin.region.surface.center)
#     # x_div, y_div = self.__calculate_square_mesh_coord_hex_assem(outer_hex, clean_map)
#     y_div = [1.4182465, 0.8509479, 0.0, -0.8509479, -1.4182465]
#     x_div = [
#       [-1.146355, -0.491295, 0.0, 0.491295, 1.146355], 
#       [-1.63765, -1.146355, -0.491295, 0.0, 0.491295, 1.146355, 1.63765], 
#       [-1.63765, -1.146355, -0.491295, 0.0, 0.491295, 1.146355, 1.63765], 
#       [-1.146355, -0.491295, 0.0, 0.491295, 1.146355]
#     ]
#     self.points_mesh = self.__get_rectangles_from_mesh_coord(x_div, y_div)#, outer_hex, clean_map)
#     self.coarse_nodes_map = self.__get_map_mesh(clean_map)
#     print("self.coarse_nodes_map: ")
#     print(self.coarse_nodes_map)
#     print("--"*70)

#     # print(self.coarse_nodes_map)
#     self.__symmetry = self.__get_symmetry_hex_assem()
    
#     self.coarse_nodes = self.__get_coarse_nodes_hex_assem(fuel_mat, coolant_mat, radius_fuel)