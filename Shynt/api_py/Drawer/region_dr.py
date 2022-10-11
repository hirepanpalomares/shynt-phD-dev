from PIL import Image, ImageDraw

from Shynt.api_py.Geometry.regions import SurfaceSide, Region
from Shynt.api_py.Geometry.surfaces import InfiniteCylinderZ, Surface
from Shynt.api_py.Drawer.surface_drawing import draw_surface


def scale_value(val, scale_f):
    return val * scale_f
    


def scale_points(points, scale_f):
    new_points = []
    for p in points:
        new_points.append(
            (p[0]*scale_f, p[1]*scale_f)
        )
    return new_points

def convert_points(points, dx, dy):
    new_points = []
    for p in points:
        new_points.append(
            (p[0]+dx, p[1]+dy)
        )
    return new_points

def draw_region(img, region, color, y_max):

    surfaces_to_draw = {}
    if isinstance(region, SurfaceSide):
        surf1 = region.surface
        surfaces_to_draw[surf1.id] = surf1
    elif isinstance(region, Region):
        surf1 = region.child1.surface
        surf2 = region.child2.surface
        surfaces_to_draw[surf1.id] = surf1
        surfaces_to_draw[surf2.id] = surf2

    for s_id, surface in surfaces_to_draw.items():
   
        img = draw_surface(surface, img, y_max)
        point_in_region = region.point_in_region()
        color_point = (point_in_region[0], y_max-point_in_region[1])
        ImageDraw.floodfill(img, color_point, value=color)
        
            
    return img


