from typing import Dict
from Shynt.api_py.Geometry.surfaces import Hexagon
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderYtype
from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ
from Shynt.api_py.Geometry.surfaces import Surface
from Shynt.api_py.Geometry.surfaces import PieQuadrant


from Shynt.api_py.Geometry.regions import Region, SurfaceSide
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.universes import Lattice, Pin, SquareLattice, Universe
from Shynt.api_py.Geometry.utilities_geometry import get_all_surfaces_in_a_cell, get_materials_in_cell
from Shynt.api_py.materials import Material
from Shynt.api_py.Serpent.detectors import Detector
from Shynt.api_py.Geometry.universes import Root
import os
import sys


class SerpentInputFile():

  def __init__(self, 
    coarse_node, regions, name, root,  xs_generation=False, cell=None,
    type_calculation='criticality'
  ):
    # print(name)
    self.coarse_node = coarse_node
    # self.cell = coarse_node.cell
    self.regions = list(regions.values())
    self.name = name
    self.root = root
    self.xs_generation = xs_generation
  
    self.libraries = root.libraries
    self.energy_grid = root.energy_grid
    self.mcparams = root.mcparams
    self.global_id = coarse_node.id # is global node id 
    self.detector_surfs = {}

    self.surfaces = {}
    self.surfaces_ids = []
    
    self.xs_gcu = {}
    self.type_of_detectors = ""
    self.detectors_relation = {}
    self.detectors_region = None
    
    with open(name, "w") as self.__file:
      self.__write_title()
      self.__write_material()
      self.__write_libraries()
      # self.__file.write("\n\nset bc 2\n")
      self.__write_mc_params(cell, type_calculation)
      self.__write_energy_grid()
      if xs_generation:
        geometry, xs_gcu = self.coarse_node.get_gcu_geometry(
          self.energy_grid.name
        )
        self.xs_gcu = xs_gcu
        self.__file.write(geometry)
      else:
        geometry, detector_surfs = self.coarse_node.get_serpent_geometry()
        self.__file.write(geometry)
        self.detector_surfs = detector_surfs
      # self.__file.write("\n\n plot 3 500 500\n\n")
        

  def write_detectors(self,
    type_, reg_id=None
  ):
    ene = self.energy_grid.name
    with open(self.name, "a") as self.__file:
      coarse_node = self.coarse_node
      det_syntax = ""
      det_rel = {}
      if type_ == "region_fuel":
        det_syntax, det_rel = coarse_node.get_serpent_detectors_fuel_region(
          reg_id, ene
        )
      elif type_ == "region_nonFuel":
        det_syntax, det_rel = coarse_node.get_serpent_detectors_nonFuel_region(
          reg_id, ene
        )
      elif type_ == "surfaces":
        det_syntax, det_rel = coarse_node.get_serpent_detectors_surfaces(
          ene
        )

      self.type_of_detectors = type_
      self.detectors_relation = det_rel
      self.detectors_region = reg_id
      self.__file.write(det_syntax)

  def __write_title(self):
    file_title = self.name.split("/")[-2] + "/" + self.name.split("/")[-1]
    self.__file.write(f"set title \"{file_title}\"\n\n")

  def __write_material(self):
    written_materials = []
    for cell in self.regions:
      mat = cell.content 
      if mat.name == "void":
        continue
      if mat.name not in written_materials:
        syntax = mat.serpent_syntax
        self.__file.write(syntax+"\n")
        written_materials.append(mat.name)

  def __write_libraries(self):
    self.__file.write(self.libraries.serpent_syntax)

  def __write_mc_params(self, cell, type_calculation):
    if type_calculation == 'criticality':
      self.__file.write(self.mcparams.serpent_syntax_criticality())
    elif type_calculation == 'source':
      material = cell.content
      self.__file.write("\n")
      cell_id = cell.id
      if self.xs_generation:
         cell_id += 1000
      self.__file.write(
        self.mcparams.serpent_syntax_src_calc(
          self.energy_grid,
          f'{cell_id}_{material.name}', # src name
          cell_id,
        )
      )
      self.__file.write("\n")

  def __write_energy_grid(self, syntax="complete"):
    if syntax == "by_bin":
      self.__file.write(self.energy_grid.serpent_syntax_by_bins())
    elif syntax == "complete":
      self.__file.write(self.energy_grid.serpent_syntax())
    














class SerpentInputFileDetectorsRegion(SerpentInputFile):
  """
  #! DPRECATED
  """
  def __init__(self, coarse_node, regions, name, root, reg_id):
    super().__init__(coarse_node, regions, name, root)
    self.detector_flags = []
    self.surfaces_syntax = []
    self.surface_for_detectors = self.detector_surfs

    self.closing_surface_ids = []
    self.surface_direction = {}
    self.material_cell_ids_relation = None
    self.isFuel_relation = {}
    self.detectors = []
    self.flag_counter = 1
    self.detectors_relation = { }
    self.region_id = reg_id
    self.specific = ""

    # initialize detectors_relation variable  --------------------------------
    # if "regions" not in self.detectors_relation:
    #     self.detectors_relation["regions"] = {}
    # self.detectors_relation["regions"][self.region_id] = {  
    #     "regions": {
    #         r.cell.id: {} for r in self.regions if r.cell.id != self.region_id
    #     },
    #     "surfaces" : {
    #         s: {} for s in self.closing_surface_ids
    #     }
    # }
    # -------------------------------------------------------------------------

    with open(self.name, "a") as self.__file:
      # self.__write_detectors()
      pass
      

  def __write_detectors(self):
    # Getting surfaces for detectors -----------------------------------------

    
    # getting detectors
    regions_dict = {r.cell.id: r for r in self.regions}

    print(regions_dict)
    # Region detectors
    isFuel = self.isFuel_relation[self.region_id][1]
    if isFuel: # Is fuel
      # Fuel detectors -------------------------------------------------------
      self.specific = "region_fuel"

      if self.root.model_cell.local_mesh.type == "fuel_cross":
        self.__generate_fuel_detectors_cross_mesh(regions_dict)
      elif "pie" in self.root.model_cell.local_mesh.type:
        self.__generate_fuel_detectors_cross_mesh(regions_dict)
      elif self.root.model_cell.local_mesh.type == "cell":
        self.__generate_fuel_detectors_mat_mesh(regions_dict)
      elif self.root.model_cell.local_mesh.type == "material":
        self.__generate_fuel_detectors_mat_mesh(regions_dict)
    else: # Is not Fuel
      # Non-fuel detectors ----------------------------------------------------
      self.specific = "region_nonFuel"
      self.__generate_nonFuel_detectors(regions_dict)
    
    
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
      """
          
      """
      closing_surf = self.cell.region.surface 
      surfaces = self.coarse_node.geometry_info["surfaces_for_detectors"]
      surfaces_boundary = surfaces["boundary"]
      self.closing_surface_ids = list(surfaces_boundary.keys())
      # self.surface_direction = closing_surf.get_neutron_current_directions()
      self.surface_direction = surfaces["current_directions"]


      surfaces_to_write = ""
      for id_, syntax in surfaces_boundary.items():
          surfaces_to_write += syntax

      fuel_surfaces = surfaces["fuel"]
      for id_, syntax in fuel_surfaces.items():
          self.surface_direction[id_] = {"inward": "-1", "outward": "1"}
          surfaces_to_write += syntax + "\n"

      # ? build fuel cells relation ---------------
      universe_cells = self.cell.content.cells
      for c_id, cell in universe_cells.items():
          if isinstance(cell.content, Material):
              if cell.content.isFuel:
                  self.isFuel_relation[cell.id] = (cell.content.name, True)
              else:
                  self.isFuel_relation[cell.id] = (cell.content.name, False)    
      return surfaces_to_write

  def __generate_fuel_detectors_mat_mesh(self, regions_dict):
      flag_relation = { }
      
      fuel_cell = regions_dict[self.region_id].cell


      bin_name = self.energy_grid.name
      # Total reaction rate for each energy_bin
      name = f"total_rate_reg{fuel_cell.id}"
      det = Detector(
          name, 
          cells=[self.region_id], 
          response=("-1",fuel_cell.content.name), 
          energy_grid=bin_name
      )
      self.detectors_relation["regions"][self.region_id]["total"] = det
      self.detectors.append(det)


      surface_id = fuel_cell.region.surface.id
      # Surface detector. Inward neutrons to the fuel
      name = f"j_in_reg{fuel_cell.id}"
      det = Detector(
          name, 
          surface=(surface_id, self.surface_direction[surface_id]["inward"]),
          energy_grid=bin_name,
          flags=[(self.flag_counter, "1")]
      )
      flag_relation[f"j_in_reg{fuel_cell.id}"] = self.flag_counter
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["incoming"] = det


      # Surface detector. Outward neutrons from the fuel
      name = f"j_out_reg{fuel_cell.id}"
      det = Detector(
          name, 
          surface=(surface_id, self.surface_direction[surface_id]["outward"]),
          energy_grid=bin_name,
          flags=[(self.flag_counter, "3"), (self.flag_counter+1, "1")]
      )
      flag_relation[f"j_out_reg{fuel_cell.id}"] = self.flag_counter + 1
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["outcoming"] = det
      self.flag_counter += 2


      # All to fuel
      name = f"all_to_reg{fuel_cell.id}"
      det = Detector(
          name, 
          cells=[fuel_cell.id], 
          response=("-1", fuel_cell.content.name), 
          energy_grid=bin_name,
          flags=[(flag_relation[f"j_in_reg{fuel_cell.id}"], "2"), (flag_relation[f"j_in_reg{fuel_cell.id}"], "0")]
      )
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["all_to_fuelReg"] = det


      # Fuel to coolant (or other regions)
      for reg in self.regions:
          if reg.cell.content.name == "void":
              continue
          if reg.cell.id != self.region_id:
              name = f"reg{fuel_cell.id}_to_reg{reg.cell.id}"
              det = Detector(
                  name, 
                  cells=[(reg.cell.id)], 
                  response=("-1", reg.cell.content.name), 
                  energy_grid=bin_name,
                  flags=[(flag_relation[f"j_out_reg{fuel_cell.id}"], "2"), (flag_relation[f"j_out_reg{fuel_cell.id}"], "0")]
              )
              self.detectors.append(det)
              self.detectors_relation["regions"][self.region_id]["regions"][reg.cell.id] = det

      # Fuel to surf
      for s in self.closing_surface_ids:
          name = f"reg{fuel_cell.id}_to_surface{s}"
          det = Detector(
              name, 
              surface=(s, self.surface_direction[s]["outward"]),
              energy_grid=bin_name,
              flags=[(flag_relation[f"j_out_reg{fuel_cell.id}"], "2"), (flag_relation[f"j_out_reg{fuel_cell.id}"], "0")]
          )
          self.detectors.append(det)
          self.detectors_relation["regions"][self.region_id]["surfaces"][s] = det


  def __generate_fuel_detectors_cross_mesh(self, regions_dict):
      """
      
          Pad surfaces are used and is the same set of detectors 
          than mat_mesh
  
      """


      flag_relation = { }
      
      fuel_cell = regions_dict[self.region_id].cell
      bin_name = self.energy_grid.name
      fuel_cell_surf = fuel_cell.region.surface

      # * Total reaction rate for each energy_bin ----------------------------------------------
      name = f"total_rate_reg{fuel_cell.id}"
      det = Detector(
          name, 
          cells=[self.region_id], 
          response=("-1",fuel_cell.content.name), 
          energy_grid=bin_name
      )
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["total"] = det

      # * Surface detector. Inward neutrons to the fuel through the circle ---------------------
      
      name = f"j_in_reg{fuel_cell.id}"
      det = Detector(
          name, 
          surface=(fuel_cell_surf.id, self.surface_direction[fuel_cell_surf.id]["inward"]),
          flags=[(self.flag_counter, "1")],
          energy_grid=bin_name
      )
      flag_j_in = self.flag_counter
      flag_relation[f"j_in_reg{fuel_cell.id}"] = self.flag_counter
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["incoming"] = det


      # !Surface detector. Outward neutrons from the fuel ---------------------------------------
      # * Through Circle ----------------------------------------------------------------------
      name = f"j_out_reg{fuel_cell.id}"
      det = Detector(
          name, 
          surface=(fuel_cell_surf.id, self.surface_direction[fuel_cell_surf.id]["outward"]),
          flags=[(self.flag_counter, "3"), (self.flag_counter+1, "1")],
          energy_grid=bin_name
      )
      flag_relation[name] = self.flag_counter + 1
      flag_j_out = self.flag_counter + 1
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["outcoming"] = det
      

      # everything to region --------------------------------------------------------
      name = f"all_to_reg{fuel_cell.id}"
      det = Detector(
          name,
          cells=[fuel_cell.id],
          response=("-1", fuel_cell.content.name),
          flags=[(flag_j_in, "2"), (flag_j_in, "0")],
          energy_grid=bin_name
      )
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["all_to_fuelReg"] = det

      # Fuel to  other regions
      for reg in self.regions:
          flags = [(flag_j_out, "2"), (flag_j_out, "0")]
          name = f"reg{fuel_cell.id}_to_reg{reg.cell.id}"
          if reg.cell.id != self.region_id:
              det = Detector(
                  name,
                  cells=[reg.cell.id],
                  response=("-1", reg.cell.content.name),
                  flags=flags,
                  energy_grid=bin_name
              )
              self.detectors.append(det)
              self.detectors_relation["regions"][self.region_id]["regions"][reg.cell.id] = det
          
          
      # Fuel to surf
      for s in self.closing_surface_ids:
          name = f"reg{fuel_cell.id}_to_surface{s}"
          det = Detector(
              name,
              surface=(s, self.surface_direction[s]["outward"]),
              flags=[(flag_j_out, "2"), (flag_j_out, "0")],
              energy_grid=bin_name
          )
          self.detectors.append(det)
          self.detectors_relation["regions"][self.region_id]["surfaces"][s] = det
      

  def __generate_nonFuel_detectors(self, regions_dict):
      flag_relation = { }
      coolant_cell = regions_dict[self.region_id].cell
      bin_name = self.energy_grid.name
      # print("non Fuel detectors")
      # Total reaction rate for each energy_bin
      name = f"total_rate_reg{coolant_cell.id}"
      det = Detector(
          name, 
          cells=[coolant_cell.id], 
          response=("-1", coolant_cell.content.name), 
          energy_grid=bin_name,
          flags=[(self.flag_counter, "1")]
      )
      flag_relation[f"reg{coolant_cell.id}_total_rate"] = self.flag_counter
      total_rate_detector = det
      self.flag_counter += 1
      self.detectors_relation["regions"][self.region_id]["total"] = total_rate_detector
      
      # COOLANT ----> COOLANT
      name = f"reg{coolant_cell.id}_reg{coolant_cell.id}"
      det = Detector(
          name, 
          cells=[coolant_cell.id], 
          response=("-1", coolant_cell.content.name), 
          energy_grid=bin_name,
          flags=[
              (flag_relation[f"reg{coolant_cell.id}_total_rate"], "2"), 
              (flag_relation[f"reg{coolant_cell.id}_total_rate"], "0"), 
              (flag_relation[f"reg{coolant_cell.id}_total_rate"], "1")
          ]
      )
      self.detectors.append(det)
      self.detectors_relation["regions"][self.region_id]["regions"][self.region_id] = det

      # APPEND TOTAL RATE DETECTOR
      self.detectors.append(total_rate_detector)

      

      # Fuel to coolant (or other regions)

      for reg in self.regions:
          if reg.cell.content.name == "void":
              continue
          if reg.cell.id != self.region_id:
              # for a region that is different to the current coolant region
              # if it is another coolant region check the implementation for
              # coolant to coolant

              # COOLANT -----> REG _reg
              name = f"reg{self.region_id}_reg{reg.cell.id}"
              det = Detector(
                  name, 
                  cells=[reg.cell.id], 
                  response=("-1", reg.cell.content.name), 
                  energy_grid=bin_name,
                  flags=[
                      (flag_relation[f"reg{coolant_cell.id}_total_rate"], "2"), 
                      (flag_relation[f"reg{coolant_cell.id}_total_rate"], "0"), 
                  ]
              )
              self.detectors.append(det)
              self.detectors_relation["regions"][self.region_id]["regions"][reg.cell.id] = det

      
      # COOLANT -----> SURFACES
      for s in self.closing_surface_ids:
          
          name = f"reg{self.region_id}_surface{s}" # it should be coolant_cell.id but it cause conflicts with all the serpent files ran in the past
          det = Detector(
              name, 
              surface=(s, self.surface_direction[s]["outward"]),
              energy_grid=bin_name,
              flags=[
                  (flag_relation[f"reg{coolant_cell.id}_total_rate"], "2"), 
                  (flag_relation[f"reg{coolant_cell.id}_total_rate"], "0"), 
              ]
          )
          self.detectors_relation["regions"][self.region_id]["surfaces"][s] = det
          self.detectors.append(det)

class SerpentInputFileDetectorsSurface(SerpentInputFile):
  """
  #! DPRECATED
  """
  def __init__(self, coarse_node, regions, name, root) -> None:
    super().__init__(coarse_node, regions, name, root)
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
    self.specific = "surfaces"


    with open(self.name, "a") as self.__file:
      # self.__write_outside_cell()
      # self.__write_detectors()
      pass
  
  def __write_detectors(self):
      # Getting surfaces for detectors -----------------------------------------
      self.__file.write("% ----- Surface for detectors\n")
      surface_for_detectors = self.__get_surface_for_detectors()

      self.__file.write(surface_for_detectors)
      
      # getting detectors
      regions_dict = {r.cell.id: r for r in self.regions}

      # Surface detectors ----------------------------------------------------
      # self.__helper_surface_detectors(regions_dict)
      self.__helper_surface_detectors(regions_dict)
      
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
      # surface_for_detectors = ""
      # closing_surf = self.cell.region.surface 

      # # surfaces_in_closing = self.coarse_node.fictional_surfaces
      # surfaces_in_closing = closing_surf.get_surface_relation()
      # if isinstance(closing_surf, InfiniteHexagonalCylinderXtype) or isinstance(closing_surf, InfiniteHexagonalCylinderYtype):
      #     self.closing_surface_ids = list(surfaces_in_closing.keys())
      # else:
      #     self.closing_surface_ids = list(surfaces_in_closing.keys())

      # self.surface_direction = closing_surf.get_neutron_current_directions()

      # for surf in surfaces_in_closing.values():
      #     surface_for_detectors += surf.serpent_syntax_exact_position

      closing_surf = self.cell.region.surface 
      surfaces = self.coarse_node.geometry_info["surfaces_for_detectors"]
      surfaces_boundary = surfaces["boundary"]
      self.closing_surface_ids = list(surfaces_boundary.keys())
      # self.surface_direction = closing_surf.get_neutron_current_directions()
      self.surface_direction = surfaces["current_directions"]


      surfaces_to_write = ""
      for id_, syntax in surfaces_boundary.items():
          surfaces_to_write += syntax

      fuel_surfaces = surfaces["fuel"]
      for id_, syntax in fuel_surfaces.items():
          self.surface_direction[id_] = {"inward": "-1", "outward": "1"}
          surfaces_to_write += syntax + "\n"

      # ? build fuel cells relation ---------------
      universe_cells = self.cell.content.cells
      for c_id, cell in universe_cells.items():
          if isinstance(cell.content, Material):
              if cell.content.isFuel:
                  self.isFuel_relation[cell.id] = (cell.content.name, True)
              else:
                  self.isFuel_relation[cell.id] = (cell.content.name, False)

      return surfaces_to_write
  
  def __helper_surface_detectors(self, regions_dict):
      

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
          det = Detector(
              name, 
              surface=(s, self.surface_direction[s]["inward"]),
              energy_grid=bin_name,
              flags=[(self.flag_counter, "1")]
          )
          flag_relation[f"surf_{s}_jin"] = self.flag_counter
          self.detectors.append(det)
          self.detectors_relation["surfaces"][s]["incoming"] = det
          self.flag_counter += 1
      
      # Surf to regions
      for reg in self.regions:
          if reg.cell.content.name == "void":
              continue
          for s in self.closing_surface_ids:
              name = f"surface_{s}_to_reg{reg.cell.id}"
              det = Detector(
                  name, 
                  cells=[reg.cell.id],
                  response=("-1", reg.cell.content.name),
                  energy_grid=bin_name,
                  flags=[(flag_relation[f"surf_{s}_jin"], "2"), (flag_relation[f"surf_{s}_jin"], "0")]
              )
              self.detectors.append(det)
              self.detectors_relation["surfaces"][s]["regions"][reg.cell.id] = det

      # Surf to surf
      for s in self.closing_surface_ids:
          for sp in self.closing_surface_ids:
              name = f"surface_{s}_to_surf{sp}"
              det = Detector(
                  name, 
                  surface=(sp, self.surface_direction[sp]["outward"]),
                  energy_grid=bin_name,
                  flags=[(flag_relation[f"surf_{s}_jin"], "2"), (flag_relation[f"surf_{s}_jin"], "0")]
              )
              self.detectors.append(det)
              self.detectors_relation["surfaces"][s]["surfaces"][sp] = det

class SerpentInputFileDetectorsXsGeneration(SerpentInputFile):
  """
  #! DPRECATED
  """
  def __init__(self, coarse_node, regions, name, root) -> None:
    super().__init__(coarse_node, regions, name, root, xs_generation=True)
    with open(self.name, "a") as self.__file:
      
      self.__file.write(f"\nset nfg {self.energy_grid.name}\n")
       
class SerpentInputFileReferenceFlux():
  """
  
  #! DPRECATED
      
  Parameters:
  ----------
  coarse_node:      
    Coarse node corresponding to the serpent file
  id_coarse:        
    ID of the coarse node corresponding to the serpent file
  regions:          
    Regions inside the coarse node
  name:             
    Name of the input file (absolut path)
  libraries:        
    Serpent libraries object
  energyGrifd:      
    Grid object (energy groups)
  mc_params:        
    MontecarloParams object
  type_dectectors:  
    Type of detectors ("region", "surfaces", None). None is used 
    for XS generation
  region_id: 
    Region ID of reference for the detectors
  specific:
    Name of type of file: "region-fuel", "region-coolant", "surfaces". 
    This is to know which material we are interested in for the detectors

  
  
  Attributes:   
  ----------
      
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
      # --------------------------------------------------------
      # self.region_id = region_id # This variable is for 
      # self.specific = specific
      # --------------------------------------------------------

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
    
    



