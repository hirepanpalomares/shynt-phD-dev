from abc import ABC, abstractmethod

class CoarseNode(ABC):

  def __init__(self, id_, type_coarse_mesh):
    self.id = id_
    self.type_coarse_mesh = type_coarse_mesh
    self.surfaces = {}
    self.surfaces_areas = {}
    self.__universe = None # set of cells that form the coarse node
    self.__fine_mesh = None


  @abstractmethod
  def calculate_surfaces(self):
    pass

  def calculate_surfaces_areas(self):
    areas = {}
    for s_id, surf in self.surfaces.items():
      p1, p2 = surf

      area = self.__calculate_euclidean_distance(p1, p2)
      areas[s_id] = area
    self.surfaces_areas = areas
    return areas
  
  def __calculate_euclidean_distance(self, p1, p2):
    from math import sqrt

    x1, y1 = p1 
    x2, y2 = p2
    distance = sqrt(
      (x2-x1) ** 2 + (y2-y1) ** 2
    )
    return distance

  @property
  def universe(self):
    return self.__universe
  
  @universe.setter
  def universe(self, universe):
    self.__universe = universe

  @property
  def fine_mesh(self):
    return self.__fine_mesh
  
  @fine_mesh.setter
  def fine_mesh(self, fine_mesh):
    self.__fine_mesh = fine_mesh


class CoarseNodeSquarePinCell(CoarseNode):

  def __init__(self, id_, type_coarse_mesh, half_pitch, center):
    super().__init__(id_, type_coarse_mesh)
    self.half_pitch = half_pitch
    self.center = center
    self.surfaces = {}
    self.detectors_surfaces = {}


  def calculate_surfaces(self, s_id):
    """Class method to calculate the points of the coarse nodes 
    starting from the lower-left point following a clock-wise sense
    to number the points.It also calculates the surface of the coarse 
    node defined by two points. 
    
    In a SquarePinCell type Coarse Mesh the neumbering of the surface 
    is based on the sides of the square coarse node is the following:
      1. West
      2. North
      3. East
      4. South
    
    Parameters
    ----------
    s_id : int
      Surface identifier from where the numbering for this node will start 
      counting
    
    Returns
    -------
    s_id : int

  
    
    """
    
    surfaces = {}
    # print(self.lattice.left_bottom)
    

    
    cx, cy = self.center
    
    # print(center)
    p1 = (cx-self.half_pitch, cy-self.half_pitch) # lower-left
    p2 = (cx-self.half_pitch, cy+self.half_pitch) # upper-left
    p3 = (cx+self.half_pitch, cy+self.half_pitch) # upper-right
    p4 = (cx+self.half_pitch, cy-self.half_pitch) # lower-right
    
    surf_west = (p1, p2) 
    surf_north = (p2, p3)
    surf_east = (p3, p4)
    surf_south = (p4, p1)
    surfaces = {
      s_id+1: surf_west,
      s_id+2: surf_north,
      s_id+3: surf_east,
      s_id+4: surf_south,
    }
    
    self.surfaces = surfaces
    self.points_node = [p1, p2, p3, p4]
    return s_id + 4

  def get_serpent_geometry(self):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
      serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "
      serpent_syntax += f"{reg_info['surf(+)']}\n"
      
    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n"
    
    boundary_ids = list(self.surfaces.keys()) 

    serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
    half_pitch = self.pitch / 2
    detectors_surfaces = {
      boundary_ids[0]: {
        "syntax": f"surf {boundary_ids[0]} px -{half_pitch}\n",
        "j_in_dir": 1
      },
      boundary_ids[1]: {
        "syntax": f"surf {boundary_ids[1]} py {half_pitch}\n",
        "j_in_dir": -1
      },
      boundary_ids[2]: {
        "syntax": f"surf {boundary_ids[2]} px {half_pitch}\n",
        "j_in_dir": -1
      },
      boundary_ids[3]: {
        "syntax": f"surf {boundary_ids[3]} py -{half_pitch}\n",
        "j_in_dir": 1
      }
    }
    

    for surf_serpent in detectors_surfaces.values():
      serpent_syntax += surf_serpent["syntax"]

    
    self.detectors_surfaces = detectors_surfaces

    return serpent_syntax, detectors_surfaces
    
  def get_gcu_geometry(self, ene):

    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    xs_gcu = {}
    u4gcu = []
    gcu_id = 1
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
      serpent_syntax += f"{reg_info['material']} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      serpent_syntax += f"cell {r_id+2000} pin_fuel{self.id} fill "
      serpent_syntax += f"u4gcu{gcu_id} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      u4gcu.append(f"u4gcu{gcu_id}")
      xs_gcu[r_id] = f"u4gcu{gcu_id}"
      gcu_id += 1

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax, xs_gcu
    
  def get_surfaces_serpent_syntax(self):
    from Shynt.api_py.Geometry.universes import Pin
    serpent_syntax = ""
    node_universe = super().universe

    try:
      assert isinstance(node_universe, Pin)
      pin_levels = node_universe.pin_levels

      assert len(pin_levels) > 1
      # regions = {
      #   cell_id: {
      #     "material":mat_name,
      #     "surf-": id_,
      #     "surf+": id_,
      #   }
      # }

      # cylinders = {
      #   s_id: radius
      # }
      # Closing surface: square with  id = 100

      half_pitch = self.pitch / 2
      closing_square = f"surf closing_surf "
      closing_square += f"sqc 0.0000 0.0000 {half_pitch}\n\n\n"

      cylinders = {}
      regions = {}
      num_surf = 1

      # surfaces ---------------------------------------
      for l, level in enumerate(pin_levels):
        num_cell = level.cell_id
        if level.radius is not None:
          cylinders[f"{num_surf}_geom"] = level.radius
          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": f"{num_surf}_geom",
            "surf(+)": ""
          }
          if l >= 1:
            regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
        else:
          # is surroundings of pin
          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": "closing_surf",
            "surf(+)": f"{num_surf-1}_geom"
          }
        num_surf += 1
      
      serpent_syntax += "\n\n\n"
      for s_id, rad in cylinders.items():
        serpent_syntax += f"surf {s_id} cyl 0.0000 0.0000 {rad}\n"
      serpent_syntax += closing_square
      return serpent_syntax, regions
    except AssertionError:
      raise NotImplementedError
    
  def get_serpent_detectors_fuel_region(self, c_id, ene):
    det_syntax = ""
    det_relation = { 
      "total_rate": "",
      "j_in_fuel": "",
      "j_out_fuel": "",
      "all_to_fuel": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[c_id]
    surf_fuel = cell.region.surface
    radius = surf_fuel.radius
    det_syntax += f"surf fuel_surf cyl 0.0000 0.0000 {radius}\n\n\n\n"
    
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]

    det_syntax += "% Detectors ------------------------------------\n"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id} \n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"
    # Detector  Jin fuel ------------
    det_syntax += f"det j_in_reg{c_id}  ds {'fuel_surf'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_relation["j_in_fuel"] = f"j_in_reg{c_id}"
    # Detector  Jout fuel ------------
    det_syntax += f"det j_out_reg{c_id} ds {'fuel_surf'}  1 "
    det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
    det_relation["j_out_fuel"] = f"j_out_reg{c_id}"
    # Detector All to fuel ------------
    det_syntax += f"det all_to_reg_{c_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {c_id} de {ene}  dfl 1 2  dfl 1 0\n"
    det_relation["all_to_fuel"] = f"all_to_reg_{c_id}"
    for r_id, cell in regions.items():
      if r_id == c_id: continue
      # Detector  fuel region to other region (r_id)------------
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_nonFuel_region(self, c_id, ene):
    det_syntax = "\n\n\n"
    det_relation = { 
      "total_rate": "",
      "same_region": "",
      "region_to_region": {},
      "region_to_surface": {}
    }
    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]
    # Detector region to same region ------------
    det_syntax += f"det reg{c_id}_to_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_relation["same_region"] = f"reg{c_id}_to_reg{c_id}"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}    dfl 1 1\n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    for r_id, cell in regions.items():
      if r_id == c_id: continue
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"

    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    det_relation = { 
      "surface_to_region": {},
      "surface_to_surface": {}
    }
    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    # J_in detectors thrpough the surfaces just to flag the neutrons ----------
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"]
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}\n"
    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      det_relation["surface_to_region"][s_id] = {}
      det_relation["surface_to_surface"][s_id] = {}

      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():
        # Detector surface to region ---------------------
        det_name = f"surface_{s_id}_to_reg{r_id}"
        det_syntax += f"det {det_name} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"
        det_relation["surface_to_region"][s_id][r_id] = det_name
      for s_id_p in self.detectors_surfaces.keys():
        # Detector surface to surface ---------------------
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_name = f"surface_{s_id}_to_surface{s_id_p}"
        det_syntax += f"det {det_name} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
        det_relation["surface_to_surface"][s_id][s_id_p] = det_name

    # print(det_syntax)
    return det_syntax, det_relation

  @property
  def pitch(self):
    return self.half_pitch * 2


class CoarseNodeHexagonalPinCell(CoarseNode):

  def __init__(self, id_, type_coarse_mesh, pincell_wrapper):
    super().__init__(id_, type_coarse_mesh)
    self.wrapper = pincell_wrapper
    self.half_width = pincell_wrapper.half_width
    self.center = pincell_wrapper.center
    self.surfaces = {}
    self.regions_surfaces = {}
    self.cylinders = {}
    self.detectors_surfaces = {}

  def calculate_surfaces(self, s_id):
    """Class method to calculate the points of the coarse nodes 
    for a hexagonal pin_cell mesh (only aplicable for a pin) 
    
    
    
    Parameters
    ----------
    s_id : int
    
    Returns
    -------
    s_id : int
    
    """
    
    surfaces = {}

    p1, p2, p3, p4, p5, p6 = self.wrapper.get_vertex_points()
    
    surf_1 = (p1, p2) 
    surf_2 = (p2, p3)
    surf_3 = (p3, p4)
    surf_4 = (p4, p5)
    surf_5 = (p5, p6)
    surf_6 = (p5, p1)

    surfaces = {
      s_id+1: surf_1,
      s_id+2: surf_2,
      s_id+3: surf_3,
      s_id+4: surf_4,
      s_id+5: surf_5,
      s_id+6: surf_6,

    }
    
    self.surfaces = surfaces
    self.points_node = [p1, p2, p3, p4, p5, p6]
    return s_id + 6

  def get_serpent_geometry(self):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    self.regions_surfaces = regions
    # cells ---------------------------------------
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
      serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "
      serpent_syntax += f"{reg_info['surf(+)']}\n"
      
    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n"
    
    boundary_ids = list(self.surfaces.keys()) 

    serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
    
    detectors_surfaces = {
      boundary_ids[0]: {
        "syntax": f"surf {boundary_ids[0]} py {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[1]: {
        "syntax": f"surf {boundary_ids[1]} px {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[2]: {
        "syntax": f"surf {boundary_ids[2]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[3]: {
        "syntax": f"surf {boundary_ids[3]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[4]: {
        "syntax": f"surf {boundary_ids[4]} px -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[5]: {
        "syntax": f"surf {boundary_ids[5]} py {self.half_width}\n",
        "j_in_dir": -1
      }
    }

    detectors_surfaces[boundary_ids[0]]["syntax"] += f'trans s {boundary_ids[0]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[2]]["syntax"] += f'trans s {boundary_ids[2]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    detectors_surfaces[boundary_ids[3]]["syntax"] += f'trans s {boundary_ids[3]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[5]]["syntax"] += f'trans s {boundary_ids[5]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    

    for surf_serpent in detectors_surfaces.values():
      serpent_syntax += surf_serpent["syntax"]

    
    self.detectors_surfaces = detectors_surfaces

    return serpent_syntax, detectors_surfaces

  def get_gcu_geometry(self, ene):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    xs_gcu = {}
    u4gcu = []
    gcu_id = 1
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
      serpent_syntax += f"{reg_info['material']} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      serpent_syntax += f"cell {r_id+2000} pin_fuel{self.id} fill "
      serpent_syntax += f"u4gcu{gcu_id} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      u4gcu.append(f"u4gcu{gcu_id}")
      xs_gcu[r_id] = f"u4gcu{gcu_id}"
      gcu_id += 1

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax, xs_gcu

  def get_surfaces_serpent_syntax(self):
    from Shynt.api_py.Geometry.universes import Pin
    serpent_syntax = ""
    node_universe = super().universe

    try:
      assert isinstance(node_universe, Pin)
      pin_levels = node_universe.pin_levels

      assert len(pin_levels) > 1
      # regions = {
      #   cell_id: {
      #     "material":mat_name,
      #     "surf-": id_,
      #     "surf+": id_,
      #   }
      # }

      # cylinders = {
      #   s_id: radius
      # }
      # Closing surface: square with  id = 100

      
      closing_surf = f"surf closing_surf "
      closing_surf += f"hexxc 0.0000 0.0000 {self.half_width}\n\n\n"

      cylinders = {}
      regions = {}
      prev_radius = 0.0
      num_surf = 1

      fine_mesh_regs_ids = list(self.fine_mesh.regions.keys())
      # surfaces ---------------------------------------
      for l, level in enumerate(pin_levels):
        num_cell = fine_mesh_regs_ids[l]
        if level.radius is not None:
          cylinders[f"{num_surf}_geom"] = level.radius

          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": f"{num_surf}_geom",
            "surf(+)": ""
          }
          if l >= 1:
            regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
        else:
          # is surroundings of pin
          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": "closing_surf",
            "surf(+)": f"{num_surf-1}_geom"
          }
        num_surf += 1
      
      for s_id, radius in cylinders.items():
        serpent_syntax += f"surf {s_id} cyl 0.0000 0.0000 {radius}\n"
      serpent_syntax += closing_surf
      self.cylinders = cylinders
      return serpent_syntax, regions
    except AssertionError:
      raise NotImplementedError
    
  
  def get_serpent_detectors_fuel_region(self, c_id, ene):
    det_syntax = ""
    det_relation = { 
      "total_rate": "",
      "j_in_fuel": "",
      "j_out_fuel": "",
      "all_to_fuel": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[c_id]
    

    print(self.regions_surfaces)
    surfaces_fuel = self.regions_surfaces[c_id]
    surf_neg = surfaces_fuel['surf(-)']
    surf_pos = surfaces_fuel['surf(+)']
    
    r2 = self.cylinders[surf_neg]

    det_syntax += f"surf fuel_surf1 cyl 0.0000 0.0000 {r2} \n\n\n"

    if surf_pos != '':
      r1 = self.cylinders[surf_pos]
      det_syntax += f"surf fuel_surf2 cyl 0.0000 0.0000 {r1} \n\n\n"
      
    
    
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]

    det_syntax += "% Detectors ------------------------------------\n"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id} \n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    # Detector  Jin fuel ------------ FLAG-1 TO COUNT ALL->FUEL
    det_syntax += f"det j_in1_reg{c_id}  ds {'fuel_surf1'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_relation["j_in_fuel"] = f"j_in_reg{c_id}"
    if surf_pos != '':
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_in2_reg{c_id}  ds {'fuel_surf2'} -1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_out2_reg{c_id}  ds {'fuel_surf2'} 1 "
      det_syntax += f"de {ene} dfl 2 3  dfl 1 1\n"
    else:
      # Detector  Jout fuel ------------
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_relation["j_out_fuel"] = f"j_out_reg{c_id}"
    

    # Detector All to fuel ------------
    det_syntax += f"det all_to_reg_{c_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {c_id} de {ene}  dfl 1 2  dfl 1 0\n"
    det_relation["all_to_fuel"] = f"all_to_reg_{c_id}"
    for r_id, cell in regions.items():
      if r_id == c_id: continue
      # Detector  fuel region to other region (r_id)------------
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_nonFuel_region(self, c_id, ene):
    det_syntax = "\n\n\n"
    det_relation = { 
      "total_rate": "",
      "same_region": "",
      "region_to_region": {},
      "region_to_surface": {}
    }
    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]
    # Detector region to same region ------------
    det_syntax += f"det reg{c_id}_to_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_relation["same_region"] = f"reg{c_id}_to_reg{c_id}"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}    dfl 1 1\n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    for r_id, cell in regions.items():
      if r_id == c_id: continue
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"

    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation
  
  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    det_relation = { 
      "surface_to_region": {},
      "surface_to_surface": {}
    }
    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    # J_in detectors thrpough the surfaces just to flag the neutrons ----------
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"]
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}\n"
    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      det_relation["surface_to_region"][s_id] = {}
      det_relation["surface_to_surface"][s_id] = {}

      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():
        # Detector surface to region ---------------------
        det_name = f"surface_{s_id}_to_reg{r_id}"
        det_syntax += f"det {det_name} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"
        det_relation["surface_to_region"][s_id][r_id] = det_name
      for s_id_p in self.detectors_surfaces.keys():
        # Detector surface to surface ---------------------
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_name = f"surface_{s_id}_to_surface{s_id_p}"
        det_syntax += f"det {det_name} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
        det_relation["surface_to_surface"][s_id][s_id_p] = det_name

    # print(det_syntax)
    return det_syntax, det_relation
  

class CoarseNodeTriangularMesh(CoarseNode):

  def __init__(self, id_, type_coarse_mesh, pitch):
    super().__init__(id_, type_coarse_mesh)
    self.pitch = pitch
    self.surfaces = {}
    self.detectors_surfaces = {}
    self.type_coarse_node = None
  
  def calculate_surfaces(self, surf_points, s_id):
    surfaces = {}

    np = len(surf_points)
    for i in range(np-1):
      p1 = surf_points[i]
      p2 = surf_points[i+1]
      
      surf = (p1,p2)
      surfaces[s_id+1] = surf
      s_id += 1
    
    last_point = surf_points[-1]
    first_point = surf_points[0]
    last_surf = (last_point, first_point)
    surfaces[s_id + 1] = last_surf
    s_id += 1
    
    self.surfaces = surfaces

    return surfaces, s_id

  
class CoarseNodeSquareGridHexPin(CoarseNode):

  def __init__(
    self, id_, type_coarse_mesh, width, height, position, hex_center
  ):
    super().__init__(id_, type_coarse_mesh)
    self.width = width
    self.height = height # this is the radius of the hexagon
    self.position = position
    self.hex_center = hex_center
    self.surfaces = {}
    self.regions_surfaces = {}
    self.detectors_surfaces = {}
  
  def calculate_surfaces(self, s_id):
    """
    
    Parameters
    ----------
    s_id : int
      Surface identifier from where the numbering for this node will start 
      counting
    
    Returns
    -------
    s_id : int

  
    
    """
    
    surfaces = {}
    # print(self.lattice.left_bottom)
    hh = self.height / 2
    cx, cy = self.hex_center
    if self.position == "top_left":
      p1 = (cx-self.width, cy) # lower-left
      p2 = (cx-self.width, cy+hh) # upper-left
      p3 = (cx, cy+self.height) # upper-right
      p4 = (cx, cy) # lower-right
    elif self.position == "top_right":
      p1 = (cx, cy) # lower-left
      p2 = (cx, cy+self.height) # upper-left
      p3 = (cx+self.width, cy+hh) # upper-right
      p4 = (cx+self.width, cy) # lower-right
    elif self.position == "lower_left":
      p1 = (cx-self.width, cy-hh) # lower-left
      p2 = (cx-self.width, cy) # upper-left
      p3 = (cx, cy) # upper-right
      p4 = (cx, cy-self.height) # lower-right
    elif self.position == "lower_right":
      p1 = (cx, cy-self.height) # lower-left
      p2 = (cx, cy) # upper-left
      p3 = (cx+self.width, cy) # upper-right
      p4 = (cx+self.width, cy-hh) # lower-right
    
    surf_west = (p1, p2) 
    surf_north = (p2, p3)
    surf_east = (p3, p4)
    surf_south = (p4, p1)
    surfaces = {
      s_id+1: surf_west,
      s_id+2: surf_north,
      s_id+3: surf_east,
      s_id+4: surf_south,
    }
    
    self.surfaces = surfaces
    self.points_node = [p1, p2, p3, p4]
    return s_id + 4
  
  def get_serpent_geometry(self):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    self.regions_surfaces = regions
    # cells ---------------------------------------
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
      if isinstance(reg_info['surf(-)'], dict):
        serpent_syntax += f"{reg_info['material']} "
        serpent_syntax += f"-{reg_info['surf(-)']['rectangle']} "
        serpent_syntax += f"-{reg_info['surf(-)']['diagonal']} "

      elif isinstance(reg_info['surf(-)'], str):
        serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "
      serpent_syntax += f"{reg_info['surf(+)']}\n"

    serpent_syntax += f"cell void1 pin_fuel{self.id} void closing_diagonal"
    serpent_syntax += f" -closing_rectangle\n"


    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_rectangle\n"

    serpent_syntax += f"cell root_out 0 outside closing_rectangle\n"
    
    serpent_syntax += "\n\nplot 3 500 500\n\n"
    boundary_ids = list(self.surfaces.keys()) 

    serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
    detectors_surfaces = {
      boundary_ids[0]: {
        "syntax": f"surf {boundary_ids[0]} px -{self.width}\n",
        "j_in_dir": 1,
        "trans": False
      },
      boundary_ids[1]: {
        "syntax": f"surf {boundary_ids[1]} py {self.width}\n",
        "j_in_dir": -1,
        "trans": True
      },
      boundary_ids[2]: {
        "syntax": f"surf {boundary_ids[2]} px 0.0\n",
        "j_in_dir": -1,
        "trans": False
      },
      boundary_ids[3]: {
        "syntax": f"surf {boundary_ids[3]} py 0.0\n",
        "j_in_dir": 1,
        "trans": False
      }
    }
    b1 = boundary_ids[1]
    detectors_surfaces[b1]['syntax'] += f'trans s {b1} 0.0 0.0 0.0 0 0 -30\n'
    


    for surf_serpent in detectors_surfaces.values():
      serpent_syntax += surf_serpent["syntax"]

    self.detectors_surfaces = detectors_surfaces

    return serpent_syntax, detectors_surfaces
    
  def get_gcu_geometry(self, ene):
    
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    xs_gcu = {}
    u4gcu = []
    gcu_id = 1

    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
      serpent_syntax += f"{reg_info['material']} "
      serpent_syntax += f"{reg_info['surf(+)']} "

      if isinstance(reg_info['surf(-)'], dict):
        serpent_syntax += f"-{reg_info['surf(-)']['rectangle']} "
        serpent_syntax += f"-{reg_info['surf(-)']['diagonal']} \n"
      elif isinstance(reg_info['surf(-)'], str):
        serpent_syntax += f"-{reg_info['surf(-)']} \n"

      serpent_syntax += f"cell {r_id+2000} pin_fuel{self.id} fill "
      serpent_syntax += f"u4gcu{gcu_id}  {reg_info['surf(+)']} "
      if isinstance(reg_info['surf(-)'], dict):
        serpent_syntax += f"-{reg_info['surf(-)']['rectangle']} "
        serpent_syntax += f"-{reg_info['surf(-)']['diagonal']} \n"
      elif isinstance(reg_info['surf(-)'], str):
        serpent_syntax += f"-{reg_info['surf(-)']} \n"

      u4gcu.append(f"u4gcu{gcu_id}")
      xs_gcu[r_id] = f"u4gcu{gcu_id}"
      gcu_id += 1

    serpent_syntax += f"cell void1 pin_fuel{self.id} void closing_diagonal"
    serpent_syntax += f" -closing_rectangle\n"

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_rectangle\n"

    serpent_syntax += f"cell root_out 0 outside closing_rectangle\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax, xs_gcu
    
  def get_surfaces_serpent_syntax(self):
    from Shynt.api_py.Geometry.universes import Pin
    serpent_syntax = ""
    node_universe = super().universe

    try:
      assert isinstance(node_universe, Pin)
      pin_levels = node_universe.pin_levels

      assert len(pin_levels) > 1

      closing_square = f"surf closing_rectangle "
      closing_square += f"rect {-self.width} {0.0} {0.0} {self.height}\n"
      closing_diagonal = f"surf closing_diagonal py {self.width}\n"
      closing_diagonal+=  f"trans s closing_diagonal "
      closing_diagonal+= "0.0 0.0 0.0 0.0 0.0 -30\n\n\n"

      pads = {}
      regions = {}
      prev_radius = 0.0
      num_surf = 1

      fine_mesh_regs_ids = list(self.fine_mesh.regions.keys())
      # surfaces ---------------------------------------
      for l, level in enumerate(pin_levels):
        num_cell = fine_mesh_regs_ids[l]
        if level.radius is not None:
          pads[f"{num_surf}_geom"] = {
            "r1": prev_radius,
            "r2":  level.radius
          }

          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": f"{num_surf}_geom",
            "surf(+)": "",
            "r1": prev_radius,
            "r2":  level.radius
          }
          prev_radius = level.radius

          if l >= 1:
            regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
        else:
          # is surroundings of pin
          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": {
              "rectangle": "closing_rectangle",
              "diagonal": "closing_diagonal"
            },
            "surf(+)": "last_cyl"
          }
        num_surf += 1
      
      last_cyl_surf = f"surf last_cyl cyl 0.0000 0.0000 {prev_radius}\n\n\n"
      serpent_syntax += "\n\n\n"
      for s_id, radius in pads.items():
        r1 = radius["r1"]
        r2 = radius["r2"]
        serpent_syntax += f"surf {s_id} pad 0.0000 0.0000 {r1} {r2} 180 270\n"

      serpent_syntax += closing_square
      serpent_syntax += closing_diagonal
      serpent_syntax += last_cyl_surf
      return serpent_syntax, regions
    except AssertionError:
      raise NotImplementedError
    
  def get_serpent_detectors_fuel_region(self, c_id, ene):
    det_syntax = ""
    det_relation = { 
      "total_rate": "",
      "j_in_fuel": "",
      "j_out_fuel": "",
      "all_to_fuel": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[c_id]
    r1 = self.regions_surfaces[c_id]["r1"]
    r2 = self.regions_surfaces[c_id]["r2"]

    det_syntax += f"surf fuel_surf pad 0.0000 0.0000 {r1} {r2} 180 270\n\n\n"
    
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]

    det_syntax += "% Detectors ------------------------------------\n"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id} \n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"
    # Detector  Jin fuel ------------
    det_syntax += f"det j_in_reg{c_id}  ds {'fuel_surf'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_relation["j_in_fuel"] = f"j_in_reg{c_id}"
    # Detector  Jout fuel ------------
    det_syntax += f"det j_out_reg{c_id} ds {'fuel_surf'}  1 "
    det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
    det_relation["j_out_fuel"] = f"j_out_reg{c_id}"
    # Detector All to fuel ------------
    det_syntax += f"det all_to_reg_{c_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {c_id} de {ene}  dfl 1 2  dfl 1 0\n"
    det_relation["all_to_fuel"] = f"all_to_reg_{c_id}"
    for r_id, cell in regions.items():
      if r_id == c_id: continue
      # Detector  fuel region to other region (r_id)------------
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_nonFuel_region(self, c_id, ene):
    det_syntax = "\n\n\n"
    det_relation = { 
      "total_rate": "",
      "same_region": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]
    # Detector region to same region ------------
    det_syntax += f"det reg{c_id}_to_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_relation["same_region"] = f"reg{c_id}_to_reg{c_id}"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}    dfl 1 1\n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    for r_id, cell in regions.items():
      if r_id == c_id: continue
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"

    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    det_relation = { 
      "surface_to_region": {},
      "surface_to_surface": {}
    }

    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    boundary_ids = list(self.detectors_surfaces.keys()) 

    
    # J_in detectors through the surfaces just to flag the neutrons ----------
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"]
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}"
      if self.detectors_surfaces[s_id]["trans"]:
        s_left_flag = surface_flags[boundary_ids[0]]
        det_syntax += f" dfl {s_left_flag} 0\n"
      else:
        det_syntax += "\n"

    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      det_relation["surface_to_region"][s_id] = {}
      det_relation["surface_to_surface"][s_id] = {}

      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():
        # Detector surface to region ---------------------
        det_name = f"surface_{s_id}_to_reg{r_id}"
        det_syntax += f"det {det_name} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"
        det_relation["surface_to_region"][s_id][r_id] = det_name
      for s_id_p in self.detectors_surfaces.keys():
        # Detector surface to surface ---------------------
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_name = f"surface_{s_id}_to_surface{s_id_p}"
        det_syntax += f"det {det_name} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
        det_relation["surface_to_surface"][s_id][s_id_p] = det_name

    # print(det_syntax)
    return det_syntax, det_relation


class CoarseNodeSquareGridHexAssembly(CoarseNode):

  def __init__(self, id_, type_coarse_mesh, half_pitch, quadrant):
    super().__init__(id_, type_coarse_mesh)
    self.half_pitch = half_pitch
    self.quadrant = quadrant
    self.surfaces = {}
    self.points_node = []

  
  def calculate_surfaces(self, s_id, rectangle_points):
    """ It calculates the surfaces for a reactangle type node
    
    Parameters
    ----------
    s_id : int
      Surface identifier from where the numbering for this node will start 
      counting
    
    Returns
    -------
    s_id : int

  
    
    """
    x1, x2 = rectangle_points[0]
    y1, y2 = rectangle_points[1]

    
    surfaces = {}
    # print(self.lattice.left_bottom)

    p1 = (x1, y1) # lower-left
    p2 = (x1, y2) # upper-left
    p3 = (x2, y2) # upper-right
    p4 = (x2, y1) # lower-right
    
    surf_west = (p1, p2) 
    surf_north = (p2, p3)
    surf_east = (p3, p4)
    surf_south = (p4, p1)
    surfaces = {
      s_id+1: surf_west,
      s_id+2: surf_north,
      s_id+3: surf_east,
      s_id+4: surf_south,
    }
    
    self.surfaces = surfaces
    self.points_node = [p1, p2, p3, p4]
    return s_id + 4


class CoarseNodeSquareGridHexAssembly_TrapezoidCorner(
  CoarseNodeSquareGridHexAssembly
):

  def __init__(
    self, id_, type_coarse_mesh, half_pitch, quadrant, hex_wrapper
  ):
    super().__init__(id_, type_coarse_mesh, half_pitch, quadrant)
    self.hex_wrapper = hex_wrapper

  def calculate_surfaces(self, s_id, rectangle_points):
    """ It calculates the surfaces for a reactangle type node
    
    Parameters
    ----------
    s_id : int
      Surface identifier from where the numbering for this node will start 
      counting
    
    Returns
    -------
    s_id : int
    """
   
    x1, x2 = rectangle_points[0]
    y1, y2 = rectangle_points[1]
    surfaces = {}
    if self.quadrant == 1:
      vp = self.hex_wrapper.vertex_points[0]
      p1 = (x1, y1)
      p2 = (vp[0],y2)
      p3 = (x2, y2)
      p4 = (x2, y1)
    elif  self.quadrant == 2:
      vp = self.hex_wrapper.vertex_points[1]
      p1 = (x1, y1)
      p2 = (x1,y2)
      p3 = (vp[0], y2)
      p4 = (x2, y1)
    elif  self.quadrant == 3:
      vp = self.hex_wrapper.vertex_points[3]
      p1 = (x1, y1)
      p2 = (x1, y2)
      p3 = (x2, y2)
      p4 = (vp[0], y1)
    elif  self.quadrant == 4:
      vp = self.hex_wrapper.vertex_points[4]
      p1 = (vp[0], y1)
      p2 = (x1, y2)
      p3 = (x2, y2)
      p4 = (x2, y1)
    
    surf_west = (p1, p2) 
    surf_north = (p2, p3)
    surf_east = (p3, p4)
    surf_south = (p4, p1)
    surfaces = {
      s_id+1: surf_west,
      s_id+2: surf_north,
      s_id+3: surf_east,
      s_id+4: surf_south,
    }
    
    self.surfaces = surfaces
    self.points_node = [p1, p2, p3, p4]
    return s_id + 4

  def get_serpent_geometry(self):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    self.regions_surfaces = regions
    # cells ---------------------------------------
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
      if isinstance(reg_info['surf(-)'], dict):
        serpent_syntax += f"{reg_info['material']} "
        serpent_syntax += f"-{reg_info['surf(-)']['rectangle']} "
        serpent_syntax += f"-{reg_info['surf(-)']['diagonal']} "

      elif isinstance(reg_info['surf(-)'], str):
        serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "

      serpent_syntax += f"{reg_info['surf(+)']}\n"

    serpent_syntax += f"cell void1 pin_fuel{self.id} void closing_diagonal"
    serpent_syntax += f" -closing_rectangle\n"


    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_rectangle\n"

    serpent_syntax += f"cell root_out 0 outside closing_rectangle\n"
    
    serpent_syntax += "\n\nplot 3 500 500\n\n"
    boundary_ids = list(self.surfaces.keys()) 

    serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
    width_rectangle = self.points_node[3][0] - self.points_node[0][0]
    height_rectangle = self.points_node[1][1] - self.points_node[0][1]
    detectors_surfaces = {
      boundary_ids[0]: {
        "syntax": f"surf {boundary_ids[0]} px 0.0\n",
        "j_in_dir": 1,
        "trans": True
      },
      boundary_ids[1]: {
        "syntax": f"surf {boundary_ids[1]} py {height_rectangle}\n",
        "j_in_dir": -1,
        "trans": False
      },
      boundary_ids[2]: {
        "syntax": f"surf {boundary_ids[2]} px {width_rectangle}\n",
        "j_in_dir": -1,
        "trans": False
      },
      boundary_ids[3]: {
        "syntax": f"surf {boundary_ids[3]} py 0.0\n",
        "j_in_dir": 1,
        "trans": False
      }
    }
    b1 = boundary_ids[1]
    detectors_surfaces[b1]['syntax'] += f'trans s {b1} 0.0 0.0 0.0 0 0 30\n'
    


    for surf_serpent in detectors_surfaces.values():
      serpent_syntax += surf_serpent["syntax"]

    self.detectors_surfaces = detectors_surfaces

    return serpent_syntax, detectors_surfaces
    
  def get_gcu_geometry(self, ene):
    
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    xs_gcu = {}
    u4gcu = []
    gcu_id = 1

    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
      serpent_syntax += f"{reg_info['material']} "
      serpent_syntax += f"{reg_info['surf(+)']} "

      if isinstance(reg_info['surf(-)'], dict):
        serpent_syntax += f"-{reg_info['surf(-)']['rectangle']} "
        serpent_syntax += f"-{reg_info['surf(-)']['diagonal']} \n"
      elif isinstance(reg_info['surf(-)'], str):
        serpent_syntax += f"-{reg_info['surf(-)']} \n"

      serpent_syntax += f"cell {r_id+2000} pin_fuel{self.id} fill "
      serpent_syntax += f"u4gcu{gcu_id}  {reg_info['surf(+)']} "
      if isinstance(reg_info['surf(-)'], dict):
        serpent_syntax += f"-{reg_info['surf(-)']['rectangle']} "
        serpent_syntax += f"-{reg_info['surf(-)']['diagonal']} \n"
      elif isinstance(reg_info['surf(-)'], str):
        serpent_syntax += f"-{reg_info['surf(-)']} \n"

      u4gcu.append(f"u4gcu{gcu_id}")
      xs_gcu[r_id] = f"u4gcu{gcu_id}"
      gcu_id += 1

    serpent_syntax += f"cell void1 pin_fuel{self.id} void closing_diagonal"
    serpent_syntax += f" -closing_rectangle\n"

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_rectangle\n"

    serpent_syntax += f"cell root_out 0 outside closing_rectangle\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax, xs_gcu
    
  def get_surfaces_serpent_syntax(self):
    from Shynt.api_py.Geometry.universes import Pin
    serpent_syntax = ""
    node_universe = super().universe

    
    width_rectangle = self.points_node[3][0] - self.points_node[0][0]
    height_rectangle = self.points_node[1][1] - self.points_node[0][1]

    closing_square = f"surf closing_rectangle "
    closing_square += f"rect {0.0} {width_rectangle} {0.0} {height_rectangle}\n"
    closing_diagonal = f"surf closing_diagonal px {0.0}\n"
    closing_diagonal+=  f"trans s closing_diagonal "
    closing_diagonal+= "0.0 0.0 0.0 0.0 0.0 30\n\n\n"

    regions = {}
    
    fine_mesh_regs_ids = list(self.fine_mesh.regions.keys())

    fuel_id = fine_mesh_regs_ids[0]
    coolant_id = fine_mesh_regs_ids[1]

    regions[fuel_id] = { # fuel
      'material': self.fine_mesh.regions[fuel_id].content.name,
      'surf(-)': 'fuel_pad',
      'surf(+)': ''
    }

    regions[coolant_id] = {
        "material": self.fine_mesh.regions[coolant_id].content.name,
        "surf(-)": {
          "rectangle": "closing_rectangle",
          "diagonal": "closing_diagonal"
        },
        "surf(+)": "fuel_pad"
      }
    
    #
    
    last_cyl_surf = f'surf fuel_pad pad {width_rectangle} 0.0 0.0 '
    last_cyl_surf += f'0.357 180 270 \n\n\n'

    
    serpent_syntax += closing_square
    serpent_syntax += closing_diagonal
    serpent_syntax += last_cyl_surf
    return serpent_syntax, regions
    
    
  def get_serpent_detectors_fuel_region(self, c_id, ene):
    det_syntax = ""
    det_relation = { 
      "total_rate": "",
      "j_in_fuel": "",
      "j_out_fuel": "",
      "all_to_fuel": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[c_id]
    r1 = self.regions_surfaces[c_id]["r1"]
    r2 = self.regions_surfaces[c_id]["r2"]

    det_syntax += f"surf fuel_surf pad 0.0000 0.0000 {r1} {r2} 180 270\n\n\n"
    
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]

    det_syntax += "% Detectors ------------------------------------\n"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id} \n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"
    # Detector  Jin fuel ------------
    det_syntax += f"det j_in_reg{c_id}  ds {'fuel_surf'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_relation["j_in_fuel"] = f"j_in_reg{c_id}"
    # Detector  Jout fuel ------------
    det_syntax += f"det j_out_reg{c_id} ds {'fuel_surf'}  1 "
    det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
    det_relation["j_out_fuel"] = f"j_out_reg{c_id}"
    # Detector All to fuel ------------
    det_syntax += f"det all_to_reg_{c_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {c_id} de {ene}  dfl 1 2  dfl 1 0\n"
    det_relation["all_to_fuel"] = f"all_to_reg_{c_id}"
    for r_id, cell in regions.items():
      if r_id == c_id: continue
      # Detector  fuel region to other region (r_id)------------
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_nonFuel_region(self, c_id, ene):
    det_syntax = "\n\n\n"
    det_relation = { 
      "total_rate": "",
      "same_region": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]
    # Detector region to same region ------------
    det_syntax += f"det reg{c_id}_to_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_relation["same_region"] = f"reg{c_id}_to_reg{c_id}"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}    dfl 1 1\n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    for r_id, cell in regions.items():
      if r_id == c_id: continue
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"

    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    det_relation = { 
      "surface_to_region": {},
      "surface_to_surface": {}
    }

    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    boundary_ids = list(self.detectors_surfaces.keys()) 

    
    # J_in detectors through the surfaces just to flag the neutrons ----------
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"]
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}"
      if self.detectors_surfaces[s_id]["trans"]:
        s_left_flag = surface_flags[boundary_ids[0]]
        det_syntax += f" dfl {s_left_flag} 0\n"
      else:
        det_syntax += "\n"

    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      det_relation["surface_to_region"][s_id] = {}
      det_relation["surface_to_surface"][s_id] = {}

      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():
        # Detector surface to region ---------------------
        det_name = f"surface_{s_id}_to_reg{r_id}"
        det_syntax += f"det {det_name} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"
        det_relation["surface_to_region"][s_id][r_id] = det_name
      for s_id_p in self.detectors_surfaces.keys():
        # Detector surface to surface ---------------------
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_name = f"surface_{s_id}_to_surface{s_id_p}"
        det_syntax += f"det {det_name} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
        det_relation["surface_to_surface"][s_id][s_id_p] = det_name

    # print(det_syntax)
    return det_syntax, det_relation



class CoarseNodeSquareGridHexAssembly_SideEdge(
  CoarseNodeSquareGridHexAssembly
):

  def __init__(self, id_, type_coarse_mesh, half_pitch, quadrant, hex_wrapper):
    super().__init__(id_, type_coarse_mesh, half_pitch, quadrant)
    self.hex_wrapper = hex_wrapper
  
  def get_serpent_geometry(self):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    self.regions_surfaces = regions
    # cells ---------------------------------------
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
      serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "
      serpent_syntax += f"{reg_info['surf(+)']}\n"
      
    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n"
    
    boundary_ids = list(self.surfaces.keys()) 

    serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
    
    detectors_surfaces = {
      boundary_ids[0]: {
        "syntax": f"surf {boundary_ids[0]} py {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[1]: {
        "syntax": f"surf {boundary_ids[1]} px {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[2]: {
        "syntax": f"surf {boundary_ids[2]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[3]: {
        "syntax": f"surf {boundary_ids[3]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[4]: {
        "syntax": f"surf {boundary_ids[4]} px -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[5]: {
        "syntax": f"surf {boundary_ids[5]} py {self.half_width}\n",
        "j_in_dir": -1
      }
    }

    detectors_surfaces[boundary_ids[0]]["syntax"] += f'trans s {boundary_ids[0]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[2]]["syntax"] += f'trans s {boundary_ids[2]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    detectors_surfaces[boundary_ids[3]]["syntax"] += f'trans s {boundary_ids[3]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[5]]["syntax"] += f'trans s {boundary_ids[5]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    

    for surf_serpent in detectors_surfaces.values():
      serpent_syntax += surf_serpent["syntax"]

    
    self.detectors_surfaces = detectors_surfaces

    return serpent_syntax, detectors_surfaces

  def get_gcu_geometry(self, ene):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    xs_gcu = {}
    u4gcu = []
    gcu_id = 1
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
      serpent_syntax += f"{reg_info['material']} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      serpent_syntax += f"cell {r_id+2000} pin_fuel{self.id} fill "
      serpent_syntax += f"u4gcu{gcu_id} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      u4gcu.append(f"u4gcu{gcu_id}")
      xs_gcu[r_id] = f"u4gcu{gcu_id}"
      gcu_id += 1

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax, xs_gcu

  def get_surfaces_serpent_syntax(self):
    from Shynt.api_py.Geometry.universes import Pin
    serpent_syntax = ""
    node_universe = super().universe

    try:
      assert isinstance(node_universe, Pin)
      pin_levels = node_universe.pin_levels

      assert len(pin_levels) > 1
      # regions = {
      #   cell_id: {
      #     "material":mat_name,
      #     "surf-": id_,
      #     "surf+": id_,
      #   }
      # }

      # cylinders = {
      #   s_id: radius
      # }
      # Closing surface: square with  id = 100

      
      closing_surf = f"surf closing_surf "
      closing_surf += f"hexxc 0.0000 0.0000 {self.half_width}\n\n\n"

      cylinders = {}
      regions = {}
      prev_radius = 0.0
      num_surf = 1

      fine_mesh_regs_ids = list(self.fine_mesh.regions.keys())
      # surfaces ---------------------------------------
      for l, level in enumerate(pin_levels):
        num_cell = fine_mesh_regs_ids[l]
        if level.radius is not None:
          cylinders[f"{num_surf}_geom"] = level.radius

          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": f"{num_surf}_geom",
            "surf(+)": ""
          }
          if l >= 1:
            regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
        else:
          # is surroundings of pin
          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": "closing_surf",
            "surf(+)": f"{num_surf-1}_geom"
          }
        num_surf += 1
      
      for s_id, radius in cylinders.items():
        serpent_syntax += f"surf {s_id} cyl 0.0000 0.0000 {radius}\n"
      serpent_syntax += closing_surf
      self.cylinders = cylinders
      return serpent_syntax, regions
    except AssertionError:
      raise NotImplementedError
    
  
  def get_serpent_detectors_fuel_region(self, c_id, ene):
    det_syntax = ""
    det_relation = { 
      "total_rate": "",
      "j_in_fuel": "",
      "j_out_fuel": "",
      "all_to_fuel": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[c_id]
    

    print(self.regions_surfaces)
    surfaces_fuel = self.regions_surfaces[c_id]
    surf_neg = surfaces_fuel['surf(-)']
    surf_pos = surfaces_fuel['surf(+)']
    
    r2 = self.cylinders[surf_neg]

    det_syntax += f"surf fuel_surf1 cyl 0.0000 0.0000 {r2} \n\n\n"

    if surf_pos != '':
      r1 = self.cylinders[surf_pos]
      det_syntax += f"surf fuel_surf2 cyl 0.0000 0.0000 {r1} \n\n\n"
      
    
    
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]

    det_syntax += "% Detectors ------------------------------------\n"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id} \n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    # Detector  Jin fuel ------------ FLAG-1 TO COUNT ALL->FUEL
    det_syntax += f"det j_in1_reg{c_id}  ds {'fuel_surf1'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_relation["j_in_fuel"] = f"j_in_reg{c_id}"
    if surf_pos != '':
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_in2_reg{c_id}  ds {'fuel_surf2'} -1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_out2_reg{c_id}  ds {'fuel_surf2'} 1 "
      det_syntax += f"de {ene} dfl 2 3  dfl 1 1\n"
    else:
      # Detector  Jout fuel ------------
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_relation["j_out_fuel"] = f"j_out_reg{c_id}"
    

    # Detector All to fuel ------------
    det_syntax += f"det all_to_reg_{c_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {c_id} de {ene}  dfl 1 2  dfl 1 0\n"
    det_relation["all_to_fuel"] = f"all_to_reg_{c_id}"
    for r_id, cell in regions.items():
      if r_id == c_id: continue
      # Detector  fuel region to other region (r_id)------------
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_nonFuel_region(self, c_id, ene):
    det_syntax = "\n\n\n"
    det_relation = { 
      "total_rate": "",
      "same_region": "",
      "region_to_region": {},
      "region_to_surface": {}
    }
    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]
    # Detector region to same region ------------
    det_syntax += f"det reg{c_id}_to_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_relation["same_region"] = f"reg{c_id}_to_reg{c_id}"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}    dfl 1 1\n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    for r_id, cell in regions.items():
      if r_id == c_id: continue
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"

    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation
  
  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    det_relation = { 
      "surface_to_region": {},
      "surface_to_surface": {}
    }
    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    # J_in detectors thrpough the surfaces just to flag the neutrons ----------
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"]
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}\n"
    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      det_relation["surface_to_region"][s_id] = {}
      det_relation["surface_to_surface"][s_id] = {}

      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():
        # Detector surface to region ---------------------
        det_name = f"surface_{s_id}_to_reg{r_id}"
        det_syntax += f"det {det_name} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"
        det_relation["surface_to_region"][s_id][r_id] = det_name
      for s_id_p in self.detectors_surfaces.keys():
        # Detector surface to surface ---------------------
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_name = f"surface_{s_id}_to_surface{s_id_p}"
        det_syntax += f"det {det_name} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
        det_relation["surface_to_surface"][s_id][s_id_p] = det_name

    # print(det_syntax)
    return det_syntax, det_relation
  

class CoarseNodeSquareGridHexAssembly_TriangleCorner(
  CoarseNodeSquareGridHexAssembly
):

  def __init__(self, id_, type_coarse_mesh, half_pitch, quadrant, hex_wrapper):
    super().__init__(id_, type_coarse_mesh, half_pitch, quadrant)
    self.hex_wrapper = hex_wrapper

  def calculate_surfaces(self, s_id, rectangle_points):
    """ It calculates the surfaces for a reactangle type node
    
    Parameters
    ----------
    s_id : int
      Surface identifier from where the numbering for this node will start 
      counting
    
    Returns
    -------
    s_id : int
    """
   
    x1, x2 = rectangle_points[0]
    y1, y2 = rectangle_points[1]
    surfaces = {}
    if self.quadrant == 1:
      p1 = (x1, y1)
      p2 = (x2, y2)
      p3 = (x2, y1)
    elif  self.quadrant == 2:
      p1 = (x1, y1)
      p2 = (x1,y2)
      p3 = (x2, y1)
    elif  self.quadrant == 3:
      p1 = (x1, y1)
      p2 = (x1, y2)
      p3 = (x2, y2)
    elif  self.quadrant == 4:
      p1 = (x2, y1)
      p2 = (x1, y2)
      p3 = (x2, y2)
   
    surfaces = {
      s_id+1: (p1, p2),
      s_id+2: (p2, p3),
      s_id+3: (p3, p1),
    }
    
    self.surfaces = surfaces
    self.points_node = [p1, p2, p3]
    return s_id + 3

  def get_serpent_geometry(self):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    self.regions_surfaces = regions
    # cells ---------------------------------------
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
      serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "
      serpent_syntax += f"{reg_info['surf(+)']}\n"
      
    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n"
    
    boundary_ids = list(self.surfaces.keys()) 

    serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
    
    detectors_surfaces = {
      boundary_ids[0]: {
        "syntax": f"surf {boundary_ids[0]} py {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[1]: {
        "syntax": f"surf {boundary_ids[1]} px {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[2]: {
        "syntax": f"surf {boundary_ids[2]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[3]: {
        "syntax": f"surf {boundary_ids[3]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[4]: {
        "syntax": f"surf {boundary_ids[4]} px -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[5]: {
        "syntax": f"surf {boundary_ids[5]} py {self.half_width}\n",
        "j_in_dir": -1
      }
    }

    detectors_surfaces[boundary_ids[0]]["syntax"] += f'trans s {boundary_ids[0]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[2]]["syntax"] += f'trans s {boundary_ids[2]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    detectors_surfaces[boundary_ids[3]]["syntax"] += f'trans s {boundary_ids[3]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[5]]["syntax"] += f'trans s {boundary_ids[5]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    

    for surf_serpent in detectors_surfaces.values():
      serpent_syntax += surf_serpent["syntax"]

    
    self.detectors_surfaces = detectors_surfaces

    return serpent_syntax, detectors_surfaces

  def get_gcu_geometry(self, ene):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    xs_gcu = {}
    u4gcu = []
    gcu_id = 1
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
      serpent_syntax += f"{reg_info['material']} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      serpent_syntax += f"cell {r_id+2000} pin_fuel{self.id} fill "
      serpent_syntax += f"u4gcu{gcu_id} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      u4gcu.append(f"u4gcu{gcu_id}")
      xs_gcu[r_id] = f"u4gcu{gcu_id}"
      gcu_id += 1

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax, xs_gcu

  def get_surfaces_serpent_syntax(self):
    from Shynt.api_py.Geometry.universes import Pin
    serpent_syntax = ""
    node_universe = super().universe

    try:
      assert isinstance(node_universe, Pin)
      pin_levels = node_universe.pin_levels

      assert len(pin_levels) > 1
      # regions = {
      #   cell_id: {
      #     "material":mat_name,
      #     "surf-": id_,
      #     "surf+": id_,
      #   }
      # }

      # cylinders = {
      #   s_id: radius
      # }
      # Closing surface: square with  id = 100

      
      closing_surf = f"surf closing_surf "
      closing_surf += f"hexxc 0.0000 0.0000 {self.half_width}\n\n\n"

      cylinders = {}
      regions = {}
      prev_radius = 0.0
      num_surf = 1

      fine_mesh_regs_ids = list(self.fine_mesh.regions.keys())
      # surfaces ---------------------------------------
      for l, level in enumerate(pin_levels):
        num_cell = fine_mesh_regs_ids[l]
        if level.radius is not None:
          cylinders[f"{num_surf}_geom"] = level.radius

          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": f"{num_surf}_geom",
            "surf(+)": ""
          }
          if l >= 1:
            regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
        else:
          # is surroundings of pin
          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": "closing_surf",
            "surf(+)": f"{num_surf-1}_geom"
          }
        num_surf += 1
      
      for s_id, radius in cylinders.items():
        serpent_syntax += f"surf {s_id} cyl 0.0000 0.0000 {radius}\n"
      serpent_syntax += closing_surf
      self.cylinders = cylinders
      return serpent_syntax, regions
    except AssertionError:
      raise NotImplementedError
    
  
  def get_serpent_detectors_fuel_region(self, c_id, ene):
    det_syntax = ""
    det_relation = { 
      "total_rate": "",
      "j_in_fuel": "",
      "j_out_fuel": "",
      "all_to_fuel": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[c_id]
    

    print(self.regions_surfaces)
    surfaces_fuel = self.regions_surfaces[c_id]
    surf_neg = surfaces_fuel['surf(-)']
    surf_pos = surfaces_fuel['surf(+)']
    
    r2 = self.cylinders[surf_neg]

    det_syntax += f"surf fuel_surf1 cyl 0.0000 0.0000 {r2} \n\n\n"

    if surf_pos != '':
      r1 = self.cylinders[surf_pos]
      det_syntax += f"surf fuel_surf2 cyl 0.0000 0.0000 {r1} \n\n\n"
      
    
    
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]

    det_syntax += "% Detectors ------------------------------------\n"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id} \n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    # Detector  Jin fuel ------------ FLAG-1 TO COUNT ALL->FUEL
    det_syntax += f"det j_in1_reg{c_id}  ds {'fuel_surf1'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_relation["j_in_fuel"] = f"j_in_reg{c_id}"
    if surf_pos != '':
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_in2_reg{c_id}  ds {'fuel_surf2'} -1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_out2_reg{c_id}  ds {'fuel_surf2'} 1 "
      det_syntax += f"de {ene} dfl 2 3  dfl 1 1\n"
    else:
      # Detector  Jout fuel ------------
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_relation["j_out_fuel"] = f"j_out_reg{c_id}"
    

    # Detector All to fuel ------------
    det_syntax += f"det all_to_reg_{c_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {c_id} de {ene}  dfl 1 2  dfl 1 0\n"
    det_relation["all_to_fuel"] = f"all_to_reg_{c_id}"
    for r_id, cell in regions.items():
      if r_id == c_id: continue
      # Detector  fuel region to other region (r_id)------------
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_nonFuel_region(self, c_id, ene):
    det_syntax = "\n\n\n"
    det_relation = { 
      "total_rate": "",
      "same_region": "",
      "region_to_region": {},
      "region_to_surface": {}
    }
    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]
    # Detector region to same region ------------
    det_syntax += f"det reg{c_id}_to_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_relation["same_region"] = f"reg{c_id}_to_reg{c_id}"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}    dfl 1 1\n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    for r_id, cell in regions.items():
      if r_id == c_id: continue
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"

    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation
  
  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    det_relation = { 
      "surface_to_region": {},
      "surface_to_surface": {}
    }
    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    # J_in detectors thrpough the surfaces just to flag the neutrons ----------
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"]
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}\n"
    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      det_relation["surface_to_region"][s_id] = {}
      det_relation["surface_to_surface"][s_id] = {}

      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():
        # Detector surface to region ---------------------
        det_name = f"surface_{s_id}_to_reg{r_id}"
        det_syntax += f"det {det_name} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"
        det_relation["surface_to_region"][s_id][r_id] = det_name
      for s_id_p in self.detectors_surfaces.keys():
        # Detector surface to surface ---------------------
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_name = f"surface_{s_id}_to_surface{s_id_p}"
        det_syntax += f"det {det_name} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
        det_relation["surface_to_surface"][s_id][s_id_p] = det_name

    # print(det_syntax)
    return det_syntax, det_relation
  

class CoarseNodeSquareGridHexAssembly_Inside(
  CoarseNodeSquareGridHexAssembly
):

  def __init__(self, id_, type_coarse_mesh, half_pitch, quadrant, hex_wrapper):
    super().__init__(id_, type_coarse_mesh, half_pitch, quadrant)
    self.hex_wrapper = hex_wrapper

  def get_serpent_geometry(self):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    self.regions_surfaces = regions
    # cells ---------------------------------------
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
      serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "
      serpent_syntax += f"{reg_info['surf(+)']}\n"
      
    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n"
    
    boundary_ids = list(self.surfaces.keys()) 

    serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
    
    detectors_surfaces = {
      boundary_ids[0]: {
        "syntax": f"surf {boundary_ids[0]} py {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[1]: {
        "syntax": f"surf {boundary_ids[1]} px {self.half_width}\n",
        "j_in_dir": -1
      },
      boundary_ids[2]: {
        "syntax": f"surf {boundary_ids[2]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[3]: {
        "syntax": f"surf {boundary_ids[3]} py -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[4]: {
        "syntax": f"surf {boundary_ids[4]} px -{self.half_width}\n",
        "j_in_dir": 1
      },
      boundary_ids[5]: {
        "syntax": f"surf {boundary_ids[5]} py {self.half_width}\n",
        "j_in_dir": -1
      }
    }

    detectors_surfaces[boundary_ids[0]]["syntax"] += f'trans s {boundary_ids[0]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[2]]["syntax"] += f'trans s {boundary_ids[2]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    detectors_surfaces[boundary_ids[3]]["syntax"] += f'trans s {boundary_ids[3]}  0.0 0.0 0.0 0.0 0.0 30\n'
    detectors_surfaces[boundary_ids[5]]["syntax"] += f'trans s {boundary_ids[5]}  0.0 0.0 0.0 0.0 0.0 -30\n'
    

    for surf_serpent in detectors_surfaces.values():
      serpent_syntax += surf_serpent["syntax"]

    
    self.detectors_surfaces = detectors_surfaces

    return serpent_syntax, detectors_surfaces

  def get_gcu_geometry(self, ene):
    serpent_syntax, regions = self.get_surfaces_serpent_syntax()
    
    # cells ---------------------------------------
    xs_gcu = {}
    u4gcu = []
    gcu_id = 1
    for r_id, reg_info in regions.items():
      serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
      serpent_syntax += f"{reg_info['material']} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      serpent_syntax += f"cell {r_id+2000} pin_fuel{self.id} fill "
      serpent_syntax += f"u4gcu{gcu_id} "
      serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

      u4gcu.append(f"u4gcu{gcu_id}")
      xs_gcu[r_id] = f"u4gcu{gcu_id}"
      gcu_id += 1

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax, xs_gcu

  def get_surfaces_serpent_syntax(self):
    from Shynt.api_py.Geometry.universes import Pin
    serpent_syntax = ""
    node_universe = super().universe

    try:
      assert isinstance(node_universe, Pin)
      pin_levels = node_universe.pin_levels

      assert len(pin_levels) > 1
      # regions = {
      #   cell_id: {
      #     "material":mat_name,
      #     "surf-": id_,
      #     "surf+": id_,
      #   }
      # }

      # cylinders = {
      #   s_id: radius
      # }
      # Closing surface: square with  id = 100

      
      closing_surf = f"surf closing_surf "
      closing_surf += f"hexxc 0.0000 0.0000 {self.half_width}\n\n\n"

      cylinders = {}
      regions = {}
      prev_radius = 0.0
      num_surf = 1

      fine_mesh_regs_ids = list(self.fine_mesh.regions.keys())
      # surfaces ---------------------------------------
      for l, level in enumerate(pin_levels):
        num_cell = fine_mesh_regs_ids[l]
        if level.radius is not None:
          cylinders[f"{num_surf}_geom"] = level.radius

          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": f"{num_surf}_geom",
            "surf(+)": ""
          }
          if l >= 1:
            regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
        else:
          # is surroundings of pin
          regions[num_cell] = {
            "material": level.material.name,
            "surf(-)": "closing_surf",
            "surf(+)": f"{num_surf-1}_geom"
          }
        num_surf += 1
      
      for s_id, radius in cylinders.items():
        serpent_syntax += f"surf {s_id} cyl 0.0000 0.0000 {radius}\n"
      serpent_syntax += closing_surf
      self.cylinders = cylinders
      return serpent_syntax, regions
    except AssertionError:
      raise NotImplementedError
    
  
  def get_serpent_detectors_fuel_region(self, c_id, ene):
    det_syntax = ""
    det_relation = { 
      "total_rate": "",
      "j_in_fuel": "",
      "j_out_fuel": "",
      "all_to_fuel": "",
      "region_to_region": {},
      "region_to_surface": {}
    }

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[c_id]
    

    print(self.regions_surfaces)
    surfaces_fuel = self.regions_surfaces[c_id]
    surf_neg = surfaces_fuel['surf(-)']
    surf_pos = surfaces_fuel['surf(+)']
    
    r2 = self.cylinders[surf_neg]

    det_syntax += f"surf fuel_surf1 cyl 0.0000 0.0000 {r2} \n\n\n"

    if surf_pos != '':
      r1 = self.cylinders[surf_pos]
      det_syntax += f"surf fuel_surf2 cyl 0.0000 0.0000 {r1} \n\n\n"
      
    
    
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]

    det_syntax += "% Detectors ------------------------------------\n"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id} \n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    # Detector  Jin fuel ------------ FLAG-1 TO COUNT ALL->FUEL
    det_syntax += f"det j_in1_reg{c_id}  ds {'fuel_surf1'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_relation["j_in_fuel"] = f"j_in_reg{c_id}"
    if surf_pos != '':
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_in2_reg{c_id}  ds {'fuel_surf2'} -1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_syntax += f"det j_out2_reg{c_id}  ds {'fuel_surf2'} 1 "
      det_syntax += f"de {ene} dfl 2 3  dfl 1 1\n"
    else:
      # Detector  Jout fuel ------------
      det_syntax += f"det j_out1_reg{c_id}  ds {'fuel_surf1'} 1 "
      det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"
      det_relation["j_out_fuel"] = f"j_out_reg{c_id}"
    

    # Detector All to fuel ------------
    det_syntax += f"det all_to_reg_{c_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {c_id} de {ene}  dfl 1 2  dfl 1 0\n"
    det_relation["all_to_fuel"] = f"all_to_reg_{c_id}"
    for r_id, cell in regions.items():
      if r_id == c_id: continue
      # Detector  fuel region to other region (r_id)------------
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation

  def get_serpent_detectors_nonFuel_region(self, c_id, ene):
    det_syntax = "\n\n\n"
    det_relation = { 
      "total_rate": "",
      "same_region": "",
      "region_to_region": {},
      "region_to_surface": {}
    }
    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[c_id]
    # Detector region to same region ------------
    det_syntax += f"det reg{c_id}_to_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_relation["same_region"] = f"reg{c_id}_to_reg{c_id}"
    # Detector total_rate ------------
    det_syntax += f"det total_rate_reg{c_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {c_id}    dfl 1 1\n"
    det_relation["total_rate"] = f"total_rate_reg{c_id}"

    for r_id, cell in regions.items():
      if r_id == c_id: continue
      det_syntax += f"det reg{c_id}_to_reg{r_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
      det_relation["region_to_region"][r_id] = f"reg{c_id}_to_reg{r_id}"

    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{c_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"
      det_relation["region_to_surface"][s_id] = f"reg{c_id}_to_surface{s_id}"

    return det_syntax, det_relation
  
  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    det_relation = { 
      "surface_to_region": {},
      "surface_to_surface": {}
    }
    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    # J_in detectors thrpough the surfaces just to flag the neutrons ----------
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"]
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}\n"
    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      det_relation["surface_to_region"][s_id] = {}
      det_relation["surface_to_surface"][s_id] = {}

      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():
        # Detector surface to region ---------------------
        det_name = f"surface_{s_id}_to_reg{r_id}"
        det_syntax += f"det {det_name} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"
        det_relation["surface_to_region"][s_id][r_id] = det_name
      for s_id_p in self.detectors_surfaces.keys():
        # Detector surface to surface ---------------------
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_name = f"surface_{s_id}_to_surface{s_id_p}"
        det_syntax += f"det {det_name} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
        det_relation["surface_to_surface"][s_id][s_id_p] = det_name

    # print(det_syntax)
    return det_syntax, det_relation
  



