import numpy as np
import math

def rotate(point, angle, ref_point):
    """
        The plane is rotated considering a unit vector from the ref_point 
        in the positive "x" direction.

        The vector is rotated and the equation of the plane is calculated
        based on two points in the vector
    """
    try: 
        assert(angle != 0)
    except AssertionError:
        return 0
    
    angle = math.radians(angle)

    xc, yc = ref_point 
    x0, y0 = point
    #x0 = xc + 1 # This only works if the plane hasn't been rotated
    #y0 = yc     # This only works if the plane hasn't been rotated
    
    x1 = (x0 - xc) * np.cos(angle) - (y0 - yc) * np.sin(angle) + xc
    y1 = (x0 - xc) * np.sin(angle) + (y0 - yc) * np.cos(angle) + yc

    # Calculating line equation
    m = (y1-yc)/(x1-xc)
    b = y1 - m * x1

    print(xc, yc)
    print(x1, y1)
    print(m, b)



rotate((2,0), 45, (1,0))