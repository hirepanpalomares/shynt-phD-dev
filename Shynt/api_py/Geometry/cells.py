from Shynt.api_py.materials import Material
from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Geometry.regions import SurfaceSide

class Cell:

    def __init__(self, name, fill_material=None, region=None, fill_universe=None, universe=None):
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
        self.__filled_material = self.checkMaterial(fill_material)
        self.__region = self.checkRegion(region)
        self.__filled_universe = fill_universe
        self.__universe = universe
        
        self.__global_mesh = None
        self.__local_mesh = None

    
    def __str__(self):
        print_statement = ""
        if self.__filled_universe:
            print_statement = """Cell %s
            - filled with material: %s
            - filled with universe: %s
            - region: %s
            """%(self.__name, self.__filled_material, self.__filled_universe.name, self.__region)
            return print_statement
        else:
            print_statement = """Cell %s
            - filled with material: %s
            - filled with universe: %s
            - region: %s
            """%(self.__name, self.__filled_material, self.__filled_universe, self.__region)
            return print_statement

    def checkMaterial(self, mat):
        if isinstance(mat, Material):
            # the cell is being filled by a material
            pass
        else:
            # the cell is being filled by a universe
            pass
        return mat            

    def checkRegion(self, reg):
        print_statement = "Argument 'region' must be either of type <class Region> or <class SurfaceSide>"
        assert isinstance(reg, Region) or isinstance(reg, SurfaceSide), print_statement
        return reg
    
    def has_global_mesh(self):
        return self.__global_mesh

    def has_local_mesh(self):
        return self.__local_mesh  

    @property
    def name(self):
        return self.__name
    
    @property
    def material(self):
        return self.__filled_material
    
    @property
    def universe(self):
        return self.__universe
    
    @property
    def filled_by_universe(self):
        return self.__filled_universe

    @property
    def region(self):
        return self.__region
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @material.setter
    def material(self, material):
        self.__filled_material = material
    
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

