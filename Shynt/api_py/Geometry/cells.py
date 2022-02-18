import os

from json.tool import main
from Shynt.api_py.Geometry.surfaces import Surface
from Shynt.api_py.materials import Material


from Shynt.api_py.Geometry.regions import Region, destructure_region
from Shynt.api_py.Geometry.regions import SurfaceSide
from .universes import Pin, Universe


class Cell:

    def __init__(self, name="", fill=None, region=None, universe=None):
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
        
        
        self.__global_mesh = None
        self.__local_mesh = None
        

        self.__id = self.calculateId()
        self.__volume = None

        self.__universe_name_for_gcu = ["u4gcu_", "1"]
        self.__gcu_universes = []
        
        self.__gcuName = None

        self.__region_syntax = ""
        self.__region_out_syntax = ""

        self.__is_global_node = False
        self.__is_local_node = False


    def calculateId(self):
        """
            Class method to calculate the consecutive id of the cell

            It generates a file with a single line where the number
            of created cells is updated every time the user calls
            this class.

            Parameters
            ----------------------------------------------------------------
            No parameters
            ----------------------------------------------------------------
        """
        try:
            id_ = None
            with open("cell-counter", "r") as fileCounter:
                for line in fileCounter:
                    id_ = int(line.split()[0]) + 1
                    break
            with open("cell-counter", "w") as fileCounter:
                fileCounter.write(str(id_))
            return id_
            
            
        except FileNotFoundError:
            with open("cell-counter", "w") as fileCounter:
                fileCounter.write("1")
            id_ = 1
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
                raise SystemExit                

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
        assert isinstance(reg, Region) or isinstance(reg, SurfaceSide), print_statement
        return reg

    def check_fill(self, fill):
        # TODO: When a cell is filled with a universe check the coordinates of that universe. Translate all the content of the universe to the cell bounded by the surface
        if isinstance(fill, Universe):
            #  Here translate content of the universe
            if isinstance(fill, Pin):
                # declare last cell
                fill.close_last_level(self.__region)
            return fill
        elif isinstance(fill, Material):
            # the cell is being filled by a material
            return fill
        elif fill == "outside":
            return fill
        return None
    
    def has_global_mesh(self):
        return self.__global_mesh

    def has_local_mesh(self):
        return self.__local_mesh  

    def content_is_material(self):
        if isinstance(self.__content, Material):
            return True
        return False

    def content_is_universe(self):
        if isinstance(self.__content, Universe):
            return True
        return False
    
    def serpent_syntax_cell_with_material_gcu(self, simple_cell):
        """
            This method does not check when the simple_cell is another universe 
            and contains more cells in it
        """
        syntax = ""
        gcu_id = self.calculateId()
        univ_4gcu = "".join(self.__universe_name_for_gcu)
        self.__gcu_universes.append(univ_4gcu)
        simple_cell.gcuName = univ_4gcu
        # print(univ_4gcu)
        self.__universe_name_for_gcu[1] = str(int(self.__universe_name_for_gcu[1]) + 1)

        syntax += f"\ncell {gcu_id} {univ_4gcu} {simple_cell.__content.name}"
        syntax += self.serpent_syntax_region(simple_cell.region)

        filled_id = self.calculateId()
        syntax += f"\ncell {filled_id} {self.__content.name} fill {univ_4gcu}"
        syntax += self.serpent_syntax_region(simple_cell.region) + "\n"
        return syntax

    def serpent_syntax_gcu(self):
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
            for cell in uni.cells:
                syntax += self.serpent_syntax_cell_with_material_gcu(cell)
            
            syntax += "\n"
            main_id = self.calculateId()
            syntax += f"cell {main_id} {self.__universe} fill {uni.name} "
            syntax += self.serpent_syntax_region(self.__region)
            syntax += "\n"

            outside_id = self.calculateId()
            outside_reg = self.__region.invert()
            syntax += f"cell {outside_id} {self.__universe} outside"
            syntax += self.serpent_syntax_region(outside_reg)
            syntax += "\n\nset gcu "
            for gcu in self.__gcu_universes:
                syntax += f"{gcu} "
        elif self.__content == "outside":
            syntax += f"outside" 
        return syntax

    def serpent_syntax(self):
        """
            Method to print the cell in the serpent syntax 
            It will be printed by material found in the cell


            Parameters
            -----------------------------------------------
                - gcu :   It is when the xs generation is needed
            -----------------------------------------------
        """
        syntax = f"\ncell {self.__id} {self.__universe} "
        
        # for the content of the cell
        if isinstance(self.__content, Material):
            syntax += f"{self.__content.name} "
        elif isinstance(self.__content, Universe):
            syntax += f"fill {self.__content.name}" 
        elif self.__content == "outside":
            syntax += f"outside" 

        
        syntax += self.serpent_syntax_region(self.__region)

        # checking if the content is a universe to declare that universe' cells
        if isinstance(self.__content, Universe):
            syntax += self.serpent_syntax_universe_cells(self.__content)
    
        return syntax

    def serpent_syntax_region(self, reg):
        syntax = ""
        side = lambda s: s if s == "-" else ""
        # For the regions:
        if isinstance(reg, SurfaceSide):
            syntax += f" {side(reg.side)}{reg.surface.id}"
        elif isinstance(reg, Region):
            # find the surfaces sides of the Region
            surfaces_sides = destructure_region(reg)
            for surf_side in surfaces_sides:
                syntax += f" {side(surf_side.side)}{surf_side.surface.id}"
        syntax += ""
        return syntax

    def serpent_syntax_universe_cells(self, universe):
        # print(universe.cells)
        syntax = ""
        for cell in universe.cells:
            syntax += cell.serpent_syntax()
        return syntax
        
    def __str__(self):
        print_statement = ""
        print_statement += "Cell: %s:\n"%self.__name
        if self.content_is_material():
            print_statement += "\t- filled with material: %s\n"%self.__content
        elif self.content_is_universe():
            print_statement += "\t- filled with universe: %s\n"%self.__content
        print_statement += "\t- region: %s\n\n\n"%self.__region

        return print_statement
    
    def __eq__(self, other) -> bool:
        """
            Method to determine if a cell is equal or different to other

        """
        pass

    @property
    def id(self):
        return self.__id

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


def reset_cell_counter():
    try:
        os.remove("cell-counter")
    except FileNotFoundError:
        pass

