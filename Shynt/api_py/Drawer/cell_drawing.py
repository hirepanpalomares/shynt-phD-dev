

from Shynt.api_py import materials
from Shynt.api_py.Geometry.universes import (
  HexagonalLatticeTypeX, 
  SquareLattice, 
  Universe, 
  Pin
)

from Shynt.api_py.Geometry.regions import (
  SurfaceSide, 
  Region
)

from Shynt.api_py.Geometry.utilities_geometry import find_cylinder_cells_in_universe

from Shynt.api_py.materials import Material

from PIL import Image, ImageDraw, ImageOps

from Shynt.api_py.Drawer.region_dr import draw_region
from Shynt.api_py.Geometry.surfaces import (
  InfiniteHexagonalCylinderXtype,
  InfiniteHexagonalCylinderYtype,
  InfiniteSquareCylinderZ
)

from Shynt.api_py.Drawer.surface_drawing import (
  draw_square, 
  draw_surface, 
  draw_square_from_points, 
  draw_line,
  write_text
)




class PlotAssembly:

  def __init__(self, 
    cell, dimensions=(1000,1000), name="", rectangle_mesh={},
    y_div=[], x_div=[], rectangle_linewidth=5
  ) -> None:
    self.__mainCell = cell
    self.__imageDimensions = dimensions
    self.__imageName = name
    self.__rectangles = rectangle_mesh
    self.__rectangle_linewidth = rectangle_linewidth
    self.__scaleF = self.__calculate_scaling_factor()
    self.__transVector = self.__calculate_dxdy(cell)
    self.__mainCell.content.expand(self.__scaleF)
    self.__surfacesToDraw = self.__get_surfaces_colors_from_lattice(self.__mainCell.content)

    print("Pillow version:", Image.__version__)
    self.__img = Image.new('RGB', self.__imageDimensions, color=(254,254,254))
    self.plot_assembly()
    # self.plot_rectangles()
    
  def plot_assembly(self):
    x_max, y_max = self.__imageDimensions

    # plot surfaces ---------------------------------------------
    num_surfaces_to_plot = len(self.__surfacesToDraw)
    print(f"plotting {num_surfaces_to_plot} surfaces")
    for s in range(num_surfaces_to_plot):
      surf, material = self.__surfacesToDraw[s]
      surf.scale(self.__scaleF)
      surf.translate(self.__transVector)
      color = material.color
      self.__img = draw_surface(surf, self.__img,y_max, fill=color)

  def plot_rectangles(self, rectangles, lw=2):
    x_max, y_max = self.__imageDimensions
    dx, dy = self.__transVector
    num_rectangles = len(rectangles)
    print(f"plotting {num_rectangles} rectangles")
    for r, mesh in enumerate(rectangles):
      x1,x2 = mesh[0]
      y1,y2 = mesh[1]

      x1 = x1*self.__scaleF+dx
      x2 = x2*self.__scaleF+dx
      y1 = y1*self.__scaleF+dy
      y2 = y2*self.__scaleF+dy

      self.__img = draw_square_from_points(
        x1, x2, y_max-y1, y_max-y2, self.__img, width=lw
      )

      xc = (x2+x1)/2
      yc = (y2+y1)/2
      self.__img =  write_text((xc,y_max-yc), f"{r+1}", self.__img)

  def plot_y_div(self, y_div, lw):
    x_max, y_max = self.__imageDimensions
    dx, dy = self.__transVector

    for y_coor in y_div:
      first_point = (0, y_coor*self.__scaleF + dy)
      second_point = (x_max, y_coor*self.__scaleF + dy)

      self.__img = draw_line(
        [first_point, second_point],
        self.__img,
        width=lw
      )
    
  def plot_x_div(self, x_div, lw):
    x_max, y_max = self.__imageDimensions
    dx, dy = self.__transVector

    for x_coor_row in x_div:
      for x_coor in x_coor_row:
        first_point = (x_coor*self.__scaleF + dx, 0.0)
        second_point = (x_coor*self.__scaleF + dy, y_max)

        self.__img = draw_line(
          [first_point, second_point],
          self.__img,
          width=lw
        )
  
  def save(self):
    print("rotating...")
    # self.__img = self.__img.rotate(180)
    # self.__img = ImageOps.flip(self.__img, )
    print("saving...")
    self.__img.save(f"{self.__imageName}.png")
  
  def show(self):
    self.__img.show()
    
  
  def __calculate_scaling_factor(self):
    # surface enclosing the cell -----
    enclosing_surf = self.__mainCell.region.surface
    figsize_x = self.__imageDimensions[0]
    if isinstance(enclosing_surf, InfiniteSquareCylinderZ):
        # Calculating scaling factor with x, assuming it is a square
        width_square = enclosing_surf.half_width * 2
        scale_f = figsize_x * 0.9 / width_square # leaving 5% of margin each side for the drawing area
        return scale_f
    elif isinstance(enclosing_surf, InfiniteHexagonalCylinderXtype):
        width_hexagon = enclosing_surf.radius * 2
        scale_f = figsize_x * 0.9 / width_hexagon # leaving 5% of margin each side for the drawing area
        return scale_f
    elif isinstance(enclosing_surf, InfiniteHexagonalCylinderYtype):
        width_hexagon = enclosing_surf.radius * 2
        scale_f = figsize_x * 0.9 / width_hexagon # leaving 5% of margin each side for the drawing area
        return scale_f
    else:
        print("Geometry not suported for plotting")
        raise SystemExit
    
  def __calculate_dxdy(self, cell):
    enclosing_surf = cell.region.surface
    center_x = enclosing_surf.center_x
    center_y = enclosing_surf.center_y
    
    xt, yt = self.__imageDimensions
    new_center = (xt/2, yt/2)
    fig_center_x = self.__imageDimensions[0]/2

    dy = new_center[0] - center_y   # assuming it is a square
    dx = new_center[0] - center_x

    return dx, dy
  
  def __get_surfaces_colors_from_lattice(self, lattice):
    coolant = Material("default_coolant", color=(100, 141, 176)) # default coolant
    surfaces_to_draw = [
      (self.__mainCell.region.surface, coolant)
    ]
    pin_cells = lattice.enclosed_cells
    for pin_cell in pin_cells:
      cells = pin_cell.content.cells
      
      pin_levels = find_cylinder_cells_in_universe(pin_cell.content)
    
      
      for level in pin_levels:
        if isinstance(level.region, SurfaceSide):
          surfaces_to_draw.append((level.region.surface, level.content))
        elif isinstance(level.region, Region):
          surf_1 = level.region.child1.surface
          surf_2 = level.region.child2.surface
          if surf_1.radius > surf_2.radius:
            surfaces_to_draw.append((surf_1, level.content))
          else:
            surfaces_to_draw.append((surf_2, level.content))

    

    return surfaces_to_draw
  
  def to_ipython_img(self):
    from IPython.display import Image

    return Image(f"{self.__imageName}.png"
                 )

  @property
  def img(self):
    return self.__img
