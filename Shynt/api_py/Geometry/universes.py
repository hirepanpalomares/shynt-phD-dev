from . import surfaces as surf
from .cells import Cell
from Shynt.api_py.materials import Material
from collections import namedtuple

"""

    # TODO:
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
        self.__outer_most_surface = None
        self.__check_init_levels(material, radius, surroundings)
        
    
    def __check_init_levels(self, mat, radius, surroundings):
        if isinstance(mat, Material) and (isinstance(radius, float) or isinstance(radius, int)):
            self.add_level(mat, radius)
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
                    self.add_level(surroundings)
            except AssertionError:
                print(f"*** Error while difining either materials or radius for pin '{self.__name}'")
                print("material and radius must be introduced in an array")
                raise SystemExit
        pass
    
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
        Level = namedtuple("Level", ["cell", "radius"])
        if radius:
            corresponding_cyl =  surf.InfiniteCylinderX(0.0, 0.0, radius)
            surface_limits = None
            if len(self.__pin_levels) == 0:
                surface_limits = -corresponding_cyl
            else:
                surface_limits = +self.__outer_most_surface & -corresponding_cyl
            self.__outer_most_surface = corresponding_cyl
            cell = Cell(
                "cell_%s_%s"%(self.name,len(self.__pin_levels)), 
                fill_material=material,
                region=surface_limits
            )
            level = Level(cell, radius)
            self.add_cells(cell)
            self.__pin_levels.append(level)
        else:
            cell_region = +self.__outer_most_surface if self.__outer_most_surface else None
            cell = Cell(
                "cell_%s_%s"%(self.name,len(self.__pin_levels)), 
                fill_material=material,
                region=cell_region
            )
            level = Level(cell, None)
            self.add_cells(cell)
            self.__pin_levels.append(level)

    @property
    def pin_levels(self):
        """
            Getter method for attribute self.__pin_levels
        """
        return self.__pin_levels
    
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
                    level.cell.material.name, 
                    level.radius
                ) for level in self.__pin_levels
        ]
        return """
        Pin universe
        - name: %s
        - pin levels:
            %s
        """%(self.name, "".join(pin_levels_str))


class SquareLattice(Universe):
    """
        Square lattice universe composed by an array of fuel pins
        or universes
    """

    def __init__(self, name, pitch, array):
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
        self.__pitch = pitch
        self.__array = array
        self.__check_rows_cols()
        self.__ny = len(array)
        self.__nx = len(array[0])
        self.__pin_types = self.__calculate_different_pins()
        self.__num_pin_types = len(self.__pin_types)
        self.__create_grid_surfaces()
        self.__create_lattice_surface()

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
        pass

    def __check_rows_cols(self):
        init_num_cols = len(self.__array[0])
        for row in self.__array:
            try:
                assert(len(row) == init_num_cols)
            except AssertionError:
                print("****** error ******")
                print("All rows of square lattice must have equal number of pin elements")
            
    def __calculate_different_pins(self):
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
    def pitch(self):
        return self.__pitch

