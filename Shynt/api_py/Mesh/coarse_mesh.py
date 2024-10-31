
from Shynt.api_py.Mesh.coarse_node import (
  CoarseNodeTriangularMesh_InnerTriangle,
  CoarseNodeTriangularMesh_SquareSubChanell,
  CoarseNodeTriangularMesh_TriangleCorner,
  CoarseNodeTriangleHexPin,
  CoarseNodeSquarePinCell,
  CoarseNodeHexagonalPinCell
)

from Shynt.api_py.Geometry.universes import (
  SquareLattice,
  HexagonalLatticeTypeX,
  HexagonalLattice,
  Pin
)
from Shynt.api_py.Geometry.surfaces import (
  InfiniteSquareCylinderZ,
  InfiniteHexagonalCylinderXtype,
  InfiniteHexagonalCylinderYtype,
)

from Shynt.api_py.Geometry.cells import Cell


class CoarseMesh():

  def __init__(self, cell: Cell) -> None:
    super().__init__()
    self.__cell = cell
  
  def calculate_surfaces_twins(self):
    """Class method to extract the surface twins of every node. It sweeps all
    surfaces and then call the method  find_surface_twin()

    Returns
    -------
    surface_twins : dict

    """

    num_coarse_nodes = len(self.coarse_nodes)
    print(f"Calculating surface twins for {num_coarse_nodes} coarse_nodes ...")

    surf_checked = {s_idx: False for s_idx in range(1,self.num_surfaces+2)}
    surface_twins = {s_idx: [[None, None, None]] for s_idx in range(1,self.num_surfaces+2)}
    for n_id, coarse_node in self.coarse_nodes.items():
      print(n_id, end=",")
      if n_id % 20 == 0: print()
      
      node_surfs = coarse_node.surfaces
      for s_id, points in node_surfs.items():
        if surf_checked[s_id]: continue
        twin_info = self.__find_surface_twin(n_id, points)
        # if n_id == 7: print(s_id, twin)
        if twin_info:
          # twin_info: (surf_twin, node_of_twin)
          surf_twin, other_nid = twin_info
          surface_twins[s_id] = [[surf_twin, other_nid, 1.0]] # weight is 1.0
          surface_twins[surf_twin] = [[s_id, n_id, 1.0]] # weight is 1.0
          surf_checked[surf_twin] = True
          surf_checked[s_id] = True
          
    print()
    self.surface_twins = surface_twins
  
  def __find_surface_twin(self, n_id, points):
    """Class method to find the surface twin of one surface. It sweeps all the
    surfaces and compare the points  in order to determine wether is a twin or
    not.
    
    Parameters
    ----------
    n_id : int

    points : tuple

    rings : list

    Returns
    -------
    surf_twin : int or None
    """
    p1, p2 = points
    p1 = (round(p1[0], 6), round(p1[1], 6))
    p2 = (round(p2[0], 6), round(p2[1], 6))

    p1x, p1y = p1
    p2x, p2y = p2

    # if n_id <= 6: print("surf: ", s_id, p1,p2, "searching -----------")

    # print(rings)
    
    for other_n_id, coarse_node in self.coarse_nodes.items():
      if n_id == other_n_id: continue      
      node_surfs = coarse_node.surfaces
      for s_id_other, points_other in node_surfs.items():
        p1_other, p2_other = points_other
        p1_other = (round(p1_other[0], 6), round(p1_other[1], 6))
        p2_other = (round(p2_other[0], 6), round(p2_other[1], 6)) 

        p1x_o, p1y_o = p1_other
        p2x_o, p2y_o = p2_other
        
        if p1x == p1x_o and p1y == p1y_o and p2x == p2x_o and p2y == p2y_o:
          return s_id_other, other_n_id
        
        if p1x == p2x_o and p1y == p2y_o and p2x == p1x_o and p2y == p1y_o:
          return s_id_other, other_n_id
    


  @property
  def cell(self) -> Cell:
    return self.__cell


class PinCellMesh(CoarseMesh):
  """Class to represent  a pin cell mesh only used in a square lattice.
  Each coarse node is a pin cell, so different coarse nodes be differentiate
  by type of pin.
  Steps to generate the coarse_mesh:
    1. Calculate the nodes coordinates (points of the mesh) and the 
      map of nodes
    2. With each set of points generate instance CoarseNode
      2.a Generate surfaces (only a set of two points)
      2.b Count surfaces ids and calculate surface twins
    4. Calculate equivalent coarse nodes or provide them

  Attributes
  ----------

  Methods
  -------
  """
    
  def __init__(self, cell):
    try:
      if isinstance(cell.content, SquareLattice):
        pass
      elif isinstance(cell.content, Pin):
        pass
      else:
        raise AssertionError
    except AssertionError:
      print(" ************ Error ************ ")
      print("PinCellMesh only supported for SquareLattice or Pin")
      raise SystemExit
    
    super().__init__(cell)
    self.__isPin = False
    if isinstance(cell.content, Pin):
      self.__isPin = True

    self.type_mesh = ""
    self.lattice = super().cell.content
    self.points_mesh = {}
    self.coarse_nodes_map = []
    self.coarse_nodes = {}
    self.num_surfaces = 0
    self.surfaces = {}
    self.surface_twins = {}

    self.unique_nodes = []
    self.equivalent_nodes = {} # num to array
    self.equivalent_nodes_rel = {} # num to num
    
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}

  
  
    
  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    coarse_nodes = {}
    surfaces = {}
    nodes_map = []
    s_id = 0
    n_id = 1
    if self.__isPin:
      # check surface
      pin_universe = super().cell.content
      print(pin_universe)
      pin_cell_wrapper = super().cell.region.surface
      if isinstance(pin_cell_wrapper, InfiniteSquareCylinderZ):
        node = CoarseNodeSquarePinCell(
          n_id, 'pin_cell_mesh', pin_cell_wrapper.half_width,
          pin_cell_wrapper.center
        )
        s_id = node.calculate_surfaces(s_id)
        surfaces.update(node.surfaces)
        coarse_nodes[1] = node
      else:
        # hexagonal cell
        node = CoarseNodeHexagonalPinCell(
          n_id, 'pin_cell_mesh', pin_cell_wrapper
        )
        s_id = node.calculate_surfaces(s_id)
        node.universe = pin_universe 
        surfaces.update(node.surfaces)
        coarse_nodes[1] = node
      
    else:
      pin_centers = self.lattice.pin_centers
      half_pitch = self.lattice.pitch / 2
      
      for i, row in enumerate(pin_centers):
        row_node = []
        for j, center in enumerate(row):
          pin_universe = self.lattice.array[i][j]

          node = CoarseNodeSquarePinCell(
            n_id, 'pin_cell_mesh', half_pitch, center
          )
          s_id = node.calculate_surfaces(s_id)
          surfaces.update(node.surfaces)
          node.universe = pin_universe 
          coarse_nodes[n_id] = node

          row_node.append(n_id)
          n_id += 1
        nodes_map.append(row_node)
        
    self.surfaces = surfaces
    self.coarse_nodes_map = nodes_map
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id


  def find_equivalent_nodes(self):
    """Class method to calculate the equivalent nodes in the square lattice.
    It takes the name of every pin to differentiate from other pins

    Parameters
    ----------

    Returns
    -------

    """
    equivalent_nodes = {}

    if self.__isPin:
      equivalent_nodes[1] = [1]
    else:
      array = self.lattice.array
      pin_types = {

      }
      for i, row in enumerate(array):
        for j, pin in enumerate(row):
          node_id = self.coarse_nodes_map[i][j]
          try:
            pin_types[pin.name].append(node_id)
          except KeyError:
            pin_types[pin.name] = [node_id]
      
      for pin_name, array in pin_types.items():
        equivalent_nodes[array[0]] = array
    
    self.equivalent_nodes = equivalent_nodes
    self.unique_nodes = list(equivalent_nodes.keys())

  def find_equivalent_nodes_symmetry(self):
    """Class method to find the equivalent nodes symmetry. For
    This mesh all the nodes have "same" symmetry
    
    Parameters
    ----------

    Returns
    -------

    """

    nodes_symmetry = {}
    for n_id in self.unique_nodes:
      nodes_symmetry[n_id] = {}
      for n_eq in self.equivalent_nodes[n_id]:
        nodes_symmetry[n_id][n_eq] = {"same": ""}
    self.symmetry = nodes_symmetry

  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}

    eq_nodes_node_to_node = {}

    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      eq_nodes_node_to_node[n_id] = n_id

      # print(regs_main_node)
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        eq_nodes_node_to_node[eq_node] = n_id

        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]

    self.equivalent_nodes_rel = eq_nodes_node_to_node

    self.equivalent_regions = regions_eq

  def find_eq_surfaces(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the dictionary
    since the surfaces are declared in the same order.

    Parameters
    ----------

    Returns
    -------
    
    """
    surfaces_eq = {}

    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      for surf in surfs_main_node:
        surfaces_eq[surf] = surf
      for eq_node in eq_nodes:
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s, s_p in enumerate(surfs_eq_node):
          surfaces_eq[s_p] = surfs_main_node[s]
    self.equivalent_surfaces = surfaces_eq

  
  @property
  def nodes_surfaces(self):
    nodes_surfaces = {}
    for n_id, coarse_node in self.coarse_nodes.items():
      nodes_surfaces[n_id] = coarse_node.surfaces
    return nodes_surfaces
  

class TriangularMesh(CoarseMesh):
  """Class to represent a triangular coarse mesh in a hexagonal assembly.

  ...

  Attributes
  ----------
  __offset : float

  __map_pins : list
  
  __symmetry : dict

  clean_mesh_map : list

  points_mesh : list

  rectangles : list

  surface_twins : dict

  nodes_surfaces : dict

  num_surfaces : int

  equivalent_nodes : dict

  corse_nodes_regions : dict

  regions_coarse_node : dict

  coarse_nodes_regions_material : dict

  regions_volume : dict

  coarse_nodes : dict

  type_mesh : str

  hex_assembly : Universe

  map_nodes : list of list
  
  clean_map : list of list
  
  x_div : list
  
  y_div : list of list

  Methods
  -------
  __create_nodes_hex_assem()
  
  """
    
  def __init__(self, cell):
    super().__init__(cell)
    self.hex_assembly = super().cell.content
    self.points_mesh = {}
    self.mesh_rings = []
    self.coarse_nodes = {}
    self.type_nodes = {}
    self.nodes_surfaces = {}
    self.num_surfaces = 0
    self.surface_twins = {}
    self.surfaces = {}

    # self.calculate_nodes_coordinates()
    # self.calculate_nodes_surfaces()
    # self.calculate_surfaces_twins()
    
    self.map_pins = []
    self.symmetry = {}
    self.mesh_map = [] # mesh in rings

    self.pin_coarse_nodes = {}
    self.pins_in_nodes = {}

    self.main_nodes = []
    self.main_regions = []
    self.main_regions_vol = []

    self.main_surfaces = []

    self.equivalent_nodes = {}
    self.equivalent_nodes_rel = {}
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}


    self.corse_nodes_regions = {}
    self.regions_coarse_node = {}
    self.coarse_nodes_regions_material = {}
    self.regions_volume = {}

    self.type_mesh = ""

    # self.map_nodes = self.__get_node_map()
    # self.clean_map = self.__get_clean_map()
    
  def create_coarse_nodes(self, initial_nid=1, initial_sid=0, no_void=False):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    
    (
      nodes_surfaces, 
      nodes_map, 
      nodes_diff, 
      node_pin_levels,
      triangle_type,
      nodes_center,
      boundary_node_theta,
    ) = self.__get_mesh_in_rings(initial_n_id=initial_nid)

    self.points_mesh = nodes_surfaces
    self.mesh_rings = nodes_map
    self.coarse_nodes_differentiator = nodes_diff



    coarse_nodes = {}
    surfaces = {}
    nodes_surfaces = {}

    s_id = initial_sid
    
    num_rings = len(self.mesh_rings)
    for r, ring in enumerate(self.mesh_rings):
      for n_id in ring:
        surface_points = self.points_mesh[n_id]
        node = None
        if r < num_rings - 1:
          node = CoarseNodeTriangularMesh_InnerTriangle(
            n_id, self.hex_assembly, surface_points, no_void,
            node_pin_levels[n_id],  None, nodes_center[n_id]
            # triangle_type[n_id],
            # nodes_center[n_id]
          )
          node.pins_in_node = self.pins_in_nodes[n_id]
        else:
          num_points = len(surface_points)
          if num_points == 4: 
            node = CoarseNodeTriangularMesh_SquareSubChanell(
              n_id, self.hex_assembly, surface_points
            )
            node.pins_in_node = self.pins_in_nodes[n_id]
            node.theta_corners = boundary_node_theta[n_id]
          elif num_points == 3: 
            node = CoarseNodeTriangularMesh_TriangleCorner(
              n_id, self.hex_assembly, surface_points, no_void,
              node_pin_levels[n_id], 
            )
            node.pins_in_node = self.pins_in_nodes[n_id]
            node.theta_corners = boundary_node_theta[n_id]

            
        surfs, s_id = node.calculate_surfaces(s_id)
        surfaces.update(surfs)
        
        
        nodes_surfaces[n_id] = surfs 
        coarse_nodes[n_id] = node

    self.num_coarse_nodes = n_id
    self.coarse_nodes = coarse_nodes
    self.surfaces = surfaces
    self.nodes_surfaces = nodes_surfaces

    final_sid = s_id
    self.num_surfaces = final_sid - initial_sid

  def __get_mesh_in_rings(self, initial_n_id):
    """
    The function __get_mesh_in_rings calculates the triangles and 
    triangle rings for a mesh based on the pin centers of an assembly
    
    
    :return: three values: node_id, triangles, and triangle_rings.
    """
    
    

    nodes_surfaces = {}
    nodes_triangle_type = {}
    nodes_center = {}
    nodes_differentiator = {}
    node_pin_levels = {}
    nodes_map = []
    boundary_node_theta = {}
    assembly = self.cell.content
    pin_centers = assembly.element_centers
    num_rings = assembly.num_rings
    assembly_rings = assembly.rings
    pitch = assembly.pitch

    pins_coarse_nodes = {
      r: {
        e: [] for e in range(r*6)
      } for r in range(self.hex_assembly.num_rings)
    }
    pins_coarse_nodes[0][0] = [
      initial_n_id,
      initial_n_id + 1,
      initial_n_id + 2,
      initial_n_id + 3,
      initial_n_id + 4,
      initial_n_id + 5,
    ]
    pins_in_nodes = {}

    # first ring ----------------
    center = pin_centers[0][0] # center of the hexagonal assembly

    # Second ring --------------
    node_id = initial_n_id
    nid_ring = []
    triangle_up = True
    # tr_up: left_fuel
    # tr_up: top_fuel
    # tr_up: right_fuel
    for p in range(-6,0):
      # In every pin look for the material -----------------------------
      p1 = center # Always the center of the hexagonal assembly
      p2 = pin_centers[1][p] # Center of that pin in the second ring
      p3 = pin_centers[1][p+1] # center of next pin in the ring
      # --------------------------------------------------
      pin1 = (0,0)
      pin2 = (1,p+6)
      if p == -1:
        pin3 = (1,0)
      else:
        pin3 = (1,p+6+1)

      pins_coarse_nodes[pin2[0]][pin2[1]].append(node_id)
      pins_coarse_nodes[pin3[0]][pin3[1]].append(node_id)
      
      pins_in_nodes[node_id] = {pin1:0, pin2:1, pin3:2}
      # --------------------------------------------------

      
      nodes_center[node_id] = self.__calc_node_centroid((p1,p2,p3))
      nodes_surfaces[node_id] = (p1, p2, p3)
      nodes_differentiator[node_id] = (
        assembly_rings[0][0].name,    #p1
        assembly_rings[1][p].name,    #p2
        assembly_rings[1][p+1].name   #p3
      )
      node_pin_levels[node_id] = (
        assembly_rings[0][0].pin_levels,    #p1
        assembly_rings[1][p].pin_levels,    #p2
        assembly_rings[1][p+1].pin_levels   #p3
      )
      if triangle_up:
        nodes_triangle_type[node_id] = "up"
      else:
        nodes_triangle_type[node_id] = "down"
      
      triangle_up = not triangle_up

      nid_ring.append(node_id)
      node_id += 1
    nodes_map.append(nid_ring)

    # Other rings -------------

    if num_rings > 2:
      num_pins_on_side = 1
      for r in range(2, num_rings):
        # print(f'\nring {r}')
        nid_ring = []
        prev_ring = pin_centers[r-1]
        num_pins_prev_ring = len(prev_ring)
        prev_ring_idx = -num_pins_prev_ring
        num_pins = len(pin_centers[r])
        on_side_pins_counter = 0
        on_side = False
        for p in range(-num_pins,0):
          # print(f'{p+num_pins}', end=' ')
          if on_side: # Pin is on one of the sides
            p1 = pin_centers[r][p]
            p2 = prev_ring[prev_ring_idx]
            p3 = prev_ring[prev_ring_idx+1]
            # -------------------------------------------------------
            pin1 = (r,p+num_pins)
            pin2 = (r-1,prev_ring_idx+num_pins_prev_ring)
            if prev_ring_idx == -1:
              pin3 = (r-1,0)
            else:
              pin3 = (r-1,prev_ring_idx+num_pins_prev_ring+1)

            pins_coarse_nodes[pin1[0]][pin1[1]].append(node_id)
            pins_coarse_nodes[pin2[0]][pin2[1]].append(node_id)
            pins_coarse_nodes[pin3[0]][pin3[1]].append(node_id)
            
            pins_in_nodes[node_id] = {pin1:0, pin2:1, pin3:2}
            # -------------------------------------------------------

            


            nodes_surfaces[node_id] = (p1, p2, p3)
            nodes_center[node_id] = self.__calc_node_centroid((p1,p2,p3))

            nid_ring.append(node_id)

            p1_levels = assembly_rings[r][p].name
            p2_levels = assembly_rings[r-1][prev_ring_idx].name
            p3_levels = assembly_rings[r-1][prev_ring_idx+1].name
            nodes_differentiator[node_id] = (
              p1_levels, p2_levels, p3_levels
            )
            node_pin_levels[node_id] = (
              assembly_rings[r][p].pin_levels,                  # p1
              assembly_rings[r-1][prev_ring_idx].pin_levels,    # p2
              assembly_rings[r-1][prev_ring_idx+1].pin_levels   # p3
            )
            if triangle_up:
              nodes_triangle_type[node_id] = "up"
            else:
              nodes_triangle_type[node_id] = "down"

            triangle_up = not triangle_up
            # ---------------------------
            p1 = pin_centers[r][p]
            p2 = pin_centers[r][p+1]
            p3 = prev_ring[prev_ring_idx+1]

            # -------------------------------------------------------
            pin1 = (r,p+num_pins)
            if p == -1:
              pin2 = (r,0)
              pin3 = (r-1,0)
            else:
              pin2 = (r,p+num_pins+1)
              pin3 = (r-1,prev_ring_idx+num_pins_prev_ring+1)

            pins_coarse_nodes[pin1[0]][pin1[1]].append(node_id+1)
            pins_coarse_nodes[pin2[0]][pin2[1]].append(node_id+1)
            pins_coarse_nodes[pin3[0]][pin3[1]].append(node_id+1)
            
            pins_in_nodes[node_id+1] = {pin1:0, pin2:1, pin3:2}


            # -------------------------------------------------------

            nodes_surfaces[node_id+1] = (p1, p2, p3)
            nodes_center[node_id+1] = self.__calc_node_centroid((p1,p2,p3))

            nid_ring.append(node_id+1)

            

            p1_levels = assembly_rings[r][p].name
            p2_levels = assembly_rings[r][p+1].name
            p3_levels = assembly_rings[r-1][prev_ring_idx+1].name

            nodes_differentiator[node_id+1] = (
              p1_levels, p2_levels, p3_levels
            )
            node_pin_levels[node_id+1] = (
              assembly_rings[r][p].pin_levels,                  # p1
              assembly_rings[r][p+1].pin_levels,    # p2
              assembly_rings[r-1][prev_ring_idx+1].pin_levels   # p3
            )
            
            if triangle_up:
              nodes_triangle_type[node_id] = "up"
            else:
              nodes_triangle_type[node_id] = "down"

            triangle_up = not triangle_up


            node_id += 2
            on_side_pins_counter += 1
            prev_ring_idx += 1

          else: # Pin is in one of the corners
            on_side = True
            
            p1 = pin_centers[r][p]          
            p2 = pin_centers[r][p+1]        
            p3 = prev_ring[prev_ring_idx]   

            # -------------------------------------------------------
            pin1 = (r,p+num_pins)
            pin3 = (r-1,prev_ring_idx+num_pins_prev_ring)
            if p == -1:
              pin2 = (r,0)
            else:
              pin2 = (r,p+num_pins+1)

            pins_coarse_nodes[pin1[0]][pin1[1]].append(node_id)
            pins_coarse_nodes[pin2[0]][pin2[1]].append(node_id)
            pins_coarse_nodes[pin3[0]][pin3[1]].append(node_id)
            
            pins_in_nodes[node_id] = {pin1:0, pin2:1, pin3:2}


            # -------------------------------------------------------

            nodes_surfaces[node_id] = (p1, p2, p3)
            nodes_center[node_id] = self.__calc_node_centroid((p1,p2,p3))

            nid_ring.append(node_id)

            p1_levels = assembly_rings[r][p].name
            p2_levels = assembly_rings[r][p+1].name
            p3_levels = assembly_rings[r-1][prev_ring_idx].name
            nodes_differentiator[node_id] = (
              p1_levels, p2_levels, p3_levels
            )
            node_pin_levels[node_id] = (
              assembly_rings[r][p].pin_levels,                  # p1
              assembly_rings[r][p+1].pin_levels,    # p2
              assembly_rings[r-1][prev_ring_idx].pin_levels   # p3
            )
            if triangle_up:
              nodes_triangle_type[node_id] = "up"
            else:
              nodes_triangle_type[node_id] = "down"

            triangle_up = not triangle_up
            
            node_id += 1

          if on_side_pins_counter == num_pins_on_side: 
            on_side = False
            on_side_pins_counter = 0
        nodes_map.append(nid_ring)
        num_pins_on_side += 1

    self.pin_coarse_nodes = pins_coarse_nodes
    self.pins_in_nodes = pins_in_nodes
    (
      nsurfs_boundary, 
      boundary_ring, 
      node_diff, 
      pin_levels_node,
      boundary_node_theta
    ) = self.__get_mesh_in_boundary(node_id)


    nodes_surfaces.update(nsurfs_boundary)
    nodes_map.append(boundary_ring)
    nodes_differentiator.update(node_diff)
    node_pin_levels.update(pin_levels_node)

    
    return (
      nodes_surfaces, 
      nodes_map, 
      nodes_differentiator, 
      node_pin_levels, 
      nodes_triangle_type, 
      nodes_center,
      boundary_node_theta
    )

  def __get_mesh_in_boundary(self, node_id):
    from math import (
      cos, sin, radians
    )
    import numpy as np

    boundary_node_theta = {}

    n_id = node_id

    assembly = self.cell.content
    pin_centers = assembly.element_centers
    num_rings = assembly.num_rings
    pitch = assembly.pitch
    
    # Boundary ----------------
    wrapper = self.cell.region.surface
    wrapper_radius = wrapper.radius
    
    wrapper_last_pin_radius = (num_rings-1)*pitch
    wlpr_square = wrapper_last_pin_radius * wrapper_last_pin_radius
    wrapper_last_pin_hw = np.sqrt(
      wlpr_square - wlpr_square/4
    )
    
    dptc = wrapper_radius - wrapper_last_pin_radius  # distance_pin_to_corner
    dpts = wrapper.half_width - wrapper_last_pin_hw  # distance_pin_to_side

    dx_dptc = dptc * np.cos(np.radians(30))
    dy_dptc = dptc * np.sin(np.radians(30))

    sides_dxdy = {
      'A': {
        'dx': 0,
        'dy': dpts,
        "dtc": +dptc
      },
      'B': {
        'dx': dpts * np.cos(np.radians(30)),
        'dy': dpts * np.sin(np.radians(30)),
        "dtc": +dptc
      },
      'C': {
        'dx': dpts * np.cos(np.radians(30)),
        'dy': -dpts * np.sin(np.radians(30)),
        "dtc": dptc
      },
      'D': {
        'dx': 0,
        'dy': -dpts,
        "dtc": dptc
      },
      'E': {
        'dx': -dpts * np.cos(np.radians(30)),
        'dy': -dpts * np.sin(np.radians(30)),
        "dtc": dptc
      },
      'F': {
        'dx': -dpts * np.cos(np.radians(30)),
        'dy': dpts * np.sin(np.radians(30)),
        "dtc": dptc
      }
    }
    theta = {
      'F': {
        'corner': [(150,180),(180,210)],
        'side': [(60,150),(150,240)],
      },
      'A': {
        'corner': [(120,150),(90,120)],
        'side': [(0,90),(90,180)],
      },
      'B': {
        'corner': [(60,90),(30,60)],
        'side': [(-60,30),(30,120)],
      },
      'C': {
        'corner': [(0,30),(330,360)],
        'side': [(240,330),(-30,60)],
      },
      'D': {
        'corner': [(270,300), (300,330)],
        'side': [(180,270),(270,360)],
      },
      'E': {
        'corner': [(240,270),(210,240)],
        'side': [(120,210),(210,300)],
      },
    }
    dtc_dx_dy = {
      'A': {
        't1': {
          "dx": -dpts * np.cos(np.radians(30)),
          "dy":  dpts * np.sin(np.radians(30)),
          "dptc_dx": -dptc * np.cos(np.radians(60)),
          "dptc_dy":  dptc * np.sin(np.radians(60))

        },
        't2': {
          "dx":  0.0,
          "dy":  dpts,
          "dptc_dx": -dptc * np.cos(np.radians(60)),
          "dptc_dy": dptc * np.sin(np.radians(60))
        },
      },
      'B': {
        't1': {
          "dx":  0.0,
          "dy":  dpts,
          "dptc_dx": dptc * np.cos(np.radians(60)),
          "dptc_dy": dptc * np.sin(np.radians(60))
        },
        't2': {
          "dx":  dpts * np.cos(np.radians(30)),
          "dy":  dpts * np.sin(np.radians(30)),
          "dptc_dx": dptc * np.cos(np.radians(60)),
          "dptc_dy": dptc * np.sin(np.radians(60))
        },
      },
      'C': {
        't1': {
          "dx":  dpts * np.cos(np.radians(30)),
          "dy":  dpts * np.sin(np.radians(30)),
          "dptc_dx": dptc,
          "dptc_dy": 0.0
        },
        't2': {
          "dx":  dpts * np.cos(np.radians(30)),
          "dy":  -dpts * np.sin(np.radians(30)),
          "dptc_dx": dptc,
          "dptc_dy": 0.0
        },
      },
      'D': {
        't1': {
          "dx":  dpts * np.cos(np.radians(30)),
          "dy":  -dpts * np.sin(np.radians(30)),
          "dptc_dx": dptc * np.cos(np.radians(60)),
          "dptc_dy": -dptc * np.sin(np.radians(60))
        },
        't2': {
          "dx":  0.0,
          "dy":  -dpts,
          "dptc_dx": dptc * np.cos(np.radians(60)),
          "dptc_dy": -dptc * np.sin(np.radians(60))
        },
      },
      'E': {
        't1': {
          "dx":  0.0,
          "dy":  -dpts,
          "dptc_dx": -dptc * np.cos(np.radians(60)),
          "dptc_dy": -dptc * np.sin(np.radians(60))
        },
        't2': {
          "dx":  -dpts * np.cos(np.radians(30)),
          "dy":  -dpts * np.sin(np.radians(30)),
          "dptc_dx": -dptc * np.cos(np.radians(60)),
          "dptc_dy": -dptc * np.sin(np.radians(60))
        },
      },
      'F': {
        't1': {
          "dx": -dpts * np.cos(np.radians(30)),
          "dy": -dpts * np.sin(np.radians(30)),
          "dptc_dx": -dptc,
          "dptc_dy": 0
        },
        't2': {
          "dx": -dpts * np.cos(np.radians(30)),
          "dy":  dpts * np.sin(np.radians(30)),
          "dptc_dx": -dptc,
          "dptc_dy": 0
        },
      },
    }
    
    hexagon_sides =  ['F','A','B','C','D','E']
    last_ring = pin_centers[-1]
    num_pins_last_ring = len(last_ring)

    last_ring_pins = assembly.rings[-1]

    
    corner_positions = [0]
    num_pins_last_ring = len(last_ring)
    pins_to_corner = int(num_pins_last_ring / 6)
    p2c_count = 0
    for i in range(5):
      corner_positions.append(p2c_count + pins_to_corner)
      p2c_count += pins_to_corner
    

    nodes = {}
    node_diff = {}
    node_pin_levels = {}
    node_ring = []

    
    side_idx = 0
    distance = 0.0
    for p in range(-num_pins_last_ring, 0):
      side = hexagon_sides[side_idx]
      
      # Corners first -----------------------------------
      if p+num_pins_last_ring in corner_positions:
        dx = round(dtc_dx_dy[side]['t1']['dx'], 8)
        dy = round(dtc_dx_dy[side]['t1']['dy'], 8)
        dptc_dx = round(dtc_dx_dy[side]['t1']['dptc_dx'], 8)
        dptc_dy = round(dtc_dx_dy[side]['t1']['dptc_dy'], 8)
        p1 = last_ring[p]
        p2 = (
          last_ring[p][0] + dptc_dx, 
          last_ring[p][1] + dptc_dy, 
        )
        p3 = (
          last_ring[p][0] + dx, 
          last_ring[p][1] + dy, 
        )
        # ----------------------------------------------
        pin1 = (num_rings-1,p+num_pins_last_ring)
        

        self.pin_coarse_nodes[pin1[0]][pin1[1]].append(n_id)
        self.pin_coarse_nodes[pin1[0]][pin1[1]].append(n_id+1)

        self.pins_in_nodes[n_id] = {pin1: 0}
        self.pins_in_nodes[n_id+1] = {pin1: 0}
        boundary_node_theta[n_id] = [theta[side]["corner"][0]]
        boundary_node_theta[n_id+1] = [theta[side]["corner"][1]]

        # ----------------------------------------------

        nodes[n_id] = (p1, p2, p3)
        node_ring.append(n_id)


        dx = round(dtc_dx_dy[side]['t2']['dx'], 8)
        dy = round(dtc_dx_dy[side]['t2']['dy'], 8)
        dptc_dx = round(dtc_dx_dy[side]['t2']['dptc_dx'], 8)
        dptc_dy = round(dtc_dx_dy[side]['t2']['dptc_dy'], 8)

        p1 = last_ring[p]
        p2 = (
          last_ring[p][0] + dptc_dx, 
          last_ring[p][1] + dptc_dy, 
        )
        p3 = (
          last_ring[p][0] + dx, 
          last_ring[p][1] + dy, 
        )
        nodes[n_id+1] = [p1, p2, p3]
        node_ring.append(n_id+1)

        pin1_levels = last_ring_pins[p].name
        node_diff[n_id] = (pin1_levels,)
        node_diff[n_id+1] = (pin1_levels,)
        node_pin_levels[n_id] = (
          last_ring_pins[p].pin_levels,     # p1
        )
        node_pin_levels[n_id+1] = (
          last_ring_pins[p].pin_levels,     # p1
        )

        n_id += 2

      # Then sides -------------------------------------
      # dx = round(sides_dxdy[side]['dx'], 8)
      # dy = round(sides_dxdy[side]['dy'], 8)
      dx = sides_dxdy[side]['dx']
      dy = sides_dxdy[side]['dy']

      p1 = last_ring[p]
      
      p2 = (
        last_ring[p][0] + dx, 
        last_ring[p][1] + dy, 
      )
      p3 = (
        last_ring[p+1][0] + dx, 
        last_ring[p+1][1] + dy, 
      )
      p4 = last_ring[p+1]

      # ----------------------------------------------
      pin1 = (num_rings-1,p+num_pins_last_ring)
      if p == -1:
        pin2 = (num_rings-1,0)
      else:
        pin2 = (num_rings-1,p+num_pins_last_ring+1)

      self.pin_coarse_nodes[pin1[0]][pin1[1]].append(n_id)
      self.pin_coarse_nodes[pin2[0]][pin2[1]].append(n_id)

      self.pins_in_nodes[n_id] = {pin1: 0, pin2: 1}
      boundary_node_theta[n_id] = theta[side]["side"]

      # ----------------------------------------------
      
      nodes[n_id] = (p1, p2, p3, p4)
      node_ring.append(n_id)

      pin1_levels = last_ring_pins[p].name
      pin2_levels = last_ring_pins[p+1].name
      node_diff[n_id] = (
        pin1_levels, pin2_levels
      )
      node_pin_levels[n_id] = (
        last_ring_pins[p].pin_levels,     # p1
        last_ring_pins[p+1].pin_levels,   # p2
      )
      

      n_id += 1
      


      distance += pitch
      # print(distance)
      if abs(distance - wrapper_last_pin_radius) <= 1e-8:
        side_idx += 1
        distance = 0.0
      
    return nodes, node_ring, node_diff, node_pin_levels, boundary_node_theta
  
  def calculate_nodes_surfaces(self):
    nodes_surfaces = {}
    surfaces = {}
    s_id = 1
    for n_id, node_points in self.points_mesh.items():
      num_points = len(node_points)
      if num_points == 3: # triangle
        p1, p2, p3 = node_points
        surf1 = (p1,p2)
        surf2 = (p2,p3)
        surf3 = (p3,p1)
        nodes_surfaces[n_id] = {
          s_id: surf1, 
          s_id+1: surf2, 
          s_id+2: surf3
        }
        surfaces[s_id] = surf1
        surfaces[s_id+1] = surf2
        surfaces[s_id+2] = surf3

        s_id += 3
      elif num_points == 4: # rectangle
        p1, p2, p3, p4 = node_points
        surf1 = (p1,p2)
        surf2 = (p2,p3)
        surf3 = (p3,p4)
        surf4 = (p4,p1)

        nodes_surfaces[n_id] = {
          s_id: surf1, 
          s_id+1: surf2, 
          s_id+2: surf3,
          s_id+3: surf4
        }
        surfaces[s_id] = surf1
        surfaces[s_id+1] = surf2
        surfaces[s_id+2] = surf3
        surfaces[s_id+3] = surf4

        s_id += 4
    self.surfaces = surfaces
    self.nodes_surfaces = nodes_surfaces
    self.num_surfaces = s_id - 1

  def __calc_node_centroid(self, points): 
    xc = 0.0
    yc = 0.0
    num_points = len(points)
    for p in points:
      xp, yp = p
      xc += xp
      yc += yp

    return xc/num_points, yc/num_points
  
  def find_regions_of_pin(self):
    pins_regions = {}
    for r in range(self.hex_assembly.num_rings):
      for e in range(len(self.hex_assembly.rings[r])):
        pins_regions[(r,e)] = {}
        nodes_pin = self.pin_coarse_nodes[r][e]
        for nid in nodes_pin:
          for mat_name, regs_list in self.coarse_nodes[nid].regions_points_relation.items():
            pin_idx = self.pins_in_nodes[nid][(r,e)]
            if mat_name in pins_regions[(r,e)]:
              pins_regions[(r,e)][mat_name].append(regs_list[pin_idx])
            else:
              pins_regions[(r,e)][mat_name] = [regs_list[pin_idx]]
    return pins_regions

  def find_equivalent_nodes(self):
    """Class method to calculate the equivalent nodes in the triangular mesh.
    
    For an hexagonal assembly with one pin_cell type there is only three types
    of nodes:
      - the triangular subchannel inside the hexagon
      - the triangular subchannel in the corner
      - the squared subchannel on the edges
    
    So the proccess, to find the equivalent nodes is simply to check the zone
    where the coarse node is. This is all nodes are the same contained in all
    rings, except for the last ring.  In the last ring the way to differentiate
    is the number of points to check if it is a square or a triangle.

    Parameters
    ----------

    Returns
    -------

    """
    
    equivalent_nodes = {
      1: [], # inner triangle
      2: [], # corner triangles
      3: []  # square sides
    }
    
    # Assuming a single pin type inside the hexagonal assembly
    num_rings = len(self.mesh_rings)
    for r in range(num_rings-1):
      ring = self.mesh_rings[r]
      for n_id in ring:
        equivalent_nodes[1].append(n_id)

    last_ring = self.mesh_rings[-1]
    for n_id in last_ring:
      node_surfs = self.points_mesh[n_id]
      
      if len(node_surfs) == 3:
        equivalent_nodes[2].append(n_id)
      if len(node_surfs) == 4:
        equivalent_nodes[3].append(n_id)
    
    
    # print(equivalent_nodes[2])
    self.equivalent_nodes = {
      equivalent_nodes[1][0]: equivalent_nodes[1], # inner triangles
      equivalent_nodes[2][0]: equivalent_nodes[2], # corner triangles
      equivalent_nodes[3][0]: equivalent_nodes[3], # square sides
    }
    self.main_nodes = [
      equivalent_nodes[1][0],
      equivalent_nodes[2][0],
      equivalent_nodes[3][0]
    ]
    self.type_nodes = {
      "inner_triangle": equivalent_nodes[1],
      "corner_triangle": equivalent_nodes[2],
      "square_side": equivalent_nodes[3],
    }
    self.unique_nodes = list(self.equivalent_nodes.keys())
  
  def find_equivalent_nodes_symmetry(self):
    """Class method to calculate the equivalent nodes symmetry 
    in the triangular mesh.
    
    
      - the triangular subchannel inside the hexagon
      - the triangular subchannel in the corner
      - the squared subchannel on the edges
    
    For the inner triangles and for the squares the symmetry is the same,
    and for the corner triangles it is {"mirror" : "right"}

    #TODO Check if it is neccesary to change for the inner triangles to 
    #TODO mirror-down when it comes to region symmetry
    Parameters
    ----------

    Returns
    -------

    """
    nodes_symmetry = {}
    
    for ttype, eq_nodes_list in self.type_nodes.items():
      main_node = eq_nodes_list[0]
      nodes_symmetry[main_node] = {}
      for n, n_eq in enumerate(eq_nodes_list):
        if ttype == 'inner_triangle':
          nodes_symmetry[main_node][n_eq] = {'same': ''}
        elif ttype == 'corner_triangle':
          if n%2 == 0: 
            nodes_symmetry[main_node][n_eq] = {'same': ''}
          else:
            nodes_symmetry[main_node][n_eq] = {'mirror': 'right'}
        elif ttype == 'square_side':
          nodes_symmetry[main_node][n_eq] = {'same': ''}
          

    self.symmetry = nodes_symmetry
    
  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}

    eq_nodes_node_to_node = {}

    main_regions = []
    main_regions_vol = []


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      main_regions += regs_main_node

      for rid in regs_main_node:
        main_regions_vol.append(
          self.coarse_nodes[n_id].fine_mesh.regions[rid].volume
        )
      
      eq_nodes_node_to_node[n_id] = n_id
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        eq_nodes_node_to_node[eq_node] = n_id

        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]

    self.equivalent_nodes_rel = eq_nodes_node_to_node
    self.main_regions = main_regions
    self.main_regions_vol = main_regions_vol
    self.equivalent_regions = regions_eq
    
  def find_eq_surfaces(self):
    """Class method to find the equivalent surfaces of nodes of the same type
    with respect to the main node. The criteria is the symmetry of the node

    Parameters
    ----------

    Returns
    -------
    
    """
   

    surfaces_eq = {}
    mirror_right = {'mirror': 'right'}
    mirror_down = {'mirror': 'down'}
    mirror_right_down = {'mirror': 'right_down'}

    main_surfaces = []


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # print(n_id, eq_nodes)
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      main_surfaces += surfs_main_node
      # print(surfs_main_node)
      for surf in surfs_main_node: surfaces_eq[surf] = surf 
        

      for eq_node in eq_nodes:
        node_symmetry = self.symmetry[n_id][eq_node]
        # print(eq_node, node_symmetry)
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s_eq, s_m in zip(surfs_eq_node, surfs_main_node):
          surfaces_eq[s_eq] = s_m 
    self.main_surfaces = main_surfaces
    self.equivalent_surfaces = surfaces_eq


class TriangularMeshHexPin(CoarseMesh):
  """Class to represent a triangular coarse mesh in a hexagonal assembly.

  ...

  Attributes
  ----------
  __offset : float

  __map_pins : list
  
  __symmetry : dict

  clean_mesh_map : list

  points_mesh : list

  rectangles : list

  surface_twins : dict

  nodes_surfaces : dict

  num_surfaces : int

  equivalent_nodes : dict

  corse_nodes_regions : dict

  regions_coarse_node : dict

  coarse_nodes_regions_material : dict

  regions_volume : dict

  coarse_nodes : dict

  type_mesh : str

  hex_assembly : Universe

  map_nodes : list of list
  
  clean_map : list of list
  
  x_div : list
  
  y_div : list of list

  Methods
  -------
  __create_nodes_hex_assem()
  
  """
    
  def __init__(self, cell):
    try:
      assert(isinstance(cell.content, Pin))
        
    except AssertionError:
      print(" ************ Error ************ ")
      print("TriangularMeshHexPin only supported for Pin universe")
      raise SystemExit
    
    super().__init__(cell)

    self.type_mesh = ""
    self.lattice = super().cell.content
    self.points_mesh = {}
    self.coarse_nodes_map = []
    self.coarse_nodes = {}
    self.num_surfaces = 0
    self.surfaces = {}
    self.surface_twins = {}

    self.unique_nodes = []
    self.equivalent_nodes = {} # num to array
    self.equivalent_nodes_rel = {} # num to num
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}
    
  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype
    from Shynt.api_py.Mesh.coarse_node import CoarseNodeSquareGridHexPin
    coarse_nodes = {}
    surfaces = {}
    nodes_map = []
    s_id = 0
    n_id = 1
    
    # check surface
    pin_universe = super().cell.content
    pin_cell_wrapper = super().cell.region.surface
    half_width = pin_cell_wrapper.half_width
    hexwrap_radius = pin_cell_wrapper.radius
    cx, cy = pin_cell_wrapper.center

    if isinstance(pin_cell_wrapper, InfiniteHexagonalCylinderXtype):
      #Hexagonal Pin type X
      nodes_positions = [
        'top_left', 'top_right', 
        'right',
        'bottom_right', 'bottom_left',
        'left'
      ]
      node_points = {
        'top_left': (
          (cx,cy),
          (cx-half_width, cy+hexwrap_radius/2),
          (cx, cy+hexwrap_radius)
        ), 
        'top_right': (
          (cx,cy),
          (cx, cy+hexwrap_radius),
          (cx+half_width, cy+hexwrap_radius/2),
        ), 
        'right': (
          (cx,cy),
          (cx+half_width, cy+hexwrap_radius/2),
          (cx+half_width, cy-hexwrap_radius/2),
        ), 
        'bottom_right': (
          (cx,cy),
          (cx+half_width, cy-hexwrap_radius/2),
          (cx, cy-hexwrap_radius),
        ), 
        'bottom_left': (
          (cx,cy),
          (cx, cy-hexwrap_radius),
          (cx-half_width, cy-hexwrap_radius/2),
        ), 
        'left': (
          (cx,cy),
          (cx-half_width, cy-hexwrap_radius/2),
          (cx-half_width, cy+hexwrap_radius/2),
        ), 
      }
      for p, position in enumerate(nodes_positions):

        node = CoarseNodeTriangleHexPin(
          n_id, 'triangular_hex_pin', pin_universe, pin_cell_wrapper,
          node_points[position]
        )
        node.universe = pin_universe
        # print(s_id)
        s_id = node.calculate_surfaces(s_id)
        surfaces.update(node.surfaces)
        coarse_nodes[p+1] = node
    else:
      #Hexagonal Pin type Y
      raise NotImplementedError
      
     
    self.surfaces = surfaces
    self.coarse_nodes_map = nodes_map
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id


  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}

    eq_nodes_node_to_node = {}


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      eq_nodes_node_to_node[n_id] = n_id
      # print(regs_main_node)
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        eq_nodes_node_to_node[eq_node] = n_id

        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]
    
    self.equivalent_nodes_rel = eq_nodes_node_to_node

    self.equivalent_regions = regions_eq

  def find_eq_surfaces(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the dictionary
    since the surfaces are declared in the same order.

    Parameters
    ----------

    Returns
    -------
    
    """
    surfaces_eq = {}

    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      for surf in surfs_main_node:
        surfaces_eq[surf] = surf
      for eq_node in eq_nodes:
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s, s_p in enumerate(surfs_eq_node):
          surfaces_eq[s_p] = surfs_main_node[s]
    self.equivalent_surfaces = surfaces_eq

  def __find_surface_twin(self, n_id, points, s_id):
    """Class method to find the surface twin of one surface. It sweeps all the
    surfaces and compare the points  in order to determine wether is a twin or
    not.
    
    Parameters
    ----------
    n_id : int

    points : tuple

    rings : list

    Returns
    -------
    surf_twin : int or None
    """
    p1, p2 = points
    p1 = (round(p1[0], 10), round(p1[1], 10))
    p2 = (round(p2[0], 10), round(p2[1], 10))

    p1x, p1y = p1
    p2x, p2y = p2

    # if n_id <= 6: print("surf: ", s_id, p1,p2, "searching -----------")
    surf_twin = None

    # print(rings)
    
    for other_n_id, coarse_node in self.coarse_nodes.items():
      if n_id == other_n_id: continue      
      node_surfs = coarse_node.surfaces
      for s_id_other, points_other in node_surfs.items():
        p1_other, p2_other = points_other
        p1_other = (round(p1_other[0], 10), round(p1_other[1], 10))
        p2_other = (round(p2_other[0], 10), round(p2_other[1], 10)) 

        p1x_o, p1y_o = p1_other
        p2x_o, p2y_o = p2_other
        
        if p1x == p1x_o and p1y == p1y_o and p2x == p2x_o and p2y == p2y_o:
          return s_id_other
        
        if p1x == p2x_o and p1y == p2y_o and p2x == p1x_o and p2y == p1y_o:
          return s_id_other

  @property
  def nodes_surfaces(self):
    nodes_surfaces = {}
    for n_id, coarse_node in self.coarse_nodes.items():
      nodes_surfaces[n_id] = coarse_node.surfaces
    return nodes_surfaces
  

class CoreMesh(CoarseMesh):

  def __init__(self, cell, boundary_bc, surface_twins=None):
    super().__init__(cell)
    self.core = super().cell.content
    self.boundary_bc = boundary_bc
    self.points_mesh = {}
    self.mesh_rings = [] # will be rings with the mesh of every assembly
    self.coarse_nodes = {}
    self.boundary_coarse_nodes = []
    self.coarse_nodes_differentiator = {}
    self.type_nodes = {}
    self.nodes_surfaces = {}
    self.surfaces = {}
    self.num_surfaces = 0
    self.surface_twins = surface_twins


    self.main_nodes = []
    self.main_regions = []
    self.main_regions_vol = []
    self.main_surfaces = []


    self.assembly_coarse_meshes = {}
    self.equivalent_nodes = {} # num to array
    self.equivalent_nodes_rel = {} # num to num
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.unique_nodes = []

    self.type_nodes = {}
    self.corse_nodes_regions = {}
    self.regions_coarse_node = {}
    self.coarse_nodes_regions_material = {}
    self.regions_volume = {}
    self.core_map = {}
  
  def create_coarse_nodes(self, no_void=False, last_ring=None):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    # nodes_surfaces, nodes_map, nodes_diff, node_pin_levels
    print("creating coarse_nodes ....")
    core_pitch = self.core.pitch
    node_id = 0
    surf_id = 0
    all_rings_mesh = []
    if isinstance(self.core, HexagonalLattice):
      
      # Assemblies --------------------------------------------------------
      for r, ring in enumerate(self.core.rings): # Reach ring of assemblies
        ring_mesh = []
        self.assembly_coarse_meshes[r] = {}
        for e, hex_lattice in enumerate(ring): # each assembly
          hexagon_surf_assembly = None
          if isinstance(hex_lattice, HexagonalLatticeTypeX):
            hexagon_surf_assembly = InfiniteHexagonalCylinderYtype(
              hex_lattice.center[0], hex_lattice.center[1], core_pitch/2
            )
          
          cell_lattice = Cell(region=-hexagon_surf_assembly, fill=hex_lattice)
          hex_lattice_mesh = TriangularMesh(cell_lattice)
          hex_lattice_mesh.create_coarse_nodes(
            initial_nid=node_id+1, no_void=no_void, initial_sid=surf_id
          )
          node_id = hex_lattice_mesh.num_coarse_nodes
          surf_id += hex_lattice_mesh.num_surfaces

          self.points_mesh.update(hex_lattice_mesh.nodes_surfaces)

          # self.mesh_rings = (hex_lattice_mesh.nodes_map)
          
          self.coarse_nodes_differentiator.update(
            hex_lattice_mesh.coarse_nodes_differentiator
          )
          ring_mesh.append(hex_lattice_mesh.mesh_rings)

          self.coarse_nodes.update(hex_lattice_mesh.coarse_nodes)
          self.nodes_surfaces.update(hex_lattice_mesh.nodes_surfaces)
          self.surfaces.update(hex_lattice_mesh.surfaces)

          self.num_surfaces += hex_lattice_mesh.num_surfaces
          self.assembly_coarse_meshes[r][e] = hex_lattice_mesh
        all_rings_mesh.append(ring_mesh)
      # Boundaries ------------------------------------------------
      # print(self.cell.region.surface)
      # print("Boundaries")
      last_ring = self.core.rings[self.core.num_rings-1]
      core_wrapper = self.cell.region.surface
      # print(last_ring)
      for hex_assembly in last_ring:
        # is center over the hexant line??
        # print(hex_assembly.closing_hexagon)
        center_hex = hex_assembly.closing_hexagon.center
        is_on_line_fhexant, hexant_line = core_wrapper.isPointOverHexantLine(
          center_hex
        )
        # print(center_hex, is_on_line_fhexant, hexant_line)
        # which hexant ??
        # break
      self.mesh_rings = all_rings_mesh
      

  def calculate_surfaces_twins(self):
    """Class method to extract the surface twins of every node. It will 
      find it by rings

    Returns
    -------
    surface_twins : dict

    """

    num_coarse_nodes = len(self.coarse_nodes)
    print(f"Calculating surface twins for {num_coarse_nodes} coarse_nodes ...")
    surf_checked = {s_idx: False for s_idx in range(1,self.num_surfaces+1)}
    surface_twins = {s_idx: [[None, None, None]] for s_idx in range(1,self.num_surfaces+1)}
    core_map = self.core.calculate_lattice_map()
    # (self.mesh_rings[0][0][-1])
    self.core_map = core_map
    print(f"{len(core_map)} rings")

    for core_ring_idx, core_ring in enumerate(self.mesh_rings): 
      print('-'*100)
      print("Core ring: ", core_ring_idx)
      print('Number of assemblies: ', len(core_ring))
      a = 0
      # the ring of assemblies ------------
      for assembly_idx, assembly in enumerate(core_ring):
        a += 1
        print(f'{assembly_idx+1}, ', end='')
        # Calculating surfaces twins inside each assembly --------------------
        num_rings_in_assembly = len(assembly)
        for cn_ring_idx, cn_ring in enumerate(assembly): 
          # for each ring of coarse ndoes ------------------------------------
          prev_ring = []
          current_ring = cn_ring
          next_ring = []
          # for the last ring in the assembly, boundary with other assembly
          if cn_ring_idx == num_rings_in_assembly-1:
            # This is the last ring of the assembly
            assemblies_around = core_map[core_ring_idx][assembly_idx]
            # print(assemblies_around)
            for assem_pos in assemblies_around:
              r_idx, p_idx = assem_pos
              # if r_idx == 6: continue
              last_ring_assembly_around = self.mesh_rings[r_idx][p_idx][-1]
              # print(last_ring_assembly_around)
              next_ring += last_ring_assembly_around
          else:
            # is inside the assembly
            next_ring = assembly[cn_ring_idx+1]
          if cn_ring_idx != 0:
            prev_ring = assembly[cn_ring_idx-1]
          
          # Now, prev_ring, current_ring and nex_ring are calculated
          for cn_id in cn_ring: # the coarse node id: cn_id
            node_surfs = self.coarse_nodes[cn_id].surfaces # get the surfaces of the node
            # print("coarse node: ", cn_id)
            for s_id, points in node_surfs.items():
              # if cn_ring_idx == len(assembly)-1:
                # print("surf: ", end='')
              # the surface of the coarse node
              if surf_checked[s_id]: 
                # print()
                continue
              twin_info = self.find_surface_twin(
                prev_ring, current_ring, next_ring, points, cn_id
              )
              # if cn_ring_idx == len(assembly)-1:
              #   print(twin_info)
              if twin_info:
                # twin_info: (surf_twin, node_of_twin)
                surf_twin, other_nid = twin_info
                # standard weight for a twin surface = 1.0
                surface_twins[s_id] = [[surf_twin, other_nid, 1.0]] 
                surface_twins[surf_twin] = [[s_id, cn_id, 1.0]]
                surf_checked[surf_twin] = True
                surf_checked[s_id] = True
          # if cn_ring_idx == len(assembly)-1:
          #   print("--------------")
          # if cn_ring_idx == len(assembly)-1:
          #   break
        if a % 6 == 0: print()
      # break
      print()
    self.surface_twins = surface_twins

  def calculate_sufaces_twins_boundary(self):
    def calculate_euclidean_distance(p1, p2):
      from math import sqrt

      x1, y1 = p1 
      x2, y2 = p2
      distance = sqrt(
        (x2-x1) ** 2 + (y2-y1) ** 2
      )
      return distance
    
    segment_counter = 0
    count_b = 0
      
    last_ring_core = self.mesh_rings[-1]    # last ring of assemblies
    assem_mesh = last_ring_core[0]          # First assembly of the last ring
    last_ring_assem = assem_mesh[-1]        # last ring mesh (boundaries) of that assembly
    boundary_surfaces = {}

    for bn in self.boundary_coarse_nodes:
      for bsid, bound_surf in self.coarse_nodes[bn].surfaces.items():
        self.surface_twins[bsid] = [[None,None,None]]

    for assem_mesh in last_ring_core:
      
      for nid in assem_mesh[-1]: # 

        surfaces = self.coarse_nodes[nid].surfaces
        for sid in surfaces:
          twin = self.surface_twins[sid]
          if twin[0][0] is None: # surface is connected to boundary node
            # look for twin in in boundary node
            # print(surfaces[sid])
            # print(twin)
            count_b += 1
            boundary_surfaces[sid] = surfaces[sid]
            for bn in self.boundary_coarse_nodes:
              # print(bn)
              # bn = 70127
              for bsid, bound_surf in self.coarse_nodes[bn].surfaces.items():
                # print(bsid, end=',')
                # print(bound_surf, surfaces[sid])
                # print("-"*50)
                point1_on_line = self.is_point_on_line_segment(
                  surfaces[sid][0], bound_surf[0], bound_surf[1]
                )
                point2_on_line = self.is_point_on_line_segment(
                  surfaces[sid][1], bound_surf[0], bound_surf[1]
                )
                # print("-"*50)

                if point1_on_line and point2_on_line:
                  # the surface is a segment of bn_surface
                  segment_counter += 1
                  area_i = calculate_euclidean_distance(surfaces[sid][0], surfaces[sid][1])
                  area_boundary = calculate_euclidean_distance(bound_surf[0], bound_surf[1])
                  weight = area_i / area_boundary

                  self.surface_twins[sid] = [[bsid, bn, weight]]
                  try:
                    assert (self.surface_twins[bsid][0][0] is None)
                    self.surface_twins[bsid] = [[sid, nid, weight]]

                  except AssertionError:
                    self.surface_twins[bsid] += [[sid, nid, weight]]

    print(segment_counter)
    print(count_b)
    return boundary_surfaces

  def is_point_on_line_segment(self, p, p1, p2):
    """
    Checks colineariy of a surface with a point by calculating the 
    determinant of

    | x1  y1  1 | 
    | x2  y2  1 |
    | x   y   1 |
    

    """
    
    x, y = p[0], p[1]
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    
    epsilon = 1e-7

    # If both points are the same, check if the point is the same
    # if abs(delta_x) < epsilon and abs(delta_y) < epsilon:
    #   return abs(x - x1) < epsilon and abs(y - y1) < epsilon

    # Calculate the determinant to check for collinearity
    determinant = x1*(y2-y) + x2*(y-y1) + x*(y1-y2)

    # Check if the determinant is close to zero
    if abs(determinant) >= epsilon:
      return False

    # Check if the point is within the segment bounds
    # Compare the x-coordinates and y-coordinates to ensure 
    # the point lies between line_point1 and line_point2
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    is_in_interval_x = (min_x - epsilon) <= x <= (max_x + epsilon)
    is_in_interval_y = (min_y - epsilon) <= y <= (max_y + epsilon)

    return is_in_interval_x and is_in_interval_y


  def find_surface_twin(self, prev_ring, current_ring, next_ring, points, n_id):
    """Class method to find the surface twin of one surface. It sweeps all the
    surfaces in the previous, current and next ring to check for the twin


    Parameters
    ----------
    n_id : int

    points : tuple

    rings : list

    Returns
    -------
    surf_twin : int or None
    """
    p1, p2 = points
    p1 = (p1[0], p1[1])
    p2 = (p2[0], p2[1])

    p1x, p1y = p1
    p2x, p2y = p2

    rings_to_search = [
      prev_ring, current_ring, next_ring
    ]
    epsilon = 1e-7
    for ring_search in rings_to_search:
      # print("searching in ring")
      for other_n_id in ring_search:
        if n_id == other_n_id: continue      
        other_node_surfs = self.coarse_nodes[other_n_id].surfaces
        for s_id_other, points_other in other_node_surfs.items():
          p1_other, p2_other = points_other
          p1_other = (p1_other[0], p1_other[1])      
          p2_other = (p2_other[0], p2_other[1])

          # print("Point ", p1, p2)
          # print("Other ", p1_other, p2_other)

          p1x_o, p1y_o = p1_other
          p2x_o, p2y_o = p2_other
          
          # if (
          #   (
          #     p1x == p1x_o
          #   ) and (
          #     p1y == p1y_o
          #   ) and (
          #     p2x == p2x_o
          #   ) and (
          #     p2y == p2y_o
          #   )
          # ):
          #   return s_id_other, other_n_id
          
          # if ((
          #   p1x == p2x_o
          #   ) and (
          #   p1y == p2y_o
          #   ) and (
          #   p2x == p1x_o
          #   ) and (
          #   p2y == p1y_o
          #   )):
          #   return s_id_other, other_n_id 
          if (
            (
              abs(p1x - p1x_o) <= epsilon
            ) and (
              abs(p1y - p1y_o) <= epsilon
            ) and (
              abs(p2x - p2x_o) <= epsilon
            ) and (
              abs(p2y - p2y_o) <= epsilon
            )
          ):
            return s_id_other, other_n_id
          
          if ((
            abs(p1x - p2x_o) <= epsilon
            ) and (
            abs(p1y - p2y_o) <= epsilon
            ) and (
            abs(p2x - p1x_o) <= epsilon
            ) and (
            abs(p2y - p1y_o) <= epsilon
            )):
            return s_id_other, other_n_id   
  
  def find_equivalent_nodes(self,):
    """
      This is not implemented to find the equivalent mesh with assemblies
      with different pins inside
    """
    type_assemblies_mesh = {}
    equivalent_nodes = {}
    
    type_nodes = {
    
    }

    for r, ring in self.assembly_coarse_meshes.items():
      print(f"ring {r} -------------------")
      for e, assembly_mesh in ring.items():

        assembly_mesh.find_equivalent_nodes()
        
        assem_name = self.core.rings[r][e].name
        if assem_name not in type_nodes:
          type_nodes[assem_name] = assembly_mesh.type_nodes
        else:
          type_nodes[assem_name]['inner_triangle'] += assembly_mesh.type_nodes['inner_triangle']
          type_nodes[assem_name]['corner_triangle'] += assembly_mesh.type_nodes['corner_triangle']
          type_nodes[assem_name]['square_side'] += assembly_mesh.type_nodes['square_side']

        
    # print(type_assemblies_mesh.keys())

    

    for assem_name in type_nodes:
      for node_type, node_list in type_nodes[assem_name].items():
        equivalent_nodes[node_list[0]] = node_list

    self.type_nodes = type_nodes
    self.equivalent_nodes = equivalent_nodes
    self.unique_nodes = list(equivalent_nodes.keys())
    self.main_nodes = list(equivalent_nodes.keys())

    
  def find_equivalent_nodes_symmetry(self):
    """Class method to calculate the equivalent nodes symmetry 
    in the triangular mesh.
    
    
      - the triangular subchannel inside the hexagon
      - the triangular subchannel in the corner
      - the squared subchannel on the edges
    
    For the inner triangles and for the squares the symmetry is the same,
    and for the corner triangles it is {"mirror" : "right"}

    #TODO Check if it is neccesary to change for the inner triangles to 
    #TODO mirror-down when it comes to region symmetry
    Parameters
    ----------

    Returns
    -------

    """
    nodes_symmetry = {}
    
    for ttype, eq_nodes_dict in self.type_nodes.items():
      for mid, eq_nodes_list in eq_nodes_dict.items():
        main_node = mid
        nodes_symmetry[main_node] = {}
        for n, n_eq in enumerate(eq_nodes_list):
          if ttype == 'inner_triangle':
            nodes_symmetry[main_node][n_eq] = {'same': ''}
          elif ttype == 'corner_triangle':
            if n%2 == 0: 
              nodes_symmetry[main_node][n_eq] = {'same': ''}
            else:
              nodes_symmetry[main_node][n_eq] = {'mirror': 'right'}
          elif ttype == 'square_side':
            nodes_symmetry[main_node][n_eq] = {'same': ''}
          

    self.symmetry = nodes_symmetry

  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}
    main_regions = []
    main_regions_vol = []
    eq_nodes_node_to_node = {}
    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      for rid in regs_main_node:
        main_regions_vol.append(
          self.coarse_nodes[n_id].fine_mesh.regions[rid].volume
        )
      main_regions += regs_main_node
      eq_nodes_node_to_node[n_id] = n_id

      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        eq_nodes_node_to_node[eq_node] = n_id
        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]

    self.equivalent_nodes_rel = eq_nodes_node_to_node
    self.main_regions = main_regions
    self.main_regions_vol = main_regions_vol
    self.equivalent_regions = regions_eq
    
  def find_eq_surfaces(self):
    """Class method to find the equivalent surfaces of nodes of the same type
    with respect to the main node. The criteria is the symmetry of the node

    Parameters
    ----------

    Returns
    -------
    
    """
   

    surfaces_eq = {}
    mirror_right = {'mirror': 'right'}
    mirror_down = {'mirror': 'down'}
    mirror_right_down = {'mirror': 'right_down'}

    main_surfaces = []

    for n_id, eq_nodes in self.equivalent_nodes.items():
      # print(n_id, eq_nodes)
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      main_surfaces += surfs_main_node

      # print(surfs_main_node)
      for surf in surfs_main_node: surfaces_eq[surf] = surf 
        

      for eq_node in eq_nodes:
        # node_symmetry = self.symmetry[n_id][eq_node]
        # print(eq_node, node_symmetry)
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s_eq, s_m in zip(surfs_eq_node, surfs_main_node):
          surfaces_eq[s_eq] = s_m 
    self.equivalent_surfaces = surfaces_eq
    self.main_surfaces = main_surfaces



class SquareGridHexPin(CoarseMesh):
  """Class to represent  a square grid mesh only used in a hexagonal pin.
  Each coarse node is a quarter of the hexagonal pin

  
  Attributes
  ----------

  Methods
  -------
  """
    
  def __init__(self, cell):
    try:
      assert(isinstance(cell.content, Pin))
        
    except AssertionError:
      print(" ************ Error ************ ")
      print("SquareGridHexPin only supported for Pin universe")
      raise SystemExit
    
    super().__init__(cell)

    self.type_mesh = ""
    self.lattice = super().cell.content
    self.points_mesh = {}
    self.coarse_nodes_map = []
    self.coarse_nodes = {}
    self.num_surfaces = 0
    self.surfaces = {}
    self.surface_twins = {}

    self.unique_nodes = []

    self.equivalent_nodes = {} # num to array
    self.equivalent_nodes_rel = {} # num to num

    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}

  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """
    from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype
    from Shynt.api_py.Mesh.coarse_node import CoarseNodeSquareGridHexPin
    coarse_nodes = {}
    surfaces = {}
    nodes_map = []
    s_id = 0
    n_id = 1
    
    # check surface
    pin_universe = super().cell.content
    pin_cell_wrapper = super().cell.region.surface
    if isinstance(pin_cell_wrapper, InfiniteHexagonalCylinderXtype):
      #Hexagonal Pin type X
      nodes_positions = ["top_left", "top_right", "lower_right", "lower_left"]
      for p, position in enumerate(nodes_positions):
        node = CoarseNodeSquareGridHexPin(
          n_id, 'square_grid_hex_pin', pin_cell_wrapper.half_width,
          pin_cell_wrapper.radius, position, pin_cell_wrapper.center
        )
        node.universe = pin_universe
        s_id = node.calculate_surfaces(s_id)
        surfaces.update(node.surfaces)
        coarse_nodes[p+1] = node
    else:
      #Hexagonal Pin type Y
      raise NotImplementedError
      
     
    self.surfaces = surfaces
    self.coarse_nodes_map = nodes_map
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id


  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}

    eq_nodes_node_to_node = {}



    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      eq_nodes_node_to_node[n_id] = n_id
      # print(regs_main_node)
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        eq_nodes_node_to_node[eq_node] = n_id
        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]

    self.equivalent_nodes_rel = eq_nodes_node_to_node

    self.equivalent_regions = regions_eq

  def find_eq_surfaces(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the dictionary
    since the surfaces are declared in the same order.

    Parameters
    ----------

    Returns
    -------
    
    """
    surfaces_eq = {}

    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      for surf in surfs_main_node:
        surfaces_eq[surf] = surf
      for eq_node in eq_nodes:
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        for s, s_p in enumerate(surfs_eq_node):
          surfaces_eq[s_p] = surfs_main_node[s]
    self.equivalent_surfaces = surfaces_eq

  def __find_surface_twin(self, n_id, points, s_id):
    """Class method to find the surface twin of one surface. It sweeps all the
    surfaces and compare the points  in order to determine wether is a twin or
    not.
    
    Parameters
    ----------
    n_id : int

    points : tuple

    rings : list

    Returns
    -------
    surf_twin : int or None
    """
    p1, p2 = points
    p1 = (round(p1[0], 10), round(p1[1], 10))
    p2 = (round(p2[0], 10), round(p2[1], 10))

    p1x, p1y = p1
    p2x, p2y = p2

    # if n_id <= 6: print("surf: ", s_id, p1,p2, "searching -----------")
    surf_twin = None

    # print(rings)
    
    for other_n_id, coarse_node in self.coarse_nodes.items():
      if n_id == other_n_id: continue      
      node_surfs = coarse_node.surfaces
      for s_id_other, points_other in node_surfs.items():
        p1_other, p2_other = points_other
        p1_other = (round(p1_other[0], 10), round(p1_other[1], 10))
        p2_other = (round(p2_other[0], 10), round(p2_other[1], 10)) 

        p1x_o, p1y_o = p1_other
        p2x_o, p2y_o = p2_other
        
        if p1x == p1x_o and p1y == p1y_o and p2x == p2x_o and p2y == p2y_o:
          return s_id_other
        
        if p1x == p2x_o and p1y == p2y_o and p2x == p1x_o and p2y == p1y_o:
          return s_id_other

  @property
  def nodes_surfaces(self):
    nodes_surfaces = {}
    for n_id, coarse_node in self.coarse_nodes.items():
      nodes_surfaces[n_id] = coarse_node.surfaces
    return nodes_surfaces
  

class SquareGridHexAssembly(CoarseMesh):
  """Class to represent a square grid coarse mesh where the coarse nodes
  surfaces are shared totally with the contiguous coarse node, i.e. there
  is no splitting of outward neutron currents between two coarse nodes.

  For the mesh to work the following parameters have to be provided hardcoded
  and externally:
    - Unique nodes
    - the surfaces of the nodes that have a diagonal (done in fix boundaries)
    - equivalent nodes
    - equivalent nodes symmetry
    - coarse_nodes_regions
    - coarse_nodes_regions_materials
    - regions_coarse_node
    - regions volume
  ...

  Attributes
  ----------
  __offset : float

  __map_pins : list
  
  __symmetry : dict

  clean_mesh_map : list

  points_mesh : list

  rectangles : list

  surface_twins : dict

  nodes_surfaces : dict

  num_surfaces : int

  equivalent_nodes : dict

  corse_nodes_regions : dict

  regions_coarse_node : dict

  coarse_nodes_regions_material : dict

  regions_volume : dict

  coarse_nodes : dict

  type_mesh : str

  hex_assembly : Universe

  map_nodes : list of list
  
  clean_map : list of list
  
  x_div : list
  
  y_div : list of list

  Methods
  -------
  __create_nodes_hex_assem() :

  __get_node_map() :

  __get_clean_map() :

  __get_x_div() :

  __get_y_div() :
  
  """

  def __init__(self, cell, offset=0.075):
    super().__init__(cell)
    self.__offset = offset
    self.hex_assembly = cell.content
    self.hex_wrapper = cell.region.surface
    self.coarse_nodes_map = []
    self.node_types = {}
    self.node_quadrants = {}

    self.x_div = []
    self.y_div = []
    self.points_mesh = []
    self.rectangles = []

    self.nodes_surfaces = {}
    self.num_surfaces = 0
    self.surface_twins = {}
    
    
    self.coarse_nodes = {}

    self.unique_nodes = []
    self.equivalent_nodes = {}
    self.equivalent_nodes_lookup = {}

    
    self.equivalent_regions = {}
    self.equivalent_surfaces = {}
    self.symmetry = {}

    self.corse_nodes_regions = {}
    self.regions_coarse_node = {}
    self.coarse_nodes_regions_material = {}
    self.type_mesh = "square_grid"

  def create_coarse_nodes(self):
    """Class method that created the coarse nodes and the 
    ids of its surfaces.
    
    Parameters
    ----------

    Returns
    -------

    """

    coarse_nodes = {}
    surfaces = {}
    nodes_surfaces = {}
    s_id = 0
    
    pin_centers = self.hex_assembly.pin_centers
    half_pitch = self.hex_assembly.pitch / 2

    # self.calculate_rectangles()
    
    for i, row in enumerate(self.coarse_nodes_map):
      row_node = []
      for j, n_id in enumerate(row):
        if n_id == 0: continue
        node_type = ""
        quadrant = ""
        try:
          node_type = self.node_types[n_id]
          quadrant = self.node_quadrants[n_id]
        except KeyError:
          pass
        coarse_node_class = grid_coarse_node_manager(node_type)
        # print(coarse_node_class)
        node = coarse_node_class(
          n_id, 'pin_cell_mesh', half_pitch, quadrant, self.hex_wrapper
        )

        rectangle_points = self.rectangles[n_id-1]
        s_id = node.calculate_surfaces(s_id, rectangle_points)
        surfaces.update(node.surfaces)
        nodes_surfaces[n_id] = node.surfaces
        coarse_nodes[n_id] = node

        row_node.append(n_id)
        
    self.surfaces = surfaces
    self.nodes_surfaces = nodes_surfaces
    self.coarse_nodes = coarse_nodes
    self.num_surfaces = s_id

  def calculate_rectangles(self):
    x_div = self.calculate_x_div()
    y_div = self.calculate_y_div(x_div)
    self.x_div = x_div
    self.y_div = y_div

    rectangles = self.get_rectangles_from_mesh_coord(x_div, y_div)
    print(len(rectangles))

  def calculate_x_div(self):
    x_div = []
    pins_array = self.hex_assembly.array
    middle_idx = len(pins_array) // 2
    
    first_row = pins_array[0]
    middle_row = pins_array[middle_idx]
    # hex_wrapper = super().cell.region.surface

    
    central_x_div = [
      self.hex_wrapper.center[0] - self.hex_wrapper.radius
    ]
    pitch = self.hex_assembly.pitch
    limit1 = first_row[0].center[0]
    limit2 = first_row[-1].center[0]

    for pin in middle_row:
      cx, cy = pin.center

      if cx < limit1:
        central_x_div.append(round(cx - self.__offset,8))
        if round(cx + pitch/2,8) == limit1:
          central_x_div.append(round(cx + pitch/2,8))
        else:
          central_x_div.append(round(cx - self.__offset + pitch/2,8))
        
      elif cx + pitch > limit1 and cx + pitch < limit2:
        if cx + pitch/2 == limit1:
          central_x_div.append(cx - self.__offset)
          central_x_div.append(cx + pitch/2)
        else:
          central_x_div.append(cx)
          central_x_div.append(cx + pitch/2)
      elif cx + pitch > limit2:
        if cx + pitch/2 == limit2:
          central_x_div.append(cx)
          central_x_div.append(cx + pitch/2)
        else:
          central_x_div.append(cx + self.__offset)
          central_x_div.append(cx + self.__offset + pitch/2)
    
    central_x_div[-1] = self.hex_wrapper.center[0] + self.hex_wrapper.radius
    
    x_div.append(central_x_div.copy()) 
    x_div.append(central_x_div.copy()) 

    last_row = central_x_div.copy()
    for i in range(9):
      new_row = last_row[1:-1]
      x_div.append(new_row)
      x_div = [new_row] + x_div

      last_row = new_row
        
  
    return x_div

  def calculate_y_div(self, x_div):
    y_div = [
      self.hex_wrapper.half_width
    ]
    for row in x_div:
      x_value = row[0]
      new_y = round(
        self.hex_wrapper.surf_F.useFunction(x_value, given="x"),8
      )
      y_div.append(new_y)
    
      if new_y == self.hex_wrapper.center[1]:
        break
    
    
    half_y_div = []
    for i in range(-2, -len(y_div)-1, -1):
      # print(i)
      
      half_y_div.append(y_div[i]*-1)
      
    y_div += half_y_div
  
   
    return y_div
    
  def get_rectangles_from_mesh_coord(self, x_div, y_div):
    self.x_div = x_div
    self.y_div = y_div

    mesh = []
    node_counter = 1
    row_x = 0
    num_y_div = len(y_div)
    
    for y in range(1, num_y_div):
      y_t = y_div[y-1]
      y_b = y_div[y]

      num_x_div = len(x_div[row_x])
      for x in range(1,num_x_div):
        x_l = x_div[row_x][x-1]
        x_r = x_div[row_x][x]
        rectangle = ((x_l,x_r),(y_b,y_t))
        
        mesh.append(rectangle)
        node_counter += 1

      row_x += 1
  
    self.rectangles = mesh
    return mesh

  def generate_fine_mesh_regions(self, unique_regions):
    from Shynt.api_py.Geometry.cells import Cell
    from Shynt.api_py.Mesh.local_mesh_material import MaterialMesh
    
    print('creating fine mesh ...')
    for n_id in  self.coarse_nodes:
      eq_node = self.equivalent_nodes_lookup[n_id]
      fine_regs = {}
      for reg in unique_regions[eq_node]:
        new_fine_reg = (Cell(fill=reg['material'], volume=reg['volume'])) 
        fine_regs[new_fine_reg.id] = new_fine_reg 
        # print(new_fine_reg.volume)
      new_fine_mesh = MaterialMesh(
        coarse_node=self.coarse_nodes[n_id],
        type_coarse_mesh=self.type_mesh
      )
      new_fine_mesh.regions = fine_regs
      self.coarse_nodes[n_id].fine_mesh = new_fine_mesh
        
  def find_eq_regions(self):
    """Class method to find the equivalent regions of nodes of the same type
    with respect to the main node. The criteria is the order in the 
    fine_mesh.regions dictionary since the regions are declared in the same 
    order.

    Parameters
    ----------

    Returns
    -------
    
    """
    regions_eq = {}


    for n_id, eq_nodes in self.equivalent_nodes.items():
      # coarse_node_regions = coarse_node.fine_mesh.regions
      regs_main_node = list(self.coarse_nodes[n_id].fine_mesh.regions.keys())
      for reg in regs_main_node:
        regions_eq[reg] = reg
      for eq_node in eq_nodes:
        regions_eq_node = list(
          self.coarse_nodes[eq_node].fine_mesh.regions.keys()
        )
        for r, reg_p in enumerate(regions_eq_node):
          regions_eq[reg_p] = regs_main_node[r]


    self.equivalent_regions = regions_eq
    
  def find_eq_surfaces(self):
    """Class method to find the equivalent surfaces of nodes of the same type
    with respect to the main node. The criteria is the symmetry of the node

    Parameters
    ----------

    Returns
    -------
    
    """
   

    surfaces_eq = {}

    same = {'same': ''}
    mirror_right = {'mirror': 'right'}
    mirror_down = {'mirror': 'down'}
    mirror_right_down = {'mirror': 'right_down'}



    for n_id, eq_nodes in self.equivalent_nodes.items():

      surfs_main_node = list(self.coarse_nodes[n_id].surfaces)
      for surf in surfs_main_node:
        surfaces_eq[surf] = surf
      for eq_node in eq_nodes:
        node_symmetry = self.symmetry[n_id][eq_node]
        # print(node_symmetry)
        surfs_eq_node = list(
          self.coarse_nodes[eq_node].surfaces.keys()
        )
        
        if node_symmetry == mirror_right:
          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
          elif len(surfs_main_node) == 4:

            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[3]
        elif node_symmetry == mirror_down:

          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[1]
          elif len(surfs_main_node) == 4:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[3]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[1]
        elif node_symmetry == mirror_right_down:

          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[1]
          elif len(surfs_main_node) == 4:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[3]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[1]
        else:
          # same
          if len(surfs_main_node) == 3:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
          elif len(surfs_main_node) == 4:
            surfaces_eq[surfs_eq_node[0]] = surfs_main_node[0]
            surfaces_eq[surfs_eq_node[1]] = surfs_main_node[1]
            surfaces_eq[surfs_eq_node[2]] = surfs_main_node[2]
            surfaces_eq[surfs_eq_node[3]] = surfs_main_node[3]
          
    self.equivalent_surfaces = surfaces_eq


def grid_coarse_node_manager(node_type):
  from Shynt.api_py.Mesh.coarse_node import (
    CoarseNodeSquareGridHexAssembly,
    CoarseNodeSquareGridHexAssembly_Inside1,
    CoarseNodeSquareGridHexAssembly_Inside2,
    CoarseNodeSquareGridHexAssembly_TrapezoidCorner,
    CoarseNodeSquareGridHexAssembly_SideEdge,
    CoarseNodeSquareGridHexAssembly_TriangleCorner
  )
  if node_type == 'trapezoid_corner':
    return CoarseNodeSquareGridHexAssembly_TrapezoidCorner
  elif node_type == 'inside1':
    return CoarseNodeSquareGridHexAssembly_Inside1
  elif node_type == 'inside2':
    return CoarseNodeSquareGridHexAssembly_Inside2
  elif node_type == 'side_edge':
    return CoarseNodeSquareGridHexAssembly_SideEdge
  elif node_type == 'triangle_corner':
    return CoarseNodeSquareGridHexAssembly_TriangleCorner
  else:
    return CoarseNodeSquareGridHexAssembly



