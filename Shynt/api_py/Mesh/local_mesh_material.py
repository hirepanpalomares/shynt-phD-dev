
from Shynt.api_py.Mesh.local_fine_mesh import FineMesh

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
  def __init__(self, coarse_node, type_coarse_mesh):
    super().__init__(coarse_node)
    self.__type_coarse_mesh = type_coarse_mesh

    self.regions = {}
    self.regions_volume = {}

    if type_coarse_mesh == 'pin_cell':
      self.__create_regions_pin_cell_mesh()

  
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

  def calculate_volumes(self):
    pass

    
    

