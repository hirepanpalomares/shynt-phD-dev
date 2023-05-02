
from Shynt.api_py.Geometry.surfaces import CylinderPad, PlaneX, PlaneY, InfiniteCylinderZ
from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderYtype
from Shynt.api_py.Geometry.surfaces import InfiniteRectangleCylinderZ

from Shynt.api_py.Geometry.regions import SurfaceSide

from Shynt.api_py.Geometry.universes import Pin

from Shynt.api_py.Serpent.global_nodes_geometry import hexagonal_assembly as coarse_node_geometry


class CoarseNode():

  def __init__(self, cell, geometry_info=False) -> None:
    super().__init__()
    self.__cell = cell
    self.__id = None
    
    if geometry_info:
      self.__surfaces = geometry_info["surfaces_for_detectors"]["boundary_surfaces"]
      self.__surface_areas = geometry_info["surfaces_for_detectors"]["boundary_surfaces_areas"]
      self.__surface_directions = geometry_info["surfaces_for_detectors"]["boundary_guide_inv"]
    else:
      self.__surfaces = self.__getSurfaces()                      # Dictionary of surface classes {id: <Surface class>}
      self.__surface_areas = self.__getSurfaceAreas()             # Dictionary of surfaces areas {id: area}
      self.__surface_directions = self.__getSurfaceDirections()   # Dictionary with the direction of the surfaces
    # self.fictional_surfaces = self.__getFictionalSurfaces()
    self.__surface_ids = list(self.__surfaces.keys())           # Array with surface ids
    self.__fine_nodes = {}                                      # Dictionary of cell classes {id: <FineNode class>}
    self.__fine_nodes_ids = []                                  # Array with fine nodes ids
    self.__fine_nodes_volume = {}                               # Dictionary of fine nodes volume {id: vol}
    self.differentiator = ""

  def __getSurfaces(self):
      region = self.cell.region
      relation = {}
      if isinstance(region, SurfaceSide):
          relation = region.surface.get_surface_relation()
      return relation


  def __getSurfaceAreas(self):
      areas = {}
      
      region = self.cell.region

      if isinstance(region, SurfaceSide):
          surface = self.cell.region.surface
          # if isinstance(surface, InfiniteSquareCylinderZ):
          areas = surface.evaluate_surface_area() 
      else: 
          for s_id in self.surface_ids:
              a = self.surfaces[s_id].evaluate_surface_area()
              areas[s_id] = a
      return areas
  
  def __getSurfaceDirections(self):
    directions = {}

    region = self.cell.region
    if isinstance(region, SurfaceSide):
        surface = self.cell.region.surface
        # if isinstance(surface, InfiniteSquareCylinderZ):
        directions = surface.get_surface_orientation()
    return directions

  def setFineNodes(self, fine_nodes):
    for id_, node in fine_nodes.items():
      self.__fine_nodes[id_] = node
      self.__fine_nodes_volume[id_] = node.cell.volume
      self.__fine_nodes_ids.append(id_)
      
  def getDiagonalRegions(self):
    cell_content = self.__cell.content
    if isinstance(cell_content, Pin):
      # Retrieve levels of the pin
      pin_levels = cell_content.pin_levels


  @property
  def cell(self):
    return self.__cell

  @cell.setter
  def cell(self, new_cell):
    self.__cell = new_cell

  @property
  def id(self):
    return self.__id
  
  @id.setter
  def id(self, id_):
    self.__id = id_

  @property
  def surfaces(self):
    return self.__surfaces

  @property
  def surface_ids(self):
    return self.__surface_ids

  @property
  def surface_areas(self):
    return self.__surface_areas

  @property
  def surface_directions(self):
    return self.__surface_directions

  @property
  def fine_nodes(self):
    return self.__fine_nodes

  @property
  def fine_nodes_ids(self):
    return self.__fine_nodes_ids

  @property
  def fine_nodes_volume(self):
    return self.__fine_nodes_volume
    

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
    

  @property
  def x1_x2(self):
    x1 = self.geometry_info["rectangle_x1"]
    x2 = self.geometry_info["rectangle_x2"]
    return (x1, x2)



