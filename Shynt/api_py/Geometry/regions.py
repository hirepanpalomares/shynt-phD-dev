from Shynt.api_py.Geometry.surfaces import PieQuadrant



class Region:
  """ 
    Class used to represent the euclidean space generated
    by a Halspace or the intersection of two or more.

    The Region is respresented as a binary tree having as childs
    two different SurfaceSide classes and boolean operation as 
    atribute

    ...

    Attributes
    ----------
    child1 : SurfaceSide | Region
      Child SurfaceSide or Region of the binary tree
    child2 : SurfaceSide | Region
      Child SurfaceSide or Region of the binary tree
    __operation : str
      Atribute of the root of the binary tree, it is the boolean 
      operation involving the 2 childs
    
    Methods
    -------
    invert()

    clone(new_center_x, new_center_y, clone_vector)

    destructure_region(surfaces_sides)

    translate(trans_vector)

    scale(scale_f)

    surfaces_of_region(surfaces)

    serpent_syntax()

    get_point_in_region()

    --------

    #TODO:     Implement the case when the two childs are already region instances
    #TODO:     Implement A or B ----> Boolean union  __or__
    #TODO:     Implement A xor B ----> Boolean opposite to or __xor__ (Might not be used in reactor physics)
    #TODO:     Implement A - B ----> Boolean negation

  """


  def __init__(self, child1=None, child2=None, operation=""):
    """
      Checar los child?? yes/no
    """
    self.child1 = child1
    self.child2 = child2
    self.__operation = operation
    
  
  def invert(self):
    """
        Method to invert the region
    """
    surface_sides = self.destructure_region()
    new_surface_sides = []
    for ss in surface_sides:
      side = ss.side
      new_side = "-"
      if side == "-":
        new_side = "+"
      new_surface_sides.append(SurfaceSide(ss.surface, new_side))
    
    inverted = new_surface_sides[0]
    for ss in range(1, len(new_surface_sides)):
      inverted &= new_surface_sides[ss]
    
    return inverted
      
  def clone(self, new_center_x, new_center_y, clone_vector=None):
    # try: 
    #     assert isinstance(self.child1, SurfaceSide)
    #     assert isinstance(self.child2, SurfaceSide)
    #     child1_clone = self.child1.clone(new_center_x, new_center_y)
    #     child2_clone = self.child2.clone(new_center_x, new_center_y)
    #     return child1_clone & child2_clone
    # except AssertionError:
    #     # Cloning of two regions not supported, only two surfaceSides
    #     raise SystemError
    child1_clone = self.child1.clone(new_center_x, new_center_y, clone_vector=clone_vector)
    child2_clone = self.child2.clone(new_center_x, new_center_y, clone_vector=clone_vector)
    return child1_clone & child2_clone

  def destructure_region(self, surfaces_sides=None):
      """
          Recursive function to destructurate a region in its surfaces sides

          returns:
              Array(<SurfaceSide class>)
      """
      if surfaces_sides is None:
          surfaces_sides = {}
      if isinstance(self, SurfaceSide):
          # Base case
          if isinstance(self.surface, PieQuadrant):
              surfaces_sides.update(self.surface.get_surface_sides())
          else:
              surfaces_sides.update({
                  self.surface.id: self
              })

          return surfaces_sides
      elif isinstance(self, Region):
          surfaces_sides.update(self.child1.destructure_region())
          surfaces_sides.update(self.child2.destructure_region())
          return surfaces_sides

  def translate(self, trans_vector, surfs_translated):
    if self.child1 is not None:  
      surfs_translated = self.child1.translate(trans_vector, surfs_translated)
    if self.child2 is not None:  
      surfs_translated = self.child2.translate(trans_vector, surfs_translated)
    return surfs_translated
  
  def scale(self, scale_f):
      self.child1.scale(scale_f)
      self.child2.scale(scale_f)

  def surfaces_of_region(self, surfaces=None):
      if surfaces is None:
          surfaces = {}
      if isinstance(self, SurfaceSide):
          # base case
          surf = self.surface
          surfaces.update({
              surf.id: surf
          })
          return surfaces
      elif isinstance(self, Region):
          reg1 = self.child1
          reg2 = self.child2
          new_surf_reg1 = reg1.surfaces_of_region(surfaces=surfaces) 
          surfaces.update(new_surf_reg1)
          new_surf_reg2 = reg2.surfaces_of_region(surfaces=surfaces)
          surfaces.update(new_surf_reg2)
          return surfaces

  def serpent_syntax(self):
      """
          It returns the region using serpent syntax for boolean geometry:

          If the region is comprised between the outside of a cylinder->id=2 and 
          the inside of a square->id=3 it will return the following:

          return: "2 -3"
      """
      syntax = ""
      side = lambda s: s if s == "-" else ""
      # # For the regions:
      # if isinstance(self, SurfaceSide):
      #     syntax += f" {side(self.side)}{self.surface.id}"
      # elif isinstance(self, Region):
      #     # find the surfaces sides of the Region
      #     surfaces_sides = self.destructure_region()
      #     for s_id, surf_side in surfaces_sides.items():
      #         syntax += f" {side(surf_side.side)}{surf_side.surface.id}"
      # syntax += ""
      surface_sides = self.destructure_region()
      for s_id, ss in surface_sides.items():
          syntax += f" {side(ss.side)}{s_id} "
      return syntax

  def get_point_in_region(self):
      percentage = 0.01
      point = self.child1.get_point_in_region(percentage)
      return point

  def __and__(self, other):
    """Class method to add to create the intersection of two Regions

    Parameters
    ----------
    self    :   Region type
    other   :   Region type
    ----------
    
    """
    return Region(child1=self, child2=other, operation="and")

  def __neg__(self):
    pass
  
  def __pos__(self):
    pass

  @property
  def operation(self):
      return self.__operation
  
  @property
  def center(self):
      center1 = self.child1.surface.center
      center2 = self.child2.surface.center
      if center1 == center2:
          return center1
      else:
          return (0,0)



class SurfaceSide(Region):

  def __init__(self, surface, side):
      self.surface = surface
      self.side = side

  def clone(self, new_center_x, new_center_y, clone_vector=None):
      surface_clone = self.surface.clone(
          new_center_x, new_center_y, clone_vector=clone_vector
      )
      if self.side == "-":
          return -surface_clone
      elif self.side == "+":
          return +surface_clone
      else:
          raise SystemError

  def __and__(self, other):
      """
      Class overloading operator __and__

      This overwrites the parent class method so it performs the
      boolean addition between two SurfaceSide classes.

      It returns an instance of the Region Class by merging the euclidean
      space between the two instances 'self' and 'other'

      Parameters
      ---------------------------------------------------------------
      self        :   It is an instance of the class SurfaceSide
      other       :   It is an instance of the class SurfaceSide
      ---------------------------------------------------------------
      
      
      
      """
      
      return Region(self, other, operation="and")
  
  def encloses(self, other):
      others_vertex = other.surface.vertex_points
      for point in others_vertex:
          if not self.surface.isPointNegativeSide(point):
              return False
      return True
  
  def isPointInsideRegion(self, point):
      if self.side == "-":
          return self.surface.isPointNegativeSide(point)
      elif self.side == "+":
          return self.surface.isPointPositiveSide(point)

  def translate(self, trans_vector, surfs_translated):
    if self.surface.id not in surfs_translated:
      self.surface.translate(trans_vector)
      surfs_translated.append(self.surface.id)
    return surfs_translated
  
  def scale(self, scale_f):
    self.surface.scale(scale_f)

  def get_point_in_region(self, percentage=0.1):
    from Shynt.api_py.Geometry.surfaces import (
      InfiniteCylinderZ, InfiniteSquareCylinderZ
    )
    from Shynt.api_py.Geometry.surfaces import (
      InfiniteHexagonalCylinderXtype, InfiniteHexagonalCylinderYtype
    )
    point = None
    if self.side == "-":
        if isinstance(self.surface, InfiniteCylinderZ):
            dx = self.surface.radius * (1-percentage)
            point = (self.surface.center_x + dx, self.surface.center_y)
            # point = self.surface.center
        elif isinstance(self.surface, InfiniteSquareCylinderZ):
            dx = self.surface.half_width * (1-percentage)
            point = (self.surface.center_x + dx, self.surface.center_y)
            # point = self.surface.center
        elif isinstance(self.surface, InfiniteHexagonalCylinderXtype):
            dx = self.surface.half_width * (1-percentage)
            point = (self.surface.center_x + dx, self.surface.center_y)
        elif isinstance(self.surface, InfiniteHexagonalCylinderYtype):
            dy = self.surface.half_width * (1-percentage)
            point = (self.surface.center_x, self.surface.center_y + dy)
    elif self.side == "+":
        if isinstance(self.surface, InfiniteCylinderZ):
            dx = self.surface.radius * (1+percentage)
            point = (self.surface.center_x + dx, self.surface.center_y)
            # point = self.surface.center
        elif isinstance(self.surface, InfiniteSquareCylinderZ):
            dx = self.surface.half_width * (1+percentage)
            point = (self.surface.center_x + dx, self.surface.center_y)
            # point = self.surface.center
        elif isinstance(self.surface, InfiniteHexagonalCylinderXtype):
            dx = self.surface.half_width * (1+percentage)
            point = (self.surface.center_x + dx, self.surface.center_y)
        elif isinstance(self.surface, InfiniteHexagonalCylinderYtype):
            dy = self.surface.half_width * (1+percentage)
            point = (self.surface.center_x, self.surface.center_y + dy)
    return point
  
  @property
  def center(self):
    return self.surface.center


