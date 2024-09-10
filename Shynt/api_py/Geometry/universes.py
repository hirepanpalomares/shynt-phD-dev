
from Shynt.api_py.Geometry.regions import Region
from collections import namedtuple

from Shynt.api_py.Geometry.utilities_geometry import (
   get_all_surfaces_in_a_cell, 
   get_all_surfaces_in_a_universe,
   declare_pin_by_cells
)

from Shynt.api_py.materials import Material

from Shynt.api_py.Geometry.surfaces import *
from Shynt.api_py.Geometry.regions import SurfaceSide

from Shynt.api_py.Geometry.cells import reset_cell_counter




class Universe:
  """
    Universe class
  """

  def __init__(self, name="") :
    self.__name = name
    self.__cells = {}
  
  def mark_cells(self):
    for id_, cell in self.__cells.items():
      cell.universe = self.__name

  def add_cell(self, cell):
    # print(cell)
    if isinstance(cell.content, Universe):
      self.__cells[cell.id] = cell
      self.add_cells(cell.content.cells)
    else:
      self.__cells[cell.id] = cell
  
  def add_cells(self, cells):
    self.__cells.update(cells)

  def translate(self, trans_vector):
    """Class method to translate all the cells of the universe
    
    """
    print(self.__cells.values())
    surfs_translated = []
    for cell in self.__cells.values():
      surfs_translated = cell.translate(trans_vector, surfs_translated)
    # surfaces_universe = get_all_surfaces_in_a_universe(self)
    # for id_, surf in surfaces_universe.items():
    #   surf.translate(trans_vector)

    return surfs_translated
  
  def find_fuel_cells(self):
    fuel = []
    no_fuel = []
    for c_id, cell in self.__cells.items():
      try:
        assert isinstance(cell.content, Material)
        if cell.content.isFuel:
          fuel.append(cell)
        else:
          no_fuel.append(cell)
      except AssertionError:
        print("***"*50)
        print()
        print ("Error trying to find material in cell")
        print("cell content is not Material instance")
        print()
        print("***"*50)
        raise SystemError
    return fuel, no_fuel

  def __eq__(self, __o: object) -> bool:
    """
      Comparaison of a universe:

      1.- It compares first the number of cells
      2.- It compares each of the cells

      Criteria:
      For a universe to be equal:
      1. Number of cells should be the same
      2. Each cell has to be equal to at least one of the cells in "__o" param
    """
    try:
      assert isinstance(__o, Universe)
      assert len(self.__cells) == len(__o.cells)
      compare_ = {c_id:False for c_id in self.__cells.keys()}
      for c_id, cell in self.__cells.items():
        for cell_other in __o.cells.values():
          if cell == cell_other:
            compare_[c_id] = True
      for key_, hasEqual in compare_.items():
        assert(hasEqual)
      return True
    except AssertionError:
      return False

  
  @property
  def name(self):
      return self.__name

  @name.setter
  def name(self, name):
      self.__name = name
      for cell in self.cells.values():
          cell.universe = name

  @property
  def cells(self):
      return self.__cells

  @cells.setter
  def cells(self, new_cells):
      self.__cells = new_cells


class Root(Universe):

  def __init__(
    self, cell, outside, mesh, energy_grid=None, mcparams=None, 
    libraries=""
  ):
    super().__init__(name="0")
    self.add_cell(cell)
    self.add_cell(outside)
    self.cell = cell
    self.outside_cell = outside
    self.mesh = mesh
    self.energy_grid = energy_grid  # Grid type
    self.mcparams = mcparams        # MontecarloParams type
    self.libraries = libraries      # Libraries for Serpent
    self.detector_files = {}
    self.xs_files = {}
    
    self.add_universe_to_cells()
    self.half_width = 0.0
    reset_surface_counter()
    reset_cell_counter()
  
  def add_universe_to_cells(self):
    for cell in self.cells.values():
      cell.universe = self.name


class Pin(Universe):

  """Class to represent a Pin universe composed by concentric cylinders 
  and its respective materials

  """
  def __init__(self, name):
    """Init method of the class

      Parameters
      ----------
      name : str   
        A string with the name of the pin universe

      material : Material()   
        An object or a list of objects of class Meterial corresponding to the 
        cylinder levels of the pincell in case of provided
      
      radius : float   
        An number or a lis of numbers corresponding to the radius of the 
        levels of the fuel pin universe.
    """
    super().__init__(name)
    self.__pin_levels = [] # These are the cells of the universe Pin
    self.pin_volumes = []
    self.__clone = False
    self.__outer_most_surface = None
    self.__last_region = None

    
    # self.__check_init_levels(material, radius, surroundings)
      
  def __check_init_levels(self, mat, radius, surroundings):
    """
      Checks the first material and radius given to the pin

      --------------------------------------------------------

      It has a bug: generates more cells than expected

      cancelled on May 27 2022

      If restored fix the bug!!!!
    """
    if mat and radius: # both are not None
      # single level is declared
      if isinstance(mat, Material) and (isinstance(radius, float) or isinstance(radius, int)):
        # a single level is declared
        self.add_level(mat, radius)
        if surroundings:
          self.add_level(surroundings)
      else:
        try:
          assert(isinstance(mat, list) and isinstance(radius, list))
          if len(mat) != len(radius):
            print(f"*** Error while difining either materials or radius for pin '{self.name}'")
            print("material and radius arrays must have the same length")
            raise SystemExit
          for m in range(len(mat)):
            self.add_level(mat[m], radius[m])
          if surroundings:
            self.add_level(surroundings)
        except AssertionError:
          print(f"*** Error while difining either materials or radius for pin '{self.name}'")
          print("material and radius must be introduced in an array")
          raise SystemExit
      # print("--- Warning --- Do not forget to declare the levels for the pin")
    elif mat is None and radius is None:
      if surroundings is not None:
        # Empty Pin declared
        # surroundings is a material
        self.add_level(surroundings) # Adding a material as a level for a void Pin
      else:
        print(f"*** Warning *** Remember to declare materials for the pin '{self.name}'")
    else:
      print(f"*** Error while difining either materials or radius for pin '{self.name}'")
      print("material and radius must be introduced either both or none")
      # Error: material and radius have to be declared either both or none
      raise SystemExit
          
  def add_level(self, material, radius=None):
    """
      Adds a concentric pin level

      Parameters
      -----------
      material    :   An object of the class Material

      radius      :   A float or integer, radius of the concentric cylinder 
                      from the center of the first level, if it is False, 
                      assumes that is the last material of the pin, i.e. 
                      surroundings of the pin
      
    """
    from .cells import Cell
    

    Level = namedtuple("Level", ["cell_id", "radius", "material"])
    corresponding_cyl = None
    if radius:
      cell_volume = None
      corresponding_cyl = InfiniteCylinderZ(0.0, 0.0, radius)
      if len(self.__pin_levels) == 0:
        # First level to be declared
        self.__last_region = -corresponding_cyl # SurfaceSide type
        cell_volume = corresponding_cyl.volume
      else:
        self.__last_region = +self.__outer_most_surface & -corresponding_cyl  # Region type
        cell_volume = corresponding_cyl.volume - self.__outer_most_surface.volume
      self.__outer_most_surface = corresponding_cyl
      
      cell = Cell(
        "%s_level_%s"%(self.name,len(self.__pin_levels)), 
        fill=material,
        region=self.__last_region,
        universe=self.name,
        volume=cell_volume
      )
      
      level = Level(cell.id, radius, material)
      super().add_cell(cell)
      self.__pin_levels.append(level)
    else:
      #surroundings
      if self.__outer_most_surface is None:
        # surroundnigs for a void pin
        cell = Cell(
          "%s_level_%s"%(self.name,len(self.__pin_levels)), 
          fill=material,
          universe=self.name,
          
        )
        level = Level(cell.id, None, material)
        super().add_cell(cell)
        self.__pin_levels.append(level)
      else:
        # surroundings of a pin with levels in it already
        cell_region = +self.__outer_most_surface
        cell = Cell(
          "%s_level_%s"%(self.name,len(self.__pin_levels)), 
          fill=material,
          region=cell_region,
          universe=self.name
        )
        level = Level(cell.id, None, material)
        super().add_cell(cell)
        self.__pin_levels.append(level)

  def close_last_level(self, surface):
    last_level = self.__pin_levels[-1]
    first_level = self.__pin_levels[0]
    ll_id = last_level.cell_id
    num_levels = len(self.__pin_levels)
    last_level_volume = None
    if num_levels == 0:
      # Void pin with no materials inside
      pass
    elif num_levels == 1:
      # The pin has only one level (surroundings)
      if first_level.radius is None:
        # Pin only with the surroundings (no cylinders inside)
        region = -surface
        last_level_volume = surface.volume
        super().cells[ll_id].region = region
        super().cells[ll_id].volume = last_level_volume

      else:
        # It means that there is a cylinder and could be an error
        # because the pin will be closed with a void space (no material)
        pass
    else:
      # The pin has two or more levels
      if last_level.radius is None:
        # the last level is infinite and will be closed with the region
        # Closing the last region, normally the coolant:
        last_level_volume = surface.volume - self.__outer_most_surface.volume
        # print(last_level_volume)
        new_half_space = -surface
        ll_region = super().cells[ll_id].region & new_half_space
        super().cells[ll_id].region = ll_region
        super().cells[ll_id].volume = last_level_volume

  def add_pin_levels(self, materials, radius, clone=False):
    """
      Setter method for attribute self.__pin_levels

      Params
      -------------------
      levels      |   
    """
    self.__clone = clone
    try:
      assert len(materials) == len(radius)
      for i in range(len(materials)):
        self.add_level(materials[i], radius[i])
    except AssertionError:
      print("**** Error in adding levels, materials and radius arrays",end="")
      print(" musthave the same length ****")
      raise SystemExit

  def translate_to(self, point):
    new_x, new_y = point
    center = self.__get_center()
    trans_vector = (
      new_x - center[0],
      new_y - center[1]
    )
    self.translate(trans_vector)

  def translate(self, trans_vector):
    """Class method to translate all the cells of the universe
    
    """
    num_levels = len(self.__pin_levels)
    surfs_translated = []
    for l in range(num_levels-1):
      level_id = self.__pin_levels[l].cell_id
      level = self.cells[level_id]
      surfs_translated = level.region.translate(trans_vector, surfs_translated)
    
  def copy(self):
    """
      It makes a copy of the pin with new surfaces,
      new cells, different ids
    """
    materials = []
    radius = []
    volumes = []
    first_level = self.__pin_levels[0]
    cell = super().cells[first_level.cell_id]
    if first_level.radius is None: # Void pin
      pin_copy = Pin(self.name)
      pin_copy.add_pin_levels([cell.content], [None])
      return pin_copy
    else:
      for level in self.__pin_levels:
        content = super().cells[level.cell_id].content
        materials.append(content)
        radius.append(level.radius)
      pin_copy = Pin(self.name)
      pin_copy.add_pin_levels(materials, radius)
      return pin_copy
  
  def __get_center(self):
    first_level = self.__pin_levels[0]
    cell = super().cells[first_level.cell_id]
    if first_level.radius is None:
      # center of a void pin
      return (0,0)
    else:
      cell_id = first_level.cell_id
      cell = super().cells[cell_id]
      return cell.region.surface.center

  def serpent_pin_syntax(self):
      syntax = f"pin {self.name}\n"
      for l in self.__pin_levels:
          mat_name = l.cell.content.name
          if l.radius:
              syntax += "%s %E \n"%(mat_name, l.radius)
          else:
              syntax += f"{mat_name}\n\n"
      return syntax

  def serpent_universe_pin_by_cell_syntax(self):
      syntax = []
      # syntax = ""

      cells = super().cells # levels of the pin { }
      
      for l in self.__pin_levels:
          l_id = l.cell_id
          text = cells[l_id].serpent_syntax()
          # syntax += text
          syntax.append(text)

      # syntax += "\n"

      return syntax

  @property
  def pin_levels(self):
    """Getter method for attribute self.__pin_levels
    """

    return self.__pin_levels

  @property
  def cells(self):
    return super().cells

  @cells.setter
  def cells(self, cells):
    super().cells = cells


  @property
  def materials(self):
    return super().get_universe_materials()
  
  @property
  def center(self):
    return self.__get_center()
  
  def __str__(self):

    statement = f"Pin({self.name})"
    return statement
  

  def __eq__(self, other) -> bool:
    """
      A pin is only equal to other when they have the same number
      of levels and the materials and radius in each level are similar
    """
    if len(self.__pin_levels) == len(other.pin_levels):
      # check that the levels are the same
      for i in range(len(self.__pin_levels)):
        self_level = self.__pin_levels[i]
        other_level = other.pin_levels[i]
        self_level_cell = super().cells[self_level.cell_id]
        other_level_cell = other.cells[other_level.cell_id]
        if (
          self_level_cell.content != other_level_cell.content
        ) or (
          self_level.radius != other_level.radius
        ):
          return False
      return True
    
    return False


class Lattice(Universe):

    def __init__(self, name=""):
        super().__init__(name)


class SquareLattice(Universe):
  """Square lattice universe composed by an array of fuel pins
  or universes

  """

  def __init__(self, name, left_bottom, pitch, array):
    """Init method of the class

      Parameters
      ----------
      name : str
        A string with the name of lattice universe
      left_bottom : tuple
        Point of lattice origin (origin is left bottom corner)
      pitch : float
        Pitch of the assembly
      array : list of list
        Lattice array

    """
    super().__init__(name)
    self.__left_bottom = left_bottom # corner
    self.__pitch = pitch
    self.__array = array
    self.centers = []

    self.__check_rows_cols()
    self.__ny = len(array)
    self.__nx = len(array[0])

    # self.__pin_types = self.__get_different_pins()
    # self.__num_pin_types = len(self.__pin_types)
    
    self.__create_cells()
    
  
  def __check_rows_cols(self):
    init_num_cols = len(self.__array[0])
    for row in self.__array:
      try:
        assert(len(row) == init_num_cols)
      except AssertionError:
        print("****** error ******")
        print("All rows of square lattice must have equal number of pin elements")

  def __create_cells(self):
    from .cells import Cell

    num_rows = self.__nx
    num_cols = self.__ny

    new_array = [
      [None for i in range(num_cols)] for j in range(num_rows)
    ]
    self.pin_centers = self.calculate_pin_centers(
      pitch=self.__pitch, left_bottom=self.__left_bottom
    )
    
    

    # pin_replacement = None
    for r, row in enumerate(self.__array):
      for p, pin in enumerate(row):
      
        copy_pin = pin.copy()
        new_center = self.pin_centers[r][p]
        copy_pin.translate_to(new_center)
        
        closing_square = InfiniteSquareCylinderZ(
          new_center[0], new_center[1], half_width=self.__pitch/2
        )
        copy_pin.close_last_level(closing_square)
        new_array[r][p] = copy_pin
        cells = copy_pin.cells
        super().add_cells(cells)

    self.__array = new_array

  def calculate_pin_centers(self, pitch=0.0, left_bottom=(0.0,0.0)):
    num_rows = self.__nx
    num_cols = self.__ny
    
    pin_centers = [
      [() for i in range(num_cols)] for j in range(num_rows)
    ]
    
    x_lb, y_lb = left_bottom
    # print(x_lb, y_lb)
    top_left = (x_lb, y_lb + num_rows*pitch)
    # print(top_left)
    x0, y0 = top_left
    # print(pitch)
    top_left_center_x = x0 + pitch/2
    top_left_center_y = y0 - pitch/2

    # pin_replacement = None
    for r, row in enumerate(self.__array):
      new_center_y = top_left_center_y - pitch * r
      for p, pin in enumerate(row):
        new_center_x = top_left_center_x + pitch * p
        new_center = (new_center_x, new_center_y)
        pin_centers[r][p] = new_center

    return pin_centers
  
  def recalculate_pin_centers(self, scale_f):
    """Class method to recalculate the pin centers with a scale factor. It acts
    over the pitch, this is used mainly for plotting.

    """
    pitch = self.__pitch * scale_f
    
    lb_x, lb_y = self.__left_bottom
    left_bottom = (lb_x*scale_f, lb_y*scale_f)

    new_pin_centers = self.calculate_pin_centers(
      pitch=pitch, left_bottom=left_bottom
    )
    

    return new_pin_centers
  
  def __get_different_pins(self):
    types = []
    for row in self.__array:
      for pin in row:
        if pin.name not in types:
          types.append(pin.name)
    return types

  def expand(self, scale_f):
    """
      This method expands the lattice moving the centers of the cells 
      by a scaling factor - only for plotting purposes
    """
    lattice_cells = super().cells
    new_pitch = self.__pitch * scale_f
    

    # Expand the lattice moving the centers, starting from the left top corner
    first_cell_center = self.centers[0][0]
    center_x, center_y = first_cell_center
    center_x *= scale_f
    center_y *= scale_f
    new_centers = []
    for y in range(self.__ny):
      row_centers = []
      for x in range(self.__nx):
        row_centers.append((center_x, center_y))
        center_x += new_pitch
      new_centers.append(row_centers)
      center_x = first_cell_center[0] * scale_f
      center_y -= new_pitch
      row_centers = []
    
    # now change the centers of every pin_cell of the lattice
    self.centers = new_centers
    for y in range(self.__ny):
      for x in range(self.__nx):
        pin_cell = lattice_cells[self.__array[y][x]]
        internal_cells = pin_cell.content.cells
        for c_id, inter_cell in internal_cells.items():
          if isinstance(inter_cell.region, SurfaceSide):
            inter_cell.region.surface.center = new_centers[y][x]
          elif isinstance(inter_cell.region, Region):
            inter_cell.region.child1.surface.center = new_centers[y][x]
            inter_cell.region.child2.surface.center = new_centers[y][x]

  def serpent_syntax_pin_by_cell(self):
      # pin_cells_syntax = []
      pin_cells_syntax = ""
      cells = {}
      pin_cells = super().cells
      array = self.__array
      
      # pin cells by separate --> probably for gcu or flux generation
      for id_, pin_cell in pin_cells.items():
          # The id_ variable is the id of the cell that was created
          # for the pin in the lattice in the specific position
          pin_uni = pin_cell.content
          cells.update(pin_uni.cells)
          pin_uni.name = pin_uni.name + f"_{id_}"
          # pin_cells_syntax += cell_.serpent_syntax()
          cells_in_pin = pin_uni.cells
          pin_cells_syntax += "\n"
          for c_id, cell in pin_uni.cells.items():
              try:
                  assert isinstance(cell.content, Material)
                  region_syntax = cell.region.serpent_syntax()
                  pin_cells_syntax += f"cell {c_id} {pin_uni.name} {cell.content.name} {region_syntax}\n"
              except AssertionError:
                  raise SystemError

      x_lb, y_lb = self.__left_bottom

      lattice_syntax = f"\n\n\nlat {super().name} 1 {x_lb} {y_lb} {self.__nx} {self.__ny} {self.__pitch}\n"
      for row in array:
          for id_ in row:
              lattice_syntax += f"{pin_cells[id_].content.name} "
          lattice_syntax += "\n"
      
      

      return pin_cells_syntax + lattice_syntax, cells

  def translate(self, trans_vector):
    cells = super().cells

    dx, dy = trans_vector
    lb_x, lb_y = self.__left_bottom
    self.__left_bottom = (lb_x+dx, lb_y+dy)
    new_centers = self.recalculate_pin_centers(scale_f=1.0)
    self.pin_centers = new_centers

    surfs_translated = []

    for c_id, pin_cell in cells.items():
      # pin_cell.region.translate
      pin_cell.translate(trans_vector, surfs_translated)
    

  @property
  def array(self):
    return self.__array

  @array.setter
  def array(self, array):
    self.__array = array
  
  @property
  def nx(self):
    return self.__nx

  @property
  def ny(self):
    return self.__ny

  @property
  def left_bottom(self):
    return self.__left_bottom

  @property
  def pitch(self):
    return self.__pitch
  
  @property
  def cells(self):
    return super().cells



class HexagonalLattice(Universe):

  def __init__(self, 
    name, center, pitch, num_rings=0, rings=[], element=None,
    plot_closing_hex=None
  ):
    """
      Init method of the class

      Parameters
      ----------------------------------------------------------------
      name        :   A string with the name of lattice universe

      left_bottom :   Point of lattice origin (origin is left bottom corner)

      pitch       :   Pitch of the assembly
      
      array       :   lattice array
      ----------------------------------------------------------------
    """
    super().__init__(name)
    self.__center = (np.float64(center[0]), np.float64(center[1]))
    self.__pitch = np.float64(pitch)
    if len(rings) == 0:
      self.__num_rings = num_rings
    else:
      self.__num_rings = len(rings)

    self.rings = rings
    self.__element = element
    self.closing_hexagon = None
    self.plot_closing_hex = plot_closing_hex

    self.array = []

    self.pitch_square = self.__pitch * np.sqrt(3) / 2
    self.element_centers = []
    self.element_cells = []

    self.element_numbering_position = {}

    self.__create_cells()

  

  def __create_cells(self):
    """Class method to create the pin cells from a given number of rings
    and a specified pin or the rings themselves. Prioritizing the rings that 
    where given.
    """
    from .cells import Cell
    
    
    if len(self.rings) == 0: 
      # Assembly with only one pin type
      self.create_rings()
    
    
    self.element_centers = self.calculate_element_centers()
    
    
    new_rings = []
    for r in range(self.__num_rings):
      new_ring = []
      ring = self.rings[r]
      num_elements_in_ring = len(ring)
      for p in range(num_elements_in_ring):
        element = ring[p]
        copy_element = element.copy()
        new_center = self.element_centers[r][p]
        copy_element.translate_to(new_center)
        closing_hex = InfiniteHexagonalCylinderXtype(
          new_center[0], new_center[1], half_width=self.__pitch/2
        )
        if isinstance(copy_element, Pin):
          copy_element.close_last_level(closing_hex)
        elif isinstance(copy_element, HexagonalLatticeTypeX):
          # not close hexagonal lattice until the creation of the mesh
          closing_hex = InfiniteHexagonalCylinderYtype(
            new_center[0], new_center[1], half_width=self.__pitch/2
          )
          copy_element.closing_hexagon = closing_hex
          pass
        elif isinstance(copy_element, HexagonalLatticeTypeY):
          # not close hexagonal lattice until the creation of the mesh
          closing_hex = InfiniteHexagonalCylinderXtype(
            new_center[0], new_center[1], half_width=self.__pitch/2
          )
          copy_element.closing_hexagon = closing_hex
          pass
        super().add_cells(copy_element.cells)

        
        new_ring.append(copy_element)
      new_rings.append(new_ring)
    
    


    self.rings = new_rings

  def create_rings(self):
    """ Class method to obtain the rings of the hexagonal assembly

    Returns
    -------
    rings : list of lists

    """

    assert self.__element is not None
    
    rings = [[self.__element]]
    num_elements_next_ring = 6

    for i in range(self.__num_rings-1): # Ring sweep
      ring = [self.__element]*num_elements_next_ring

      rings.append(ring)
      num_elements_next_ring += 6
    self.rings = rings
    return rings
  
  def __get_different_elements(self):
    types = []
    for row in self.__array:
      for element in row:
        if element.name not in types:
          types.append(element.name)
    return types

  def copy(self):
    """
    It makes a copy of the lattice
    
    """
    name = self.name
    center = self.__center
    pitch = self.__pitch
    rings = self.rings
    

    copy_lattice = HexagonalLatticeTypeX(
      name, center, pitch, rings=rings
    )

    return copy_lattice

  def translate_to(self, point):
    new_x, new_y = point
    cx, cy = self.__center
    trans_vector = (
      new_x - cx,
      new_y - cy
    )
    self.translate(trans_vector)

  def translate(self, trans_vector):

    # Recalculate element centers -----------------------------
    dx, dy = trans_vector
    cx, cy = self.__center

    self.__center  = (cx + dx, cy + dy)

    if self.plot_closing_hex is not None:
      self.plot_closing_hex.translate(trans_vector)
    
    new_centers = self.recalculate_element_centers(
      scale_f=1.0, center=(cx, cy)
    )
    

    self.element_centers = new_centers

    # Translate the content of the lattice --------------------

    for ring in self.rings:
      for element in ring:
        # print(element)
        if isinstance(element, HexagonalLatticeTypeX):
          element.translate(trans_vector)
        elif isinstance(element, Pin):
          element.translate(trans_vector)

  def expand(self, scale_f):
    """
    This method expands the lattice moving the centers of the cells 
    by a scaling factor - only for plotting purposes
    """

    # Change first the radius of the pin_levels
    # for ring in self.rings:
    #   for pin in ring:
    #     levels



    self.plot_closing_hex.expand(scale_f)

    lattice_cells = super().cells

    new_pitch = self.__pitch * scale_f

    new_half_width = new_pitch / 2
    new_radius = 2 * new_half_width / math.sqrt(3)

    new_displacement_y = new_radius * 1.5

    # Expand the lattice moving the centers, starting from the left top corner
    first_cell_center = self.centers[0][0]
    center_x, center_y = first_cell_center
    center_x *= scale_f
    center_y *= scale_f

    start_x = center_x
    new_centers = []
    
    for y in range(self.__ny):
      row_centers = []
      for x in range(self.__nx):
        row_centers.append((start_x + x * new_pitch, center_y))
        center_x += new_pitch
      new_centers.append(row_centers)
      start_x += new_half_width
      center_y -= new_displacement_y
      row_centers = []
    
    # now change the centers of every pin_cell of the lattice
    self.cell_centers = new_centers
    for y in range(self.__ny):
      for x in range(self.__nx):
        if self.__array[y][x] is not None:
          cell_id = self.__array[y][x][0]
          pin_cell = lattice_cells[cell_id]
          internal_cells = pin_cell.content.cells
          for c_id, inter_cell in internal_cells.items():
            if isinstance(inter_cell.region, SurfaceSide):
              inter_cell.region.surface.center = new_centers[y][x]
            elif isinstance(inter_cell.region, Region):
              inter_cell.region.child1.surface.center = new_centers[y][x]
              inter_cell.region.child2.surface.center = new_centers[y][x]

  def calculate_enclosed_cells(self, region):
      
    for r in range(self.__ny):
      for c in range(self.__nx):
        c_id = self.__array[r][c]
        self.__array[r][c] = (c_id, "inside")
        cell = super().cells[c_id]
        #check cell center coordinates if they are inside the hexagon
        hexagon = cell.region.surface
        try:
          is_inside = False
          if region.side == "-":
            is_inside = region.surface.isPointNegativeSide(hexagon.center)
          elif region.side == "+":
            is_inside = region.surface.isPointPositiveSide(hexagon.center)
          else:
            # Check implementation for a union of regions, etc, 
            # composed by different surfaces
            raise SystemError
          assert is_inside
          self.__enclosed_cells.append(cell)
        except AssertionError:
          # center of the cell is hexagon
          vertexs = hexagon.get_vertex_points()
          side_points = hexagon.get_side_middle_points()
          points = vertexs + side_points
          some_inside = [region.surface.isPointNegativeSide(p) for p in points]
          if True in some_inside:    
            self.__array[r][c] = (c_id, "edge")
          else:
            self.__array[r][c] = None
          continue
      a = 0

  def get_fuel_elements_centers(self):
    elements_centers = []
    for row in self.__array:
      row_centers = []
      for element in row:
        if element is None: continue
        p_id, where = element
        if where == "inside":
          center = super().cells[p_id].center
          row_centers.append(center)
      if len(row_centers) != 0: elements_centers.append(row_centers)
      
    return elements_centers
  
  @property
  def num_rings(self):
    return self.__num_rings
  
  @property
  def pitch(self):
    return self.__pitch

  @property
  def center(self):
    return self.__center

  @property
  def cells(self):
    return super().cells
  
  @property
  def centers(self):
    return self.element_centers
  
  @property
  def enclosed_cells(self):
    return self.__enclosed_cells

  @property
  def element(self):
    return self.__element




class HexagonalLatticeTypeX(HexagonalLattice):
  """
    Hexagonal Lattice Type X composed by an array of pins, Example:

  """

  def __init__(self, 
    name, center, pitch, num_rings=0, rings=[], element=None,
    plot_closing_hex=None
  ):
    super().__init__(
      name, center, pitch, num_rings, rings, element, plot_closing_hex
    )

  def recalculate_element_centers(self, scale_f, center):
    """Class method to recalculate the element centers with a scale factor. 
    It acts
    over the pitch, this is used mainly for plotting.

    """
    pitch = self.pitch * scale_f

    new_element_centers = self.calculate_element_centers(
      pitch=pitch,
      center=center
    )

    return new_element_centers

  def calculate_element_centers(self, pitch=None, center=None):
    """Class method to calculate the centers of all the elements in the hexagonal
    assembly. They are calculated as follows. I starts in the center and then 
    moves to the outer ring by applying a dx to the left and start calculating
    the centers of that ring by applying dx and dy deppending on the side of 
    the imaginary hexagon that the element is on.

    Returns
    -------

    element_centers : list of lists
    
    """
    if center is None:
      cx, cy = self.center
    else:
      cx, cy = center
    element_centers = [[(cx, cy)]]
    start = (cx, cy)
    if pitch is None: 
      pitch = self.pitch

    square_pitch = pitch * np.sqrt(3) / 2
    

    sides_dxdy = {
      'A': {
        'dx': pitch,
        'dy': 0
      },
      'B': {
        'dx': pitch / 2,
        'dy': -square_pitch
      },
      'C': {
        'dx': -pitch / 2,
        'dy': -square_pitch
      },
      'D': {
        'dx': -pitch,
        'dy': 0
      },
      'E': {
        'dx': -pitch / 2,
        'dy': square_pitch
      },
      'F': {
        'dx': pitch / 2,
        'dy': square_pitch
      }
    }
    hexagon_sides =  ['F','A','B','C','D','E']
    
    for r in range(1,self.num_rings): # Ring sweep
      
      ring = self.rings[r]

      start = (start[0]-pitch, start[1])

      side_legth = cx - start[0]

      distance = 0.0
      side_idx = 0
      new_center = start
      centers = [new_center]
      elements_in_ring = len(ring)
      for p in range(1,elements_in_ring):
        side = hexagon_sides[side_idx]
        dx = sides_dxdy[side]['dx']
        dy = sides_dxdy[side]['dy']
  
        ncx = new_center[0]+dx
        ncy = new_center[1]+dy

        new_center = (ncx, ncy)
        centers.append(new_center)
        distance += pitch
        if abs(distance - side_legth) <= 1e-6:
          side_idx += 1
          distance = 0.0
        
      element_centers.append(centers)

    return element_centers
  
  def generate_array_from_rings(self):
    look_up_ordering = {
      'y_coord': {}
    }
    for r in self.rings:
      for element in r:
        cx, cy = element.center
        if cy not in look_up_ordering['y_coord']:
          look_up_ordering["y_coord"][cy] = [element]
        else:
          look_up_ordering["y_coord"][cy].append(element)
    
    y_coord_sorted = sorted(list(look_up_ordering["y_coord"].keys()))[::-1]

    
    array = []
    for y_coord in y_coord_sorted:

      element_array = look_up_ordering["y_coord"][y_coord]
      #sort element array in base of cx
      look_up_sortering = {element.center[0]: element for element in element_array}
      x_coord_sorted = sorted(list(look_up_sortering.keys()))

      row = [look_up_sortering[x_coord] for x_coord in x_coord_sorted]
      
      array.append(row)
    
    self.array = array
  
  

class HexagonalLatticeTypeY(HexagonalLattice):
  """
    Hexagonal Lattice Type Y composed by an array of pins, Example:

  """


  def __init__(self, 
    name, center, pitch, num_rings=0, rings=[], element=None,
    plot_closing_hex=None
  ):
    super().__init__(
      name, center, pitch, num_rings, rings, element, plot_closing_hex
    )

    centers_indexes_in_rings = {} # key: center, value: (num_ring, idx)
    

  def recalculate_element_centers(self, scale_f, center):
    """Class method to recalculate the element centers with a scale factor. 
    It acts
    over the pitch, this is used mainly for plotting.

    """
    pitch = self.pitch * scale_f

    new_element_centers = self.calculate_element_centers(
      pitch=pitch,
      center=center
    )

    return new_element_centers

  def calculate_element_centers(self, pitch=None, center=None):
    """Class method to calculate the centers of all the elements in the 
    hexagonal
    assembly. They are calculated as follows. I starts in the center and then 
    moves to the outer ring by applying a dx to the left and start calculating
    the centers of that ring by applying dx and dy deppending on the side of 
    the imaginary hexagon that the element is on.

    Returns
    -------

    element_centers : list of lists
    
    """
    if center is None:
      cx, cy = self.center
    else:
      cx, cy = center

    
    element_centers = [[(cx, cy)]]
    self.element_numbering_position[0] = (0,0)
    start = (cx, cy)
    # centers_idxs_rings = {
    #   f'{cx},{cy}': (0.0,0.0)
    # }
    if pitch is None: 
      pitch = self.pitch
    x_pitch = pitch * np.sqrt(3) / 2
    sides_dxdy_to_travel = {
      'F': {
        'dx': x_pitch,
        'dy': pitch/2
      },
      'A': {
        'dx': x_pitch,
        'dy': -pitch/2
      },
      'B': {
        'dx': 0.0,
        'dy': -pitch
      },
      'C': {
        'dx': -x_pitch,
        'dy': -pitch/2
      },
      'D': {
        'dx': -x_pitch,
        'dy': pitch/2
      },
      'E': {
        'dx': 0.0,
        'dy': pitch
      },
    }
    hexagon_sides =  ['F','A','B','C','D','E']
    el_number = 1
    for r in range(1,self.num_rings): # Sweep from second ring
      
      ring = self.rings[r]
      concentric_hexagon = InfiniteHexagonalCylinderXtype(
        cx, cy, r*x_pitch
      )
      cchex_vertexes = concentric_hexagon.vertex_points

      
      cchex_side = concentric_hexagon.radius
      centers = [
        cchex_vertexes[5]
      ]
      elements_in_ring = len(ring)
      new_center = centers[0]
      traveled_distance = 0.0
      side_idx = 0
      for p in range(0,elements_in_ring):
        side = hexagon_sides[side_idx]
        dx = sides_dxdy_to_travel[side]['dx']
        dy = sides_dxdy_to_travel[side]['dy']
        # ----------------------------------------------------
        ncx = new_center[0]+dx
        ncy = new_center[1]+dy
        new_center = (ncx, ncy)
        # ----------------------------------------------------
        self.element_numbering_position[el_number] = (r,p)
        el_number += 1
        
        # centers_idxs_rings[f'{ncx},{ncy}'] = (r,p)
        centers.append(new_center)
        traveled_distance += pitch
        if abs(traveled_distance - cchex_side) <= 1e-8:
          side_idx += 1
          traveled_distance = 0.0
        
      element_centers.append(centers)
      
    # self.centers_indexes_in_rings = centers_idxs_rings
    return element_centers
  
  def calculate_lattice_map(self):
    def get_ring_index(index):
      if index == 0:
        return 0
      n = 1
      while index > 3 * n * (n + 1):
        n += 1
      return n

    def get_ring_start(num_ring):
      if num_ring == 0:
        return 0
      elif num_ring == 1:
        return 1
      else: 
        return 3 * (num_ring - 1) * num_ring + 1
      
    def get_corner_idxs(num_ring):

      if num_ring == 0: return [0]
      elif num_ring == 1: return [0,1,2,3,4,5]
      else: 
        increment = num_ring
        indexes = list(range(0,num_ring*6,increment))

        return indexes

    def get_num_elements_ring(num_ring):
      if num_ring == 0:
        return 1
      else:
        return num_ring * 6

    def get_neighbors(index):
      if index == 0:
        # All elements in the first ring
        return list(range(1, 7))
    
      # Ring of the element at index ------------------
      n = get_ring_index(index)
      # Position within the current ring --------------
      start = get_ring_start(n)
      end = get_ring_start(n + 1) - 1
      pos = index - start
      # Neighbors within the same ring ----------------
      neighbors = [
        start + (pos - 1) % (6 * n),  # Previous element in the ring
        start + (pos + 1) % (6 * n),  # Next element in the ring
      ]
      
      # Is it in a corner?
      currentR_corner_idxs = get_corner_idxs(n)
      prevR_corner_idxs = get_corner_idxs(n-1)
      nextR_corner_idxs = get_corner_idxs(n+1)

      is_corner = pos in currentR_corner_idxs

      prev_ring_start = get_ring_start(n-1)
      next_ring_start = get_ring_start(n+1)

      if is_corner:
        # get number of corner
        num_corner = currentR_corner_idxs.index(pos)
        # get position of that corner in prev
        if n-1 == 0:
          pos_corner_prev = 0
        else:
          pos_corner_prev = get_corner_idxs(n-1)[num_corner] # this is index

        # get position of that corner in next
        pos_corner_next = get_corner_idxs(n+1)[num_corner] # this is index

        # append previous ring --------
        neighbors.append(prev_ring_start+pos_corner_prev)
        # append next ring --------
        neighbors.append(next_ring_start+pos_corner_next)

        # append adjacent position to corner in next ring
        neighbors.append(next_ring_start+pos_corner_next+1)
        if pos_corner_next == 0:
          num_elements_ring = get_num_elements_ring(n+1)
          neighbors.append(next_ring_start+num_elements_ring-1)
        else:
          neighbors.append(next_ring_start+pos_corner_next-1)

      else:
        # Calculate last corner:
        last_corner_idx = None
        for i, corner_idx in enumerate(currentR_corner_idxs):
          if pos < corner_idx:
            last_corner_idx = i - 1
            break
        if last_corner_idx is None:
          last_corner_idx = len(currentR_corner_idxs)-1
        # Calculate Distance to previous corner:

        dist_to_corner = pos - currentR_corner_idxs[last_corner_idx]

        corner_idx_prev = prevR_corner_idxs[last_corner_idx]
        corner_idx_next = nextR_corner_idxs[last_corner_idx]

        corner_pos_prev = prev_ring_start + corner_idx_prev
        corner_pos_next = next_ring_start + corner_idx_next

        neighbors.append(corner_pos_prev + dist_to_corner - 1)
        if corner_idx_prev + (dist_to_corner - 1) + 1 >= get_num_elements_ring(n-1):
          neighbors.append(prev_ring_start)
        else:
          neighbors.append(corner_pos_prev + dist_to_corner)

        neighbors.append(corner_pos_next + dist_to_corner)
        neighbors.append(corner_pos_next + dist_to_corner+1)
        
      return neighbors
  

    map_lattice = [ ]

    elem_num = 0
    for r in range(self.num_rings):
      num_of_elements = len(self.rings[r])
      ring = []
      for e in range(num_of_elements):
        element = []
        neighbors = get_neighbors(elem_num)
        for ne in neighbors:
          try:
            element.append(self.element_numbering_position[ne])
          except KeyError:
            # out of boundary furtheremore, key does not exist
            pass
        ring.append(element)
        elem_num += 1
      map_lattice.append(ring)

    return map_lattice

  def calculate_lattice_map_DEPRECATED(self):
    map_lattice = [ # rings
      [[(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),]], # list of six of the ring 1 (only one element on the ring)
    ]

    cx, cy = self.center
    pitch = self.pitch
    pitch_square = round(pitch * math.sqrt(3) / 2, 8)
    half_pitch = round(pitch/2,8)
    
    for r in range(1,self.num_rings): # Sweep from second ring
      
      map_ring = []
      ring = self.rings[r]
      concentric_hexagon = InfiniteHexagonalCylinderXtype(
        cx, cy, r*pitch_square
      )
      cchex_vertexes = concentric_hexagon.vertex_points

      
      cchex_side = concentric_hexagon.radius
      centers = [
        cchex_vertexes[0]
      ]

      elements_in_ring = len(ring)
      elements_in_ring_prev = len(self.rings[r-1])
      elements_in_ring_next = 0
      if r < self.num_rings-1:
        elements_in_ring_next = len(self.rings[r+1])


      new_center = centers[0]
      traveled_distance = 0.0
      side_idx = 0
      for p in range(elements_in_ring):
        list_of_idxs = []
        center = self.element_centers[r][p]

        cx, cy = center
        # new_x = cx-pitch_square    
        # if f'{new_x}' == '-0.0':
        #   new_x = 0.0
        el1_center = (
          round(cx-pitch_square, 8),
          round(cy+half_pitch, 8),
        )
        el2_center = (
          round(cx, 8),
          round(cy+pitch, 8),
        )
        el3_center = (
          round(cx+pitch_square, 8),
          round(cy+half_pitch, 8),
        )
        el4_center = (
          round(cx+pitch_square, 8),
          round(cy-half_pitch, 8),
        )
        el5_center = (
          round(cx, 8),
          round(cy-pitch, 8),
        )
        el6_center = (
          round(cx-pitch_square, 8),
          round(cy-half_pitch, 8),
        )
        surrounding_elements = [
          el1_center, el2_center, el3_center, el4_center, el5_center, el6_center
        ]
        # ----------------------------------------------------
        
        # print('surrounding: ', surrounding_elements)
        for e in range(elements_in_ring):
          center_to_compare = self.element_centers[r][e]
          if center_to_compare in surrounding_elements:
            list_of_idxs.append((r,e))
        for e in range(elements_in_ring_prev):
          center_to_compare = self.element_centers[r-1][e]
          if center_to_compare in surrounding_elements:
            list_of_idxs.append((r-1,e))
        for e in range(elements_in_ring_next):
          center_to_compare = self.element_centers[r+1][e]
          if center_to_compare in surrounding_elements:
            list_of_idxs.append((r+1,e))

        map_ring.append(list_of_idxs)
      map_lattice.append(map_ring)


    return map_lattice


  def generate_array_from_rings(self):
    look_up_ordering = {
      'y_coord': {}
    }
    for r in self.rings:
      for element in r:
        cx, cy = element.center
        if cy not in look_up_ordering['y_coord']:
          look_up_ordering["y_coord"][cy] = [element]
        else:
          look_up_ordering["y_coord"][cy].append(element)
    
    y_coord_sorted = sorted(list(look_up_ordering["y_coord"].keys()))[::-1]

    
    array = []
    for y_coord in y_coord_sorted:

      element_array = look_up_ordering["y_coord"][y_coord]
      #sort element array in base of cx
      look_up_sortering = {element.center[0]: element for element in element_array}
      x_coord_sorted = sorted(list(look_up_sortering.keys()))

      row = [look_up_sortering[x_coord] for x_coord in x_coord_sorted]
      
      array.append(row)
    
    self.array = array




if __name__=='__main__':
  hex_lat = HexagonalLatticeTypeX('test', (0,0), 30.0, num_rings=18)
  hex_lat.create_rings()
  centers = hex_lat.calculate_pin_centers()
  print(centers)