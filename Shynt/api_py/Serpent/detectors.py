
class Detector():

    """
        Class for a single detector

        Parameters:
        -------------------------------------------------------------------
        - name  :   Name for the detector in serpent card
        - type  :   Type of detector regarding the probability that 
                    we  want to calculate. Types:
                    * total_rate
                    * cell_to_surface
                    * cell_to_surface
                    * surface_to_all
                    * surface_to_cell
                    * surface_to_surface 
        -------------------------------------------------------------------
    """


    def __init__(self, name, cells=[], response=(), energy_grid=None, surface=(), type_="", flags=[]):
        self.name = name
        self.type = type_
        self.__surface = surface
        self.__energy_bins = energy_grid
        self.__response = response
        self.__flags = flags
        self.__cells = cells
        

        # self.__cell_to_cell = None
        # self.__cell_to_surf = None
        # self.__surf_to_cell = None
        # self.__surf_to_surf = None
        

    def syntax(self):
        syn = f"det {self.name} "
        if len(self.__surface) == 2:
            surf, direction = self.__surface
            syn += f"ds {surf} {direction} "
        if self.__energy_bins:
            syn += f"de {self.energy_bins} "
        if len(self.__response) == 2:
            rxn, material = self.__response
            syn += f"dr {rxn} {material} "
        
        for cell in self.__cells:
            syn += f"dc {cell} "

        for flag in self.__flags:
            fl, option = flag
            syn += f"dfl {fl} {option} "
        syn += "\n"
        return syn

    def set_surface_det(self, surf, direction):
        self.__surface = f"ds {surf} {direction}"
    
    def set_energy_bins(self, energy_struct):
        self.__energy_bins = f"de {energy_struct}"

    def set_response(self, resp_number, material):
        self.__response = f"dr {resp_number} {material}"

    def set_flag(self, flag_number, option):
        self.__flags.append(f"dfl {flag_number} {option}")
    
    def set_cell(self, cell):
        self.__cells.append(cell)


    @property
    def surface_det(self):
        return self.__surface
    
    @property
    def energy_bins(self):
        return self.__energy_bins

    @property
    def response(self):
        return self.__response

    @property
    def flag(self):
        return self.__flag
    
    @property
    def cell(self):
        return self.__cell

