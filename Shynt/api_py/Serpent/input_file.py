from Shynt.api_py.Geometry.surfaces import Hexagon, InfiniteSquareCylinderZ, Surface
from Shynt.api_py.Geometry.regions import Region, SurfaceSide
from Shynt.api_py.Geometry.cells import Cell, materials_in_cell
from Shynt.api_py.Geometry.universes import Lattice, Pin, SquareLattice, Universe
from Shynt.api_py.Geometry.utilities import get_all_surfaces_in_a_cell
from Shynt.api_py.materials import Material


import os
import sys
# import pdb
# pdb.set_trace()

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


    def __init__(self, name, type_=""):
        self.name = name
        self.type = type_
        self.__surface = ""
        self.__energy_bins = ""
        self.__response = ""
        self.__flags = []
        self.__cells = []

        # self.__cell_to_cell = None
        # self.__cell_to_surf = None
        # self.__surf_to_cell = None
        # self.__surf_to_surf = None
        

    def syntax(self):
        syn = f"det {self.name} {self.__surface} {self.energy_bins}"
        syn += f" {self.__response} \n"
        for cell in self.__cells:
            syn += f"dc {cell}\n"
        for flag in self.__flags:
            syn += f" {flag} "
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

class SerpentInputFile():
    
    def __init__(self, cell, name, libraries, energyGrid, mc_params, type_detectors=None):
        self.cell = cell
        self.name = name
        self.libraries = libraries
        self.energy_grid = energyGrid
        self.mcparams = mc_params
        self.type_detectors = type_detectors
        self.surfaces_ids = []

        with open(name, "w") as self.__file:
            self.__write_title()
            self.__write_material()
            self.__write_libraries()
            self.__file.write("\n\nset bc 2\n\n")
            self.__write_mc_params()
            if self.type_detectors == "flux":
                self.__write_energy_grid()
                self.__write_geometry()
                self.__write_outside_cell()

    
    def __write_title(self):
        self.__file.write(f"set title \"{self.cell.name}\"\n\n")

    def __write_material(self):
        if isinstance(self.cell.content, Pin):
            materials = self.cell.content.materials
            for mat in materials:
                syntax = mat.serpent_syntax
                self.__file.write(syntax)
        elif isinstance(self.cell.content, SquareLattice):
            materials = materials_in_cell(self.cell)
            for mat in materials.values():
                syntax = mat.serpent_syntax
                self.__file.write(syntax)
            a = 10

    def __write_libraries(self):
        self.__file.write(self.libraries.serpent_syntax)
 
    def __write_mc_params(self):
        self.__file.write("\n\n")
        self.__file.write(self.mcparams.serpent_syntax)
        self.__file.write("\n\n")

    def __write_energy_grid(self, syntax="complete"):
        self.__file.write("\n\n")
        if syntax == "by_bin":
            self.__file.write(self.energy_grid.serpent_syntax_by_bins())
        elif syntax == "complete":
            self.__file.write(self.energy_grid.serpent_syntax())
        self.__file.write("\n\n")

    def __write_geometry(self):
        """
            # Consider if it is better to print the geometry from the local problems
        """
        

        # Surfaces for region enclosing the cell ----------------------------------------------
        region = self.cell.region
        # searching surfaces
        surfaces_region = self.__surface_searcher_in_region(region, surfaces=[])
        # self.__surface_searcher_in_region(region)
        self.surfaces = surfaces_region

        # Looking for surfaces in the cells of the universe ---------------------------------
        if isinstance(self.cell.content, Universe):
            universe = self.cell.content
            for c in universe.cells.values():
                cell_region = c.region
                surfaces = self.__surface_searcher_in_region(cell_region, surfaces=[])
                self.surfaces += surfaces
        
        self.__file.write("\n\n")
        for surf in self.surfaces:
            self.__file.write(surf)
        
        # Write cell
        cell_syntax = ""
        if isinstance(self.cell.content, Lattice):
            # write all the cells of the pins separetely to call them in the detectors
            pass
        elif isinstance(self.cell.content, Pin):
            pass
        elif isinstance(self.cell.content, Material):
            pass
        

        if self.type_detectors == "xs_generation":
            cell_syntax = self.cell.serpent_syntax_gcu()
        elif self.type_detectors is not None:
            cell_syntax = self.cell.serpent_syntax()
            # print(cell_syntax)
            # print(self.cell)
        self.__file.write(cell_syntax)
    
    def __surface_searcher_in_region(self, region, surfaces=[]):
        
        """
            This is a recursive function
            
            Whichever region is received, returns the surfaces needed to build that region
        """

        if isinstance(region, SurfaceSide):
            # base case
            surf = region.surface
            surf_id = surf.id
            surf_syntax = surf.serpent_syntax
            if surf_id not in self.surfaces_ids:
                self.surfaces_ids.append(surf_id)
                if surf_syntax not in surfaces:
                    surfaces.append(surf_syntax)
            # print("surf after", surfaces)
            return surfaces
        elif isinstance(region, Region):
            # print("reg")
            reg1 = region.child1
            reg2 = region.child2
            surfaces += self.__surface_searcher_in_region(reg1, surfaces=surfaces)
            surfaces += self.__surface_searcher_in_region(reg2, surfaces=surfaces)
            return surfaces

    def __surfaces_from_region_instance(self, reg, surfaces=[]):
        print("surf before", surfaces)
        if isinstance(reg, SurfaceSide):
            # base case
            surf = reg.surface
            print("surface side", surf)
            if surf.id not in self.surfaces_ids:
                self.surfaces_ids.append(surf.id)
                if surf.serpent_syntax not in surfaces:
                    surfaces.append(surf.serpent_syntax)
            print("surf after", surfaces)
            return surfaces
        elif isinstance(reg, Region):
            print("reg")
            reg1 = reg.child1
            reg2 = reg.child2
            surfaces = self.__surfaces_from_region_instance(reg1, surfaces)
            surfaces = self.__surfaces_from_region_instance(reg2, surfaces)
            return surfaces


class SerpentInputFileRmm():
    """
       
        ------------------------
        Parameters:
            - coarse_node:      Coarse node corresponding to the serpent file
            - id_coarse:        ID of the coarse node corresponding to the serpent file
            - regions:          Regions inside the coarse node
            - name:             Name of the input file (absolut path)
            - libraries:        Serpent libraries object
            - energyGrifd:      Grid object (energy groups)
            - mc_params:        MontecarloParams object
            - type_dectectors:  Type of detectors ("region", "surfaces", None). None is used 
                                for XS generation
            -region_id:         Region ID of reference for the detectors
            -specific:          Name of type of file: "region-fuel", "region-coolant", "surfaces". This is for knowing which material
                                we are interested in for the detectors

        
        ------------------------
        Attributes:
            
        ------------------------
        
    """
    

    def __init__(self, 
        root,
        name,
        type_detectors=None, 
        region_id=None, 
        specific=None
    ):
        self.root = root
        self.cell = root.model_cell
        self.outside_cell = root.outside_cell
        self.name = name
        self.libraries = root.libraries
        self.energy_grid = root.energy_grid
        self.mcparams = root.mcparams
        self.global_id = self.cell.id 
        self.type_detectors = type_detectors
        # --------------------------------------------------------------------------------------------------
        self.region_id = region_id # This variable is for 
        self.specific = specific
        # --------------------------------------------------------------------------------------------------

        # self.detector_flags = []
        self.cells_for_flux = {}
        self.surfaces_ids = []
        self.surfaces_syntax = []
        # self.surface_for_detectors = None
        # self.closing_surface_ids = None
        self.surface_direction = None
        # self.material_cell_ids_relation = None
        # self.isFuel_relation = {}
        self.detectors = []
        # self.flag_counter = 1
        # self.detectors_relation = {
        #     "regions": {},
        #     "surfaces": {}
        # }

        with open(name, "w") as self.__file:
            self.__write_title()
            self.__write_material()
            self.__write_libraries()
            self.__file.write("\n\nset bc 2\n\n")
            self.__write_mc_params()
            self.__write_energy_grid()
            if self.type_detectors == "flux":
                self.__write_surfaces()
                self.__write_system_cells()
                self.__write_main_cell()
                self.__write_outside_cell()
                self.__write_detectors()
    

    def __write_title(self):
        self.__file.write(f"set title \"{self.cell.name}\"\n\n")

    def __write_surfaces(self):
        
        main_cell_surfaces = get_all_surfaces_in_a_cell(self.cell)
        # Apparently the lattice doesn not create new surfaces 
        # for the same type of pin, it uses the same object in
        # memory
        self.__add_surfaces(main_cell_surfaces)
                
        
        self.__file.write("\n\n")
        for surf in self.surfaces_syntax:
            self.__file.write(surf)
        
    def __write_system_cells(self):
        cell_syntax = ""
        lattice_syntax = ""
        if isinstance(self.cell.content, SquareLattice):
            lattice = self.cell.content
            
            cell_syntax, cells = lattice.serpent_syntax_pin_by_cell()
            self.cells_for_flux.update(cells)

        # self.__write(lattice_syntax)
        self.__file.write(cell_syntax)

    def __write_main_cell(self):
        main_cell_syntax = ""
        main_cell = self.cell
        self.__file.write(main_cell.serpent_syntax())

    def __write_outside_cell(self):
        self.__file.write(self.outside_cell.serpent_syntax())
        

    def __add_surfaces(self, surfaces):
        for surf in surfaces:
            if surf.id not in self.surfaces_ids:
                self.surfaces_ids.append(surf.id)
                self.surfaces_syntax.append(surf.serpent_syntax_for_lattice)

    def __write_material(self):
        materials = self.cell.get_cell_materials()
        for mat_name, mat in materials.items():
            syntax = mat.serpent_syntax
            self.__file.write(syntax)
        
    def __write_libraries(self):
        self.__file.write(self.libraries.serpent_syntax)
 
    def __write_mc_params(self):
        self.__file.write("\n\n")
        self.__file.write(self.mcparams.serpent_syntax)
        self.__file.write("\n\n")

    def __write_energy_grid(self, syntax="complete"):
        self.__file.write("\n\n")
        if syntax == "by_bin":
            self.__file.write(self.energy_grid.serpent_syntax_by_bins())
        elif syntax == "complete":
            self.__file.write(self.energy_grid.serpent_syntax())
        self.__file.write("\n\n")

    def __write_detectors(self):
        """
            
        """

        # getting detectors
        

        if self.type_detectors == "flux":
            name = f"flux_by_cell_by_group"
            det = Detector(name)
            for c_id, cell in self.cells_for_flux.items():
                det.set_cell(c_id)
            det.set_energy_bins(self.energy_grid.name)
            self.detectors.append(det)




        # Writing detectors in the serpent file --------------------------------
        self.__file.write("\n\n% ----- Detectors ------\n")
        for det in self.detectors:
            self.__file.write(det.syntax())

    

   