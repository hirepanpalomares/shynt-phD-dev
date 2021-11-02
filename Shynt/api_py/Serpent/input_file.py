from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ
from Shynt.api_py.Geometry.regions import Region, SurfaceSide
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.universes import Pin, Universe
from Shynt.api_py.materials import Material


import os
import sys

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


    def __init__(self, name, type_):
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
    def __init__(self, cell, id_global, local_nodes, name, libraries, energy, params) -> None:
        self.cell = cell
        self.name = name
        self.libraries = libraries
        self.energy_grid = energy
        self.mcparams = params
        self.global_id = id_global # is del global node 
        self.local_nodes = local_nodes
        
        self.detector_flags = []
        self.surfaces_ids = []
        self.detectors = []
        self.detectors_relation = {}
        with open(name, "w") as self.__file:
            self.write_title()
            self.write_material()
            self.write_geometry()
            self.write_outside_cell()
            self.write_libraries()
            self.write_mc_params()
            self.write_energy_grid()
            self.write_detectors()

    
    def write_title(self):
        self.__file.write(f"set title \"{self.cell.name}\"\n\n")

    def write_geometry(self):
        """
            # Consider if it is better to print the geometry from the local problems
        """
        
        # Write surfaces
        surfaces_in_cell = self.surface_searcher(self.cell)
        self.__file.write("\n\n")
        for surf in surfaces_in_cell:
            self.__file.write(surf)
        self.__file.write("\n\nset bc 2\n\n")
        
        # Write cell
        cell_syntax = self.cell.serpent_syntax()
        
        
        self.__file.write(cell_syntax)

    def write_outside_cell(self):
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

    def surface_searcher(self, cell, surfaces=[]):
        """
            This is a recursive function
        """
        # Whichever cell is received, append corresponding region to surface array
        region = cell.region
        # print(cell)
        # raise SystemExit
        surfaces = self.surfaces_from_region_instance(region)
        
        if isinstance(cell.content, Material):
            # base case
            return surfaces
        elif isinstance(cell.content, Universe):
            universe = cell.content
            universe_cells = universe.cells
            for c in universe_cells:
                surfaces = self.surface_searcher(c, surfaces)
            return surfaces
    
    def surfaces_from_region_instance(self, reg, surfaces=[]):
        if isinstance(reg, SurfaceSide):
            # base case
            surf = reg.surface
            if surf.serpent_syntax not in surfaces:
                surfaces.append(surf.serpent_syntax)
                self.surfaces_ids.append(surf.id)
            return surfaces
        elif isinstance(reg, Region):
            reg1 = reg.child1
            reg2 = reg.child2
            surfaces = self.surfaces_from_region_instance(reg1, surfaces)
            surfaces = self.surfaces_from_region_instance(reg2, surfaces)
            return surfaces

    def write_material(self):
        if isinstance(self.cell.content, Pin):
            materials = self.cell.content.materials
            for mat in materials:
                syntax = mat.serpent_syntax
                self.__file.write(syntax)

    def write_libraries(self):
        self.__file.write(self.libraries.serpent_syntax)
 
    def write_mc_params(self):
        self.__file.write("\n\n")
        self.__file.write(self.mcparams.serpent_syntax)
        self.__file.write("\n\n")

    def write_energy_grid(self):
        self.__file.write(self.energy_grid.serpent_syntax())
        self.__file.write("\n\n")

    def write_detectors(self):
        self.__file.write("% ----- Surface for detectors\n")

        # Surfaces for detectors -----------------------------------------------
        surface_for_detectors = ""
        surface_ids = []
        surface_direction = {}
        closing_surf = self.cell.region.surface 
        if isinstance(closing_surf, InfiniteSquareCylinderZ):
            surf_1 = closing_surf.surf_top      # cell in - side 
            surf_2 = closing_surf.surf_right    # cell in - side
            surf_3 = closing_surf.surf_bottom   # cell in + side
            surf_4 = closing_surf.surf_left     # cell in + side

            # surf T --> outward current = +1 --> inward current = -1
            # surf R --> outward current = +1 --> inward current = -1
            # surf B --> outward current = -1 --> inward current = +1
            # surf L --> outward current = -1 --> inward current = +1

            surface_for_detectors += surf_1.serpent_syntax
            surface_for_detectors += surf_2.serpent_syntax
            surface_for_detectors += surf_3.serpent_syntax
            surface_for_detectors += surf_4.serpent_syntax

            surface_ids.append(surf_1.id)
            surface_ids.append(surf_2.id)
            surface_ids.append(surf_3.id)
            surface_ids.append(surf_4.id)

            surface_direction = {
                surf_1.id: {"inward": "-1", "outward": "1"},
                surf_2.id: {"inward": "-1", "outward": "1"},
                surf_3.id: {"inward": "1", "outward": "-1"},
                surf_4.id: {"inward": "1", "outward": "-1"},
            }

        
        self.__file.write(surface_for_detectors)
        
        cell_ids_relation = {c.id: c for c in self.local_nodes}
        # TODO: Checar como hacerle para poner la direccion de la surface en el detector
        detectors_relation = {
            "total_rate": {},
            "surf_count": {},
            "surf_to_region": {},
            "surf_to_surf": {},
            "region_to_region": {},
            "region_to_surf": {}
        }
        detectors = []
        flag_counter = 1

        # Region to All neutrons (for each surface) -------------------------
        for i, cell in cell_ids_relation.items(): # for each region
            # Total reaction rates for each region ----------------------------------
            name = f"total_rate_{i}"
            det = Detector(name, "total_rate")
            det.set_cell(i)
            det.set_response("-1", cell.content.name)
            det.set_flag(flag_counter, "1")
            det.set_energy_bins(self.energy_grid.name)
            detectors.append(det)
            detectors_relation["total_rate"][i] = det
            # Region to region neutrons ---------------------------------------------
            for c in cell_ids_relation.keys():
                name = f"cell_{i}_to_cell_{c}"
                det = Detector(name, "region_to_region")
                det.cell_to_cell = (i, c)
                det.set_cell(c)
                det.set_energy_bins(self.energy_grid.name)
                det.set_response("-1", cell_ids_relation[c].content.name)
                if c == i:
                    det.set_flag(flag_counter, "2")
                else:
                    det.set_flag(flag_counter, "2")
                    det.set_flag(flag_counter, "0")
                    detectors.append(det)
                if i in detectors_relation["region_to_region"]:
                    detectors_relation["region_to_region"][i][c] = det
                else:
                    detectors_relation["region_to_region"][i] = {
                        c: det
                    }
            # Region to surface neutrons --------------------------------------------
            for s in surface_ids:
                name = f"cell_{i}_to_surf_{s}"
                det.set_cell(i)
                det = Detector(name, "region_to_surf")
                det.cell_to_surf = (i, s)
                det.set_surface_det(s, surface_direction[s]["outward"])
                det.set_energy_bins(self.energy_grid.name)
                det.set_flag(flag_counter, "2")
                det.set_flag(flag_counter, "0")
                detectors.append(det)
                if i in detectors_relation["region_to_surf"]:
                    detectors_relation["region_to_surf"][i][s] = det
                else:
                    detectors_relation["region_to_surf"][i] = {
                        s: det
                    }    
            flag_counter += 1

        # Surface to All neutrons (for each surface) -------------------------
        for s in surface_ids:
            name = f"surf_count_{s}"
            det = Detector(name, "surf_to_all")
            det.set_surface_det(s, surface_direction[s]["inward"])
            det.set_energy_bins(self.energy_grid.name)
            det.set_flag(flag_counter, "1")
            detectors.append(det)
            detectors_relation["surf_count"][s] = det
            # surface to region
            for c in cell_ids_relation.keys():
                name = f"surf_{s}_to_cell_{c}"
                det = Detector(name, "surf_to_region")
                det.set_cell(c)
                det.set_energy_bins(self.energy_grid.name)
                det.set_response("-1", cell_ids_relation[c].content.name)
                det.set_flag(flag_counter, "2")
                det.set_flag(flag_counter, "0")    
                detectors.append(det)
                if s in detectors_relation["surf_to_region"]:
                    detectors_relation["surf_to_region"][s][c] = det
                else:
                    detectors_relation["surf_to_region"][s] = {
                        c: det
                    }
            #surface to surface
            for sp in surface_ids:
                name = f"surf_{s}_to_surf_{sp}"
                det = Detector(name, "surf_to_surf")
                det.set_energy_bins(self.energy_grid.name)
                det.set_surface_det(sp, surface_direction[s]["outward"])
                det.set_flag(flag_counter, "2")
                det.set_flag(flag_counter, "0")    
                detectors.append(det)
                if s in detectors_relation["surf_to_surf"]:
                    detectors_relation["surf_to_surf"][s][sp] = det
                else:
                    detectors_relation["surf_to_surf"][s] = {
                        sp: det
                    }
            flag_counter += 1

        self.__file.write("\n\n% ----- Detectors ------\n")
        for det in detectors:
            self.__file.write(det.syntax())

        self.detectors_relation = detectors_relation
        self.detectors = detectors

        if flag_counter > 64:
            print(f"*** Error *** flag number for serpent detectors reached {flag_counter}, must be between 1 - 64")
            print("This happens because Serpent's limit is 64, and internally could happen for excess of regions or\nsurfaces in the local problem")
            raise SystemExit
