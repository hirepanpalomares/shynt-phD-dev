import math

import numpy as np

from Shynt.api_py.Geometry.regions import SurfaceSide
from .surf_counter import surf_ids

class Surface:

    def __init__(self, type_surface="",  name=""):
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
        self.__lineParameters = {
            "b": None,
            "m": "inf"
        }
        self.__isRotated = False
        self.serpent_syntax = f"surf {self.id} px {format(x0, '.4f')}\n"

    def useFunction(self, var_):
        try:
            assert(var_ is not None)
            return self.__function(var_)
        except AssertionError:
            print("Error in using lambda function of Surface PlaneX - value is None type")
            raise SystemExit

    def rotate(self, angle, ref_point):
        """
            The plane is rotated considering a unit vector from the ref_point 
            in the positive "y" direction.

            The vector is rotated and the equation of the plane is calculated
            based on two points in the vector
        """
        try: 
            assert(angle != 0)
        except AssertionError:
            return 0
        
        angle = math.radians(angle)
        xc, yc = ref_point # TODO check that the refpoint is on the plane
        # TODO choose a point over the line (plane) instead just adding one
        x0 = xc     # This only works if the plane hasn't been rotated
        y0 = yc + 1     # This only works if the plane hasn't been rotated
        
        x1 = (x0 - xc) * np.cos(angle) - (y0 - yc) * np.sin(angle) + xc
        y1 = (x0 - xc) * np.sin(angle) + (y0 - yc) * np.cos(angle) + yc

        # Calculating line equation
        m = (y1-yc)/(x1-xc)
        b = yc - m * xc

        # print(f"y = {m:.6f}x + {b:.6f}")
        self.__lineParameters["m"] = m 
        self.__lineParameters["b"] = b 
        self.__function = lambda x: m*x + b
        self.__isRotated = True
        
    def translate(self, trans_vector):
        x_t, y_t = trans_vector
        if self.__isRotated:
            # eval any point --> x = 0 
            x1 = 0
            y1 = self.__function(x1)
            x2 = x1 + x_t
            y2 = y1 + y_t
            new_b = y2 - self.__lineParameters["m"] * x2
            self.__lineParameters["b"] = new_b
            self.__function = lambda x: self.__lineParameters["m"]*x + new_b
        else:
            self.__x0 += x_t

    def reset_rotation(self):
        self.__isRotated == False
        self.__lineParameters = {
            "b": None,
            "m": "inf"
        }

        self.__function = lambda x: x - self.__x0

    def isPointNegativeSide(self, x=None, y=None):
        # print(x, y)

        if self.__isRotated:
            y_in_line = self.useFunction(x)
            # print(y_in_line)
            try:
                if self.__lineParameters["m"] < 0:
                    assert(y <= y_in_line)
                else:
                    assert(y >= y_in_line)
                return True
            except AssertionError:
                return False
        else:
            x_new = self.useFunction(x)
            try:
                assert(x_new <= 0)
                return True
            except AssertionError:
                return False

    def isPointPositiveSide(self, x=None, y=None):
        try:
            assert(self.isPointNegativeSide(x=x, y=y))
            return False
        except AssertionError:
            return True
    
    @property
    def serpent_syntax_for_detector(self):
        return f"surf {self.id} px {format(self.x0, '.4f')}\n"
    
    @property
    def serpent_syntax_for_lattice(self):
        return f"surf {self.id} px {0.0000}\n"

    @property
    def x0(self):
        return self.__x0

    @x0.setter
    def x0(self, new_x0):
        self.__x0 = new_x0

    @property
    def line_params(self):
        return self.__lineParameters


class PlaneY(Surface):
    """
    Class for an inifinite Plane perpendicular to y-axis

    Surface equation: S(y) = y - y0
    """

    def __init__(self, y0, name="", boundary=None):
        super().__init__(type_surface="plane_y", name=name)
        self.__y0 = y0
        self.__function = lambda y: y - self.__y0
        self.__lineParameters = {
            "b": None,
            "m": "inf"
        }
        self.__isRotated = False
        

    def useFunction(self, var_):
        try:
            assert(var_ is not None)
            return self.__function(var_)
        except AssertionError:
            print("Error in using lambda function of Surface PlaneY - value is None type")
            raise SystemExit

    def rotate(self, angle, ref_point):
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
        xc, yc = ref_point # TODO checck that the refpoint is on the plane
        # TODO choose a point over the line (plane) instead just adding one
        x0 = xc + 1 # This only works if the plane hasn't been rotated
        y0 = yc     # This only works if the plane hasn't been rotated
        
        x1 = (x0 - xc) * np.cos(angle) - (y0 - yc) * np.sin(angle) + xc
        y1 = (x0 - xc) * np.sin(angle) + (y0 - yc) * np.cos(angle) + yc

        # Calculating line equation
        m = (y1-yc)/(x1-xc)
        b = yc - m * xc
        
        # print(f"y = {m:.2f}x + {b:.2f}")
        self.__lineParameters["m"] = m 
        self.__lineParameters["b"] = b 
        self.__function = lambda x: m*x + b
        self.__isRotated = True

    def reset_rotation(self):
        self.__isRotated == False
        self.__lineParameters = {
            "b": None,
            "m": "inf"
        }

        self.__function = lambda y: y - self.__y0

    def isPointNegativeSide(self, x=None, y=None):
        # print(x, y)
        if self.__isRotated:
            y_in_line = self.useFunction(x)
            # print(y_in_line)
            try:
                assert(y <= y_in_line)
                return True
            except AssertionError:
                return False
        else:
            y_in_line = self.useFunction(y)
            try:
                assert(y_in_line <= 0)
                return True
            except AssertionError:
                return False

    def isPointPositiveSide(self, x=None, y=None):
        try:
            assert(self.isPointNegativeSide(x=x, y=y))
            return False
        except AssertionError:
            return True

    def eval_point(self, y=None, x=None):
        if self.__isRotated:
            return self.useFunction(x)
        else:
            return self.useFunction(y)

    def translate(self, trans_vector):
        x_t, y_t = trans_vector
        if self.__isRotated:
            # eval any point --> x = 0 
            x1 = 0
            y1 = self.__function(x1)
            x2 = x1 + x_t
            y2 = y1 + y_t
            new_b = y2 - self.__lineParameters["m"] * x2
            self.__lineParameters["b"] = new_b
            self.__function = lambda x: self.__lineParameters["m"]*x + new_b
        else:
            self.__y0 += y_t
    
    @property
    def serpent_syntax_for_detector(self):
        return f"surf {self.id} py {format(self.y0, '.4f')}\n"
    
    @property
    def serpent_syntax_for_lattice(self):
        return f"surf {self.id} py {0.0000}\n"

    @property
    def y0(self):
        return self.__y0
    
    @y0.setter
    def y0(self, new_y0):
        self.__y0 = new_y0

    @property
    def line_params(self):
        return self.__lineParameters
    

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
        
        
    def translate_to(self, new_x, new_y):
        trans_vector = (
            new_x - self.__center_x,
            new_y - self.__center_y
        )
        self.translate(trans_vector)
    
    def translate(self, trans_vector):
        t_x, t_y = trans_vector
        self.__center_x += t_x
        self.__center_y += t_y


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
    def serpent_syntax_for_detector(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"cyl {format(self.__center_x, '.4f')} " 
        serpent_syntax += f"{format(self.__center_y, '.4f')} "
        serpent_syntax += f"{format(self.__radius, '.4f')}\n"
        return serpent_syntax

    @property
    def serpent_syntax_for_lattice(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"cyl {0.0000} " 
        serpent_syntax += f"{0.0000} "
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

    surf_top    --> cell in - side
    surf_right  --> cell in - side
    surf_bottom --> cell in + side
    surf_left   --> cell in + side

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
    
    def get_neutron_current_directions(self):
        # surf T --> outward current = +1 --> inward current = -1
        # surf R --> outward current = +1 --> inward current = -1
        # surf B --> outward current = -1 --> inward current = +1
        # surf L --> outward current = -1 --> inward current = +1
        return {
            self.__surf_top.id: {"inward": "-1", "outward": "1"},
            self.__surf_right.id: {"inward": "-1", "outward": "1"},
            self.__surf_bottom.id: {"inward": "1", "outward": "-1"},
            self.__surf_left.id: {"inward": "1", "outward": "-1"},
        }

    # def __str__(self):    
    #     return """Surface of infinite square cylinder in z-axis:
    #         - name: %s
    #         - center (x,y): (%s,%s)
    #         - half width: %s
    #         - width: %s
    #     """%(self.name, self.__center_x, self.__center_y, self.__half_width, 2*self.__half_width)

    @property
    def serpent_syntax_for_detector(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"sqc {format(self.__center_x, '.4f')} " 
        serpent_syntax += f"{format(self.__center_y, '.4f')} "
        serpent_syntax += f"{format(self.__half_width, '.4f')}\n"
        return serpent_syntax

    @property
    def serpent_syntax_for_lattice(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"sqc {0.0000} " 
        serpent_syntax += f"{0.0000} "
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


class Hexagon(Surface):

    def __init__(self, type_surface="", name=""):
        super().__init__(type_surface, name)
        
class InfiniteHexagonalCylinderXtype(Hexagon):
    """
    
        surf_A   --> cell in - side
        surf_B   --> cell in - side
        surf_C   --> cell in + side
        surf_D   --> cell in + side
        surf_E   --> cell in + side
        surf_F   --> cell in - side

    """

    def __init__(self, center_x, center_y, half_width, name="", boundary=None):
        super().__init__(name=name, type_surface="inf hex_x")
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__boundary = boundary
        self.__radius = 2 * self.__half_width / math.sqrt(3)
        self.__side = self.__radius
        self.__surf_A, self.__surf_B, self.__surf_C, self.__surf_D, self.__surf_E, self.__surf_F = self.__generate_surfaces()
        self.serpent_syntax = f"surf {self.id} hexxc {center_x} {center_y} {half_width}\n"
        # self.serpent_syntax = f"surf {self.id} hexyc {center_x} {center_y} {half_width}\n"

    def __generate_surfaces(self):
        """
            To rotate the plane-Y we consider the rotation of a vector with unitary length
            pointing in the positive x-direction
        
        """
        rot_ref_A = (self.__center_x, self.__center_y + self.__radius)
        rot_ref_C = (self.__center_x, self.__center_y - self.__radius)
        rot_ref_D = (self.__center_x, self.__center_y - self.__radius)
        rot_ref_F = (self.__center_x, self.__center_y + self.__radius)

        _A = PlaneY(self.__center_y + self.__radius, boundary=self.__boundary)
        _B = PlaneX(self.__center_x + self.__half_width, boundary=self.__boundary)
        _C = PlaneY(self.__center_y - self.__radius, boundary=self.__boundary)
        _D = PlaneY(self.__center_y - self.__radius, boundary=self.__boundary)
        _E = PlaneX(self.__center_x - self.__half_width, boundary=self.__boundary)
        _F = PlaneY(self.__center_y + self.__radius, boundary=self.__boundary)
        _A.rotate(-30, rot_ref_A)
        _C.rotate(+30, rot_ref_C)
        _D.rotate(-30, rot_ref_D)
        _F.rotate(+30, rot_ref_F)
        
        surfaces = [_A, _B, _C, _D, _E, _F ]

        return surfaces
    
    def translate(self, translation_vector):
        x_tr, y_tr = translation_vector
        
        self.__center_x += x_tr
        self.__center_y += y_tr

        self.surf_A.translate(translation_vector)
        self.surf_B.translate(translation_vector)
        self.surf_C.translate(translation_vector)
        self.surf_D.translate(translation_vector)
        self.surf_E.translate(translation_vector)
        self.surf_F.translate(translation_vector)

        return 1


    def isPointNegativeSide(self, point):
        x, y = point
        try:
            assert self.__surf_A.isPointNegativeSide(x=x,y=y)
            assert self.__surf_B.isPointNegativeSide(x=x,y=y)
            assert self.__surf_C.isPointPositiveSide(x=x,y=y)
            assert self.__surf_D.isPointPositiveSide(x=x,y=y)
            assert self.__surf_E.isPointPositiveSide(x=x,y=y)
            assert self.__surf_F.isPointNegativeSide(x=x,y=y)
            return True
        except AssertionError:
            return False
    
    def isPointPositiveSide(self, point):
        x, y = point
        try:
            assert(self.isPointNegativeSide((x,y)))
            return False
        except AssertionError:
            return True
    
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
    
    def get_neutron_current_directions(self):
        # surf A --> outward current = +1 --> inward current = -1
        # surf B --> outward current = +1 --> inward current = -1
        # surf C --> outward current = -1 --> inward current = +1
        # surf D --> outward current = -1 --> inward current = +1
        # surf E --> outward current = -1 --> inward current = +1
        # surf F --> outward current = +1 --> inward current = -1
        return {
            self.__surf_A.id: {"inward": "-1", "outward": "1"},
            self.__surf_B.id: {"inward": "-1", "outward": "1"},
            self.__surf_C.id: {"inward": "1", "outward": "-1"},
            self.__surf_D.id: {"inward": "1", "outward": "-1"},
            self.__surf_E.id: {"inward": "1", "outward": "-1"},
            self.__surf_F.id: {"inward": "-1", "outward": "1"}
        }

    def get_vertex_points(self):
        points = [
            (self.__center_x, self.__center_y - self.__radius),         # vertex F - A
            (self.__center_x, self.__center_y + self.__radius),         # vertex C - D

            (self.__surf_B.x0, self.__center_y + 0.5*self.__radius),    # vertex A - B
            (self.__surf_B.x0, self.__center_y - 0.5*self.__radius),    # vertex B - C

            (self.__surf_E.x0, self.__center_y - 0.5*self.__radius),    # vertex D - E
            (self.__surf_E.x0, self.__center_y + 0.5*self.__radius),    # vertex E - F    
        ]        
        return points

    def get_side_middle_points(self):
        sx = 0.5 * self.__half_width
        sy = math.cos(math.radians(30)) * self.__half_width
        points = [
            (self.__center_x + sx, self.__center_y + sy),   # A
            (self.__surf_B.x0, self.__center_x),            # B
            (self.__center_x + sx, self.__center_y - sy),   # C
            (self.__center_x - sx, self.__center_y - sy),   # D
            (self.__surf_E.x0, self.__center_x),            # E
            (self.__center_x - sx, self.__center_y + sy),   # F
        ]

        return points

    @property
    def radius(self):
        return self.__radius

    @property
    def boundary(self):
        return self.__boundary
    
    @property
    def surf_A(self):
        return self.__surf_A
    
    @property
    def surf_B(self):
        return self.__surf_B
    
    @property
    def surf_C(self):
        return self.__surf_C
    
    @property
    def surf_D(self):
        return self.__surf_D

    @property
    def surf_E(self):
        return self.__surf_E

    @property
    def surf_F(self):
        return self.__surf_F
    
    @property
    def center(self):
        return (self.__center_x, self.__center_y)


class InfiniteHexagonalCylinderYtype(Hexagon):
    """
    
        surf_A   --> cell in - side
        surf_B   --> cell in - side
        surf_C   --> cell in - side
        surf_D   --> cell in + side
        surf_E   --> cell in + side
        surf_F   --> cell in + side

    """

    def __init__(self, center_x, center_y, half_width, name="", boundary=None):
        super().__init__(name=name, type_surface="inf hex_x")
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__boundary = boundary
        # self.__side = 2 * self.__half_width * math.tan(math.radians(30))
        self.__radius = 2 * self.__half_width / math.sqrt(3)
        self.__side = self.__radius
        # self.__radius = self.__half_width * math.sqrt(5) / 2
        
        self.__surf_A, self.__surf_B, self.__surf_C, self.__surf_D, self.__surf_E, self.__surf_F = self.__generate_surfaces()
        self.serpent_syntax = f"surf {self.id} hexyc {center_x} {center_y} {half_width}\n"

    def __generate_surfaces(self):
        """
            To rotate the plane-Y we consider the rotation of a vector with unitary length
            pointing in the positive x-direction
        
        """
        rot_ref_B = (self.__center_x + self.__radius, self.__center_y)
        rot_ref_C = (self.__center_x + self.__radius, self.__center_y)
        rot_ref_E = (self.__center_x - self.__radius, self.__center_y)
        rot_ref_F = (self.__center_x - self.__radius, self.__center_y)

        _A = PlaneY(self.__center_y + self.__half_width, boundary=self.__boundary)
        _B = PlaneX(self.__center_x + self.__radius, boundary=self.__boundary)
        _C = PlaneX(self.__center_x + self.__radius, boundary=self.__boundary)
        _D = PlaneY(self.__center_y - self.__half_width, boundary=self.__boundary)
        _E = PlaneX(self.__center_x - self.__radius, boundary=self.__boundary)
        _F = PlaneX(self.__center_x - self.__radius, boundary=self.__boundary)

        _B.rotate(+30, rot_ref_B)
        _C.rotate(-30, rot_ref_C)
        _E.rotate(+30, rot_ref_E)
        _F.rotate(-30, rot_ref_F)
        
        surfaces = [_A, _B, _C, _D, _E, _F ]

        return surfaces
    
    def translate(self, translation_vector):
        x_tr, y_tr = translation_vector
        
        self.__center_x += x_tr
        self.__center_y += y_tr

        self.surf_A.translate(translation_vector)
        self.surf_B.translate(translation_vector)
        self.surf_C.translate(translation_vector)
        self.surf_D.translate(translation_vector)
        self.surf_E.translate(translation_vector)
        self.surf_F.translate(translation_vector)

        return 1
        
    def isPointNegativeSide(self, point):
        x, y = point
        try:
            assert self.__surf_A.isPointNegativeSide(x=x,y=y)
            assert self.__surf_B.isPointNegativeSide(x=x,y=y)
            assert self.__surf_C.isPointNegativeSide(x=x,y=y)
            assert self.__surf_D.isPointPositiveSide(x=x,y=y)
            assert self.__surf_E.isPointPositiveSide(x=x,y=y)
            assert self.__surf_F.isPointPositiveSide(x=x,y=y)
            return True
        except AssertionError:
            return False
    
    def isPointPositiveSide(self, point):
        x, y = point
        try:
            assert(self.isPointNegativeSide((x,y)))
            return False
        except AssertionError:
            return True
    
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

    def get_neutron_current_directions(self):
        # surf A --> outward current = +1 --> inward current = -1
        # surf B --> outward current = +1 --> inward current = -1
        # surf C --> outward current = +1 --> inward current = -1
        # surf D --> outward current = -1 --> inward current = +1
        # surf E --> outward current = -1 --> inward current = +1
        # surf F --> outward current = -1 --> inward current = +1
        return {
            self.__surf_A.id: {"inward": "-1", "outward": "1"},
            self.__surf_B.id: {"inward": "-1", "outward": "1"},
            self.__surf_C.id: {"inward": "-1", "outward": "1"},
            self.__surf_D.id: {"inward": "1", "outward": "-1"},
            self.__surf_E.id: {"inward": "1", "outward": "-1"},
            self.__surf_F.id: {"inward": "1", "outward": "-1"}
        }

    def get_vertex_points(self):
        points = [
            (self.__center_x - self.__radius, self.__center_y),         # vertex E - F
            (self.__center_x + self.__radius, self.__center_y),         # vertex B - C
            (self.__center_x - 0.5*self.__radius, self.__surf_A.y0),    # vertex F - A    
            (self.__center_x + 0.5*self.__radius, self.__surf_A.y0),    # vertex A - B
            (self.__center_x - 0.5*self.__radius, self.__surf_D.y0),    # vertex D - E
            (self.__center_x + 0.5*self.__radius, self.__surf_D.y0),    # vertex C - D
        ]        
        return points

    def get_side_middle_points(self):
        sx = math.cos(math.radians(30)) * self.__half_width
        sy = 0.5 * self.__half_width
        points = [
            (self.__center_x, self.__surf_A.y0),            # A
            (self.__center_x + sx, self.__center_y + sy),   # B
            (self.__center_x + sx, self.__center_y - sy),   # C
            (self.__center_x, self.__surf_D.y0),            # D
            (self.__center_x - sx, self.__center_y - sy),   # E
            (self.__center_x - sx, self.__center_y + sy),   # F
        ]

        return points

    @property
    def radius(self):
        return self.__radius

    @property
    def boundary(self):
        return self.__boundary

    @property
    def surf_A(self):
        return self.__surf_A
    
    @property
    def surf_B(self):
        return self.__surf_B
    
    @property
    def surf_C(self):
        return self.__surf_C
    
    @property
    def surf_D(self):
        return self.__surf_D

    @property
    def surf_E(self):
        return self.__surf_E

    @property
    def surf_F(self):
        return self.__surf_F
    
    @property
    def center(self):
        return self.__center_x, self.__center_y



def reset_surface_counter():
    surf_ids = []
    return 0
        