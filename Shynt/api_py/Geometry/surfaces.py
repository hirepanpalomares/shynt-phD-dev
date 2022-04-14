import math

import numpy as np

from Shynt.api_py.Geometry.regions import SurfaceSide
from .surf_counter import surf_ids

class Surface:

    def __init__(self, type_surface,  name=""):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :       String to name the surface
            id          :       Integer numering the surface
            ----------------------------------------------------------------
        """
        
        self.__name = name
        self.__type = type_surface
        self.__id = self.calculateId()
    
    def calculateId(self):
        """
            Class method to calculate the consecutive id of the surface

            It generates a file with a single line where the number
            of created surfaces is updated every time the user calls
            this class or the child classes of Surfaces

            Parameters
            ----------------------------------------------------------------
            No parameters
            ----------------------------------------------------------------
        """
        if len(surf_ids) == 0:
            id_ = 1
            surf_ids.append(id_)
            return id_
        else:
            id_ = surf_ids[-1] + 1
            surf_ids.append(id_)
            return id_
        # path = os.getcwd() + "/surf-id-counter"
        # try:
        #     id_ = None
        #     with open(path, "r") as fileCounter:
        #         for line in fileCounter:
        #             id_ = int(line.split()[0]) + 1
        #             self.__id = id_
        #             break
        #     with open(path, "w") as fileCounter:
        #         fileCounter.write(str(id_))
            
        # except FileNotFoundError:
        #     self.__id = 1
        #     with open(path, "w") as fileCounter:
        #         fileCounter.write("1")
    
    
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def surface_type(self):
        return self.__type

    @id.setter
    def id(self, id):
        self.__id = id
            
    def __neg__(self):
        return SurfaceSide(self, "-")

    def __pos__(self):
        return SurfaceSide(self, "+")


class PlaneX(Surface):
    """
    Class for an inifinite Plane perpendicular to x-axis

    Surface equation: S(x) = x - x0
    """

    def __init__(self, x0, name="", boundary=None):
        super().__init__(type_surface="plane_x", name=name)
        self.__x0 = x0

        self.__function = lambda x: x - self.__x0
        
        self.serpent_syntax = f"surf {self.id} px {format(x0, '.4f')}\n"

        
        
    def eval_point(self, x):
        return self.__function(x)
    
    @property
    def x0(self):
        return self.__x0


class PlaneY(Surface):
    """
    Class for an inifinite Plane perpendicular to y-axis

    Surface equation: S(y) = y - y0
    """

    def __init__(self, y0, name="", boundary=None):
        super().__init__(type_surface="plane_y", name=name)
        self.__y0 = y0
        self.__function = lambda y: y - self.__y0
        self.__isRotated = False
        self.serpent_syntax = f"surf {self.id} py {format(y0, '.4f')}\n"

    def rotate(self, angle, ref_point):
        """
            The plane is rotated considering a unit vector from the ref_point 
            in the positive "x" direction.

            The vector is rotated and the equation of the plane is calculated
            based on two points in the vector
        """
        x0, y0 = ref_point
        x1 = x0 + 1
        
        
        x2 = np.cos(angle) / x1
        y2 = np.sin(angle) / x1

        # Calculating line equation
        m = (y2-y0)/(x2-x0)
        b = y2 - m * x2

        self.__function = lambda x: m*x + b
        self.__isRotated = True

    def isPointNegativeSide(self, y=None, x=None):
        if self.__isRotated:
            y_new = self.__function(x)
            try:
                assert(y < y_new)
                return True
            except AssertionError:
                return False
        else:
            y_new = self.__function(x)
            try:
                assert(y < 0)
                return True
            except AssertionError:
                return False

    def isPointPositiveSide(self, y=None, x=None):
        if self.__isRotated:
            y_new = self.__function(x)
            try:
                assert(y > y_new)
                return True
            except AssertionError:
                return False
        else:
            y_new = self.__function(x)
            try:
                assert(y > 0)
                return True
            except AssertionError:
                return False

    def eval_point(self, y=None, x=None):
        if self.__isRotated:
            return self.__function(x)
        else:
            return self.__function(y)

        

    @property
    def y0(self):
        return self.__y0
    

class PlaneZ(Surface):
    """
    Class for an inifinite Plane perpendicular to z-axis

    Surface equation: S(z) = z - z0
    """

    def __init__(self, z0, name="", boundary=None):
        super().__init__(type_surface="plane_z", name=name)
        self.__z0 = z0
        self.__function = lambda z: z - self.__z0
        self.serpent_syntax = f"surf {self.id} pz {format(z0, '.4f')}\n"


    def eval_point(self, z):
        return self.__function(z)

    @property
    def z0(self):
        return self.__z0


class InfiniteCylinderZ(Surface):

    """
    Class for an Infinite Cylinder parallel to Z-axis

    Surface equation: S(x, y) =  (y - y0)**2 + (x - x0)**2 - r**2
    """

    def __init__(self, center_x, center_y, radius, name="", boundary=None):
        super().__init__(type_surface="cylinder_z", name=name)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius
        self.__function = lambda x, y: (x - self.__center_x)**2 + (y - self.__center_y)**2 - self.__radius**2
        
        
    def translate(self, dx, dy):
        self.__center_x += dx
        self.__center_y += dy

    def eval_point(self, x, y):
        return self.__function(x, y)

    def is_point(self, point):
        x = point[0]
        y = point[1]
        return self.eval_point(x, y) < 0

    # def __str__(self):    
    #     return """infinite cylinder:
    #         - name: %s
    #         - id: %s
    #         - radius: %s
    #     """%(self.name, self.id, self.__radius)
    
    def evaluate_enclosed_volume(self):
        return np.pi * self.__radius * self.__radius
    
    def evaluate_surface_area(self):
        return {
            self.id: 2 * np.pi * self.__radius
        }
        

    @property
    def center(self):
        return (self.__center_x, self.__center_y)
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def serpent_syntax(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"cyl {format(self.__center_x, '.4f')} " 
        serpent_syntax += f"{format(self.__center_y, '.4f')} "
        serpent_syntax += f"{format(self.__radius, '.4f')}\n"
        return serpent_syntax


    @property
    def vertex_points(self):
        """
            The vertex points for the circle are set to be
            4, every 90 degrees on the surface line
        """
        points = [
            (self.__center_x, self.__center_y + self.__radius),
            (self.__center_x + self.__radius, self.__center_y),
            (self.__center_x, self.__center_y - self.__radius),
            (self.__center_x - self.__radius, self.__center_y),
        ]

        return points


class InfiniteCylinderY(Surface):

    """
    Class for an Infinite Cylinder parallel to Y-axis

    Surface equation: S(x, z) =  (x - x0)**2 + (z - z0)**2 - r**2
    
    """

    def __init__(self, center_x, center_z, radius, name="", boundary=None):
        super().__init__(type_surface="cylinder_y", name=name)
        self.__center_x = center_x
        self.__center_z = center_z
        self.__radius = radius
        self.__function = lambda x, z: (x - self.__center_x)**2 + (z - self.__center_z)**2 - self.__radius**2
        self.serpent_syntax = f"surf {self.id} cyly {center_x} {center_z} {radius}\n"
        

    def eval_point(self, x, z):
        return self.__function(x, z)

    def is_point(self, x, z):
        return self.eval_point(x, z) < 0

    def __str__(self):    
        return """infinite cylinder:
            - name: %s
            - id: %s
            - radius: %s
        """%(self.name, self.id, self.__radius)
    
    @property
    def center_x(self):
        return self.__center_x
    
    @property
    def center_z(self):
        return self.__center_z
    
    @property
    def radius(self):
        return self.__radius
    

class InfiniteCylinderX(Surface):

    """
    Class for an Infinite Cylinder parallel to Z-axis

    Surface equation: S(y, z) =  (y - y0)**2 + (z - z0)**2 - r**2
    """

    def __init__(self, center_y, center_z, radius, name="", boundary=None):
        super().__init__(type_surface="cylinder_x", name=name)
        self.__center_y = center_y
        self.__center_z = center_z
        self.__radius = radius
        self.__function = lambda z, y: (z - self.__center_z)**2 + (y - self.__center_y)**2 - self.__radius**2
        self.serpent_syntax = f"surf {self.id} cylx {center_y} {center_z} {radius}\n"


    def eval_point(self, z, y):
        return self.__function(z, y)

    def is_point(self, z, y):
        return self.eval_point(z, y) < 0

    def __str__(self):    
        return """infinite cylinder:
            - name: %s
            - id: %s
            - radius: %s
        """%(self.name, self.id, self.__radius)
    
    @property
    def center_z(self):
        return self.__center_z
    
    @property
    def center_y(self):
        return self.__center_y
    
    @property
    def radius(self):
        return self.__radius
       

class InfiniteSquareCylinderZ(Surface):

    """
    Class for an infinite Squere Cylinder parallel to z-axis

    It is composed by 2 x-planes and 2 y-planes

    """
    def __init__(self, center_x, center_y, half_width, name="", boundary=None):
        super().__init__(type_surface="infinite square", name=name)
        self.__boundary = boundary
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__surf_left, self.__surf_top, self.__surf_right, self.__surf_bottom = self.__generate_surfaces()

        
    def __generate_surfaces(self):
        surfaces = [
            PlaneX(self.__center_x - self.__half_width, boundary=self.__boundary), # Left
            PlaneY(self.__center_y + self.__half_width, boundary=self.__boundary), # Top
            PlaneX(self.__center_x + self.__half_width, boundary=self.__boundary), # Right
            PlaneY(self.__center_y - self.__half_width, boundary=self.__boundary), # Bottom
        ]
        return surfaces

    def is_point(self, point):
        x = point[0]
        y = point[1]
        try:
            assert(x >= self.__surf_left.x0)
            assert(x <= self.__surf_right.x0)
            assert(y >= self.__surf_bottom.y0)
            assert(y <= self.__surf_top.y0)
            return True
        except AssertionError:
            return False

    def evaluate_enclosed_volume(self):
        return self.__half_width * self.__half_width * 4
    
    def evaluate_surface_area(self):
        side_length = 2 * self.__half_width
        return {
            self.__surf_left.id: side_length,
            self.__surf_right.id: side_length,
            self.__surf_top.id: side_length,
            self.__surf_bottom.id: side_length
        }

    def get_surface_orientation(self):
        return {
            self.__surf_left.id : "left",
            self.__surf_right.id : "right",
            self.__surf_top.id : "top",
            self.__surf_bottom.id : "bottom",
        }

    def get_surface_relation(self):
        return {
            self.__surf_left.id: self.__surf_left,
            self.__surf_right.id: self.__surf_right,
            self.__surf_top.id: self.__surf_top,
            self.__surf_bottom.id:self.__surf_bottom
        }

    # def __str__(self):    
    #     return """Surface of infinite square cylinder in z-axis:
    #         - name: %s
    #         - center (x,y): (%s,%s)
    #         - half width: %s
    #         - width: %s
    #     """%(self.name, self.__center_x, self.__center_y, self.__half_width, 2*self.__half_width)

    @property
    def serpent_syntax(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"sqc {format(self.__center_x, '.4f')} " 
        serpent_syntax += f"{format(self.__center_y, '.4f')} "
        serpent_syntax += f"{format(self.__half_width, '.4f')}\n"
        return serpent_syntax

    @property
    def center_x(self):
        return self.__center_x
    
    @property
    def center_y(self):
        return self.__center_y
    
    @property
    def surf_left(self):
        return self.__surf_left

    @property
    def surf_right(self):
        return self.__surf_right

    @property
    def surf_top(self):
        return self.__surf_top

    @property
    def surf_bottom(self):
        return self.__surf_bottom

    @property
    def half_width(self):
        return self.__half_width
    
    @property
    def boundary(self):
        return self.__boundary

    @property
    def vertex_points(self):
        points = [
            (self.__center_x + self.__half_width, self.__center_y + self.__half_width),
            (self.__center_x + self.__half_width, self.__center_y - self.__half_width),
            (self.__center_x - self.__half_width, self.__center_y - self.__half_width),
            (self.__center_x - self.__half_width, self.__center_y + self.__half_width),
        ]

        return points


class InfiniteHexagonalCylinderXtype(Surface):

    def __init__(self, center_x, center_y, half_width, name="", boundary=None):
        super()._init__(name, type_surf="inf hex_x")
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__boundary = boundary
        self.__radius = self.__half_width * math.sqrt(5) / 2
        self.__surf_A, self.__surf_B, self.__surf_C, self.__surf_D, self.__surf_E, self.__surf_F = self.__generate_surfaces()

    def __generate_surfaces(self):
        """
            To rotate the plane-Y we consider the rotation of a vector with unitary length
            pointing in the positive x-direction
        
        """
        rot_ref_A = (self.__center_x, self.__center_y + self.__radius)
        rot_ref_C = (self.__center_x, self.__center_y - self.__radius)
        rot_ref_D = (self.__center_x - self.__half_width, self.__center_y - 0.5 * self.__radius)
        rot_ref_F = (self.__center_x - self.__half_width, self.__center_y + 0.5 * self.__radius)

        _A = PlaneY(self.__center_y + 0.5*self.__radius, boundary=self.__boundary)
        _B = PlaneX(self.__center_x + self.__half_width, boundary=self.__boundary)
        _C = PlaneY(self.__center_y - 0.5*self.__radius, boundary=self.__boundary)
        _D = PlaneY(self.__center_y - 0.5*self.__radius, boundary=self.__boundary)
        _E = PlaneX(self.__center_x - self.__half_width, boundary=self.__boundary)
        _F = PlaneY(self.__center_y + 0.5*self.__radius, boundary=self.__boundary)
        _A.rotate(-30, rot_ref_A)
        _C.rotate(+30, rot_ref_C)
        _D.rotate(-30, rot_ref_D)
        _F.rotate(+30, rot_ref_F)
        
        surfaces = [_A, _B, _C, _D, _E, _F ]

        return surfaces
    
    def is_point(self, point):
        x = point[0]
        y = point[1]
        try:
            assert(self.__surf_A.eval_point(y) <= 0)
            assert(self.__surf_B.eval_point(x) <= 0)
            assert(self.__surf_C.eval_point(y) >= 0)
            assert(self.__surf_D.eval_point(y) >= 0)
            assert(self.__surf_E.eval_point(x) >= 0)
            assert(self.__surf_F.eval_point(y) <= 0)
            return True
        except AssertionError:
            return False
    
    def evaluate_enclosed_volume(self):
        return self.__half_width * self.__radius * 3
    
    def evaluate_surface_area(self):
        return {
            self.__surf_A.id: self.__radius,
            self.__surf_B.id: self.__radius,
            self.__surf_C.id: self.__radius,
            self.__surf_D.id: self.__radius,
            self.__surf_E.id: self.__radius,
            self.__surf_F.id: self.__radius,
        }

    def get_surface_orientation(self):
        return {
            self.__surf_A.id: "A",
            self.__surf_B.id: "B",
            self.__surf_C.id: "C",
            self.__surf_D.id: "D",
            self.__surf_E.id: "E",
            self.__surf_F.id: "F",
        }

    def get_surface_relation(self):
        return {
            self.__surf_A.id: self.__surf_A,
            self.__surf_B.id: self.__surf_B,
            self.__surf_C.id: self.__surf_C,
            self.__surf_D.id: self.__surf_D,
            self.__surf_E.id: self.__surf_E,
            self.__surf_F.id: self.__surf_F,
        }

    @property
    def boundary(self):
        return self.__boundary




class InfiniteHexagonalCylinderYtype(Surface):

    def __init__(self, center_x, center_y, half_width, name="", boundary=None):
        super()._init__(name, type_surf="inf hex_y")
        self.serpent_syntax = f"surf {self.id} hexyc {center_x} {center_y} {half_width}\n"






def reset_surface_counter():
    surf_ids = []
    return 0
        