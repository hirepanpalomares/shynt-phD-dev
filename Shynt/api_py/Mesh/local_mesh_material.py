
from Shynt.api_py.Mesh.local_fine_mesh import FineMesh
from Shynt.api_py.Geometry.cells import Cell



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
    self, coarse_node=None, type_coarse_mesh='', is_hex_lattice=False
  ):
    super().__init__(coarse_node)
    self.__type_coarse_mesh = type_coarse_mesh
    self.__is_hex_lattice = is_hex_lattice
    self.regions = {}
    self.regions_volume = {}

    if type_coarse_mesh == 'pin_cell':
      self.__create_regions_pin_cell_mesh()
    elif type_coarse_mesh == 'square_grid_hex_pin':
      self.__create_regions_square_grid_hex_pin()
    elif type_coarse_mesh == 'square_grid':
      # Square grid applied to hexagonal lattices
      self.__create_regions_square_grid_hex_assem()
    elif type_coarse_mesh == 'triangular':
      self.__create_regions_triangular_mesh()
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

  def __create_regions_triangular_mesh(self):
    """Class method to create the regions of a triangular type coarse_node
    THE COARSE NODE SHOULD BE FROM A TRIANGULAR TYPE COARSE MESH

    It will have 3 or 4 points. Either a triangle or a square. There is two
    types of triangles: inner or corner triangle. The square is in the 
    boundary.

    

    
    """
    try:
      assert(self.__is_hex_lattice)
      num_surfaces = self.coarse_node.surfaces.keys()
      # print(num_surfaces)
      # pin_levels = 
      # print(self.coarse_node.type_coarse_node)
      print(super().coarse_node.universe)
      # ! GET PIN FROM THE HEXAGONAL LATTICE
    except AssertionError:
      print('triangular mesh not valid')
      raise SystemExit

    

  def calculate_volumes(self):
    volumes = {}
    # print(self.__type_coarse_mesh)
    if self.__type_coarse_mesh == 'pin_cell':
      # print("222")
      volumes = self.__calculate_volumes_pin_cell_mesh()
    elif self.__type_coarse_mesh == "square_grid_hex_pin":
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

    
    

