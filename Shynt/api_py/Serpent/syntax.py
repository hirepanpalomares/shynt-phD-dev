from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Geometry.surfaces import PlaneX, Surface
from Shynt.api_py.Geometry.universes import Universe

import Shynt.api_py.Geometry.surfaces as surf_types



class SerpentSyntax:

    def __init__(self, item) -> None:
        self.__item = item
        self.item_syntax = None
        self.__process_item()
    
    def __process_item(self):
        if isinstance(self.__item, Universe):
            self.__process_universe()
        elif isinstance(self.__item, Cell):
            self.__process_cell()
        elif isinstance(self.__item, Surface):
            self.__process_surface()
        elif isinstance(self.__item, Region):
            self.__process_region()
    
    def __process_universe(self):
        pass

    def __process_cell(self):
        pass

    def __process_region(self):
        pass

    def __process_surface(self):
        if isinstance(self.__item, surf_types.PlaneX):
            pass
        elif isinstance(self.__item, surf_types.PlaneY):
            pass
        elif isinstance(self.__item, surf_types.PlaneZ):
            pass
        elif isinstance(self.__item, surf_types.InfiniteCylinderX):
            pass
        elif isinstance(self.__item, surf_types.InfiniteCylinderY):
            pass
        elif isinstance(self.__item, surf_types.InfiniteCylinderZ):
            pass
        elif isinstance(self.__item, surf_types.InfiniteSquareCylinderZ):
            pass
        elif isinstance(self.__item, surf_types.InfiniteHexagonalCylinderXtype):
            pass
        elif isinstance(self.__item, surf_types.InfiniteHexagonalCylinderYtype):
            pass