from Shynt.api_py.materials import Material
from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Geometry.regions import SurfaceSide

class Cell:

    def __init__(self, name, material=None, region=None):
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
        self.__material = self.checkMaterial(material)
        self.__region = self.checkRegion(region)
        self.__universe = None

    
    def __str__(self):
        return """Cell %s
        - filled with material: %s
        - region: %s
        """%(self.__name, self.__material, self.__region)

    def checkMaterial(self, mat):
        assert isinstance(mat, Material), "The parameter 'material' must be an instance of class Material"
        return mat            

    def checkRegion(self, reg):
        print_statement = "Argument 'reg' must be either of type <class Region> or <class SurfaceSide>"
        assert isinstance(reg, Region) or isinstance(reg, SurfaceSide), print_statement
        return reg
    
    @property
    def name(self):
        return self.__name
    
    @property
    def material(self):
        return self.__material
    
    @property
    def universe(self):
        return self.__universe
    
    @property
    def region(self):
        return self.__region
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @material.setter
    def material(self, material):
        self.__material = material
    
    @universe.setter
    def universe(self, universe):
        self.__universe = universe
    
    @region.setter
    def region(self, region):
        self.__region = region
    

