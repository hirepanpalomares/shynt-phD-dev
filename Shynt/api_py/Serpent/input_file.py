from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ
from Shynt.api_py.Geometry.regions import Region, SurfaceSide
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.universes import Pin, Universe
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
    """
        Class for a serpent input file:

        ------------------------
        Parameters:
            -
        
        ------------------------
        Attributes:
            - self.detectors_relation: 
                    Dictionary with a relation of detectors including 'total_rate', 
                    'surface_count', 'surface_to_cell', 'surface_to_surf', 'cell_to_surf' and
                    'cell_to_cell', The relations are explained as follow:
                    
                    + total_rate: Counts the number of total interactions that occur in a
                                  given cell.
                    + surf_count: Count the neutrons that enters the cell crossing 
                                     a given surface.
                    + surf_to_surf: Count the neutrons entering the cell through a given
                                       surface and exiting the cell through another given
                                       surface
                    + surf_to_region: Count the neutrons entering the cell through a given
                                       surface and then first interacting in a given cell.
                    + region_to_surf: Counts the total number of neutrons that first interacts in
                                    a given cell and then cross a surface without interacting
                    + region_to_region: Counts the total number of neutrons that first interacts in
                                    a given cell and then first interact in another given cell

        ------------------------
        
    """
    

    def __init__(self, coarse_node, id_global, local_nodes, name, libraries, energy, params, type_detectors=None, specific=None):
        self.cell = coarse_node.cell
        self.name = name
        self.libraries = libraries
        self.energy_grid = energy
        self.mcparams = params
        self.global_id = id_global # is del global node 
        self.local_nodes = local_nodes
        self.type_detectors = type_detectors
        # --------------------------------------------------------------------------------------------------
        self.specific = specific
        # I think the variable specific was declared in the mean time to difference the detectors from
        #fuel, coolant and surfaces.
        # --------------------------------------------------------------------------------------------------

        self.detector_flags = []
        self.surfaces_ids = []
        self.surfaces = []
        self.surface_for_detectors = None
        self.closing_surface_ids = None
        self.surface_direction = None
        self.material_cell_ids_relation = None
        self.detectors = []
        self.detectors_relation = {}
        
        with open(name, "w") as self.__file:
            self.__write_title()
            self.__write_material()
            self.__write_libraries()
            self.__file.write("\n\nset bc 2\n\n")

            self.__write_mc_params()
            if self.type_detectors == "xs_generation":
                self.__write_energy_grid()
                self.__write_geometry()

            elif self.type_detectors is not None:
                self.__write_geometry()
                self.__write_outside_cell()
                self.__write_energy_grid(syntax="by_bin")
                self.__write_detectors()
                pass
            

    
    def __write_title(self):
        self.__file.write(f"set title \"{self.cell.name}\"\n\n")

    def __write_geometry(self):
        """
            # Consider if it is better to print the geometry from the local problems
        """
        
        # Write surfaces
        surfaces_in_cell = self.__surface_searcher(self.cell)
        
        self.__file.write("\n\n")
        for surf in surfaces_in_cell:
            self.__file.write(surf)
        
        # Write cell
        if self.type_detectors == "xs_generation":
            cell_syntax = self.cell.serpent_syntax_gcu()
        elif self.type_detectors is not None:
            cell_syntax = self.cell.serpent_syntax()
        self.__file.write(cell_syntax)

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

    def __surface_searcher(self, cell, surfaces=[]):
        
        """
            This is a recursive function
        """
        # Whichever cell is received, append corresponding region to surface array
        region = cell.region
        # print(cell)
        # raise SystemExit
        from_region = self.__surfaces_from_region_instance(region)
        surfaces = from_region

        if isinstance(cell.content, Material):
            # base case
            return surfaces
        elif isinstance(cell.content, Universe):
            universe = cell.content
            universe_cells = universe.cells
            for c in universe_cells:
                surfaces = self.__surface_searcher(c, surfaces)
            return surfaces
    
    def __surfaces_from_region_instance(self, reg, surfaces=[]):
        if isinstance(reg, SurfaceSide):
            # base case
            surf = reg.surface
            if surf.id not in self.surfaces_ids:
                self.surfaces_ids.append(surf.id)
                if surf.serpent_syntax not in surfaces:
                    surfaces.append(surf.serpent_syntax)
            return surfaces
        elif isinstance(reg, Region):
            reg1 = reg.child1
            reg2 = reg.child2
            surfaces = self.__surfaces_from_region_instance(reg1, surfaces)
            surfaces = self.__surfaces_from_region_instance(reg2, surfaces)
            return surfaces

    def __write_material(self):
        if isinstance(self.cell.content, Pin):
            materials = self.cell.content.materials
            for mat in materials:
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
            TODO Write a method to differentiate between cells if it's fuel or something else
            Right now is hard coded:
                - fuel1
                - coolant
            Because the kind of detectors depend on if its (coolant, any other material) or (fuel)
        """

        #  getting surfaces for detectors -----------------------------------------
        self.__file.write("% ----- Surface for detectors\n")
        surface_for_detectors = self.__get_surface_for_detectors()        
        self.__file.write(surface_for_detectors)
        cell_ids_relation = {c.cell.id: c.cell for c in self.local_nodes}
        
        # Preparing detectors relation and flag counter ------------------------
        detectors_relation = {}
        detectors = []
        flag_counter = 1
        groups = self.energy_grid.energy_groups

        # getting fuel cell inside the pin -------------------------------------
        fuel_cell_id = self.material_cell_ids_relation["fuel"]
        fuel_cell = cell_ids_relation[fuel_cell_id]

        # getting coolant cell inside the pin ----------------------------------
        coolant_cell_id = self.material_cell_ids_relation["coolant"]
        coolant_cell = cell_ids_relation[coolant_cell_id]

        # getting detectors
        if self.type_detectors == "local_cell":
            if self.specific == "fuel1":
                detectors_relation = {
                    "fuel": {
                        "total": {g: None for g in range(groups)},
                        "incoming": {g: None for g in range(groups)},
                        "outcoming": {g: None for g in range(groups)},
                        "surface&coolant": {g: None for g in range(groups)},
                        "coolant": {g: None for g in range(groups)},
                        "surface" : {
                            s: {g: {} for g in range(groups)} for s in self.closing_surface_ids
                        }
                    }
                }
                
                # Fuel detectors -------------------------------------------------------
                detectors, detectors_relation, flag_counter = self.__helper_fuel_detectors(
                    fuel_cell, 
                    coolant_cell, 
                    detectors, 
                    detectors_relation,
                    flag_counter
                )

            if self.specific == "coolant":
                detectors_relation = {
                    "coolant": {
                        "total": {g: None for g in range(groups)},
                        "fuel": {g: {} for g in range(groups)},
                        "coolant": {g: {} for g in range(groups)},
                        "surface": {
                            s: {g: {} for g in range(groups)} for s in self.closing_surface_ids
                        },
                    }
                }
                # Coolant detectors ----------------------------------------------------
                detectors, detectors_relation, flag_counter = self.__helper_coolant_detectors(
                    fuel_cell, 
                    coolant_cell, 
                    detectors, 
                    detectors_relation, 
                    flag_counter
                )
        elif self.specific == "surfaces":
            detectors_relation = {
                "surfaces": { }
            }
            for s in self.closing_surface_ids:
                detectors_relation["surfaces"][s] = {
                    "incoming": {g: None for g in range(groups)},
                    "fuel": {g: None for g in range(groups)},
                    "coolant": {g: None for g in range(groups)},
                } 
                for sp in self.closing_surface_ids:
                    detectors_relation["surfaces"][s][sp] = {g: None for g in range(groups)}

            # Surface detectors ----------------------------------------------------
            detectors, detectors_relation, flag_counter = self.__helper_surface_detectors(
                fuel_cell, 
                coolant_cell, 
                detectors, 
                detectors_relation, 
                flag_counter
            )

        # Writing detectors in the serpent file --------------------------------
        self.__file.write("\n\n% ----- Detectors ------\n")
        for det in detectors:
            self.__file.write(det.syntax())

        self.detectors_relation = detectors_relation
        self.detectors = detectors
        # Checking flag number to not exceed 64 --------------------------------
        try:
            assert(flag_counter < 64)
        except AssertionError:
            print(f"*** Error *** flag number for serpent detectors reached {flag_counter}, must be between 1 - 64")
            print("This happens because Serpent's limit is 64, and internally could happen for excess of regions or\nsurfaces in the local problem")
            raise SystemExit

    def __write_gcu(self):
        self.__file.write("set gcu")

    def __get_surface_for_detectors(self):
        surface_for_detectors = ""
        self.closing_surface_ids = []
        self.surface_direction = {}
        closing_surf = self.cell.region.surface 
        # TODO Code this for every closing surf in general
        if isinstance(closing_surf, InfiniteSquareCylinderZ):
            surf_1 = closing_surf.surf_top      # cell in - side 
            surf_2 = closing_surf.surf_right    # cell in - side
            surf_3 = closing_surf.surf_bottom   # cell in + side
            surf_4 = closing_surf.surf_left     # cell in + side
            
            # print(f"Top    surface: {surf_1.id}")
            # print(f"Right  surface: {surf_2.id}")
            # print(f"Bottom surface: {surf_3.id}")
            # print(f"Left   surface: {surf_4.id}")

            # surf T --> outward current = +1 --> inward current = -1
            # surf R --> outward current = +1 --> inward current = -1
            # surf B --> outward current = -1 --> inward current = +1
            # surf L --> outward current = -1 --> inward current = +1

            surface_for_detectors += surf_1.serpent_syntax
            surface_for_detectors += surf_2.serpent_syntax
            surface_for_detectors += surf_3.serpent_syntax
            surface_for_detectors += surf_4.serpent_syntax

            self.closing_surface_ids.append(surf_1.id)
            self.closing_surface_ids.append(surf_2.id)
            self.closing_surface_ids.append(surf_3.id)
            self.closing_surface_ids.append(surf_4.id)

            self.surface_direction = {
                surf_1.id: {"inward": "-1", "outward": "1"},
                surf_2.id: {"inward": "-1", "outward": "1"},
                surf_3.id: {"inward": "1", "outward": "-1"},
                surf_4.id: {"inward": "1", "outward": "-1"},
            }
        
        # Adding surfaces from inside the pin cell
        self.material_cell_ids_relation = {"fuel": 2, "coolant": 3}
        universe = self.cell.content
        universe_cells = universe.cells
        # print(self.surfaces_ids)
        for cell in universe_cells:
            if cell.content.name == "fuel1":
                surf = cell.region.surface
                if surf.id not in self.surfaces_ids:
                    surface_for_detectors += surf.serpent_syntax
                self.surface_direction[surf.id] = {"inward": "-1", "outward": "1"}
                self.material_cell_ids_relation["fuel"] = cell.id
            if cell.content.name == "coolant":
                self.material_cell_ids_relation["coolant"] = cell.id
        return surface_for_detectors
        
    def __helper_fuel_detectors(self, fuel_cell, coolant_cell, detectors, detectors_relation, flag_counter):
        energy_bins = self.energy_grid.bins_names_relation
        flag_relation = { }
        
        for g, bin_name in energy_bins.items():
            # Total reaction rate for each energy_bin
            name = f"total_rate_fuel_g{g}"
            det = Detector(name)
            det.set_cell(fuel_cell.id)
            det.set_response("-1", fuel_cell.content.name)
            det.set_energy_bins(bin_name)
            detectors.append(det)
            detectors_relation["fuel"]["total"][g] = det


            surface_id = fuel_cell.region.surface.id
            # Surface detector. Inward neutrons to the fuel
            name = f"j_in_fuel_g{g}"
            det = Detector(name)
            det.set_surface_det(surface_id, self.surface_direction[surface_id]["inward"])
            det.set_energy_bins(bin_name)
            det.set_flag(flag_counter, "1")
            flag_relation[f"j_in_fuel_g{g}"] = flag_counter
            detectors.append(det)
            detectors_relation["fuel"]["incoming"][g] = det
            # Surface detector. Outward neutrons from the fuel
            name = f"j_out_fuel_g{g}"
            det = Detector(name)
            det.set_surface_det(surface_id, self.surface_direction[surface_id]["outward"])
            det.set_energy_bins(bin_name)
            det.set_flag(flag_counter, "3")
            det.set_flag(flag_counter+1, "1")
            flag_relation[f"j_out_fuel_g{g}"] = flag_counter + 1
            detectors.append(det)
            detectors_relation["fuel"]["outcoming"][g] = det
            flag_counter += 2

            # Surf and coolant to fuel
            name = f"surface_coolant_to_fuel_g{g}"
            det = Detector(name)
            det.set_cell(fuel_cell.id)
            det.set_response("-1", fuel_cell.content.name)
            det.set_energy_bins(bin_name)
            det.set_flag(flag_relation[f"j_in_fuel_g{g}"], "2")
            det.set_flag(flag_relation[f"j_in_fuel_g{g}"], "0")
            detectors.append(det)
            detectors_relation["fuel"]["surface&coolant"][g] = det

            # Fuel to coolant
            name = f"fuel_to_coolant_g{g}"
            det = Detector(name)
            det.set_cell(coolant_cell.id)
            det.set_response("-1", coolant_cell.content.name)
            det.set_energy_bins(bin_name)
            det.set_flag(flag_relation[f"j_out_fuel_g{g}"], "2")
            det.set_flag(flag_relation[f"j_out_fuel_g{g}"], "0")
            detectors.append(det)
            detectors_relation["fuel"]["coolant"][g] = det

            # Fuel to surf
            for s in self.closing_surface_ids:
                name = f"fuel_to_surface-{s}_g{g}"
                det = Detector(name)
                det.set_surface_det(s, self.surface_direction[s]["outward"])
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"j_out_fuel_g{g}"], "2")
                det.set_flag(flag_relation[f"j_out_fuel_g{g}"], "0")
                detectors.append(det)
                detectors_relation["fuel"]["surface"][s][g] = det

        return detectors, detectors_relation, flag_counter

    def __helper_coolant_detectors(self, fuel_cell, coolant_cell, detectors, detectors_relation, flag_counter):
        energy_bins = self.energy_grid.bins_names_relation
        flag_relation = { }

        total_rate_detectors = {}
        # Total reaction rate for each energy_bin
        for g in range(self.energy_grid.energy_groups):
            name = f"total_rate_coolant_g{g}"
            det = Detector(name)
            det.set_cell(coolant_cell.id)
            det.set_response("-1", coolant_cell.content.name)
            det.set_energy_bins(energy_bins[g])
            det.set_flag(flag_counter, "1")
            flag_relation[f"coolant_total_rate_g{g}"] = flag_counter
            # detectors.append(det)
            # detectors_relation["coolant"]["total"][g] = det
            total_rate_detectors[g] = det
            flag_counter += 1
            
        # Coolant to coolant, fuel and surf
        for g in range(self.energy_grid.energy_groups):

            for gp in range(self.energy_grid.energy_groups):
                # COOLANT ----> COOLANT
                name = f"coolant_coolant_g{g}_to_g{gp}"
                det = Detector(name)
                det.set_cell(coolant_cell.id)
                det.set_response("-1", coolant_cell.content.name)
                det.set_energy_bins(energy_bins[gp])
                det.set_flag(flag_relation[f"coolant_total_rate_g{g}"], "2")
                det.set_flag(flag_relation[f"coolant_total_rate_g{g}"], "0")
                det.set_flag(flag_relation[f"coolant_total_rate_g{gp}"], "1")
                detectors.append(det)
                detectors_relation["coolant"]["coolant"][g][gp] = det

        for g in range(self.energy_grid.energy_groups):
            detectors.append(total_rate_detectors[g])
            detectors_relation["coolant"]["total"][g] = total_rate_detectors[g]

        for g in range(self.energy_grid.energy_groups):
            for gp in range(self.energy_grid.energy_groups):
                # COOLANT -----> FUEL
                name = f"coolant_fuel_g{g}_to_g{gp}"
                det = Detector(name)
                det.set_cell(fuel_cell.id)
                det.set_response("-1", fuel_cell.content.name)
                det.set_energy_bins(energy_bins[gp])
                det.set_flag(flag_relation[f"coolant_total_rate_g{g}"], "2")
                det.set_flag(flag_relation[f"coolant_total_rate_g{g}"], "0")
                detectors.append(det)
                detectors_relation["coolant"]["fuel"][g][gp] = det

        for g in range(self.energy_grid.energy_groups):
            for gp in range(self.energy_grid.energy_groups):
                # COOLANT -----> SURFACES
                for s in self.closing_surface_ids:
                    name = f"coolant_surface{s}_g{g}_to_g{gp}"
                    det = Detector(name)
                    det.set_surface_det(s, self.surface_direction[s]["outward"])
                    det.set_energy_bins(energy_bins[gp])
                    det.set_flag(flag_relation[f"coolant_total_rate_g{g}"], "2")
                    det.set_flag(flag_relation[f"coolant_total_rate_g{g}"], "0")
                    detectors.append(det)
                    detectors_relation["coolant"]["surface"][s][g][gp] = det


        return detectors, detectors_relation, flag_counter

    def __helper_surface_detectors(self, fuel_cell, coolant_cell, detectors, detectors_relation, flag_counter):
        energy_bins = self.energy_grid.bins_names_relation
        flag_relation = { }

        # Incoming neutrons
        for g, bin_name in energy_bins.items():
            for s in self.closing_surface_ids:
                name = f"surface_{s}_jin_g{g}"
                det = Detector(name)
                det.set_surface_det(s, self.surface_direction[s]["inward"])
                det.set_energy_bins(bin_name)
                det.set_flag(flag_counter, "1")
                flag_relation[f"surf_{s}_jin_g{g}"] = flag_counter
                detectors.append(det)
                detectors_relation["surfaces"][s]["incoming"][g] = det
                flag_counter += 1
        
        # Surf to coolant
        for g, bin_name in energy_bins.items():
            for s in self.closing_surface_ids:
                name = f"surface_{s}_to_coolant_g{g}"
                det = Detector(name)
                det.set_cell(coolant_cell.id)
                det.set_response("-1", coolant_cell.content.name)
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "2")
                det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "0")
                detectors.append(det)
                detectors_relation["surfaces"][s]["coolant"][g] = det

        # Surf to fuel
        for g, bin_name in energy_bins.items():
            for s in self.closing_surface_ids:
                name = f"surface_{s}_to_fuel_g{g}"
                det = Detector(name)
                det.set_cell(fuel_cell.id)
                det.set_response("-1", fuel_cell.content.name)
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "2")
                det.set_flag(flag_relation[f"surf_{s}_jin_g{g}"], "0")
                detectors.append(det)
                detectors_relation["surfaces"][s]["fuel"][g] = det

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
                    detectors.append(det)
                    detectors_relation["surfaces"][s][sp][g] = det

        return detectors, detectors_relation, flag_counter

