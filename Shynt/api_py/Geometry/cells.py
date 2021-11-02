# from Shynt.api_py.Geometry.universes import Pin
from Shynt.api_py.materials import Material


# from Shynt.api_py.Geometry.regions import Region
# from Shynt.api_py.Geometry.regions import SurfaceSide
from .regions import *
from .surfaces import *
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
        self.__id = None
        self.calculateId()

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
            id = None
            with open("cell-counter", "r") as fileCounter:
                for line in fileCounter:
                    id = int(line.split()[0]) + 1
                    self.__id = id
                    break
            with open("cell-counter", "w") as fileCounter:
                fileCounter.write(str(id))
            
        except FileNotFoundError:
            self.__id = 1
            with open("cell-counter", "w") as fileCounter:
                fileCounter.write("1")

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
    

    def serpent_syntax(self):
        """
            Method to print the cell in the serpent syntax 

            Parameters
            -----------------------------------------------
                - u :   Universe what the cell belongs to
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

        side = lambda s: s if s == "-" else ""
        # For the regions:
        if isinstance(self.__region, SurfaceSide):
            syntax += f" {side(self.__region.side)}{self.__region.surface.id}"
        elif isinstance(self.__region, Region):
            # find the surfaces sides of the Region
            surfaces_sides = destructure_region(self.__region)
            for surf_side in surfaces_sides:
                syntax += f" {side(surf_side.side)}{surf_side.surface.id}"
        syntax += ""

        # checking if the content is a universe to declare that universe' cells
        if isinstance(self.__content, Universe):
            syntax += self.serpent_syntax_universe_cells(self.__content)
    
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



def reset_cell_counter():
    try:
        os.remove("cell-counter")
    except FileNotFoundError:
        pass
