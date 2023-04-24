import sys

from PIL import Image, ImageDraw

import matplotlib.pyplot as plt
import matplotlib.colors as mpl_colors
import matplotlib.cm as cm
from matplotlib.patches import RegularPolygon
from Shynt.api_py.Geometry.surfaces import InfiniteCylinderZ, InfiniteHexagonalCylinderXtype, InfiniteHexagonalCylinderYtype, InfiniteSquareCylinderZ
import numpy as np


def draw_plane(interval=(), im=None, name=""):
    """

        module that draws a plane in  2D

        plane - Plane(Surface) instance
    """
    if im:
        pass
    else:
        with Image.open("plane.jpg") as im:
            draw = ImageDraw.Draw(im)
            draw.line((0, 0) + im.size, fill=128)
            draw.line((0, im.size[1], im.size[0], 0), fill=128)

            # write to stdout
            im.save(sys.stdout, "PNG")        



def draw_surface(surf, img, y_max):
    if isinstance(surf, InfiniteSquareCylinderZ):
        return draw_square(surf, img, y_max)
    elif isinstance(surf, InfiniteCylinderZ):
        return draw_circle(surf, img, y_max)
    elif isinstance(surf, InfiniteHexagonalCylinderXtype):
        return draw_hexagon_x(surf, img, y_max)
        # print(f"hex_points: {surf.vertex_points}")
        # pass
    elif isinstance(surf, InfiniteHexagonalCylinderYtype):
        return draw_hexagon_y(surf, img, y_max)
    return img


def draw_circle(surf, img,  y_max):
    draw = ImageDraw.Draw(img)

    radius = surf.radius
    center_x, center_y = surf.center
    translated_center = (center_x, center_y)

    box_top_left_x = translated_center[0] - radius
    box_top_left_y = translated_center[1] + radius
    
    box_bottom_right_x = translated_center[0] + radius
    box_bottom_right_y = translated_center[1] - radius

    box_top_left_y = y_max - box_top_left_y
    box_bottom_right_y = y_max - box_bottom_right_y

    box = [
        (box_top_left_x,box_top_left_y),
        (box_bottom_right_x, box_bottom_right_y)
    ]

    draw.ellipse(
        box,
        outline=(0,0,0)
    )
    return img

    


def draw_square(surf, img, y_max):
    draw = ImageDraw.Draw(img)

    square_points = surf.vertex_points
    new_square_points = []
    for point in square_points:
        new_square_points.append((point[0],y_max - point[1]))
    draw.polygon(new_square_points, outline=(0,0,0))
    return img


def draw_square_from_points(x1, x2, y1, y2, img):
    # print(x1, x2, y1, y2)

    draw = ImageDraw.Draw(img)
    points = [
        (x1,y1), (x2,y1), (x2,y2), (x1,y2)
    ]
    draw.polygon(points, outline=(221, 51, 199), width=1)
    return img


def draw_hexagon_x(surf, img, y_max):
    draw = ImageDraw.Draw(img)

    hex_points = surf.vertex_points
    # print(f"hex points: {hex_points}")
    new_hex_points = []
    for point in hex_points:
        new_hex_points.append((point[0],y_max - point[1]))
        # new_hex_points.append((point[0],point[1]))
    draw.polygon(new_hex_points, outline=(0,0,0))
    return img

def draw_hexagon_y(surf, img, y_max):
    draw = ImageDraw.Draw(img)

    hex_points = surf.vertex_points
    new_hex_points = []
    for point in hex_points:
        new_hex_points.append((point[0],y_max - point[1]))
        # new_hex_points.append((point[0],point[1]))
    draw.polygon(new_hex_points, outline=(0,0,0))
    return img