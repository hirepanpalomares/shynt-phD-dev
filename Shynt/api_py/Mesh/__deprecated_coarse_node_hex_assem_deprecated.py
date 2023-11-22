

from Shynt.api_py.Serpent.global_nodes_geometry import hexagonal_assembly as coarse_node_geometry

from Mesh.__deprecated_coarse_node import CoarseNode




class HexAssemCoarseNode(CoarseNode):
    
  def __init__(self, cell, g_info):
    super().__init__(cell, geometry_info=g_info)
    self.geometry_info = g_info

  def serpent_geometry(self):
    if self.geometry_info["type"] == "top_edge":
      return coarse_node_geometry.top_edge(self.geometry_info)
    elif self.geometry_info["type"] == "corner":
      return coarse_node_geometry.edge_with_void(self.geometry_info)
    elif self.geometry_info["type"] == "side_edge":
      return coarse_node_geometry.edge_with_void(self.geometry_info)
    elif self.geometry_info["type"] == "inside":
      hexagon_radius = self.geometry_info["hexagon_radius"]
      return coarse_node_geometry.inside(self.geometry_info)
    elif self.geometry_info["type"] == "corner_in_pin":
      return coarse_node_geometry.corner_in_pin(self.geometry_info)
    elif self.geometry_info["type"] == "offset_inside":
      return coarse_node_geometry.inside_offset(self.geometry_info)
    elif self.geometry_info["type"] == "offset_side_edge":
      return coarse_node_geometry.edge_with_void_no_offset(self.geometry_info)
    
  def xs_generation_geometry(self):
    rect_width = self.geometry_info["rectangle_width"]
    rect_height = self.geometry_info["rectangle_height"]
    radius = self.geometry_info["radius"]
    cells = self.geometry_info["cells"]

    if self.geometry_info["type"] == "top_edge":
      return coarse_node_geometry.xs_generation_top_edge(self.geometry_info)
    elif self.geometry_info["type"] == "corner":
      return coarse_node_geometry.xs_generation_edge_with_void(self.geometry_info)
    elif self.geometry_info["type"] == "side_edge":
      return coarse_node_geometry.xs_generation_edge_with_void(self.geometry_info)
    elif self.geometry_info["type"] == "inside":
      hexagon_radius = self.geometry_info["hexagon_radius"]
      return coarse_node_geometry.xs_generation_inside(self.geometry_info)
    elif self.geometry_info["type"] == "corner_in_pin":
      return coarse_node_geometry.xs_generation_corner_in_pin(self.geometry_info)
    elif self.geometry_info["type"] == "offset_inside":
      return coarse_node_geometry.xs_generation_inside_offset(self.geometry_info)
    elif self.geometry_info["type"] == "offset_side_edge":
      return coarse_node_geometry.xs_generation_edge_with_void_no_offset(self.geometry_info)
    
  def serpent_detectors(self):
    pass
  
  def x1_x2(self, face="top"):
    return self.geometry_info[f"x1_x2_{face}"]


  @property
  def surface_ids(self):
    return list(self.geometry_info["surfaces_for_detectors"]["boundary_surfaces"].keys())

  @property
  def surface_areas(self):
    return self.geometry_info["surfaces_for_detectors"]["boundary_surfaces_areas"]
    

