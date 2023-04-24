

from Shynt.api_py import materials
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice, Universe
from Shynt.api_py.Geometry.regions import SurfaceSide, Region

from Shynt.api_py.materials import Material

from PIL import Image, ImageDraw

from Shynt.api_py.Drawer.region_dr import draw_region
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype, InfiniteHexagonalCylinderYtype, InfiniteSquareCylinderZ
from Shynt.api_py.Drawer.surface_drawing import draw_square, draw_surface, draw_square_from_points

# class PlotCell:

#     def __init__(self, cell) -> None:
#         self.__mainCell = cell
        
#         self.__materials = {}
#         self.__cellsToDraw = {}
#         self.__cellsToDraw = self.__find_cells_and_materials(cell)


def find_cells_and_materials(cell, cells_inside=None, materials=None, surfaces=None):
    cell_content = cell.content
    if cells_inside is None:
        cells_inside = []
    if materials is None:
        materials = {}
    if surfaces is None:
        surfaces = {}
    if isinstance(cell_content, Material):
        materials[cell_content.name] = cell_content
        cells_inside.append(cell)
        if isinstance(cell.region, SurfaceSide):
            surface = cell.region.surface
            surfaces[surface.id] = surface
        elif isinstance(cell.region, Region):
            surface1 = cell.region.child1.surface
            surface2 = cell.region.child2.surface
            surfaces[surface1.id] = surface1
            surfaces[surface2.id] = surface2
        return cells_inside, materials, surfaces
    elif isinstance(cell_content, HexagonalLatticeTypeX):
        cells_in_universe = cell_content.cells
        array_lattice = cell_content.array
        for row in array_lattice:
            for cell in row:
                if cell is None:
                    continue
                c = cells_in_universe[cell[0]]
                cells_inside, materials, surfaces = find_cells_and_materials(c, cells_inside=cells_inside, materials=materials, surfaces=surfaces)

        return cells_inside, materials, surfaces
    elif isinstance(cell_content, Universe):
        cells_in_universe = cell_content.cells
        for c_id, c in cells_in_universe.items():
            cells_inside, materials, surfaces = find_cells_and_materials(c, cells_inside=cells_inside, materials=materials, surfaces=surfaces)
        return cells_inside, materials, surfaces
            
def calculate_scaling_factor(cell, fig_size):
    # surface enclosing the cell -----
    enclosing_surf = cell.region.surface

    if isinstance(enclosing_surf, InfiniteSquareCylinderZ):
        # Calculating scaling factor with x, assuming it is a square
        width_square = enclosing_surf.half_width * 2
        figsize_x = fig_size[0]
        scale_f = figsize_x * 0.9 / width_square # leaving 5% of margin each side for the drawing area
        return scale_f
    elif isinstance(enclosing_surf, InfiniteHexagonalCylinderXtype):
        width_hexagon = enclosing_surf.radius * 2
        figsize_x = fig_size[0]
        
        scale_f = figsize_x * 0.9 / width_hexagon # leaving 5% of margin each side for the drawing area
        return scale_f
    elif isinstance(enclosing_surf, InfiniteHexagonalCylinderYtype):
        width_hexagon = enclosing_surf.radius * 2
        figsize_x = fig_size[0]
        
        scale_f = figsize_x * 0.9 / width_hexagon # leaving 5% of margin each side for the drawing area
        return scale_f
    else:
        print("Geometry not suported for plotting")
        raise SystemExit

def calculate_dxdy(cell, fig_size):
    enclosing_surf = cell.region.surface
    center_x = enclosing_surf.center_x
    center_y = enclosing_surf.center_y

    
    new_center = (fig_size[0]/2, fig_size[1]/2)
    fig_center_x = fig_size[0]/2

    dy = new_center[0] - center_y   # assuming it is a square
    dx = new_center[0] - center_x
    return dx, dy



def plot_cell(cell, dimensions=(500, 500), name="", cell_colors=None, rectangles=[]):
    x_max, y_max = dimensions

    # Transform lattice to plot
    scale_f = calculate_scaling_factor(cell, dimensions)
    print(f"scaling factor: {scale_f}")

    cell.scale(scale_f)
    dx, dy = calculate_dxdy(cell, dimensions)

    cell.translate((dx,dy))

    print(f"translation vector: {dx}, {dy}")

    # # Find cells in cell in case of the content is a universe -----
    cells_to_plot, \
    materials, \
    surfaces_to_plot = find_cells_and_materials(cell)
    surfaces_to_plot = list(surfaces_to_plot.values())

    # # Assign a color to each cell -----------------------------
    if cell_colors is None:
        cell_colors = {}
        for c in cells_to_plot:
            cell_colors[c.id] = c.content.color
    
    img = Image.new('RGB', dimensions, color=(254,254,254))
    # Draw surface enclosing the cell -----------------------------
    enclosing_surf = cell.region.surface
    # enclosing_surf.translate((dx,dy))
    img = draw_surface(enclosing_surf, img, y_max)

    num_surfaces_to_plot = len(surfaces_to_plot)
    # plot surfaces ---------------------------------------------
    for s in range(num_surfaces_to_plot):
        # print(f"plotting surface  {s+1}/{num_surfaces_to_plot} ")
        img = draw_surface(surfaces_to_plot[s],img,y_max)
        progress = s/num_surfaces_to_plot 


    # color the cells -------------------------------------------
    number_cells_to_plot = len(cells_to_plot)
    for c in range(number_cells_to_plot):
        cell = cells_to_plot[c]
        region = cell.region
        # print(f"Color in cell {c+1}/{number_cells_to_plot} RGB {cell_colors[cell.id]}")
        point_in_region = cell.region.get_point_in_region()
        
       
        color_point = (point_in_region[0], y_max-point_in_region[1])
        # ImageDraw.floodfill(img, color_point, value=cell_colors[cell.id])

    if len(rectangles) > 0:
        # print(rectangles)
        for id_, mesh in rectangles.items():
            x1,x2 = mesh[0]
            y1,y2 = mesh[1]
            img = draw_square_from_points(
                x1*scale_f+dx, 
                x2*scale_f+dx, 
                y1*scale_f+dy, 
                y2*scale_f+dy, 
                img
            )

        
        img.save(f"{name}.png")