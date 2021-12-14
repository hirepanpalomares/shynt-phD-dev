class Grid:


    def __init__(self, grid, name=""):
        self.__grid = grid
        self.__groups = len(grid) - 1
        self.__name = name
        self.__bins_names_relation, self.__bins = self.__grid_bins()
        

    def __grid_bins(self):
        bins_names_relation = {}
        bins = {}
        for g in range(self.__groups):
            bin_name = f"{self.__name}_{g}"
            bin_ = (self.__grid[g], self.__grid[g+1])
            bins_names_relation[g] = bin_name
            bins[g] = bin_
        return bins_names_relation, bins

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
        for g, b_name in self.__bins_names_relation.items():
            syntax += f"ene {b_name} 1 {self.__bins[g][0]} {self.__bins[g][1]}\n"

        
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
    
    @property
    def bins_names_relation(self):
        return self.__bins_names_relation

    
    @property
    def bins(self):
        return self.__bins