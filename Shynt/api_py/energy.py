class Grid:


    def __init__(self, grid, name=""):
        self.__grid = grid
        self.__groups = len(grid) - 1
        self.__name = name
        self.__bins = self.grid_bins()
        

    def grid_bins(self):
        bins = {}
        for g in range(self.__groups):
            bin_name = f"{self.__name}_{g}"
            bin_ = (self.__grid[g], self.__grid[g+1])
            bins[bin_name] = bin_
        return bins

    def serpent_syntax(self):
        """
            
        """
        syntax = f"ene {self.__name} 1 "

        for ener in self.__grid:
            syntax += f"{ener} "
        syntax += "\n"
        
        return syntax
    
    def serpent_syntax_by_bins(self):
        """
            
        """
        syntax = ""
        for b_name, grid in self.__bins.items():
            syntax += f"ene {b_name} 1 {grid[0]} {grid[1]}\n"

        
        return syntax

    def getGrid(self):
        return self.__grid
    
    def getEnergyGroups(self):
        return self.__groups
    
    @property
    def name(self):
        return self.__name

    @property
    def energy_groups(self):
        return self.__groups