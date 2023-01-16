from typing import Dict
from Shynt.api_py.Geometry.surfaces import Hexagon, InfiniteHexagonalCylinderXtype, InfiniteHexagonalCylinderYtype, InfiniteSquareCylinderZ, Surface
from Shynt.api_py.Geometry.regions import Region, SurfaceSide
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.universes import Lattice, Pin, SquareLattice, Universe
from Shynt.api_py.Geometry.utilities_geometry import get_all_surfaces_in_a_cell, get_materials_in_cell
from Shynt.api_py.materials import Material
from Shynt.api_py.Serpent.detectors import Detector

import os
import sys


class SerpentInputFileRmmDetectors():
    
    def __init__(self, 
        coarse_node, 
        id_coarse, 
        regions, 
        name, 
        libraries,
        energyGrid, 
        mc_params, 
        type_detectors=None, 
        region_id=None, 
        specific=None
    ):
        self.coarse_node = coarse_node
        self.cell = coarse_node.cell
        # self.fictional_surfaces = coarse_node.fictional_surfaces
        self.name = name
        self.libraries = libraries
        self.energy_grid = energyGrid
        self.mcparams = mc_params
        self.global_id = id_coarse # is del global node 
        self.regions = list(regions.values())
        self.type_detectors = type_detectors
        # --------------------------------------------------------------------------------------------------
        self.region_id = region_id # This variable is for 
        self.specific = specific
        # --------------------------------------------------------------------------------------------------

        self.detector_flags = []
        self.surfaces_ids = []
        self.surfaces_syntax = []
        self.surfaces = {}
        self.surface_for_detectors = None
        self.closing_surface_ids = []
        self.surface_direction = {}
        self.material_cell_ids_relation = None
        self.isFuel_relation = {}
        self.detectors = []
        self.flag_counter = 1
        self.detectors_relation = { }
        self.xs_gcu = {}

        with open(name, "w") as self.__file:
            self.__write_title()
            self.__write_material()
            self.__write_libraries()
            self.__file.write("\n\nset bc 2\n")
            self.__write_mc_params()
            if self.type_detectors == "xs_generation":
                self.__write_energy_grid()
                self.__file.write(f"\nset nfg {self.energy_grid.name}\n")
                self.__write_geometry()
                self.__write_outside_cell()
            elif self.type_detectors is not None: # "any other" hay: region, surfaces, reference flux
                # self.__write_energy_grid(syntax="by_bin")
                self.__write_energy_grid(syntax="complete")
                self.__write_geometry()
                self.__write_outside_cell()
                self.__write_detectors()


    
    def __write_title(self):
        self.__file.write(f"set title \"{self.cell.name}\"\n\n")

    def __write_material(self):
        materials = get_materials_in_cell(self.cell)
        for mat_name, material in materials.items():
            syntax = material.serpent_syntax
            self.__file.write(syntax+"\n")

    def __write_libraries(self):
        self.__file.write(self.libraries.serpent_syntax)
 
    def __write_mc_params(self):
        self.__file.write("\n")
        self.__file.write(self.mcparams.serpent_syntax)
        self.__file.write("\n")

    def __write_energy_grid(self, syntax="complete"):
        if syntax == "by_bin":
            self.__file.write(self.energy_grid.serpent_syntax_by_bins())
        elif syntax == "complete":
            self.__file.write(self.energy_grid.serpent_syntax())

    def __write_geometry(self):
        """
            # Consider if it is better to print the geometry from the local problems
        """
   
        # Looking for the surfaces in the cell  ---------------------------------
        surfaces = get_all_surfaces_in_a_cell(self.cell)

        self.surfaces.update(surfaces)
        
        self.__file.write("\n\n")
        for s_id, surf in self.surfaces.items():
            self.__file.write(surf.serpent_syntax_exact_position)
            self.surfaces_ids.append(s_id)
        
        # Write all cells inside the cell
        cell_syntax = ""
        if self.type_detectors == "xs_generation":
            cell_syntax, gcu_rel = self.cell.serpent_syntax_gcu()
            self.xs_gcu = gcu_rel
        elif self.type_detectors is not None:
            cell_syntax = self.cell.serpent_syntax()
        self.__file.write(cell_syntax)
    
    def __write_outside_cell(self):
        # Write outside cell
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
            self.__file.write("\n\n")

    def __write_detectors(self):
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
                # self.__helper_fuel_detectors(regions_dict)
                self.__helper_fuel_detectors_less(regions_dict)
            else: # Is not Fuel
                # Non-fuel detectors ----------------------------------------------------
                # self.__helper_nonFuel_detectors(regions_dict)
                self.__helper_nonFuel_detectors_less(regions_dict)
        elif self.type_detectors == "surfaces":
            # Surface detectors ----------------------------------------------------
            # self.__helper_surface_detectors(regions_dict)
            self.__helper_surface_detectors_less(regions_dict)
        
        # Writing detectors in the serpent file --------------------------------
        self.__file.write("\n% ----- Detectors ------\n")
        for det in self.detectors:
            self.__file.write(det.syntax())
        # Checking flag number to not exceed 64 --------------------------------
        try:
            assert(self.flag_counter < 64)
        except AssertionError:
            print(f"*** Error *** flag number for serpent detectors reached {self.flag_counter}, must be between 1 - 64")
            print("This happens because Serpent's limit is 64, and internally could happen for excess of regions or\nsurfaces in the local problem")
            raise SystemExit

    def __get_surface_for_detectors(self):
        surface_for_detectors = ""
        closing_surf = self.cell.region.surface 

        # surfaces_in_closing = self.coarse_node.fictional_surfaces
        surfaces_in_closing = closing_surf.get_surface_relation()
        if isinstance(closing_surf, InfiniteHexagonalCylinderXtype) or isinstance(closing_surf, InfiniteHexagonalCylinderYtype):
            self.closing_surface_ids = list(surfaces_in_closing.keys())
        else:
            self.closing_surface_ids = list(surfaces_in_closing.keys())

        self.surface_direction = closing_surf.get_neutron_current_directions()

        for surf in surfaces_in_closing.values():
            surface_for_detectors += surf.serpent_syntax_exact_position

        # Adding surfaces used by detectors from inside the pin cell
        self.material_cell_ids_relation = {}
        universe_cells = self.cell.content.cells
        for c_id, cell in universe_cells.items():
            if isinstance(cell.content, Material):
                if cell.content.isFuel:
                    surf = cell.region.surface
                    if surf.id not in self.surfaces_ids:
                        surface_for_detectors += surf.serpent_syntax_exact_position
                    self.surface_direction[surf.id] = {"inward": "-1", "outward": "1"}
                    self.isFuel_relation[cell.id] = (cell.content.name, True)
                else:
                    self.isFuel_relation[cell.id] = (cell.content.name, False)
        return surface_for_detectors
    
    def __add_surfaces(self, surfaces):
        pass

    def __helper_fuel_detectors(self, regions_dict):
        energy_bins = self.energy_grid.bins_names_relation
        groups = self.energy_grid.energy_groups

        flag_relation = { }
        
        # initialize detectors_relation variable ----------------------------------
        if "regions" not in self.detectors_relation:
            self.detectors_relation["regions"] = {}
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
        # -------------------------------------------------------------------------


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

    def __helper_nonFuel_detectors(self, regions_dict):
        energy_bins = self.energy_grid.bins_names_relation
        groups = self.energy_grid.energy_groups

        flag_relation = { }

        # initialize detectprs_relation variable ----------------------------------
        if "regions" not in self.detectors_relation:
            self.detectors_relation["regions"] = {}
        self.detectors_relation["regions"][self.region_id] = {
            "total": {g: None for g in range(groups)},
            "regions": {
                r.cell.id: {g: {} for g in range(groups)} for r in self.regions
            },
            "surfaces": {
                s: {g: {} for g in range(groups)} for s in self.closing_surface_ids
            },
        }
        # -------------------------------------------------------------------------


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
                if g < gp:
                    continue # To avoid upscaterring detectors
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
                        if g < gp: # To avoid upscaterring detectors
                            continue 
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
                if g < gp:
                    continue # To avoid upscaterring detectors
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


    def __helper_fuel_detectors_less(self, regions_dict):
        flag_relation = { }
        
        # initialize detectors_relation variable ----------------------------------
        if "regions" not in self.detectors_relation:
            self.detectors_relation["regions"] = {}
        self.detectors_relation["regions"][self.region_id] = {  
            "regions": {
                r.cell.id: {} for r in self.regions if r.cell.id != self.region_id
            },
            "surfaces" : {
                s: {} for s in self.closing_surface_ids
            }
        }
        # -------------------------------------------------------------------------


        fuel_cell = regions_dict[self.region_id].cell

        bin_name = self.energy_grid.name
        # Total reaction rate for each energy_bin
        name = f"total_rate_reg{fuel_cell.id}"
        det = Detector(name)
        det.set_cell(self.region_id)
        det.set_response("-1", fuel_cell.content.name)
        det.set_energy_bins(bin_name)
        self.detectors.append(det)
        self.detectors_relation["regions"][self.region_id]["total"] = det


        surface_id = fuel_cell.region.surface.id
        # Surface detector. Inward neutrons to the fuel
        name = f"j_in_reg{fuel_cell.id}"
        det = Detector(name)
        det.set_surface_det(surface_id, self.surface_direction[surface_id]["inward"])
        det.set_energy_bins(bin_name)
        det.set_flag(self.flag_counter, "1")
        flag_relation[f"j_in_reg{fuel_cell.id}"] = self.flag_counter
        self.detectors.append(det)
        self.detectors_relation["regions"][self.region_id]["incoming"] = det


        # Surface detector. Outward neutrons from the fuel
        name = f"j_out_reg{fuel_cell.id}"
        det = Detector(name)
        det.set_surface_det(surface_id, self.surface_direction[surface_id]["outward"])
        det.set_energy_bins(bin_name)
        det.set_flag(self.flag_counter, "3")
        det.set_flag(self.flag_counter+1, "1")
        flag_relation[f"j_out_reg{fuel_cell.id}"] = self.flag_counter + 1
        self.detectors.append(det)
        self.detectors_relation["regions"][self.region_id]["outcoming"] = det
        self.flag_counter += 2


        # Surf and coolant to fuel
        name = f"all_to_reg{fuel_cell.id}"
        det = Detector(name)
        det.set_cell(fuel_cell.id)
        det.set_response("-1", fuel_cell.content.name)
        det.set_energy_bins(bin_name)
        det.set_flag(flag_relation[f"j_in_reg{fuel_cell.id}"], "2")
        det.set_flag(flag_relation[f"j_in_reg{fuel_cell.id}"], "0")
        self.detectors.append(det)
        self.detectors_relation["regions"][self.region_id]["surface&coolant"] = det


        # Fuel to coolant (or other regions)
        for reg in self.regions:
            if reg.cell.id != self.region_id:
                name = f"reg{fuel_cell.id}_to_reg{reg.cell.id}"
                det = Detector(name)
                det.set_cell(reg.cell.id)
                det.set_response("-1", reg.cell.content.name)
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}"], "2")
                det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}"], "0")
                self.detectors.append(det)
                self.detectors_relation["regions"][self.region_id]["regions"][reg.cell.id] = det

        # Fuel to surf
        for s in self.closing_surface_ids:
            name = f"reg{fuel_cell.id}_to_surface{s}"
            det = Detector(name)
            det.set_surface_det(s, self.surface_direction[s]["outward"])
            det.set_energy_bins(bin_name)
            det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}"], "2")
            det.set_flag(flag_relation[f"j_out_reg{fuel_cell.id}"], "0")
            self.detectors.append(det)
            self.detectors_relation["regions"][self.region_id]["surfaces"][s] = det

    def __helper_nonFuel_detectors_less(self, regions_dict):
        flag_relation = { }

        # initialize detectors_relation variable ----------------------------------
        if "regions" not in self.detectors_relation:
            self.detectors_relation["regions"] = {}
        self.detectors_relation["regions"][self.region_id] = {
            "total": {},
            "regions": {
                r.cell.id: {} for r in self.regions
            },
            "surfaces": {
                s: {} for s in self.closing_surface_ids
            },
        }
        # -------------------------------------------------------------------------


        coolant_cell = regions_dict[self.region_id].cell

        bin_name = self.energy_grid.name

        

        # Total reaction rate for each energy_bin
        name = f"total_rate_reg{coolant_cell.id}"
        det = Detector(name)
        det.set_cell(coolant_cell.id)
        det.set_response("-1", coolant_cell.content.name)
        det.set_energy_bins(bin_name)
        det.set_flag(self.flag_counter, "1")
        flag_relation[f"reg{coolant_cell.id}_total_rate"] = self.flag_counter
        # detectors.append(det)
        # detectors_relation["coolant"]["total"][g] = det
        total_rate_detector = det
        self.flag_counter += 1
        self.detectors_relation["regions"][self.region_id]["total"] = total_rate_detector
        
        # COOLANT ----> COOLANT
        name = f"reg{coolant_cell.id}_reg{coolant_cell.id}"
        det = Detector(name)
        det.set_cell(coolant_cell.id)
        det.set_response("-1", coolant_cell.content.name)
        det.set_energy_bins(bin_name)
        det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate"], "2")
        det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate"], "0")
        det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate"], "1")
        self.detectors.append(det)
        self.detectors_relation["regions"][self.region_id]["regions"][self.region_id] = det

        # APPEND TOTAL RATE DETECTOR
        self.detectors.append(total_rate_detector)

        

        # Fuel to coolant (or other regions)

        for reg in self.regions:
            if reg.cell.id != self.region_id:
                # for a region that is different to the current coolant region
                # if it is another coolant region check the implementation for
                # coolant to coolant

                # COOLANT -----> REG _reg
                name = f"reg{self.region_id}_reg{reg.cell.id}"
                det = Detector(name)
                det.set_cell(reg.cell.id)
                det.set_response("-1", reg.cell.content.name)
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate"], "2")
                det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate"], "0")
                self.detectors.append(det)
                self.detectors_relation["regions"][self.region_id]["regions"][reg.cell.id] = det

        
        # COOLANT -----> SURFACES
        for s in self.closing_surface_ids:
            name = f"reg{reg.cell.id}_surface{s}" # it should be coolant_cell.id but it cause conflicts with all the serpent files ran in the past
            det = Detector(name)
            det.set_surface_det(s, self.surface_direction[s]["outward"])
            det.set_energy_bins(bin_name)
            det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate"], "2")
            det.set_flag(flag_relation[f"reg{coolant_cell.id}_total_rate"], "0")
            self.detectors.append(det)
            self.detectors_relation["regions"][self.region_id]["surfaces"][s] = det

    def __helper_surface_detectors_less(self, regions_dict):
        

        self.detectors_relation["surfaces"] = {
            s: {
                "regions": {
                    r.cell.id: {} for r in self.regions
                },
                "incoming": {},
                "surfaces": {
                    s: {} for s in self.closing_surface_ids
                }
            } for s in self.closing_surface_ids
        }

        flag_relation = { }
        bin_name = self.energy_grid.name

        # Incoming neutrons
        for s in self.closing_surface_ids:
            name = f"surface_{s}_jin"
            det = Detector(name)
            det.set_surface_det(s, self.surface_direction[s]["inward"])
            det.set_energy_bins(bin_name)
            det.set_flag(self.flag_counter, "1")
            flag_relation[f"surf_{s}_jin"] = self.flag_counter
            self.detectors.append(det)
            self.detectors_relation["surfaces"][s]["incoming"] = det
            self.flag_counter += 1
        
        # Surf to regions
        for reg in self.regions:
            for s in self.closing_surface_ids:
                name = f"surface_{s}_to_reg{reg.cell.id}"
                det = Detector(name)
                det.set_cell(reg.cell.id)
                det.set_response("-1", reg.cell.content.name)
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"surf_{s}_jin"], "2")
                det.set_flag(flag_relation[f"surf_{s}_jin"], "0")
                self.detectors.append(det)
                self.detectors_relation["surfaces"][s]["regions"][reg.cell.id] = det

        # Surf to surf
        for s in self.closing_surface_ids:
            for sp in self.closing_surface_ids:
                name = f"surface_{s}_to_surf{sp}"
                det = Detector(name)
                det.set_surface_det(sp, self.surface_direction[sp]["outward"])                    
                det.set_energy_bins(bin_name)
                det.set_flag(flag_relation[f"surf_{s}_jin"], "2")
                det.set_flag(flag_relation[f"surf_{s}_jin"], "0")
                self.detectors.append(det)
                self.detectors_relation["surfaces"][s]["surfaces"][sp] = det



class SerpentInputFileReferenceFlux():
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
            - region_id:        Region ID of reference for the detectors
            - specific:         Name of type of file: "region-fuel", "region-coolant", "surfaces". This is for knowing which material
                                we are interested in for the detectors

        
        ------------------------
        Attributes:
            
        ------------------------
        
    """
    

    def __init__(self, root, name):
        self.root = root
        self.cell = root.model_cell
        self.outside_cell = root.outside_cell
        self.name = name
        self.libraries = root.libraries
        self.energy_grid = root.energy_grid
        self.mcparams = root.mcparams
        self.global_id = self.cell.id 
        # self.type_detectors = type_detectors
        # --------------------------------------------------------------------------------------------------
        # self.region_id = region_id # This variable is for 
        # self.specific = specific
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
            # Since it is a specific class for reference flux: 
            self.__write_surfaces()
            self.__write_system_cells()
            self.__write_main_cell()
            self.__write_outside_cell()
            self.__write_detectors()
    

    def __write_title(self):
        self.__file.write(f"set title \"{self.cell.name}\"\n\n")

    def __write_surfaces(self):
        main_cell_surfaces = get_all_surfaces_in_a_cell(self.cell)
        surfaces_syntax = self.__add_surfaces(main_cell_surfaces)
        self.__file.write("\n\n")
        for surf in surfaces_syntax:
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
        main_cell = self.cell
        syntax = f"\ncell {main_cell.id} {main_cell.universe} "
        
        if isinstance(main_cell.content, Material):
            syntax += f"{main_cell.content.name} "
        elif isinstance(main_cell.content, Universe):
            syntax += f"fill {main_cell.content.name}" 
        
        syntax += main_cell.region.serpent_syntax()
        self.__file.write(syntax)

    def __write_outside_cell(self):
        self.__file.write(self.outside_cell.serpent_syntax())
        
    def __write_material(self):
        materials = get_materials_in_cell(self.cell)
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
        # getting detectors ----------------------------------------------------
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

    def __add_surfaces(self, surfaces):
        for id_s, surf in surfaces.items():
            if id_s not in self.surfaces_ids:
                self.surfaces_ids.append(id_s)
                self.surfaces_syntax.append(surf.serpent_syntax_standard_position)
        return self.surfaces_syntax
    
    




