

from Shynt.api_py import materials
from Shynt.api_py.Geometry.universes import (
  HexagonalLatticeTypeX, 
  HexagonalLatticeTypeY,
  HexagonalLattice,
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
    # self.__img = Image.new('RGB', self.__imageDimensions, color=(0,0,0))
    self.__img = Image.new('RGB', self.__imageDimensions, color=(256,256,256))

    
  
  def __get_surfaces_and_colors_from_lattice(self, lattice):
    void = Material("void", color=(0,0,0)) # default void
    # void = Material("void", color=(255, 100, 100))
    print("Translation vector", self.__transVector)

    expanded_wrapper = self.__mainCell.region.surface.expand(self.__scaleF)
    surfaces_to_draw = [
      (expanded_wrapper, void)
    ]
    self.__transVector = self.__calculate_dxdy(self.__mainCell)
    print("Translation vector", self.__transVector)

    print("wrapper center ",expanded_wrapper.center)
    
    # return surfaces_to_draw
    
    print("Getting surfaces to draw ....")

    new_centers = lattice.recalculate_element_centers(
      self.__scaleF
    )
    
    if isinstance(lattice, HexagonalLattice):
      element_surfaces = self.__get_elements_surfaces_hex_lattice(
        new_centers, lattice
      )
      surfaces_to_draw += element_surfaces
    elif isinstance(lattice, SquareLattice):
      lattice_surfaces = self.__get_pin_surfaces_square_lattice(
        new_centers, lattice
      )
      for surf in lattice_surfaces:
        surfaces_to_draw.append(surf)
    
    print(f'Surfaces to draw: {len(surfaces_to_draw)}')
    
    return surfaces_to_draw
  

  def __get_pin_surfaces_square_lattice(self, new_centers, lattice):
    surfaces_to_draw = []
    lattice_array = lattice.array
    num_rows = len(lattice_array)
    
    first_element = lattice_array[0][0]

    if isinstance(first_element, Pin):
      coolant_of_center = first_element.pin_levels[-1].material
      print(coolant_of_center)
      closing_hexagon = None
      cx, cy = first_element.center
      expanded_wrapper = self.__mainCell.region.surface.expand(self.__scaleF)

      surfaces_to_draw.append(
        (expanded_wrapper, coolant_of_center)
      )
      surfaces_to_draw += self.__get_elements_surfaces_hex_lattice_of_pins(
        new_centers, lattice
      )
    elif isinstance(first_element, SquareLattice):
      # this element should have pins and not other lattice
      for r in range(num_rows):
        row = lattice_array[r]
        num_elements = len(row)
        
        for p in range(num_elements):
          element = lattice_array[r][p]
          lb = element.left_bottom

          coolant_first_element = element.array[0][0].pin_levels[-1].material
          # print(new_centers[r][p])
          closing_square = InfiniteSquareCylinderZ(
            new_centers[r][p][0], 
            new_centers[r][p][1], 
            half_width=lattice.pitch* self.__scaleF /2
          )    
          surfaces_to_draw.append(
            (closing_square, coolant_first_element)
          )

      for r in range(num_rows):
        row = lattice_array[r]
        num_elements = len(row)
        
        for p in range(num_elements):

          element = lattice_array[r][p]
          print(element.name)
          cx, cy = new_centers[r][p]
          # print(cx,cy)
          # print(lattice.pitch)
          lbx = cx-lattice.pitch*self.__scaleF/2
          lby = cy-lattice.pitch*self.__scaleF/2
          print(lbx, lby)
          new_assembly_centers = element.recalculate_element_centers(
            self.__scaleF, left_bottom=(lbx, lby)
          )
          print(new_assembly_centers[0][0])

          
          
          surfaces_from_assem = self.__get_elements_surfaces_sqr_lattice_of_pins(
            new_assembly_centers, element
          )
          
          surfaces_to_draw += surfaces_from_assem
        
        
          
        # return surfaces_to_draw

    return surfaces_to_draw

  def __get_pin_surfaces_square_lattice__(self, new_centers, lattice):
    surfaces_to_draw = []
    array_pins = lattice.array
    for i, row in enumerate(array_pins):
      for j, element in enumerate(row):
        if isinstance(element, Pin):
          cx, cy = new_centers[i][j]
          pin_levels = element.pin_levels
          num_levels = len(pin_levels)
          
          for l in range(-2,-num_levels-1, -1): 
            level = pin_levels[l]
            cyl = InfiniteCylinderZ(cx, cy, level.radius*self.__scaleF)
            # print(cx, cy, level.radius*self.__scaleF)
            surfaces_to_draw.append((cyl, level.material))
        elif isinstance(element, SquareLattice):
          print(element)
          coolant_first_element = element.array[0][0].pin_levels[-1].material
          lb = element.left_bottom
          print(lb)
          print(lattice.pitch)
          closing_square = InfiniteSquareCylinderZ(
            (lb[0] + lattice.pitch/2)*self.__scaleF, 
            (lb[1] + lattice.pitch/2)*self.__scaleF, 
            half_width=lattice.pitch* self.__scaleF /2
          )
          surfaces_to_draw.append(
            (closing_square, coolant_first_element)
          )
          # new_assembly_centers = element.recalculate_element_centers(self.__scaleF)

          # surfaces_from_assem = self.__get_pin_surfaces_square_lattice(
          #   new_assembly_centers, element
          # )
          
          # surfaces_to_draw += surfaces_from_assem
    # print(surfaces_to_draw)
    return surfaces_to_draw
    
  def __get_elements_surfaces_hex_lattice(self, new_centers, lattice):
    surfaces_to_draw = []
    lattice_rings = lattice.rings
    num_rings = len(lattice_rings)
    
    central_element = lattice_rings[0][0]

    if isinstance(central_element, Pin):
      coolant_of_center = central_element.pin_levels[-1].material
      print(coolant_of_center)
      closing_hexagon = None
      cx, cy = central_element.center
      expanded_wrapper = self.__mainCell.region.surface.expand(self.__scaleF)

      surfaces_to_draw.append(
        (expanded_wrapper, coolant_of_center)
      )
      surfaces_to_draw += self.__get_elements_surfaces_hex_lattice_of_pins(
        new_centers, lattice
      )
    elif isinstance(central_element, HexagonalLattice):
      # this element should have pins and not other lattice
      for r in range(num_rings):
        ring = lattice_rings[r]
        num_elements = len(ring)
        
        for p in range(num_elements):
          element = lattice_rings[r][p]
          cx, cy = new_centers[r][p]
          coolant_of_center = element.rings[0][0].pin_levels[-1].material
          print(coolant_of_center)
          closing_hexagon = None
          if isinstance(lattice, HexagonalLatticeTypeX):
            closing_hexagon = InfiniteHexagonalCylinderXtype(
              cx, cy, lattice.pitch * self.__scaleF / 2
            )
          elif isinstance(lattice, HexagonalLatticeTypeY):
            closing_hexagon = InfiniteHexagonalCylinderYtype(
              cx, cy, lattice.pitch * self.__scaleF / 2
            )
    
          surfaces_to_draw.append(
            (closing_hexagon, coolant_of_center)
          )

      for r in range(num_rings):
        ring = lattice_rings[r]
        num_elements = len(ring)
        
        for p in range(num_elements):
          element = lattice_rings[r][p]
          cx, cy = new_centers[r][p]



          new_assembly_centers = element.recalculate_element_centers(
            self.__scaleF, (cx, cy)
          )
          

          
          
          surfaces_from_assem = self.__get_elements_surfaces_hex_lattice_of_pins(
            new_assembly_centers, element
          )
          
          surfaces_to_draw += surfaces_from_assem
        
        
          
        # return surfaces_to_draw

    return surfaces_to_draw

  def __get_elements_surfaces_hex_lattice_of_pins(self, new_centers, lattice):
    surfaces_to_draw = []
    lattice_rings = lattice.rings
    num_rings = len(lattice_rings)
    
    for r in range(num_rings):
      ring = lattice_rings[r]
      num_pins = len(ring)
      
      for p in range(num_pins):
        element = lattice_rings[r][p]
        cx, cy = new_centers[r][p]
        
        if isinstance(element, Pin):
          pin_levels = element.pin_levels
          num_levels = len(pin_levels)
          for l in range(-2,-num_levels-1, -1): 
            level = pin_levels[l]
            cyl = InfiniteCylinderZ(cx, cy, level.radius*self.__scaleF)
            
            surfaces_to_draw.append((cyl, level.material))
  
  
    return surfaces_to_draw

  def __get_elements_surfaces_sqr_lattice_of_pins(self, new_centers, lattice):
    surfaces_to_draw = []
    lattice_array = lattice.array
    num_rows = len(lattice_array)
    
    for r in range(num_rows):
      row = lattice_array[r]
      num_pins = len(row)
      
      for p in range(num_pins):
        element = lattice_array[r][p]
        cx, cy = new_centers[r][p]
        
        if isinstance(element, Pin):
          pin_levels = element.pin_levels
          num_levels = len(pin_levels)
          for l in range(-2,-num_levels-1, -1): 
            level = pin_levels[l]
            cyl = InfiniteCylinderZ(cx, cy, level.radius*self.__scaleF)
            # cyl = InfiniteCylinderZ(
            #   29.41176470588235, 2970.5882352941176, 
            #   level.radius*self.__scaleF
            # )
            
            surfaces_to_draw.append((cyl, level.material))
  
  
    return surfaces_to_draw

  def plot_assembly(self):
    x_max, y_max = self.__imageDimensions
    print("YMAX",y_max)

    # plot surfaces ---------------------------------------------
    num_surfaces_to_plot = len(self.__surfacesToDraw)
    print(f"plotting {num_surfaces_to_plot} surfaces")
    for s in range(num_surfaces_to_plot):
      # print(s)
      surf, material = self.__surfacesToDraw[s]
      # print(s, surf, material)
      # print(surf.center)
      surf.translate(self.__transVector)
      # print(surf.center)

      color = material.color
      self.__img = draw_surface(surf, self.__img, y_max, fill=color)
  
  def __transform_points(self, points):
    import numpy as np
    x_max, y_max = self.__imageDimensions
    # print("YMAX",y_max)
    dx, dy = self.__transVector
    dy = y_max -dy
    points = np.array(points)

    num_points = points.shape[0]

    dx_dy_mat = {
      2: np.array([
        [dx, dy],
        [dx, dy],
      ]),
      3: np.array([
        [dx, dy],
        [dx, dy],
        [dx, dy],
      ]),
      4: np.array([
        [dx, dy],
        [dx, dy],
        [dx, dy],
        [dx, dy],
      ])
    }
    ymax_mat = {
      2: np.array([
        [0, y_max],
        [0, y_max],
      ]),
      3: np.array([
        [0, y_max],
        [0, y_max],
        [0, y_max],
      ]),
      4: np.array([
        [0, y_max],
        [0, y_max],
        [0, y_max],
        [0, y_max],
      ]),
    }



    # new_points = []
    # for p in points:
    #   x, y = p
    #   new_p = (
    #     x*self.__scaleF+dx,
    #     y_max - (y*self.__scaleF+dy)
    #   )
    #   new_points.append(new_p)
    new_points = None
    new_points = points * self.__scaleF
    new_points = new_points + dx_dy_mat[num_points]
    new_points = ymax_mat[num_points] - new_points
    new_points[:,0] *= -1

    tuple_new_points = [tuple(p) for p in new_points]

    return tuple(tuple_new_points)
  
  def __get_square_points(self, node):
    x1,x2 = node[0]
    y1,y2 = node[1]
    points = [
      (x1,y1), (x2,y1), (x2,y2), (x1,y2)
    ]
    transformed_points = self.__transform_points(points)

    return transformed_points

  def plot_mesh(
    self, nodes_surfaces, lw=10, font_size=10, plot_surf_numbers=False, 
    plot_node_numbers=False, line_color=(0,0,0)
  ):
    import numpy as np
    

    num_coarse_nodes = len(nodes_surfaces)
    coarse_nodes = list(nodes_surfaces.keys())

    print(f"plotting {num_coarse_nodes} coarse_nodes ...")


    node_points_transformed = []
    
    
    
    for nid, surfaces in nodes_surfaces.items():
      print(nid, end=",")
      
      node_points = np.array([surf[0] for surf in surfaces.values()])
      # print(node_points)
      npt =  self.__transform_points(node_points)
      node_points_transformed.append(
        npt
      )
 
    for n, nid in enumerate(coarse_nodes):
      surfaces = node_points_transformed[n]

      print(nid, end=",")
      
      if n % 20 == 0: 
        print()
        # print(node_points_transformed[nid-1])
      # print(surfaces.values())
      # print(surfaces)
      
      self.__img = draw_polygon(
        node_points_transformed[n], self.__img, width=lw, outline=line_color
      )
      
      node_centroid = None
      if plot_node_numbers:
        node_centroid = self.__calc_centroid(node_points_transformed[n])
        self.__img =  write_text(
          node_centroid, f"{nid}", self.__img, font_size=font_size
        )

      if plot_surf_numbers:
      
        if node_centroid is None:
          node_centroid = self.__calc_centroid(node_points_transformed[n])
        
        for s_id, surf_points in nodes_surfaces[nid].items():
          points = self.__transform_points(surf_points)


          surf_centroid = self.__calc_centroid(points)

          start_writing_s_id = self.__calc_centroid(
            (node_centroid, surf_centroid)
          )
          self.__img =  write_text(
            start_writing_s_id, f"{s_id}", self.__img, font_size=font_size,
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
        scale_f = figsize_x  / width_square # leaving 5% of margin each side for the drawing area
        return scale_f
    elif isinstance(enclosing_surf, InfiniteHexagonalCylinderXtype):
        width_hexagon = enclosing_surf.radius * 2
        scale_f = figsize_x  / width_hexagon # leaving 5% of margin each side for the drawing area
        return scale_f
    elif isinstance(enclosing_surf, InfiniteHexagonalCylinderYtype):
        width_hexagon = enclosing_surf.radius * 2
        scale_f = figsize_x  / width_hexagon # leaving 5% of margin each side for the drawing area
        return scale_f
    else:
        print("Geometry not suported for plotting")
        raise SystemExit
    
  def __calculate_dxdy(self, cell):
    # enclosing_surf = cell.region.surface for Hexagonal lattices, why??
    enclosing_surf = cell.region.surface.expand(self.__scaleF)
    
    center_x = enclosing_surf.center_x
    center_y = enclosing_surf.center_y
    print(center_x, center_y)
    xt, yt = self.__imageDimensions
    new_center = (xt/2, yt/2)
    fig_center_x = self.__imageDimensions[0]/2

    dy = new_center[1] - center_y   # assuming it is a square
    dx = new_center[0] - center_x

    return dx, dy
  
  
  
  def to_ipython_img(self):
    from IPython.display import Image

    return Image(f"{self.__imageName}.png")

  @property
  def img(self):
    return self.__img


class PlotFlux(PlotLattice):

  def __init__(self, cell, dimensions=(2000, 2000), name="", mesh={}):
    super().__init__(cell, dimensions, name, mesh)