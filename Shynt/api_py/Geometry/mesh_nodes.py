from typing import Dict
import numpy as np

from Shynt.api_py.Geometry.universes import Pin
from Shynt.api_py.Geometry.regions import SurfaceSide
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype, InfiniteHexagonalCylinderYtype, InfiniteSquareCylinderZ

class Node:

    def __init__(self) -> None:
        pass

class CoarseNode(Node):

    def __init__(self, cell) -> None:
        super().__init__()
        self.__cell = cell
        
        
        self.__surfaces = self.__getSurfaces()                      # Dictionary of surface classes {id: <Surface class>}
        self.fictional_surfaces = self.__getFictionalSurfaces()
        self.__surface_ids = list(self.__surfaces.keys())           # Array with surface ids
        self.__surface_areas = self.__getSurfaceAreas()             # Dictionary of surfaces areas {id: area}
        self.__surface_directions = self.__getSurfaceDirections()   # Dictionary with the direction of the surfaces
        self.__fine_nodes = {}                                      # Dictionary of cell classes {id: <FineNode class>}
        self.__fine_nodes_ids = []                                  # Array with fine nodes ids
        self.__fine_nodes_volume = {}                               # Dictionary of fine nodes volume {id: vol}


    def __getSurfaces(self):
        region = self.cell.region
        relation = {}
        if isinstance(region, SurfaceSide):
            relation = region.surface.get_surface_relation()
        return relation

    def __getFictionalSurfaces(self) -> Dict:
        coarse_node_region = self.cell.region

        # Doing that with the closing surfaces, 
        # the surfaces inside the cell will be fictional surfaces
        # of the FineNode
        closing_surface = self.__cell.region.surface
        if isinstance(closing_surface, InfiniteSquareCylinderZ):
            return closing_surface.get_fictional_surfaces()
        elif isinstance(closing_surface, InfiniteHexagonalCylinderXtype):
            raise SystemError
        elif isinstance(closing_surface, InfiniteHexagonalCylinderYtype):
            raise SystemError

    def __getSurfaceAreas(self):
        areas = {}
        
        region = self.cell.region

        if isinstance(region, SurfaceSide):
            surface = self.cell.region.surface
            if isinstance(surface, InfiniteSquareCylinderZ):
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
            if isinstance(surface, InfiniteSquareCylinderZ):
                directions = surface.get_surface_orientation()
        return directions

    def setFineNodes(self, fine_nodes):
        for id_, node in fine_nodes.items():
            self.__fine_nodes[id_] = node
            self.__fine_nodes_volume[id_] = node.cell.volume
            self.__fine_nodes_ids.append(id_)
        

    @property
    def cell(self):
        return self.__cell

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
    
        
class FineNode(Node):

    def __init__(self, cell) -> None:
        super().__init__()
        self.__cell = cell
        self.from_coarse_node = None
    
    @property
    def cell(self):
        return self.__cell