from . import surfaces as surf
from .cells import Cell

class Universe(object):
    """
        Universe class
    """
    def __init__(self, name) :
        self.name = name


class Pin(Universe):

    """
        Pin universe composed by concentric cylinders and
        its respective materials
    """
    def __init__(self, name, material=None, radius=False, surroundings=False):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :   A string with the name of the pin universe

            material    :   An object of the class Material corresponding 
                            to the first cylinder level in case of provided
            
            radius      :   An integer corresponding to the radius of the 
                            first cylinder level in case of provided, if it 
                            is False, assumes that is the last material of 
                            the pin, i.e. surroundings of the pin
            ----------------------------------------------------------------
        """
        super().__init__(name)
        self.__pin_levels = []
        self.__outer_most_surface = None
        if material and radius:
            self.add_level(material, radius=radius)
        if surroundings:
            self.add_level(material=surroundings)
    
    def add_level(self, material, radius=False):
        """
            Adds a concentric pin level

            Parameters
            ------------------------------------------------------------------------
            material    :   An object of the class Material

            radius      :   A float, radius of the concentric cylinder 
                            from the center of the first level, if it is False, 
                            assumes that is the last material of the pin, i.e. 
                            surroundings of the pin
            ------------------------------------------------------------------------
        """
        if radius:
            corresponding_cyl =  surf.InfiniteCylinder("cyl_%s"%self.name, 0.0, 0.0, radius)
            surface_limits = []
            if self.__pin_levels == []:
                pass
                surface_limits = -corresponding_cyl
            else:
                surface_limits = +self.__outer_most_surface & -corresponding_cyl
            self.__outer_most_surface = corresponding_cyl
            cell = Cell(
                "cell_%s_%s"%(self.name,len(self.__pin_levels)), 
                material=material,
                universe=self.name,
                region=surface_limits
            )
            self.__pin_levels.append(cell)
        else:
            cell = Cell(
                "cell_%s_%s"%(self.name,len(self.__pin_levels)), 
                material=material,
                universe=self.name,
                region=[
                    # +self.__outer_most_surface if self.__outer_most_surface else None
                ]
            )
            self.__pin_levels.append(cell)

    def getPinLevels(self):
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
                    level["material"].name, 
                    level["radius"]
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
        

    def __create_grid_surfaces(self):
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

    def setArray(self, array):
        self.__array = array
    
    def getArray(self):
        return self.__array
    
    def getPitch(self):
        return self.__pitch

