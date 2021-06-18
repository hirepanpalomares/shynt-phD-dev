class Cell:

    def __init__(self, name, material=None, universe=None, region=None):
        """
            Init method of the class

            Parameters
            -------------------------------------------------------------
            name        :   String - name of the cell
            material    :   Material class - Material which the class is filled in
            universe    :   Array of strings - Universes which the cell belongs to
            region      :   Array of integers - Positive or negative corresponding
                            to the surfaces enclosing the cell
            -------------------------------------------------------------

        """
        self.__name = name
        self.__material = material
        self.__universe = universe
        self.__region = region

    
    def __str__(self):
        return """
            Cell %s
        """%self.__name

    def setRegion(self, region):
        self.__region = region

    def setMaterial(self, material):
        self.__material = material
    
    def getName(self):
        return self.__name
    
    def getMaterial(self):
        return self.__material
    
    def fromUniverse(self):
        return self.__universe
    
    def getRegion(self):
        return self.__region
    