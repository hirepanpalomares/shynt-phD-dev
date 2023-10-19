
from Shynt.api_py.Serpent.global_nodes_geometry import square_pin_cell as square_coarse_node_geometry

from Shynt.api_py.Mesh.coarse_node import CoarseNode

class SquarePinCoarseNode(CoarseNode):
    
  def __init__(self, cell, g_info):
    super().__init__(cell, geometry_info=g_info)
    self.geometry_info = g_info

  def serpent_geometry(self):
    return square_coarse_node_geometry.square_pin_cell(self.geometry_info)
  
  def xs_generation_geometry(self):
    return square_coarse_node_geometry.xs_generation_square_pin_cell(self.geometry_info)

  def x1_x2(self, face="top"):
    return self.geometry_info[f"x1_x2_{face}"]


  @property
  def surface_ids(self):
    return list(self.geometry_info["surfaces_for_detectors"]["boundary_surfaces"].keys())

  @property
  def surface_areas(self):
    return self.geometry_info["surfaces_for_detectors"]["boundary_surfaces_areas"]
    

