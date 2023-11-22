
class CoarseNode():

  def __init__(self, id_, surface_points, type_coarse_mesh):
    self.id = id_
    self.surface_points = surface_points
    self.type_coarse_mesh = type_coarse_mesh
    self.surfaces = {}
    self.surfaces_areas = {}
    self.__universe = None # set of cells that form the coarse node
    self.__fine_mesh = None


  def calculate_node_surfaces(self, s_id):
    """Class method to calculate the surface of the coarse node defined by
    two points. The neumbering of the surface based on the sides of the square
    coarse node is the following:
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
    # nodes_surfaces = {}
    
    num_points = len(self.surface_points)
    surfaces = {}
    for p in range(num_points-1):
      p1 = self.surface_points[p]
      p2 = self.surface_points[p+1]
      surf = (p1, p2) 
      surfaces[s_id] = surf
      s_id += 1
      

    p_last = self.surface_points[-1]
    p_first = self.surface_points[0]

    last_surf = (p_last, p_first)
    surfaces[s_id] = last_surf

    self.surfaces = surfaces
    return s_id+1

  def calculate_surfaces_areas(self):
    areas = []
    for surf in self.surfaces:
      area = 0.0 # calc_area (euclidean distance)
      areas.append(area)
    self.surfaces_areas = areas

  

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

  def __init__(self, id_, surface_points, type_coarse_mesh, pitch):
    super().__init__(id_, surface_points, type_coarse_mesh)
    self.pitch = pitch
    self.detectors_surfaces = {}


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
      gcu_id += 1

    serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
    serpent_syntax += f"-closing_surf\n"

    serpent_syntax += f"cell root_out 0 outside closing_surf\n\n"
    
    
    serpent_syntax += f"set gcu "
    for gcu in u4gcu:
      serpent_syntax += f"{gcu} "
    serpent_syntax += f"\n\nplot 3 500 500\nset nfg {ene}\n\n"
    
    return serpent_syntax
    
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
    
  def get_serpent_detectors_fuel_region(self, cell_id, ene):
    det_syntax = ""

    # Additional surface for the fuel 
    cell = self.fine_mesh.regions[cell_id]
    surf_fuel = cell.region.surface
    radius = surf_fuel.radius
    det_syntax += f"surf fuel_surf cyl 0.0000 0.0000 {radius}\n\n\n\n"
    
    regions = self.fine_mesh.regions
    main_cell = regions[cell_id]

    det_syntax += "% Detectors ------------------------------------\n"
    det_syntax += f"det total_rate_reg{cell_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {cell_id} \n"
    det_syntax += f"det j_in_reg{cell_id}  ds {'fuel_surf'} -1 "
    det_syntax += f"de {ene} dfl 1 1\n"
    det_syntax += f"det j_out_reg{cell_id} ds {'fuel_surf'}  1 "
    det_syntax += f"de {ene} dfl 1 3  dfl 2 1\n"

    det_syntax += f"det all_to_reg_{cell_id} dr -1 {main_cell.content.name} "
    det_syntax += f"dc {cell_id} de {ene}  dfl 1 2  dfl 1 0\n"

    for r_id, cell in regions.items():
      if r_id == cell_id: continue
      det_syntax += f"det reg{r_id}_reg{cell_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 2 2  dfl 2 0\n"
    
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{r_id}__to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 2 2  dfl 2 0\n"
    return det_syntax

  def get_serpent_detectors_nonFuel_region(self, cell_id, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"
    regions = self.fine_mesh.regions
    main_cell = regions[cell_id]
    det_syntax += f"det reg{cell_id}_reg{cell_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {cell_id}   "
    det_syntax += "dfl 1 2  dfl 1 0  dfl 1 1\n"
    det_syntax += f"det total_rate_reg{cell_id} de {ene} dr -1 "
    det_syntax += f"{main_cell.content.name} dc {cell_id}    dfl 1 1\n"
    for r_id, cell in regions.items():
      if r_id == cell_id: continue
      det_syntax += f"det reg{r_id}_to_reg{cell_id} de {ene} dr -1 "
      det_syntax += f"{cell.content.name} dc {r_id}    dfl 1 2  dfl 1 0\n"
    
    for s_id in self.detectors_surfaces.keys():
      j_out_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det reg{r_id}_to_surface{s_id} de {ene} ds {s_id} "
      det_syntax += f"{j_out_dir}  dfl 1 2  dfl 1 0\n"

    return det_syntax

  def get_serpent_detectors_surfaces(self, ene):
    det_syntax = "\n\n\n"
    det_syntax += "% Detectors ------------------------------------\n"

    surface_flags = {}
    flag = 1
    for s_id in self.detectors_surfaces.keys():
      surface_flags[s_id] = flag
      flag += 1
    
    for s_id in self.detectors_surfaces.keys():
      j_in_dir = self.detectors_surfaces[s_id]["j_in_dir"] * -1
      det_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} "
      det_syntax += f"dfl {surface_flags[s_id]} {1}\n"
    
    regions = self.fine_mesh.regions
    for s_id in self.detectors_surfaces.keys():
      s_flag = surface_flags[s_id]
      for r_id, cell in regions.items():

        det_syntax += f"det surface_{s_id}_to_reg{r_id} de {ene} dr -1"
        det_syntax += f" {cell.content.name} dc {r_id} dfl {s_flag} 2 "
        det_syntax += f"dfl {s_flag} 0 \n"

      for s_id_p in self.detectors_surfaces.keys():
        jout_sidp = self.detectors_surfaces[s_id_p]["j_in_dir"] * -1
        det_syntax += f"det surface_{s_id}_to_surface{s_id_p} de {ene} "
        det_syntax += f"ds {s_id_p} {jout_sidp} "
        det_syntax += f"dfl {s_flag} 2  dfl {s_flag} 0 \n"
    # print(det_syntax)
    return det_syntax