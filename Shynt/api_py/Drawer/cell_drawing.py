

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
  InfiniteSquareCylinderZ,
  InfiniteCylinderZ
)

from Shynt.api_py.Drawer.surface_drawing import (
  draw_square, 
  draw_surface, 
  draw_polygon, 
  draw_line,
  write_text
)




class PlotLattice:
  """Class to plot an assembly

  """
  def __init__(self, 
    cell, dimensions=(2000,2000), name="", mesh={},
  ):
    self.__mainCell = cell
    self.__imageDimensions = dimensions
    self.__imageName = name
    self.__mesh = mesh

    self.__scaleF = self.__calculate_scaling_factor()
    self.__transVector = self.__calculate_dxdy(cell)
    
    self.__surfacesToDraw = self.__get_surfaces_and_colors_from_lattice(
      self.__mainCell.content # The content is the lattice
    )

    print("Pillow version:", Image.__version__)
    self.__img = Image.new('RGB', self.__imageDimensions, color=(254,254,254))
    self.__plot_assembly()
    
  def __plot_assembly(self):
    x_max, y_max = self.__imageDimensions

    # plot surfaces ---------------------------------------------
    num_surfaces_to_plot = len(self.__surfacesToDraw)
    print(f"plotting {num_surfaces_to_plot} surfaces")
    for s in range(num_surfaces_to_plot):
      surf, material = self.__surfacesToDraw[s]
      surf.translate(self.__transVector)
      color = material.color
      self.__img = draw_surface(surf, self.__img, y_max, fill=color)
  

  def __transform_points(self, points):
    x_max, y_max = self.__imageDimensions
    dx, dy = self.__transVector

    new_points = []
    for p in points:
      x, y = p
      new_p = (
        x*self.__scaleF+dx,
        y_max - (y*self.__scaleF+dy)
      )
      new_points.append(new_p)
    
    return new_points
  
  def __get_square_points(self, node):
    x1,x2 = node[0]
    y1,y2 = node[1]
    points = [
      (x1,y1), (x2,y1), (x2,y2), (x1,y2)
    ]
    transformed_points = self.__transform_points(points)

    return transformed_points

  def plot_rectangles(self, rectangles, lw=2):

    for rectangle in rectangles:
      points = self.__get_square_points(rectangle)
      print(points)
      self.__img = draw_polygon(points, self.__img, width=lw)

      # xc, yc = self.__calc_centroid(points)
      # self.__img =  write_text((xc,yc), f"{nid}", self.__img)
    

  def plot_mesh(self, nodes_surfaces, lw=10,):
    num_coarse_nodes = len(nodes_surfaces)
    print(f"plotting {num_coarse_nodes} coarse_nodes ...")
    points = []
    for nid, surfaces in nodes_surfaces.items():
      print(nid, end=",")
      
      if nid % 20 == 0: print()
      # print(surfaces.values())
      
      node_surfs = list(surfaces.values())
      node_points = [surf[0] for surf in node_surfs]
      node_points_transformed = self.__transform_points(node_points)
      node_centroid = self.__calc_centroid(node_points_transformed)

      self.__img =  write_text(
        node_centroid, f"{nid}", self.__img, font_size=50
      )
      for s_id, surf_points in surfaces.items():
        points = self.__transform_points(surf_points)
        self.__img = draw_polygon(points, self.__img, width=lw)

        # xc, yc = self.__calc_centroid(points)
        surf_centroid = self.__calc_centroid(points)

        start_writing_s_id = self.__calc_centroid(
          (node_centroid, surf_centroid)
        )

        self.__img =  write_text(
          start_writing_s_id, f"{s_id}", self.__img, font_size=50, 
          fill=(250,0,0)
        )
    print()

  def plot_surface_numbers(self, nodes_surfaces, fill=""):
    
    print(f"Plotting surface numbers ... ")
    for n__id, node_points in self.__mesh.items():
      print(n__id, end=",")
      if n__id % 20 == 0: print()
      print(node_points)
      points = self.__transform_points(node_points)
      

      xc, yc = self.__calc_centroid(points)
      n_surfaces = nodes_surfaces[n__id]
      for s_id, surf_points in n_surfaces.items():
        surf_points = self.__transform_points(surf_points)

        surf_centroid = self.__calc_centroid(surf_points)
        

        start_writing_s_id = self.__calc_centroid(((xc, yc), surf_centroid))

  
        self.__img =  write_text(
          start_writing_s_id, f"{s_id}", self.__img, fill=fill
        )
    print()

  def save(self, name=None, im_format='png'):
    # print("rotating...")
    # self.__img = self.__img.rotate(180)
    # self.__img = ImageOps.flip(self.__img, )
    print("Saving...")
    
    if name is None:
      save_name = f"{self.__imageName}.{im_format}"
    else:
      save_name = name

    self.__img.save(save_name)
    print(f"Saved as: {save_name}")
  
  def show(self):
    self.__img.show()
  
  def __calc_distance(self, p1, p2):
    """Calculates distance between two points
    
    """

    return 0.0
  
  def __calc_centroid(self, points): 
    xc = 0.0
    yc = 0.0
    num_points = len(points)
    for p in points:
      xp, yp = p
      xc += xp
      yc += yp

    return xc/num_points, yc/num_points
  
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
  
  def __get_surfaces_and_colors_from_lattice(self, lattice):
    coolant = Material("default_coolant", color=(100, 141, 176)) # default coolant
    expanded_wrapper = self.__mainCell.region.surface.expand(self.__scaleF)
    # print("Wrapper")
    # print(expanded_wrapper.center)
    # print(expanded_wrapper.half_width)
    # print("-------")
    surfaces_to_draw = [
      (expanded_wrapper, coolant)
    ]
    # return surfaces_to_draw
    
    new_centers = lattice.recalculate_pin_centers(self.__scaleF)
    
    if isinstance(lattice, HexagonalLatticeTypeX):
      pin_surfaces = self.__get_pin_surfaces_hex_lattice(
        new_centers, lattice
      )
      surfaces_to_draw += pin_surfaces
    elif isinstance(lattice, SquareLattice):
      pin_surfaces = self.__get_pin_surfaces_square_lattice(
        new_centers, lattice
      )
      surfaces_to_draw += pin_surfaces
    return surfaces_to_draw
  
  def __get_pin_surfaces_square_lattice(self, new_centers, lattice):
    surfaces_to_draw = []
    array_pins = lattice.array
    for i, row in enumerate(array_pins):
      for j, pin in enumerate(row):
        cx, cy = new_centers[i][j]
        pin_levels = pin.pin_levels
        num_levels = len(pin_levels)
        
        for l in range(-2,-num_levels-1, -1): 
          level = pin_levels[l]
          cyl = InfiniteCylinderZ(cx, cy, level.radius*self.__scaleF)
          # print(cx, cy, level.radius*self.__scaleF)
          surfaces_to_draw.append((cyl, level.material))
          
    return surfaces_to_draw
    

  def __get_pin_surfaces_hex_lattice(self, new_centers, lattice):
    surfaces_to_draw = []
    lattice_rings = lattice.rings
    num_rings = len(lattice_rings)
    for r in range(num_rings):
      ring = lattice_rings[r]
      num_pins = len(ring)
      # if r == 5: break
      for p in range(num_pins):
        pin = lattice_rings[r][p]
        cx, cy = new_centers[r][p]
        pin_levels = pin.pin_levels
        num_levels = len(pin_levels)
        
        for l in range(-2,-num_levels-1, -1): 
          level = pin_levels[l]
          cyl = InfiniteCylinderZ(cx, cy, level.radius*self.__scaleF)
          
          surfaces_to_draw.append((cyl, level.material))
          
        # return surfaces_to_draw

    return surfaces_to_draw
  
  def to_ipython_img(self):
    from IPython.display import Image

    return Image(f"{self.__imageName}.png")

  @property
  def img(self):
    return self.__img
