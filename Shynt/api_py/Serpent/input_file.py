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
        self.__cell = ""
        # self.__cell_to_cell = None
        # self.__cell_to_surf = None
        # self.__surf_to_cell = None
        # self.__surf_to_surf = None
        

    def syntax(self):
        syn = f"det {self.name} {self.__surface} {self.energy_bins}"
        syn += f" {self.__response} {self.__cell}"
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
        self.__cell = f"dc {cell}"


    # @property
    # def cell_to_cell(self):
    #     return self.__cell_to_cell
    
    # @cell_to_cell.setter
    # def cell_to_cell(self, cell1, cell2):
    #     self.__cell_to_cell = (cell1, cell2)

    # @property
    # def cell_to_surf(self):
    #     return self.__cell_to_surf

    # @cell_to_surf.setter
    # def cell_to_surf(self, cell, surf):
    #     self.__cell_to_surf = (cell, surf)
    
    # @property
    # def surf_to_surf(self):
    #     return self.__surf_to_surf

    # @surf_to_surf.setter
    # def surf_to_surf(self, surf1, surf2):
    #     self.__surf_to_surf = (surf1, surf2)

    # @property
    # def surf_to_cell(self):
    #     return self.__surf_to_cell
    
    # @surf_to_cell.setter
    # def surf_to_cell(self, surf, cell):
    #     self.__surf_to_cell = (surf, cell)


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
        cell,
        name, 
        libraries, 
        energyGrid, 
        mc_params, 
        type_detectors=None, 
        region_id=None, 
        specific=None
    ):
        
        self.cell = cell
        self.name = name
        self.libraries = libraries
        self.energy_grid = energyGrid
        self.mcparams = mc_params
        self.global_id = cell.id 
        self.type_detectors = type_detectors
        # --------------------------------------------------------------------------------------------------
        self.region_id = region_id # This variable is for 
        self.specific = specific
        # --------------------------------------------------------------------------------------------------

        # self.detector_flags = []
        self.surfaces_ids = []
        self.surfaces_syntax = []
        # self.surface_for_detectors = None
        # self.closing_surface_ids = None
        self.surface_direction = None
        # self.material_cell_ids_relation = None
        # self.isFuel_relation = {}
        # self.detectors = []
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

                # self.__write_main_cell()
                # self.__write_system_cells()
                #self.__write_outside_cell()
    

    def __write_title(self):
        self.__file.write(f"set title \"{self.cell.name}\"\n\n")

    def __write_surfaces(self):
        # Surfaces for region enclosing the main cell ------------------------
        region = self.cell.region
        # surfaces_main_cell = self.__surface_searcher_in_region(region, surfaces=[])
        surfaces_main_cell = region.surfaces_of_region()

        self.__add_surfaces(surfaces_main_cell)

        universe_cells = get_all_surfaces_in_a_cell(self.cell)
        # Looking for surfaces inside the main cell -------------------
        if isinstance(self.cell.content, SquareLattice):
            # only surfaces that enclose the pin cells
            lattice = self.cell.content
            for c in lattice.cells.values():
                cell_region = c.region
                surfaces = cell_region.surfaces_of_region()
                self.__add_surfaces(surfaces)
                
        
        self.__file.write("\n\n")
        for surf in self.surfaces:
            self.__file.write(surf)
        

    def __write_geometry(self):
        """
            # Consider if it is better to print the geometry from the local problems
        """
        

        

        
        
        # Write cell
        return 0
        cell_syntax = ""
        if self.type_detectors == "xs_generation":
            cell_syntax = self.cell.serpent_syntax_gcu()
        elif self.type_detectors == "flux":
            cell_syntax = self.cell.serpent_syntax_universe_cells()
        elif self.type_detectors is not None:
            cell_syntax = self.cell.serpent_syntax()
        self.__file.write(cell_syntax)
        return 0

    def __write_outside_cell(self):
        """

        """
        # Write outside
        # print(self.cell.region)
        try:
            reg = self.cell.region 
            assert not isinstance(reg, SurfaceSide) # It is assummed that is a Region class instance
            outside_reg = reg.invert()
            outside_cell = Cell(fill="outside", region=outside_reg, universe=self.cell.universe)
            
            self.__file.write(outside_cell.serpent_syntax())
        except AssertionError:
            # then it is SurfaceSide class
            out_surf = self.cell.region.surface
            outside_cell = Cell(fill="outside", region=+out_surf, universe=self.cell.universe)
            self.__file.write(outside_cell.serpent_syntax())
            

        # raise SystemExit
        pass

    def __add_surfaces(self, surfaces):
        for surf in surfaces:
            if surf.id not in self.surfaces_ids:
                self.surfaces_ids.append(surf.id)
                self.surfaces_syntax.append(surf.serpent_syntax)

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

        # Getting surfaces for detectors -----------------------------------------
        self.__file.write("% ----- Surface for detectors\n")
        surface_for_detectors = self.__get_surface_for_detectors()        
        self.__file.write(surface_for_detectors)
        
        # getting detectors
        regions_dict = {r.cell.id: r for r in self.regions}

        if self.type_detectors == "region":
            # Region detectors
            isFuel = self.isFuel_relation[self.region_id][1]
            if isFuel: # Is fuel
                # Fuel detectors -------------------------------------------------------
                self.__helper_fuel_detectors(regions_dict)
            else: # Is not Fuel
                # Coolant detectors ----------------------------------------------------
                self.__helper_coolant_detectors(regions_dict)
        elif self.type_detectors == "surfaces":
            # Surface detectors ----------------------------------------------------
            self.__helper_surface_detectors(regions_dict)
        
        # Writing detectors in the serpent file --------------------------------
        self.__file.write("\n\n% ----- Detectors ------\n")
        for det in self.detectors:
            self.__file.write(det.syntax())

        # Checking flag number to not exceed 64 --------------------------------
        try:
            assert(self.flag_counter < 64)
        except AssertionError:
            print(f"*** Error *** flag number for serpent detectors reached {self.flag_counter}, must be between 1 - 64")
            print("This happens because Serpent's limit is 64, and internally could happen for excess of regions or\nsurfaces in the local problem")
            raise SystemExit

    def __write_gcu(self):
        self.__file.write("set gcu")

    def __get_surface_for_detectors(self):
        surface_for_detectors = ""
        self.closing_surface_ids = []
        self.surface_direction = {}
        closing_surf = self.cell.region.surface 

        if isinstance(closing_surf, Surface):
            # Only for square en hexagon sufaces ATM
            surf_cl = closing_surf.get_surface_relation()
            for s_id, surf in surf_cl.items():
                surface_for_detectors += surf.serpent_syntax
                self.closing_surface_ids.append(s_id)
                self.surface_direction = closing_surf.get_neutron_current_directions()
        
        # Adding surfaces from inside the pin cell
        self.material_cell_ids_relation = {}
        universe = self.cell.content
        
        # print(self.surfaces_ids)
        for cell in universe.cells.values():
            if isinstance(cell.content, Material):
                if cell.content.isFuel:
                    # self.isFuel_relation[]
                    surf = cell.region.surface
                    if surf.id not in self.surfaces_ids:
                        surface_for_detectors += surf.serpent_syntax
                    self.surface_direction[surf.id] = {"inward": "-1", "outward": "1"}
                    # self.material_cell_ids_relation[cell.content.name] = cell.id
                    # self.material_cell_ids_relation["fuel"] = cell.id
                    self.isFuel_relation[cell.id] = (cell.content.name, True)
                else:
                    # self.material_cell_ids_relation[cell.content.name] = cell.id
                    # self.material_cell_ids_relation["coolant"] = cell.id
                    self.isFuel_relation[cell.id] = (cell.content.name, False)
        return surface_for_detectors
        
    def __helper_fuel_detectors(self, regions_dict):
        energy_bins = self.energy_grid.bins_names_relation
        groups = self.energy_grid.energy_groups

        flag_relation = { }
        
        self.detectors_relation["regions"][self.region_id] = {  
            "total": {g: None for g in range(groups)},
            "incoming": {g: None for g in range(groups)},
            "outcoming": {g: None for g in range(groups)},
            "surface&coolant": {g: None for g in range(groups)},
            "regions": {
                r.cell.id: {g: {} for g in range(groups)} for r in self.regions if r.cell.id != self.region_id
            },
            # "coolant": {g: None for g in range(groups)},
            "surfaces" : {
                s: {g: {} for g in range(groups)} for s in self.closing_surface_ids
            }
        }
        
        fuel_cell = regions_dict[self.region_id].cell

        for g, bin_name in energy_bins.items():
            # Total reaction rate for each energy_bin
            name = f"total_rate_reg{fuel_cell.id}_g{g}"
            det = Detector(name)
            det.set_cell(self.region_id)
            det.set_response("-1", fuel_cell.content.name)
            det.set_energy_bins(bin_name)
            self.detectors.append(det)
            self.detectors_relation["regions"][self.region_id]["total"][g] = det


            surface_id = fuel_cell.region.surface.id
            # Surface detector. Inward neutrons to the fuel
            name = f"j_in_reg{fuel_cell.id}_g{g}"
            det = Detector(name)
            det.set_surface_det(surface_id, self.surface_direction[surface_id]["inward"])
            det.set_energy_bins(bin_name)
            det.set_flag(self.flag_counter, "1")
            flag_relation[f"j_in_reg{fuel_cell.id}_g{g}"] = self.flag_counter
            self.detectors.append(det)
            self.detectors_relation["regions"][self.region_id]["incoming"][g] = det


            # Surface detector. Outward neutrons from the fuel
            name = f"j_out_reg{fuel_cell.id}_g{g}"
            det = Detector(name)
            det.set_surface_det(surface_id, self.surface_direction[surface_id]["outward"])
            det.set_energy_bins(bin_name)
            det.set_flag(self.flag_counter, "3")
            det.set_flag(self.flag_counter+1, "1")
            flag_relation[f"j_out_reg{fuel_cell.id}_g{g}"] = self.flag_counter + 1
            self.detectors.append(det)
            self.detectors_relation["regions"][self.region_id]["outcoming"][g] = det
            self.flag_counter += 2


            # Surf and coolant to fuel
            name = f"all_to_reg{fuel_cell.id}_g{g}"
            det = Detector(name)
            det.set_cell(fuel_cell.id)
            det.set_response("-1", fuel_cell.content.name)
            det.set_energy_bins(bin_name)
            det.set_flag(flag_relation[f"j_in_reg{fuel_cell.id}_g{g}"], "2")
            det.set_flag(flag_relation[f"j_in_reg{fuel_cell.id}_g{g}"], "0")
            self.detectors.append(det)
            self.detectors_relation["regions"][self.region_id]["surface&coolant"][g] = det


            # Fuel to coolant (or other regions)
            for reg in self.regions:
                if reg.cell.id != self.region_id:
                    name = f"reg{fuel_cell.id}_to_reg{reg.cell.id}_g{g}"
                    det = Detector(name)
                    det.set_cell(reg.cell.id)
                    det.set_response("-1", reg.cell.content.name)
                    det.set_energy_bins(bin_name)
                    det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}_g{g}"], "2")
                    det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}_g{g}"], "0")
                    self.detectors.append(det)
                    self.detectors_relation["regions"][self.region_id]["regions"][reg.cell.id][g] = det

            # Fuel to surf
            for s in self.closing_surface_ids:
                name = f"reg{fuel_cell.id}_to_surface{s}_g{g}"
                det = Detector(name)
                det.set_surface_det(s, self.surface_direction[s]["outward"])
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}_g{g}"], "2")
                det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}_g{g}"], "0")
                self.detectors.append(det)
                self.detectors_relation["regions"][self.region_id]["surfaces"][s][g] = det


    def __helper_coolant_detectors(self, regions_dict):
        energy_bins = self.energy_grid.bins_names_relation
        groups = self.energy_grid.energy_groups

        flag_relation = { }

        self.detectors_relation["regions"][self.region_id] = {
            "total": {g: None for g in range(groups)},
            "regions": {
                r.cell.id: {g: {} for g in range(groups)} for r in self.regions
            },
            "surfaces": {
                s: {g: {} for g in range(groups)} for s in self.closing_surface_ids
            },
        }

        total_rate_detectors = {}
        coolant_cell = regions_dict[self.region_id].cell

        # Total reaction rate for each energy_bin
        for g in range(self.energy_grid.energy_groups):
            name = f"total_rate_reg{coolant_cell.id}_g{g}"
            det = Detector(name)
            det.set_cell(coolant_cell.id)
            det.set_response("-1", coolant_cell.content.name)
            det.set_energy_bins(energy_bins[g])
            det.set_flag(self.flag_counter, "1")
            flag_relation[f"reg{coolant_cell.id}_total_rate_g{g}"] = self.flag_counter
            # detectors.append(det)
            # detectors_relation["coolant"]["total"][g] = det
            total_rate_detectors[g] = det
            self.flag_counter += 1
            
        # Coolant to coolant, fuel and surf
        for g in range(self.energy_grid.energy_groups):
            for gp in range(self.energy_grid.energy_groups):
                # COOLANT ----> COOLANT
                name = f"reg{coolant_cell.id}_reg{coolant_cell.id}_g{g}_to_g{gp}"
                det = Detector(name)
                det.set_cell(coolant_cell.id)
                det.set_response("-1", coolant_cell.content.name)
                det.set_energy_bins(energy_bins[gp])
                det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate_g{g}"], "2")
                det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate_g{g}"], "0")
                det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate_g{gp}"], "1")
                self.detectors.append(det)
                self.detectors_relation["regions"][self.region_id]["regions"][self.region_id][g][gp] = det

        for g in range(self.energy_grid.energy_groups):
            self.detectors.append(total_rate_detectors[g])
            self.detectors_relation["regions"][self.region_id]["total"][g] = total_rate_detectors[g]

        # Fuel to coolant (or other regions)

        for reg in self.regions:
            if reg.cell.id != self.region_id:
                # for a region that is different to the current coolant region
                # if it is another coolant region check the implementation for
                # coolant to coolant
                for g in range(self.energy_grid.energy_groups):
                    for gp in range(self.energy_grid.energy_groups):
                        # COOLANT -----> REG _reg
                        name = f"reg{self.region_id}_reg{reg.cell.id}_g{g}_to_g{gp}"
                        det = Detector(name)
                        det.set_cell(reg.cell.id)
                        det.set_response("-1", reg.cell.content.name)
                        det.set_energy_bins(energy_bins[gp])
                        det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate_g{g}"], "2")
                        det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate_g{g}"], "0")
                        self.detectors.append(det)
                        self.detectors_relation["regions"][self.region_id]["regions"][reg.cell.id][g][gp] = det

        for g in range(self.energy_grid.energy_groups):
            for gp in range(self.energy_grid.energy_groups):
                # COOLANT -----> SURFACES
                for s in self.closing_surface_ids:
                    name = f"reg{reg.cell.id}_surface{s}_g{g}_to_g{gp}"
                    det = Detector(name)
                    det.set_surface_det(s, self.surface_direction[s]["outward"])
                    det.set_energy_bins(energy_bins[gp])
                    det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate_g{g}"], "2")
                    det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate_g{g}"], "0")
                    self.detectors.append(det)
                    self.detectors_relation["regions"][self.region_id]["surfaces"][s][g][gp] = det


    def __helper_surface_detectors(self, regions_dict):
        energy_bins = self.energy_grid.bins_names_relation
        groups = self.energy_grid.energy_groups

        self.detectors_relation["surfaces"] = {
            s: {
                "regions": {
                    r.cell.id: {
                        g: {} for g in range(groups)
                    } for r in self.regions
                },
                "incoming": {g: None for g in range(groups)},
                "surfaces": {
                    s: {
                        g: {} for g in range(groups)
                    } for s in self.closing_surface_ids
                }
            } for s in self.closing_surface_ids
        }

        flag_relation = { }

        # Incoming neutrons
        for g, bin_name in energy_bins.items():
            for s in self.closing_surface_ids:
                name = f"surface_{s}_jin_g{g}"
                det = Detector(name)
                det.set_surface_det(s, self.surface_direction[s]["inward"])
                det.set_energy_bins(bin_name)
                det.set_flag(self.flag_counter, "1")
                flag_relation[f"surf_{s}_jin_g{g}"] = self.flag_counter
                self.detectors.append(det)
                self.detectors_relation["surfaces"][s]["incoming"][g] = det
                self.flag_counter += 1
        
        # Surf to regions
        for reg in self.regions:
            for g, bin_name in energy_bins.items():
                for s in self.closing_surface_ids:
                    name = f"surface_{s}_to_reg{reg.cell.id}_g{g}"
                    det = Detector(name)
                    det.set_cell(reg.cell.id)
                    det.set_response("-1", reg.cell.content.name)
                    det.set_energy_bins(bin_name)
                    det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "2")
                    det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "0")
                    self.detectors.append(det)
                    self.detectors_relation["surfaces"][s]["regions"][reg.cell.id][g] = det

        # Surf to surf
        for g, bin_name in energy_bins.items():
            for s in self.closing_surface_ids:
                for sp in self.closing_surface_ids:
                    name = f"surface_{s}_to_surf{sp}_g{g}"
                    det = Detector(name)
                    det.set_surface_det(sp, self.surface_direction[sp]["outward"])                    
                    det.set_energy_bins(bin_name)
                    det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "2")
                    det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "0")
                    self.detectors.append(det)
                    self.detectors_relation["surfaces"][s]["surfaces"][sp][g] = det


