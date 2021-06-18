

class Material:

    def __init__(self, name, moder=""):
        self.name = name
        self.__Isotopes = []
        self.__massDensity = None
        self.__atomDensity = None
        if moder == "":
            self.__moderLibrary = None
        else:
            self.__moderLibrary = moder

    def  addIsotope(self, isotope, mass_fraction=None, atom_fraction=None):
        try:
            assert (type(isotope) == Isotope)
            self.__Isotopes.append({
                "isotope": isotope,
                "mass_fraction": mass_fraction,
                "atom_fraction": atom_fraction
            })
        except AssertionError:
            print(" **** Error ***** Parameter 'isotope' must be of class Isotope")
            raise SystemExit
    
    def setMassDensity(self, value):
        self.__massDensity = value
    
    def setAtomDensity(self, value):
        self.__atomDensity = value
    
    def setModerLibrary(self, value):
        self.__moderLibrary = value
    
    def getName(self):
        return self.name

    def getMassDensity(self):
        return self.__massDensity
    
    def getAtomDensity(self):
        return self.__atomDensity
    
    def getIsotopes(self):
        return self.__Isotopes
    
    def getModerLibrary(self):
        return self.__moderLibrary


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
    


    def setTemperature(self, value):
        self.__temperature = value
    
    def getTemperature(self):
        return self.__temperature 
    
  
    
