import sys

from PIL import Image, ImageDraw




def draw_plane(plane, interval=(), im=None, name=""):
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


draw_plane(2)