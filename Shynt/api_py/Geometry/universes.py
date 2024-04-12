
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
    self.detector_files = None
    self.xs_files = None
    
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
      pin_copy = Pin(self.name, surroundings=cell.content)
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


class HexagonalLatticeTypeX(Universe):
  """
    Hexagonal Lattice Type X composed by an array of pins, Example:

  """

  def __init__(self, name, center, pitch, num_rings=0, rings=[], pin=None):
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
    self.__center_x, self.__center_y = center
    self.__pitch = pitch
    self.__num_rings = num_rings
    self.rings = rings
    self.__pin = pin
    self.array = []

    self.pitch_square = pitch * math.sqrt(3) / 2
    self.pin_centers = []
    self.pin_cells = []
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
      self.pin_centers = self.calculate_pin_centers()
    else:
      pass
    
    new_rings = []
    for r in range(self.__num_rings):
      new_ring = []
      ring = self.rings[r]
      num_pins_in_ring = len(ring)
      for p in range(num_pins_in_ring):
        copy_pin = self.__pin.copy()
        new_center = self.pin_centers[r][p]
        copy_pin.translate_to(new_center)
        closing_hex = InfiniteHexagonalCylinderXtype(
          new_center[0], new_center[1], half_width=self.__pitch/2
        )
        copy_pin.close_last_level(closing_hex)
        self.__pin = copy_pin
        cells = copy_pin.cells
        # p = [print(c, cell.content, cell.volume) for c, cell in cells.items()]
        super().add_cells(cells)
        new_ring.append(copy_pin)
      new_rings.append(new_ring)
    self.rings = new_rings
    
  def create_rings(self):
    """ Class method to obtain the rings of the hexagonal assembly

    Returns
    -------
    rings : list of lists

    """

    rings = [[self.__pin]]
    num_pins_next_ring = 6

    for i in range(self.__num_rings-1): # Ring sweep
      ring = [self.__pin]*num_pins_next_ring

      rings.append(ring)
      num_pins_next_ring += 6
    self.rings = rings
    return rings

  def calculate_pin_centers(self, pitch=None):
    """Class method to calculate the centers of all the pins in the hexagonal
    assembly. They are calculated as follows. I starts in the center and then 
    moves to the outer ring by applying a dx to the left and start calculating
    the centers of that ring by applying dx and dy deppending on the side of 
    the imaginary hexagon that the pin is on.

    Returns
    -------

    pin_centers : list of lists
    
    """
    pin_centers = [[(self.__center_x, self.__center_y)]]
    start = (self.__center_x, self.__center_y)
    if pitch is None: pitch = self.__pitch

    sides_dxdy = {
      'A': {
        'dx': pitch,
        'dy': 0
      },
      'B': {
        'dx': pitch / 2,
        'dy': -((pitch ** 2 - (pitch / 2)**2)**0.5)
      },
      'C': {
        'dx': -pitch / 2,
        'dy': -((pitch ** 2 - (pitch / 2)**2)**0.5)
      },
      'D': {
        'dx': -pitch,
        'dy': 0
      },
      'E': {
        'dx': -pitch / 2,
        'dy': (pitch ** 2 - (pitch / 2)**2)**0.5
      },
      'F': {
        'dx': pitch / 2,
        'dy': (pitch ** 2 - (pitch / 2)**2)**0.5
      }
    }
    hexagon_sides =  ['F','A','B','C','D','E']
    
    for r in range(1,self.__num_rings): # Ring sweep
      
      ring = self.rings[r]
      start = (start[0]-pitch, start[1])

      side_legth = round(self.__center_x - start[0], 8)

      distance = 0.0
      side_idx = 0
      new_center = start
      centers = [new_center]
      pins_in_ring = len(ring)
      for p in range(1,pins_in_ring):
        side = hexagon_sides[side_idx]
        dx = round(sides_dxdy[side]['dx'], 8)
        dy = round(sides_dxdy[side]['dy'], 8)
  
        ncx = round(new_center[0]+dx, 8)
        ncy = round(new_center[1]+dy, 8)

        new_center = (ncx, ncy)
        centers.append(new_center)
        distance += pitch
        if round(distance,8) == side_legth:
          side_idx += 1
          distance = 0.0
        
      pin_centers.append(centers)

    return pin_centers

  def recalculate_pin_centers(self, scale_f):
    """Class method to recalculate the pin centers with a scale factor. It acts
    over the pitch, this is used mainly for plotting.

    """
    pitch = self.__pitch * scale_f

    new_pin_centers = self.calculate_pin_centers(pitch=pitch)

    return new_pin_centers

  def rings_to_array(self):
    look_up_ordering = {
      'y_coord': {}
    }
    for r in self.rings:
      for pin in r:
        cx, cy = pin.center
        if cy not in look_up_ordering['y_coord']:
          look_up_ordering["y_coord"][cy] = [pin]
        else:
          look_up_ordering["y_coord"][cy].append(pin)
    
    y_coord_sorted = sorted(list(look_up_ordering["y_coord"].keys()))[::-1]

    
    array = []
    for y_coord in y_coord_sorted:

      pin_array = look_up_ordering["y_coord"][y_coord]
      #sort pin array in base of cx
      look_up_sortering = {pin.center[0]: pin for pin in pin_array}
      x_coord_sorted = sorted(list(look_up_sortering.keys()))

      row = [look_up_sortering[x_coord] for x_coord in x_coord_sorted]
      
      array.append(row)
    
    self.array = array


  def __get_different_pins(self):
    types = []
    for row in self.__array:
      for pin in row:
        if pin.name not in types:
          types.append(pin.name)
    return types
  
  def get_fuel_pins_centers(self):
    pins_centers = []
    for row in self.__array:
      row_centers = []
      for pin in row:
        if pin is None: continue
        p_id, where = pin
        if where == "inside":
          center = super().cells[p_id].center
          row_centers.append(center)
      if len(row_centers) != 0: pins_centers.append(row_centers)
    return pins_centers
    
  def translate(self, trans_vector):
    cells = super().cells
    surfs_translated = []
    # print(trans_vector)
    for c_id, cell in cells.items():
      surfs_translated = cell.translate(trans_vector, surfs_translated)

  def expand(self, scale_f):
    """
    This method expands the lattice moving the centers of the cells 
    by a scaling factor - only for plotting purposes
    """

    # Change first the radius of the pin_levels
    # for ring in self.rings:
    #   for pin in ring:
    #     levels




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

  @property
  def num_rings(self):
    return self.__num_rings
  
  @property
  def pitch(self):
    return self.__pitch

  @property
  def center(self):
    return (self.__center_x, self.__center_y)

  @property
  def cells(self):
    return super().cells
  
  @property
  def centers(self):
    return self.pin_centers
  
  @property
  def enclosed_cells(self):
    return self.__enclosed_cells

  @property
  def pin(self):
    if self.__pin is None:
      return
    return self.__pin
# def translate_universe(universe, trans_vector):
#   # return super().translate(trans_vector)
#   surfaces_universe = get_all_surfaces_in_a_universe(universe)
#   for id_, surf in surfaces_universe.items():
#     surf.translate(trans_vector)

if __name__=='__main__':
  hex_lat = HexagonalLatticeTypeX('test', (0,0), 30.0, num_rings=18)
  hex_lat.create_rings()
  centers = hex_lat.calculate_pin_centers()
  print(centers)