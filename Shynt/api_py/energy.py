class Grid:



    def __init__(self, grid, name=""):
        self.__grid = grid
        self.__name = name

    
    def serpent_syntax(self):
        """
            The number 1 is for bin boundaries syntax in serpent
        """
        syntax = f"ene {self.__name} 1 "

        for ener in self.__grid:
            syntax += f"{ener} "
        syntax += "\n"
        
        return syntax
    
    def getGrid(self):
        return self.__grid
    
    def getEnergyGroups(self):
        return len(self.__grid) - 1
    
    @property
    def name(self):
        return self.__name