from Shynt.api_py.Geometry.regions import Region
from collections import namedtuple

# from . import surfaces as 
from .surfaces import *

from Shynt.api_py.materials import Material


"""

"""


class Universe(object):
    """
        Universe class
    """
    def __init__(self, name="", cells=[]) :
        self.__name = name
        self.__cells = cells
        
        
        # Following lines changed to cells.py including the getter and setters methods
        # self.__global_mesh = None
        # self.__local_mesh = None
    
    def mark_cells(self):
        for cell in self.__cells:
            cell.universe = self.__name

    def add_cells(self, *args):
        for cell in args:
            self.__cells.append(cell)
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cells(self):
        return self.__cells



class Root(Universe):


    def __init__(self, cells, energy_grid=None, mcparams=None, libraries=""):
        super().__init__(name="0", cells=cells)
        self.energy_grid = energy_grid  # Grid type
        self.mcparams = mcparams        # MontecarloParams type
        self.libraries = libraries      # Libraries for Serpent
        self.add_universe_to_cells()
    
    def add_universe_to_cells(self):
        for cell in self.cells:
            cell.universe = self.name



class Pin(Universe):

    """
        Pin universe composed by concentric cylinders and
        its respective materials

    """
    def __init__(self, name="", material=None, radius=None, surroundings=None):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :   A string with the name of the pin universe

            material    :   An object or a list of objects of class Meterial 
                            corresponding to the cylinder levels of the pincell
                            in case of provided
            
            radius      :   An number or a lis of numbers corresponding to the 
                            radius of the  levels of the fuel pin universe.
            ----------------------------------------------------------------
        """
        super().__init__(name)
        self.__pin_levels = [] # These are the cells of the universe Pin
        self.__materials = []
        self.__cells = []
        self.__outer_most_surface = None
        self.__last_region = None
        self.__check_init_levels(material, radius, surroundings)
        # print(self.__pin_levels)
        
    
    def __check_init_levels(self, mat, radius, surroundings):
        if mat and radius:
            if isinstance(mat, Material) and (isinstance(radius, float) or isinstance(radius, int)):
                self.add_level(mat, radius)
                if surroundings:
                    self.add_surroundings(surroundings)
            else:
                try:
                    assert(isinstance(mat, list) and isinstance(radius, list))
                    if len(mat) != len(radius):
                        print(f"*** Error while difining either materials or radius for pin '{self.__name}'")
                        print("material and radius arrays must have the same length")
                        raise SystemExit
                    for m in range(len(mat)):
                        self.add_level(mat[m], radius[m])
                    if surroundings:
                        self.add_surroundings(surroundings)
                except AssertionError:
                    print(f"*** Error while difining either materials or radius for pin '{self.__name}'")
                    print("material and radius must be introduced in an array")
                    raise SystemExit
        else:
            print("--- Warning --- Do not forget to declare the levels for the pin")
        
    def add_surroundings(self, material):
        self.add_level(material)        

    def add_level(self, material, radius=None):
        """
            Adds a concentric pin level

            Parameters
            ------------------------------------------------------------------------
            material    :   An object of the class Material

            radius      :   A float or integer, radius of the concentric cylinder 
                            from the center of the first level, if it is False, 
                            assumes that is the last material of the pin, i.e. 
                            surroundings of the pin
            ------------------------------------------------------------------------
        """
        from .cells import Cell
        if material not in self.__materials:
            self.__materials.append(material)

        Level = namedtuple("Level", ["cell", "radius"])
        corresponding_cyl = None
        if radius:
            corresponding_cyl =  InfiniteCylinderZ(0.0, 0.0, radius)
            if len(self.__pin_levels) == 0:
                self.__last_region = -corresponding_cyl # SurfaceSide type
            else:
                self.__last_region = +self.__outer_most_surface & -corresponding_cyl  # Region type
            self.__outer_most_surface = corresponding_cyl
            cell = Cell(
                "%s_level_%s"%(self.name,len(self.__pin_levels)), 
                fill=material,
                region=self.__last_region,
                universe=self.name
            )
            self.__cells.append(cell)
            
            level = Level(cell, radius)
            self.add_cells(cell)
            self.__pin_levels.append(level)
        else:
            cell_region = +self.__outer_most_surface if self.__outer_most_surface else None
            cell = Cell(
                "%s_level_%s"%(self.name,len(self.__pin_levels)), 
                fill=material,
                region=cell_region,
                universe=self.name
            )
            level = Level(cell, None)
            self.add_cells(cell)
            self.__pin_levels.append(level)

    def close_last_level(self, region): #region
        last_level = self.__pin_levels[-1].cell
        # Closing the last region, normally the coolant:
        last_level_region = last_level.region & region 
        self.__pin_levels[-1].cell.region = last_level_region
    
    def add_pin_levels(self, materials, radius):
        """
            Setter method for attribute self.__pin_levels

            Params
            -------------------
            levels      |   
        """
        try:
            assert len(materials) == len(radius)
            for i in range(len(materials)):
                self.add_level(materials[i], radius[i])
        except AssertionError:
            print("**** Error in adding levels, materials and radius arrays must have the same length ****")
            raise SystemExit


    def replicate(self):
        materials = []
        radius = []
        for level in self.__pin_levels:
            materials.append(level.cell.content)
            radius.append(level.radius)
        replica = Pin(self.name, material=materials, radius=radius)
        return replica

    def translate(self, dx, dy):
        for level in self.__pin_levels:
            pin_cell = level.cell
            if isinstance(pin_cell.region, SurfaceSide):
                pin_cell.region.surface.translate(dx, dy)
            elif isinstance(pin_cell.region, Region):
                pin_cell.region.child2.surface.translate(dx, dy)
            
    def get_center(self):
        first_level = self.__pin_levels[0]
        return first_level.cell.region.surface.center

    def serpent_pin_syntax(self):
        syntax = f"pin {self.name}\n"
        for l in self.__pin_levels:
            mat_name = l.cell.content.name
            if l.radius:
                syntax += "%s %E \n"%(mat_name, l.radius)
            else:
                syntax += f"{mat_name}\n\n"
        return syntax

    def serpent_cell_syntax(self):
        syntax = ""
        for l in self.__pin_levels:
            text = l.cell.serpent_syntax()
            syntax += text
        syntax += "\n"    

        return syntax

    @property
    def pin_levels(self):
        """
            Getter method for attribute self.__pin_levels
        """
        return self.__pin_levels

    @property
    def cells(self):
        return [level.cell for level in self.__pin_levels]

    @property
    def materials(self):
        return self.__materials
        
    def __str__(self):
        """
            __str__ method to print the class
        """
        pin_levels_str = [
            """
                level %s:
                + material: %s
                + radius:   %s
            """ %(
                    self.__pin_levels.index(level),
                    level.cell.content.name, 
                    level.radius
                ) for level in self.__pin_levels
        ]
        return """
        Pin universe
        - name: %s
        - pin levels:
            %s
        """%(self.name, "".join(pin_levels_str))

    def __eq__(self, other) -> bool:
        """
            A pin is only equal to other when they have the same number
            of levels and the materials and radius in each level are similar
        """
        if len(self.__pin_levels) == len(other.pin_levels):
            # check that the levels are the same
            for i in range(len(self.__pin_levels)):
                self_level = self.__pin_levels[i]
                other_level = other.pin_levels[i]
                if self_level.cell.content != other_level.cell.content or self_level.radius != other_level.radius:
                    return False
            return True
        
        return False


class SquareLattice(Universe):
    """
        Square lattice universe composed by an array of fuel pins
        or universes

    """

    def __init__(self, name, left_bottom, pitch, array):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :   A string with the name of lattice universe

            pitch       :   Pitch of the assembly
            
            array       :   lattice array
            ----------------------------------------------------------------
        """
        super().__init__(name)
        self.__left_bottom = left_bottom
        self.__pitch = pitch
        self.__array = array
        self.__check_rows_cols()
        self.__ny = len(array)
        self.__nx = len(array[0])
        self.__pin_types = self.__get_different_pins()
        self.__num_pin_types = len(self.__pin_types)
        self.__create_cells()
        
    def __create_cells(self):
        from .cells import Cell

        num_rows = len(self.__array)
        num_cols = len(self.__array[0])
        new_array = [[0 for i in range(num_cols)] for j in range(num_rows)]

        for r in range(num_rows):
            dy = (num_rows-1-r+0.5)*self.__pitch + self.__left_bottom[1]
            for p in range(num_cols):
                dx = (p+0.5)*self.__pitch + self.__left_bottom[0]
                # create a pin with the same characteristics to move the cell
                pin_replacement = self.__array[r][p].replicate()

                # moving the pin
                pin_replacement.translate(dx, dy)
                
                # new_center
                new_center_x, new_center_y = pin_replacement.get_center()
                
                closing_surface = InfiniteSquareCylinderZ(new_center_x, new_center_y, self.__pitch*0.5)

                
                new_pin = Cell(region=-closing_surface, fill=pin_replacement)
                new_array[r][p] = new_pin

        self.array = new_array

    def __create_grid_surfaces(self):
        """
            Method to create the surfaces enclosing one
            pin cell for every pin in the lattice
        """
        
        pass

    def __create_lattice_surface(self):
        """
            Method to create the surfaces enclosing the lattice
            
        """
        square_side = 2 * self.__pitch
        surf = InfiniteSquareCylinderZ()
        pass

    def __check_rows_cols(self):
        init_num_cols = len(self.__array[0])
        for row in self.__array:
            try:
                assert(len(row) == init_num_cols)
            except AssertionError:
                print("****** error ******")
                print("All rows of square lattice must have equal number of pin elements")
            
    def __get_different_pins(self):
        types = []
        for row in self.__array:
            for pin in row:
                if pin.name not in types:
                    types.append(pin.name)
        return types

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, array):
        self.__array = array
    
    @property
    def nx(self):
        return self.__nx
    
    @property
    def ny(self):
        return self.__ny

    @property
    def pitch(self):
        return self.__pitch

