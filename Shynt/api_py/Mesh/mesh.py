from Shynt.api_py.Mesh.coarse_mesh import (
  PinCellMesh,
  TriangularMesh,
  SquareGridHexAssembly,
  SquareGridHexPin
) 


from Shynt.api_py.Geometry.cells import Cell


class Mesh():
  """Class that manashes the mesh, it creates:
    - coarse mesh (Every coarse node)
    - the fine mesh (for every coarse node)
    
  
    Steps to generate a mesh:
    1. Generate coarse mesh and its attributes see CoarseMesh class
    2. Generate fine mesh and its attributes
    3. generate surfaces areas
    4. generate regions volumes

  ...

  Attributes
  ----------
  cell :

  global_mesh_type :

  local_mesh_type :

  coarse_mesh :

  coarse_nodes :

  coarse_nodes_map :

  fine_mesh :

  fine_nodes :

  Methods
  -------
  create_coarse_mesh()

  create_fine_mesh()
  """

  def __init__(
  self, cell: Cell, global_mesh_type: str, local_mesh_type: str, offset=0.0
  ) -> None:
    self.cell = cell
    self.global_mesh_type = global_mesh_type
    self.local_mesh_type = local_mesh_type
    self.offset = offset
    
    self.coarse_mesh = None


    self.coarse_order = []
    self.all_surfaces_order = []
    self.all_regions_order = []
    self.coarse_region_rel = {}
    self.coarse_surface_rel = {}
    self.all_surfaces_area = {}
    self.all_regions_vol = {}
    self.__numRegions = None
    self.__numSurfaces = None
  
  def create_coarse_mesh(self) -> None:
    """Helper method to create the coarse mesh,
    It chooses between different meshes depending on the attribute 
    global_mesh_type. Types available:
      - pin_cell
      - square_grid
      - square_mesh_pin_no_share
    
    """
    print("creating coarse mesh ...")
    
    if self.global_mesh_type == "pin_cell":
      coarse_mesh =  PinCellMesh(self.cell)
    elif self.global_mesh_type == "square_grid_hex_pin":
      coarse_mesh =  SquareGridHexPin(
        self.cell
      )
    elif self.global_mesh_type == "square_grid":
      coarse_mesh =  SquareGridHexAssembly(
        self.cell, offset=self.offset
      )
    elif self.global_mesh_type == "triangular":
      coarse_mesh =  TriangularMesh(self.cell)

    self.coarse_mesh = coarse_mesh

  def create_fine_mesh(self) -> None:
    """Helper method to create the fine mesh,
    It chooses between different meshes depending on the attribute 
    local_mesh_type. Types available:
      - material 
    
      The fine mesh will be a dictionary with coarse node ids as keys
      and <class FineMesh> as value
    """
    from Shynt.api_py.Mesh.local_mesh_material import MaterialMesh
    from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX

    print("\ncreating fine mesh ...")
    is_hex_lattice = False
    if isinstance(self.cell.content, HexagonalLatticeTypeX): 
      is_hex_lattice = True

    coarse_nodes = self.coarse_mesh.coarse_nodes
    # print(coarse_nodes)
    if self.local_mesh_type == "material_cell":
      for nid, coarse_node in coarse_nodes.items():
        # print(nid)
        if coarse_node.fine_mesh is None:
          fine_mesh_of_node = MaterialMesh(
            coarse_node=coarse_node, 
            type_coarse_mesh=self.global_mesh_type, 
            is_hex_lattice=is_hex_lattice
          )
          coarse_node.fine_mesh = fine_mesh_of_node
  
  def create_regions_to_coarse_node_rel(self):
    rel = {}
    for n_id, c_node in self.coarse_mesh.coarse_nodes.items():
      regions_node = c_node.fine_mesh.regions
      for r_id in regions_node.keys():
        rel[r_id] = n_id
    
    return rel

  def create_coarse_region_rel(self):
    regions_rel = {}
    for n_id, c_node in self.coarse_mesh.coarse_nodes.items():
      regions_node = c_node.fine_mesh.regions
      regions_rel[n_id] = list(regions_node.keys())
    
    self.coarse_region_rel = regions_rel

  def create_coarse_surface_rel(self):
    surfaces_rel = {}
    for n_id, c_node in self.coarse_mesh.coarse_nodes.items():
      surfs_node = c_node.surfaces
      surfaces_rel[n_id] = list(surfs_node.keys())
    
    self.coarse_surface_rel = surfaces_rel 
  
  def create_all_surfaces_area(self):
    surfaces_areas = {}
    for c_node in self.coarse_mesh.coarse_nodes.values():
      areas = c_node.calculate_surfaces_areas()
      surfaces_areas.update(areas)
    
    self.all_surfaces_area = surfaces_areas
  
  def create_all_regions_vol(self):
    regions_vol = {}
    for n_id, c_node in self.coarse_mesh.coarse_nodes.items():
      fine_mesh = c_node.fine_mesh
      volumes = fine_mesh.calculate_volumes()
      
      regions_vol.update(volumes)
    
    self.all_regions_vol = regions_vol
  
  def get_all_coarse_nodes_ids(self):
    coarse_order = list(self.coarse_mesh.coarse_nodes.keys())
    self.coarse_order = coarse_order
    return coarse_order
  
  def get_all_regions(self):
    regions = []
    for cn in self.coarse_mesh.coarse_nodes.values():
      node_regs = cn.fine_mesh.regions
      regions += list(node_regs.keys())
    self.all_regions_order = regions
    return regions
  
  def get_all_surfaces(self):
    surfaces = []
    for cn in self.coarse_mesh.coarse_nodes.values():
      node_surfs = cn.surfaces
      surfaces += list(node_surfs.keys())
    self.all_surfaces_order = surfaces
    return surfaces


  def get_lookup_surface_to_node(self):
    lookup = {}
    for n_id, c_node in self.coarse_mesh.coarse_nodes.items():
      surfs_node = c_node.surfaces
      for sid in surfs_node:
        lookup[sid] = n_id
    
    return lookup
  
  @property
  def numRegions(self):
    if self.__numRegions is None:
      return len(self.all_regions_order)
    return self.__numRegions

  @property
  def numSurfaces(self):
    if self.__numSurfaces is None:
      return len(self.all_surfaces_order)
    return self.__numSurfaces