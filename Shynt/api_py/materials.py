
class Material:

    def __init__(self, name, atom_density=None, mass_density=None, moder="", composition=None, options=""):
        self.__name = name
        if composition is None:
            self.__composition = {"fractions":[], "type":""}
        else:
            self.__composition = composition
        self.__isotopes = {}
        self.__fractions = {}
        self.__options = options
        self.__mass_density = mass_density
        self.__atom_density = atom_density
        self.__moderLibrary = None
        if moder != "":
            self.__moderLibrary = moder
        self.__check_composition()
    
    def __check_composition(self):
        array_isos = self.__composition["fractions"]
        type_dens = self.__composition["type"]
        try:
            for item in array_isos:
                iso, density = item
                assert (isinstance(iso, Isotope))
                self.__isotopes[iso.name] = iso
                self.__fractions[iso.name] = density
        except AssertionError:
            print(" **** Error ***** Parameter 'isotope' must be of class Isotope")
            raise SystemExit

    def addIsotope(self, isotope, mass_fraction=None, atom_fraction=None, atom_density=None):
        try:
            assert (isinstance(isotope, Isotope))
            self.__isotopes[isotope.name] = isotope
            if mass_fraction is not None:
                if self.__composition["type"] == "":
                    self.__composition["type"] = "mass_fraction"
                assert self.__composition["type"] == "mass_fraction"
                self.__fractions[isotope.name] = mass_fraction
            elif atom_fraction is not None:
                if self.__composition["type"] == "":
                    self.__composition["type"] = "atom_fraction"
                assert self.__composition["type"] == "atom_fraction"
                self.__fractions[isotope.name] = atom_fraction
            elif atom_density is not None:
                if self.__composition["type"] == "":
                    self.__composition["type"] = "atom_density"
                assert self.__composition["type"] == "atom_density"
                self.__fractions[isotope.name] = atom_fraction
        except AssertionError:
            print(" **** Error ***** Parameter 'isotope' must be of class Isotope")
            raise SystemExit
    
    def __str__(self):
        return_statement = "%s\n"%self.__name
        return_statement += "\t- atom density: %s\n"%self.__atom_density
        return_statement += "\t- mass density: %s \n"%self.__mass_density
        return_statement += "\t- isotopes: \n"
        for iso in self.__isotopes:
            return_statement += "\t\t%s\n"%iso
        return return_statement
    
    def __eq__(self, other) -> bool:
        try:
            assert self.__name == other.name
            for iso, density in self.__fractions.items():
                assert density == other.fractions[iso]
            return True
        except AssertionError:
            return False
        except KeyError:
            return False


    @property
    def isFuel(self):
        for iso_name, iso in self.__isotopes.items():
            serpent_id = iso_name
            zaid = serpent_id.split(".")[0]
            if zaid.isnumeric():
                if int(zaid) >= 90000:
                    return True
        return False

    @property
    def serpent_syntax(self):
        syntax = f"mat {self.__name} "
        if self.__mass_density:
            syntax += f"-{self.__mass_density} "
        elif self.__atom_density:
            syntax += f"{self.__atom_density} "
        else:
            syntax += f"{self.__options}"
        if self.__moderLibrary:
            syntax += f"moder {self.__moderLibrary}"
        
        syntax += "\n"
        for iso, number in self.__fractions.items():
            syntax += iso
            if self.__composition["type"] == "atom_density":
                syntax += f" {number}"
            elif self.__composition["type"] == "atom_fraction":
                syntax += f" {number}"
            elif self.__composition["type"] == "mass_fraction":
                syntax += f" -{number}"
            syntax += "\n"
        return syntax

    @property
    def name(self):
        return self.__name

    @property
    def fractions(self):
        return self.__fractions

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
        self.__temperature = None

    def serpent_syntax(self):
        syntax = f"{self.name} "
        
        return syntax

    def __eq__(self, __o: object) -> bool:
        try:
            assert self.name == __o.name
        except AssertionError:
            return False
    
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
