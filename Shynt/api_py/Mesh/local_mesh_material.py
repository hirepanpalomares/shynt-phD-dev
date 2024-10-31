
from Shynt.api_py.Mesh.local_fine_mesh import FineMesh
from Shynt.api_py.Geometry.cells import Cell
import numpy as np
import math




class MaterialMesh(FineMesh):
  """Class that represents the fine mesh inside a coarse node by material.
  i.e. each reagion of the fine mesh is the different materials delimited 
  by the geometry of the coarse node

  Attributes
  ----------
  regions : dict

  Methods
  -------
  __create_regions_pin_cell: 
  
  
  """
  def __init__(
    self, coarse_node=None, type_coarse_mesh=None, is_hex_lattice=False, 
    symmetry="", init_create=True
  ):
    super().__init__(coarse_node)
    self.__type_coarse_mesh = type_coarse_mesh
    self.__is_hex_lattice = is_hex_lattice
    self.regions = {}
    self.regions_points = {}
    self.regions_symmetry = {}
    self.regions_volume = {}
    self.surface_of_regions = {}
    self.symmetry = symmetry

    if type_coarse_mesh == 'pin_cell':
      self.__create_regions_pin_cell_mesh()
    elif type_coarse_mesh == 'square_grid_hex_pin':
      self.__create_regions_square_grid_hex_pin()
    elif type_coarse_mesh == 'square_grid':
      # Square grid applied to hexagonal lattices
      # self.__create_regions_square_grid_hex_assem()
      pass
    elif type_coarse_mesh == 'triangular_hex_pin':
      self.__create_regions_pin_triangular_mesh()
    elif (
      type_coarse_mesh == 'triangular' or 
      type_coarse_mesh == 'core_assembly_triangular'
    ):
      if symmetry == "triangular_mesh":
        self.__create_regions_triangular_mesh(symmetry="triangular_mesh")
      else:
        if init_create:
          self.__create_regions_triangular_mesh()
        else:
          pass

    else:
      if type_coarse_mesh is not None:
        print(f"Error: {type_coarse_mesh} type of mesh not implemented")
        raise NotImplementedError
      else:
        pass

  
  def __create_regions_pin_cell_mesh(self):
    """Class method to create the regions of a pin-cell type coarse_node
    THE COARSE NODE SHOULD BE A SQUARE.
    Regions: fuel -> gap -> cladding ... etc

    
    """
    regions = {}
    pin_universe  = super().coarse_node.universe
    
    regions_pin = pin_universe.cells
    for r_id, cell in regions_pin.items():
      regions[r_id] = cell

    self.regions = regions

  def __create_regions_square_grid_hex_pin(self):

    regions = {}
    pin_universe  = super().coarse_node.universe
    regions_pin = pin_universe.pin_levels

    # Divide the pin_cell in 4 and each piece is a cell

    for l, level in enumerate(regions_pin):
      cell = pin_universe.cells[level.cell_id]
      vol_cell = cell.volume

      new_fine_region = Cell(fill=cell.content, volume=vol_cell/4)

      regions[new_fine_region.id] = new_fine_region
    
    
    self.regions = regions
    
  def __create_regions_square_grid_hex_assem(self):
    """Class method to create the regions. It only creates a Cell class
    for each region where only volume and material are provided
    
    """
    regions = {}
    self.regions = regions

    print("For this type of mesh regions have to be provided by the user")
    raise RuntimeWarning(
      "For this type of mesh regions have to be provided by the user"
    )

  def __create_regions_pin_triangular_mesh(self):
    
    hex_pin = super().coarse_node.pin_universe

    regions = {}
    regions_pin = hex_pin.pin_levels
    
    sum_volumes = 0.0
    for l in range(len(regions_pin)-1):
      level = regions_pin[l]
      cell = hex_pin.cells[level.cell_id]
      vol_cell = cell.volume
      
      vol_region = vol_cell / 6
      sum_volumes += vol_region
      new_fine_region = Cell(fill=cell.content, volume=vol_region)
      regions[new_fine_region.id] = new_fine_region

    # Last level: typically coolant ---------------------
    last_level = regions_pin[-1]
    cell = hex_pin.cells[last_level.cell_id]
    radius_hex = super().coarse_node.wrapper.radius
    half_width_hex = super().coarse_node.wrapper.half_width 
    vol_node = radius_hex * half_width_hex / 2
    vol_coolant = vol_node - sum_volumes
    
    new_fine_region = Cell(fill=cell.content, volume=vol_coolant)
    regions[new_fine_region.id] = new_fine_region

    self.regions = regions

  def __create_regions_triangular_mesh(self, symmetry=""):
    """Class method to create the regions of a triangular type coarse_node
    THE COARSE NODE SHOULD BE FROM A TRIANGULAR TYPE COARSE MESH

    It will have 3 or 4 points. Either a triangle or a square. There is two
    types of triangles: inner or corner triangle. The square is in the 
    boundary.

    

    
    """
    
    try:
      assert(self.__is_hex_lattice)
      
      hex_assembly = super().coarse_node.hex_assembly
      
      
      
      pin_from_assembly = hex_assembly.rings[0][0] # central pin
      regions = {}
      
      regions_pin = pin_from_assembly.pin_levels
      type_coarse_node = self.coarse_node.type_coarse_node
      regions_symmetry = {}
      
      sum_volumes = 0.0
      radius1 = 0.0
      for l in range(len(regions_pin)-1): # Loop for every level of the pin
      
        level = regions_pin[l]
        radius2 = level.radius
        cell = pin_from_assembly.cells[level.cell_id]
        vol_cell = cell.volume
        material_cell = cell.content
        self.coarse_node.regions_points_relation[material_cell.name] = []
  
        # vol_new_region = vol_cell/fuel_divider[type_coarse_node]
        node_points = self.coarse_node.surf_points
        # points_position = self.coarse_node.theta_corners
        if type_coarse_node == "inner_triangle":
          sum_volumes += vol_cell/2
          regions_ids = []
          # for point, position in zip(node_points, points_position):
          for p, point in enumerate(node_points):
            angle = self.coarse_node.theta_corners[p]

            new_fine_region = Cell(fill=cell.content, volume=vol_cell/6)
            regions[new_fine_region.id] = new_fine_region
            regions_ids.append(new_fine_region.id)
            self.coarse_node.regions_points_relation[material_cell.name].append(
              new_fine_region.id
            )
            self.surface_of_regions[new_fine_region.id] = {
              "type": "pie",
              "center": point,
              "material": material_cell,
              "radius1": radius1,
              "radius2": radius2,
              "angle": angle,
              "coolant": False
            }
            # if position == "up"
          if symmetry == "triangular_mesh":
            main_rid = regions_ids[0]
            regions_symmetry[main_rid] = [regions_ids[1], regions_ids[2]]  
        elif type_coarse_node == "square_side":
          sum_volumes += vol_cell/2
          new_fine_region1 = Cell(fill=cell.content, volume=vol_cell/4)
          new_fine_region2 = Cell(fill=cell.content, volume=vol_cell/4)
          regions[new_fine_region1.id] = new_fine_region1
          regions[new_fine_region2.id] = new_fine_region2

          self.coarse_node.regions_points_relation[material_cell.name].append(
            new_fine_region1.id
          )
          self.coarse_node.regions_points_relation[material_cell.name].append(
            new_fine_region2.id
          )
          angle1 = self.coarse_node.theta_corners[0]
          angle2 = self.coarse_node.theta_corners[1]

          self.surface_of_regions[new_fine_region1.id] = {
            "type": "pie",
            "center": node_points[0],
            "material": material_cell,
            "radius1": radius1,
            "radius2": radius2,
            "angle": angle1,
            "coolant": False
          }
          self.surface_of_regions[new_fine_region2.id] = {
            "type": "pie",
            "center": node_points[-1],
            "material": material_cell,
            "radius1": radius1,
            "radius2": radius2,
            "angle": angle2,
            "coolant": False
          }
          if symmetry == "triangular_mesh":
            regions_symmetry[new_fine_region1.id] = [new_fine_region2.id]
        elif type_coarse_node == "corner_triangle":
          sum_volumes += vol_cell/12
          new_fine_region = Cell(fill=cell.content, volume=vol_cell/12)
          regions[new_fine_region.id] = new_fine_region
          self.coarse_node.regions_points_relation[material_cell.name].append(
            new_fine_region.id
          )
          regions_symmetry[new_fine_region.id] = []
          self.surface_of_regions[new_fine_region.id] = {
            "type": "pie",
            "center": node_points[0],
            "material": material_cell,
            "radius1": radius1,
            "radius2": radius2,
            "angle":  self.coarse_node.theta_corners[0],
            "coolant": False
          }
        radius1 = radius2
      # Last level: typically coolant ---------------------
      last_level = regions_pin[-1]
      cell = pin_from_assembly.cells[last_level.cell_id]
      vol_node = self.coarse_node.calculate_node_volume()
      vol_coolant = vol_node - sum_volumes
      # print(vol_coolant)
      # print(cell.content, vol_coolant)
      new_fine_region = Cell(fill=cell.content, volume=vol_coolant)
      regions[new_fine_region.id] = new_fine_region
      regions_symmetry[new_fine_region.id] = []
      self.surface_of_regions[new_fine_region.id] = {
        "type": "coolant",  
        "material": cell.content,
        "coolant": True
      }
      

      self.regions = regions
      self.regions_symmetry = regions_symmetry
    except AssertionError:
      print('triangular mesh not valid')
      raise SystemExit

  def get_pin_regions_points(self, theta_points=10):
    """
    Only implemented for a single radius pie slice
    """
    regions_points = {}
    for r in self.regions:
      try:
        if not self.surface_of_regions[r]["coolant"]:
       
          point = self.surface_of_regions[r]["center"]
          angle = self.surface_of_regions[r]["angle"]
          radius1 = self.surface_of_regions[r]["radius1"]
          radius2 = self.surface_of_regions[r]["radius2"]
          material = self.surface_of_regions[r]['material']
          th1, th2 = angle

          # Convert angle from degrees to radians
          th1_rad = np.deg2rad(th1)
          th2_rad = np.deg2rad(th2)

          x = np.array([point[0]+radius1*math.cos(th1_rad)])
          y = np.array([point[1]+radius1*math.sin(th1_rad)])
          


          # Create theta for the pie slice (from 0 to angle)
          theta = np.linspace(th1_rad, th2_rad, theta_points)

          # Calculate the coordinates of the outer arc
          x_arc_outer = point[0] + radius2 * np.cos(theta)
          y_arc_outer = point[1] + radius2 * np.sin(theta)

          # Calculate the coordinates of the inner arc (reverse direction)
          x_arc_inner = point[0] + radius1 * np.cos(theta[::-1])
          y_arc_inner = point[1] + radius1 * np.sin(theta[::-1])

          x = np.concatenate([x, x_arc_outer, x_arc_inner])
          y = np.concatenate([y, y_arc_outer, y_arc_inner])
          regions_points[r] = {
            "x": x,
            "y": y,
            "color": material.color
          }
      except KeyError:
        pass
    return regions_points
  
  def get_coolant_regions_points(self):
    regions_points = {}

    for r in self.regions:
      try:
        if self.surface_of_regions[r]["coolant"]:
          material = self.surface_of_regions[r]['material']
          regions_points[r] = {
            "x": [p[0] for p in self.coarse_node.surf_points],
            "y": [p[1] for p in self.coarse_node.surf_points],
            "color": material.color
          }
      except KeyError:
        pass
    return regions_points
  
  
  def calculate_volumes(self):
    volumes = {}
    # print(self.__type_coarse_mesh)
    
    # if self.__type_coarse_mesh == 'pin_cell':
    #   volumes = self.__calculate_volumes_pin_cell_mesh()
    # elif self.__type_coarse_mesh == "square_grid_hex_pin":
    #   volumes = {r_id: cell.volume for r_id, cell in self.regions.items()}
    # elif self.__type_coarse_mesh == "square_grid":
    #   volumes = {r_id: cell.volume for r_id, cell in self.regions.items()}
    # elif self.__type_coarse_mesh == "triangular":
    #   volumes = {r_id: cell.volume for r_id, cell in self.regions.items()}
    # elif self.__type_coarse_mesh == "triangular_hex_pin":
    #   volumes = {r_id: cell.volume for r_id, cell in self.regions.items()}
    # elif self.__type_coarse_mesh == "core_assembly_triangular":
    #   volumes = {r_id: cell.volume for r_id, cell in self.regions.items()}

    volumes = {r_id: cell.volume for r_id, cell in self.regions.items()}
    self.regions_volume = volumes
    return volumes
  
  def __calculate_volumes_pin_cell_mesh(self):
    regions_vol = {}
    for r_id, cell in self.regions.items(): 
      vol = cell.volume
      # print(cell.content.name, vol)
      regions_vol[r_id] = vol
    return regions_vol

    
    

