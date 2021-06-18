class Grid:

    def __init__(self, grid):
        self.__grid = grid
    
    def getGrid(self):
        return self.__grid
    
    def getEnergyGroups(self):
        return len(self.__grid)