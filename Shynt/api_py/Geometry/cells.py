import os

from Shynt.api_py.Geometry.surfaces import Surface
from Shynt.api_py.Geometry.utilities_geometry import get_all_surfaces_in_a_cell
from Shynt.api_py.materials import Material

from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Geometry.regions import SurfaceSide
from .surfaces import InfiniteSquareCylinderZ, Hexagon, InfiniteRectangleCylinderZ
from .cell_counter import cell_ids


class Cell:

    def __init__(self, name="", fill=None, region=None, universe=None, isClone=False, volume=None):
        """
            Init method of the class

            Parameters
            -------------------------------------------------------------
            name        :   String - name of the cell
            material    :   Material class - Material which the class is filled in
            universe    :   Array of strings - Universes which the cell belongs to
            region      :   Region class - Built by the boolean operation between two
                            or more surface sides.
            -------------------------------------------------------------
        """
        self.__name = name
        self.__region = self.check_region(region)
        self.__content = self.check_fill(fill)        
        self.__universe = universe
        self.__isClone = isClone
        
        
        self.__global_mesh = None
        self.__local_mesh = None
        
        if self.__isClone:
            self.__id = None
        else:
            self.__id = self.calculateId()

        self.__volume = volume

        self.__universe_name_for_gcu = ["u4gcu_", "1"]
        self.__gcu_universes = {}
        
        self.__gcuName = None

        self.__region_syntax = ""
        self.__region_out_syntax = ""

        self.__is_global_node = False
        self.__is_local_node = False


    def calculateId(self):
        """
            Class method to calculate the consecutive id of the cell

            
            Parameters
            ----------------------------------------------------------------
            No parameters
            ----------------------------------------------------------------
        """
        if len(cell_ids) == 0:
            id_ = 1
            cell_ids.append(id_)
            return id_
        else:
            id_ = cell_ids[-1] + 1
            cell_ids.append(id_)
            return id_

    def __calculate_volume(self):
        region = self.__region
        if isinstance(region, Region) and isinstance(region, SurfaceSide):
            # Only surface Side ===> Simple volume of the figure
            surf = region.surface
            side = region.side
            if side == "-":
                vol = surf.evaluate_enclosed_volume()
                return vol
            elif side == "+":
                #area outside the surface
                pass
        elif isinstance(region, Region) and not isinstance(region, SurfaceSide):
            # Regions moderator-like outside of a circle enclosed by a square for example
            child1 = region.child1
            child2 = region.child2
            try:
                # Two Surface sides that contains each other
                assert isinstance(child1,SurfaceSide), "Error calculating cell volume, check source code"
                assert isinstance(child2,SurfaceSide), "Error calculating cell volume, check source code"
                vol1 = child1.surface.evaluate_enclosed_volume()
                vol2 = child2.surface.evaluate_enclosed_volume()
                if child1.encloses(child2):
                    return vol1 - vol2
                elif child2.encloses(child1)                :
                    return vol2 - vol1
            except AssertionError:
                raise SystemError             

    def calculate_surface_area_relation(self):
        relation = {}
        if isinstance(self.__region, SurfaceSide):
            relation = self.__region.surface.evaluate_surface_area()
        self.__surf_area_relation = relation
    
    def getSurface_relation(self):
        relation = {}
        if isinstance(self.__region, SurfaceSide):
            relation = self.__region.surface.getSurface_relation()
        return relation
        
    def check_region(self, reg):
        print_statement = "Argument 'region' must be either of type <class Region> or <class SurfaceSide>"
        if reg is None:
            # it can be defined later
            return None
        assert isinstance(reg, Region) or isinstance(reg, SurfaceSide), print_statement
        return reg

    def check_fill(self, fill):
        from .universes import HexagonalLatticeTypeX, Pin, SquareLattice, Universe
        from .universes import Root, Lattice

        """
            When a cell is filled with a universe check the coordinates 
            of that universe. 
            
            If it is the case of a lattice, translate all the content of the universe 
            to the cell bounded by the surface. The middle of the universe will be used 
            as a reference to fill the surface of the cell.
            
            If it is not a defined universe do not translate anything
        """
        
        if isinstance(fill, Universe):
            #  Here translate content of the universe
            if isinstance(fill, Pin):
                # declare last cell
                fill.close_last_level(self.__region)
            elif isinstance(fill, HexagonalLatticeTypeX):
                x0, y0 = fill.center
                x1, y1 = self.__region.surface.center
                xv = x1 - x0 # translation vector - x
                yv = y1 - y0 # translation vector - y
                fill.translate((xv,yv))
                fill.calculate_enclosed_cells(self.__region)
            elif isinstance(fill, SquareLattice):
                x0, y0 = fill.left_bottom # left bottom corner of lattice
                x1, y1 = self.__region.surface.left_bottom #  center of the enclosing square
                xv = x1 - x0 # translation vector - x
                yv = y1 - y0 # translation vector - y
                fill.translate((xv,yv))
                print("lattice translated")
            elif isinstance(fill, Lattice):
                # Not supported
                raise SystemError
            elif isinstance(fill, Root):
                # Not supported
                raise SystemError
            else:
                # option developed to calculate the regions enclosed
                # by a surface inside a bigger universe

                pass
            return fill
        elif isinstance(fill, Material):
            # the cell is being filled by a material
            return fill
        elif fill == "outside":
            return fill
        elif fill == "void":
            return fill
        return None
    
    def translate(self, trans_vector):
        # translating the surface delimitting the cell 
        surfaces = get_all_surfaces_in_a_cell(self)
        for id_, surf in surfaces.items():
            surf.translate(trans_vector)

    def scale(self, scale_f):
        from .universes import HexagonalLatticeTypeX, SquareLattice
        # self.__region.scale(scale_f)
        cell_surfaces = get_all_surfaces_in_a_cell(self)
        for s_id, surf in cell_surfaces.items():
            surf.scale(scale_f)
        if isinstance(self.__content, SquareLattice):
            self.__content.expand(scale_f)
        elif isinstance(self.__content, HexagonalLatticeTypeX):
            self.__content.expand(scale_f)
        



    def has_global_mesh(self):
        return self.__global_mesh

    def has_local_mesh(self):
        return self.__local_mesh  

    def content_is_material(self):
        if isinstance(self.__content, Material):
            return True
        return False

    def content_is_universe(self):
        from .universes import Universe
        if isinstance(self.__content, Universe):
            return True
        return False
    
    #             self.__content.name: self.__content
    #         }
    #     elif self.content_is_universe():
    #         universe = self.__content
    #         uni_materials = universe.get_universe_materials()
    #         return uni_materials

    def serpent_syntax_cell_with_material_gcu(self, simple_cell):
        """
            This method does not check when the simple_cell is another universe 
            and contains more cells in it
        """
        syntax = ""
        gcu_id = self.calculateId()
        univ_4gcu = "".join(self.__universe_name_for_gcu)
        self.__gcu_universes[simple_cell.id] = univ_4gcu
        simple_cell.gcuName = univ_4gcu
        # print(univ_4gcu)
        self.__universe_name_for_gcu[1] = str(int(self.__universe_name_for_gcu[1]) + 1)

        syntax += f"\ncell {gcu_id} {univ_4gcu} {simple_cell.__content.name}"
        syntax += simple_cell.region.serpent_syntax()

        filled_id = self.calculateId()
        syntax += f"\ncell {filled_id} {self.__content.name} fill {univ_4gcu}"
        syntax += simple_cell.region.serpent_syntax() + "\n"
        return syntax

    def serpent_syntax_gcu(self):
        from .universes import Universe
        syntax = ""
        if isinstance(self.__content, Material):
            """
                This will only happen if a cell with only a material 
                is deliberately asked for the gcu syntax or wether the cell
                has only a material and not another universes
            """
            syntax += self.serpent_syntax_cell_with_material_gcu(self)
        elif isinstance(self.__content, Universe):
            """
                This will be practically always the case
            """
            uni = self.__content
            # print(uni.name)
            for cell in uni.cells.values():
                syntax += self.serpent_syntax_cell_with_material_gcu(cell)
            
            syntax += "\n"
            main_id = self.calculateId()
            syntax += f"cell {main_id} {self.__universe} fill {uni.name} "
            syntax += self.__region.serpent_syntax()
            syntax += "\n"

            syntax += "\n\nset gcu "
            for c_id, gcu in self.__gcu_universes.items():
                syntax += f"{gcu} "
        elif self.__content == "outside":
            syntax += f"outside" 
        return syntax, self.__gcu_universes

    def serpent_syntax(self): 
        from .universes import Universe

        """
            Method to print the cell in the serpent syntax
            It will be printed by material found in the cell

            This is a recursive function the base cases are when
            the cell contains a material or if it is outside cell

        """
        syntax = f"\ncell {self.__id} {self.__universe} "
        
        if isinstance(self.__content, Material):
            syntax += f"{self.__content.name} "
        elif isinstance(self.__content, Universe):
            syntax += f"fill {self.__content.name}" 
        elif self.__content == "outside": 
            syntax += f"outside" 

        
        syntax += self.__region.serpent_syntax()

        # checking if the content is a universe to write that universe' cells
        if isinstance(self.__content, Universe):
            universe = self.__content
            for cell in universe.cells.values():
                syntax += cell.serpent_syntax()
    
        return syntax
 
    def serpent_syntax_pin_cell_inside(self):
        """
            This is used when we want to extract the flux from each cell
        """
        # print(universe.cells)
        syntax = ""
        if isinstance(self.content, Pin):
            pin_uni = self.content
            for id_, cell in pin_uni.cells.items():
                syntax += cell.serpent_syntax()


        return syntax

    def clone(self, new_center_x, new_center_y, clone_vector=None):
        from .universes import Universe

        """
            It makes a copy of the cell with surfaces and cells with
            same ids
        """

        clone_cell = None
        if isinstance(self.__content, Material):
            # The cell only contains a material, so only clone the surface with a new center
            material = self.__content
            # print(self.__region)
            region_clone = self.__region.clone(new_center_x, new_center_y, clone_vector=clone_vector)
            
            clone_cell = Cell(self.__name, region=region_clone, fill=material, isClone=True)
            clone_cell.id = self.__id
            clone_cell.universe = self.__universe
            return clone_cell
        elif isinstance(self.__content, Universe):
            # cloning region -------------------------------------------------------------------
            closing_surface_clone = self.__region.surface.clone(new_center_x, new_center_y, clone_vector=clone_vector)
            closing_region_clone = -closing_surface_clone

            # cloning cells of the universe ----------------------------------------------------
            uni_cells = self.__content.cells
            uni_clone = Universe(name=self.__content.name)
            for c_id, cell in uni_cells.items():
                # print(cell)
                # print(cell.region)

                cell_clone = cell.clone(new_center_x, new_center_y, clone_vector=clone_vector)
                cell_clone.id = c_id
                uni_clone.add_cell(cell_clone)

            # generating new clone cell
            clone_cell = Cell(region=closing_region_clone, fill=uni_clone, isClone=True)
            clone_cell.id = self.__id
            clone_cell.universe = self.__universe
        else:
            raise SystemError
        return clone_cell

    def isPointInside(self, point):
        return self.region.isPointInsideRegion(point)
        

    def __eq__(self, other) -> bool:
        """
            Method to determine if a cell is equal or different to other

            At the moment it only compares the volumes are the same and it has the same material

            #TODO Compare also shape of surfaces and position perhaps
        """
        try:
            assert self.content_is_material
            assert other.content_is_material
        except AssertionError:
            print("It is not possible to compare a cell with universe content")
            raise SystemExit

        try:
            assert self.volume == other.volume
            assert self.content == other.content
            return True
        except AssertionError:
            return False

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        try:
            assert(self.__isClone)
            self.__id = id
        except AssertionError:
            print("Id of non clone cell can not be asigned")
            raise SystemExit

    @property
    def name(self):
        return self.__name
    
    @property
    def content(self):
        return self.__content
    
    @property
    def volume(self):
        if self.__volume is None:
            self.__volume = self.__calculate_volume()
        return self.__volume

    @property
    def surface_area_relation(self):
        return self.__surf_area_relation

    @property
    def universe(self):
        return self.__universe

    @property
    def region(self):
        return self.__region
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @universe.setter
    def universe(self, universe):
        self.__universe = universe
    
    @region.setter
    def region(self, region):
        self.__region = region
    
    @property
    def global_mesh(self):
        return self.__global_mesh

    @global_mesh.setter
    def global_mesh(self, mesh):
        self.__global_mesh = mesh

    @property
    def local_mesh(self):
        return self.__local_mesh

    @local_mesh.setter
    def local_mesh(self, mesh):
        self.__local_mesh = mesh

    @property
    def gcu_universes(self):
        return self.__gcu_universes

    @property
    def gcuName(self):
        return self.__gcuName
    
    @gcuName.setter
    def gcuName(self, gcu):
        self.__gcuName = gcu

    @property
    def center(self):
        if isinstance(self.__region.surface, InfiniteSquareCylinderZ):
            return self.__region.surface.center
        elif isinstance(self.__region.surface, Hexagon):
            return self.__region.surface.center
        elif isinstance(self.__region.surface, InfiniteRectangleCylinderZ):
            return self.__region.surface.center



class CloneCell(Cell):

    def __init__(self, name="", fill=None, region=None, universe=None):
        super().__init__(name, fill, region, universe)


def reset_cell_counter():
    cell_ids = []
    return 0

