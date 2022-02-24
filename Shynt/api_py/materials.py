
class Material:

    def __init__(self, name, atom_density=None, mass_density=None, moder=""):
        self.__name = name
        self.__isotopes = []
        self.__mass_density = mass_density
        self.__atom_density = atom_density
        self.__moderLibrary = None
        if moder != "":
            self.__moderLibrary = moder
            
        

    def addIsotope(self, isotope, mass_fraction=None, atom_fraction=None,
        ):
        try:
            assert (isinstance(isotope, Isotope))
            new_isotope = Isotope(isotope.name)
            new_isotope.mass_fraction = mass_fraction
            new_isotope.atom_fraction = atom_fraction
            self.__isotopes.append(new_isotope)
        except AssertionError:
            print(" **** Error ***** Parameter 'isotope' must be of class Isotope")
            raise SystemExit
    
    def isFuel(self):
        for iso in self.__isotopes:
            serpent_id = iso.name
            zaid = int(serpent_id.split(".")[0])
            if zaid >= 90000:
                return True
        return False

    def __str__(self):
        return_statement = "%s\n"%self.__name
        return_statement += "\t- atom density: %s\n"%self.__atom_density
        return_statement += "\t- mass density: %s \n"%self.__mass_density
        return_statement += "\t- isotopes: \n"
        for iso in self.__isotopes:
            return_statement += "\t\t%s\n"%iso
        return return_statement
    
    def __eq__(self, other) -> bool:
        if self.__name == other.name:
            return True
        return False

    @property
    def serpent_syntax(self):
        syntax = f"mat {self.__name} "
        if self.__mass_density:
            syntax += f"-{self.__mass_density} "
        elif self.__atom_density:
            syntax += f"{self.__atom_density} "
        if self.__moderLibrary:
            syntax += f"moder {self.__moderLibrary}"
        
        syntax += "\n"
        for isotope in self.__isotopes:
            syntax += isotope.serpent_syntax()
        syntax += "\n\n"

        return syntax

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
        return self.__isotopes
    
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

    def serpent_syntax(self):
        syntax = f"{self.name} "
        if self.__atom_fraction:
            syntax += f"{self.__atom_fraction}\n"
        elif self.__mass_fraction:
            syntax += f"-{self.__mass_fraction}\n"
        return syntax

    
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
