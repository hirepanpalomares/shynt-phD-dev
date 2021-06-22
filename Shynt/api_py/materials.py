
class Material:

    def __init__(self, name, moder=""):
        self.__name = name
        self.__Isotopes = []
        self.__mass_density = None
        self.__atom_density = None
        if moder == "":
            self.__moderLibrary = None
        else:
            self.__moderLibrary = moder

    def addIsotope(self, isotope, mass_fraction=None, atom_fraction=None,
        ):
        try:
            assert (type(isotope) == Isotope)
            isotope.mass_fraction = mass_fraction
            isotope.atom_fraction
            self.__Isotopes.append(isotope)
        except AssertionError:
            print(" **** Error ***** Parameter 'isotope' must be of class Isotope")
            raise SystemExit
    
    def __str__(self):
        return_statement = "%s\n"%self.__name
        return_statement += "\t- atom density: %s\n"%self.__atom_density
        return_statement += "\t- mass density: %s \n"%self.__mass_density
        return_statement += "\t- isotopes: \n"
        for iso in self.__Isotopes:
            return_statement += "\t\t%s\n"%iso
        return return_statement
    
    @property
    def name(self):
        return self.__name

    @property
    def mass_density(self):
        return self.__massDensity
    
    @property
    def atom_density(self):
        return self.__atomDensity
    
    @property
    def isotopes(self):
        return self.__Isotopes
    
    @property
    def moder_library(self):
        return self.__moderLibrary

    @name.setter
    def name(self, value):
        self.__name = value

    @mass_density.setter
    def mass_density(self, value):
        self.__massDensity = value
    
    @atom_density.setter
    def atom_density(self, value):
        self.__atomDensity = value
    
    @moder_library.setter
    def moder_library(self, value):
        self.__moderLibrary = value
    

class Isotope:

    def __init__(self, name):
        try:
            assert(name != "")
            self.name = name
        except AssertionError:
            print(" **** Error **** Isotope must have valid parameter name")
            raise SystemExit
        self.__mass_fraction = None
        self.__atom_fraction = None
        self.__temperature = None
        self.__atom_density = None
    
    def __str__(self):
        return "%s"%self.name

    @property
    def temperature(self):
        return self.__temperature 

    @property
    def mass_fraction(self):
        return self.__mass_fraction
    
    @property
    def atom_fraction(self):
        return self.__atom_fraction
    
    @property
    def atom_density(self):
        return self.__atom_density
    
    @temperature.setter
    def temperature(self, value):
        self.__temperature = value
  
    @mass_fraction.setter
    def mass_fraction(self, value):
        self.__mass_fraction = value
    
    @atom_fraction.setter
    def atom_fraction(self, value):
        self.__atom_fraction = value

    @atom_density.setter
    def atom_density(self, value):
        self.__atom_density = value
