from abc import ABC, abstractmethod
import math
import numpy as np

from .surf_counter import surf_ids


class Surface():

    def __init__(self, type_surface="",  name="", isClone=False):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :       String to name the surface
            id          :       Integer numering the surface
            isClone     :       Parameter that is used when writing the surfaces
                                for a detector if it is the case to avoid messing
                                up with the geometry and ids of the original 
                                surfaces.
            ----------------------------------------------------------------
        """
        
        self.__name = name
        self.__type = type_surface
        self.__isClone = isClone
        if self.__isClone:
            self.__id = None
        else:
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
    
    # @abstractmethod
    # def useFunction(self):
    #     pass

    # @abstractmethod
    # def rotate(self):
    #     pass

    # @abstractmethod
    # def translate(self):
    #     pass

    # @abstractmethod
    # def reset_rotation(self):
    #     pass

    # @abstractmethod
    # def isPointNegativeSide(self):
    #     pass

    # @abstractmethod
    # def isPointPositiveSide(self):
    #     pass

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
        try:
            assert(self.__isClone)
            self.__id = id
        except AssertionError:
            print("Id of non clone surface can not be asigned")
            raise SystemExit
         
    def __neg__(self):
        from Shynt.api_py.Geometry.regions import SurfaceSide
        return SurfaceSide(self, "-")

    def __pos__(self):
        from Shynt.api_py.Geometry.regions import SurfaceSide
        return SurfaceSide(self, "+")


class CompoundSurface(Surface, ABC):

    def __init__(self) -> None:
        super().__init__()


class PlaneX(Surface):
    """
    Class for an inifinite Plane perpendicular to x-axis

    Surface equation: S(x) = x - x0
    """

    def __init__(self, x0, name="", boundary=None, isClone=False):
        super().__init__(type_surface="plane_x", name=name, isClone=isClone)
        self.__x0 = x0
        self.__isClone = isClone
        self.__function = lambda x: x - self.__x0
        self.__lineParameters = {
            "b": None,
            "m": "inf"
        }
        self.__isRotated = False
        self.__rotationAngle = None
        self.__rotationRefPoint = None
        self.serpent_syntax = f"surf {self.id} px {format(x0, '.8f')}\n"


    def useFunction(self, var_, given="x"):
        try:
            # assert(var_ is not None)
            if given == "x":
                return round(self.__function(var_),8)
            elif given == "y":
                m, b = self.__lineParameters["m"], self.__lineParameters["b"]
                assert(m != "inf")
                assert(b is not None)
                return round((var_ - b) / m,8)
        except AssertionError:
            print("Error in using lambda function of Surface PlaneY")
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
        self.__rotationAngle = angle
        self.__rotationRefPoint = ref_point
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

    def isPointNegativeSide(self, point):
        x,y = point
        if self.__isRotated:
            y_in_line = self.useFunction(x)
            # print(y_in_line)
            try:
                if self.__lineParameters["m"] < 0:
                    assert(y < y_in_line)
                else:
                    assert(y > y_in_line)
                return True
            except AssertionError:
                if y == y_in_line:
                    return None
                
                return False
        else:
            x_new = self.useFunction(x)
            try:
                assert(x_new < 0)
                return True
            except AssertionError:
                if x_new == 0:
                    return None
                else:
                    return False

    def isPointPositiveSide(self, point):
        eval_ = self.isPointNegativeSide(point)
        if eval_ is None or eval_ is True:
            return False
        elif eval_ is False:
            return True
        
    
    def clone(self, new_center_x, new_center_y, clone_vector=None):
        new_x0 = self.__x0
        if clone_vector:
            new_x0 = self.__x0 + clone_vector[0]
        surf_clone = PlaneX(new_x0, isClone=True)
        surf_clone.id = super().id
        if self.__isRotated:
            surf_clone.rotate(self.__rotationAngle, ref_point=self.__rotationRefPoint)
        return surf_clone
    
    @property
    def serpent_syntax_exact_position(self):
        serp_syntax =  f"surf {self.id} px {format(self.x0, '.8f')}\n"

        if self.__isRotated:
            serp_syntax += f"trans s {self.id} 0.0 0.0 0.0 0.0 0.0 {-1*self.__rotationAngle}\n"
        return serp_syntax
        
    
    @property
    def serpent_syntax_standard_position(self):
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

    def __init__(self, y0, name="", boundary=None, isClone=False):
        super().__init__(type_surface="plane_y", name=name, isClone=isClone)
        self.__y0 = y0
        self.__isClone = isClone
        self.__function = lambda y: y - self.__y0
        self.__lineParameters = {
            "b": None,
            "m": "inf"
        }
        self.__isRotated = False
        self.__rotationAngle = None
        self.__rotationRefPoint = None
        

    def useFunction(self, var_, given="x"):
        try:
            assert(var_ is not None)
            if given == "x":
                return round(self.__function(var_),8)
            elif given == "y":
                m, b = self.__lineParameters["m"], self.__lineParameters["b"]
                assert(m != "inf")
                assert(b is not None)
                return round((var_ - b) / m,8)
        except AssertionError:
            print("Error in using lambda function of Surface PlaneY")
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
        self.__rotationAngle = angle
        self.__rotationRefPoint = ref_point
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

    def isPointNegativeSide(self, point):
        x,y = point
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
                assert(y_in_line < 0)
                return True
            except AssertionError:
                if y_in_line == 0:
                    return None
                else:
                    return False

    def isPointPositiveSide(self, point):
        eval_ = self.isPointNegativeSide(point)
        if eval_ is None or eval_ is True:
            return False
        elif eval_ is False:
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
            self.__y0 += y_t
            x1 = 0
            y1 = self.__function(x1)
            x2 = x1 + x_t
            y2 = y1 + y_t
            new_b = y2 - self.__lineParameters["m"] * x2
            self.__lineParameters["b"] = new_b
            self.__function = lambda x: self.__lineParameters["m"]*x + new_b
        else:
            self.__y0 += y_t
    
    def clone(self, new_center_x, new_center_y, clone_vector=None):
        new_y0 = self.__y0
        if clone_vector:
            new_y0 = self.__y0 + clone_vector[1]
        surf_clone = PlaneY(new_y0, isClone=True)
        if self.__isRotated:
            surf_clone.rotate(self.__rotationAngle, ref_point=self.__rotationRefPoint)
        surf_clone.id = super().id
        return surf_clone
    

    @property
    def serpent_syntax_exact_position(self):
        serp_syntax =  f"surf {self.id} py {format(self.y0, '.8f')}\n"

        if self.__isRotated:
            serp_syntax += f"trans s {self.id} 0.0 0.0 0.0 0.0 0.0 {-1*self.__rotationAngle}\n"
        return serp_syntax
    
    @property
    def serpent_syntax_standard_position(self):
        serp_syntax =  f"surf {self.id} py {0.0000}\n"
        
        return serp_syntax

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
        self.serpent_syntax = f"surf {self.id} pz {format(z0, '.8f')}\n"


    def eval_point(self, z):
        return self.__function(z)

    @property
    def z0(self):
        return self.__z0


class InfiniteSquareCylinderZ(Surface):

    """
    Class for an infinite Squere Cylinder parallel to z-axis

    It is composed by 2 x-planes and 2 y-planes

    surf_top    --> cell in - side
    surf_right  --> cell in - side
    surf_bottom --> cell in + side
    surf_left   --> cell in + side

    """
    def __init__(self, center_x, center_y, half_width, name="", boundary=None, isClone=False):
        super().__init__(type_surface="infinite square", name=name, isClone=isClone)
        self.__boundary = boundary
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__isClone = isClone
        self.__surf_left, self.__surf_top, self.__surf_right, self.__surf_bottom = self.__generate_surfaces()
        
    def __generate_surfaces(self):
        surfaces = [
            PlaneX(
                self.__center_x - self.__half_width, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Left
            PlaneY(
                self.__center_y + self.__half_width, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Top
            PlaneX(
                self.__center_x + self.__half_width, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Right
            PlaneY(
                self.__center_y - self.__half_width, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Bottom
        ]
        return surfaces

    def translate(self, translation_vector):
        x_tr, y_tr = translation_vector
        
        self.__center_x += x_tr
        self.__center_y += y_tr

        self.__surf_left.translate(translation_vector)
        self.__surf_top.translate(translation_vector)
        self.__surf_right.translate(translation_vector)
        self.__surf_bottom.translate(translation_vector)
        
        return 1

    def scale(self, scale_f):
        new_half_width = self.__half_width * scale_f
        plane_move = new_half_width - self.__half_width

        self.__surf_left.translate((-plane_move,0))
        self.__surf_top.translate((0,plane_move))
        self.__surf_right.translate((plane_move,0))
        self.__surf_bottom.translate((0,-plane_move))

        self.__half_width = new_half_width

    def isPointNegativeSide(self, point):
        x, y = point
        try:
            assert(x >= self.__surf_left.x0)
            assert(x <= self.__surf_right.x0)
            assert(y >= self.__surf_bottom.y0)
            assert(y <= self.__surf_top.y0)
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
        return self.__half_width * self.__half_width * 4
    
    def evaluate_surface_area(self):
        side_length = 2 * self.__half_width
        return {
            self.__surf_left.id: side_length,
            self.__surf_top.id: side_length,
            self.__surf_right.id: side_length,
            self.__surf_bottom.id: side_length
        }

    def get_surface_orientation(self):
        return {
            self.__surf_left.id : "left",
            self.__surf_top.id : "top",
            self.__surf_right.id : "right",
            self.__surf_bottom.id : "bottom",
        }

    def get_surface_relation(self):
        return {
            self.__surf_left.id: self.__surf_left,
            self.__surf_top.id: self.__surf_top,
            self.__surf_right.id: self.__surf_right,
            self.__surf_bottom.id:self.__surf_bottom
        }
    
    def get_neutron_current_directions(self):
        # surf T --> outward current = +1 --> inward current = -1
        # surf R --> outward current = +1 --> inward current = -1
        # surf B --> outward current = -1 --> inward current = +1
        # surf L --> outward current = -1 --> inward current = +1
        return {
            self.__surf_left.id: {"inward": "1", "outward": "-1"},
            self.__surf_top.id: {"inward": "-1", "outward": "1"},
            self.__surf_right.id: {"inward": "-1", "outward": "1"},
            self.__surf_bottom.id: {"inward": "1", "outward": "-1"},
        }

    def clone(self, center_x, center_y, clone_vector=None):
        """
            It clones the surface: same id, but in a new center
        """
        clone_square = InfiniteSquareCylinderZ(center_x, center_y, self.__half_width, isClone=True)
        clone_square.surf_left.id = self.__surf_left.id
        clone_square.surf_right.id = self.__surf_right.id
        clone_square.surf_top.id = self.__surf_top.id
        clone_square.surf_bottom.id = self.__surf_bottom.id
        clone_square.id = super().id

        return clone_square

    def scale(self, scale_factor):
        self.__half_width *= scale_factor
        return 1

    # def __str__(self):    
    #     return """Surface of infinite square cylinder in z-axis:
    #         - name: %s
    #         - center (x,y): (%s,%s)
    #         - half width: %s
    #         - width: %s
    #     """%(self.name, self.__center_x, self.__center_y, self.__half_width, 2*self.__half_width)

    @property
    def serpent_syntax_exact_position(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"sqc {format(self.__center_x, '.8f')} " 
        serpent_syntax += f"{format(self.__center_y, '.8f')} "
        serpent_syntax += f"{format(self.__half_width, '.8f')}\n"
        return serpent_syntax

    @property
    def serpent_syntax_standard_position(self):
        serpent_syntax = f"surf {self.id} sqc {0.0000} {0.0000} "
        serpent_syntax += f"{format(self.__half_width, '.8f')}\n"
        return serpent_syntax

    @property
    def left_bottom(self):
        return (self.__center_x - self.__half_width, self.center_y - self.__half_width)
    
    @property
    def center_x(self):
        return self.__center_x
    
    @property
    def center_y(self):
        return self.__center_y
    
    @property
    def center(self):
        return (self.__center_x, self.__center_y)
    
    @center.setter
    def center(self, center):
        self.__center_x = center[0]
        self.__center_y = center[1]

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


class InfiniteRectangleCylinderZ(Surface):

    """
    Class for an infinite Squere Cylinder parallel to z-axis

    It is composed by 2 x-planes and 2 y-planes

    surf_top    --> cell in - side
    surf_right  --> cell in - side
    surf_bottom --> cell in + side
    surf_left   --> cell in + side

    """
    def __init__(self, x1, x2, y1, y2, name="", boundary=None, isClone=False):
        super().__init__(type_surface="infinite rectangle", name=name, isClone=isClone)
        self.__boundary = boundary
        # try:
        assert(x2>x1)
        assert(y2>y1)
        # except AssertionError:


        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__height = y2 - y1
        self.__width = x2 - x1
        self.__isClone = isClone
        self.__surf_left, self.__surf_top, self.__surf_right, self.__surf_bottom = self.__generate_surfaces()
    
    def __generate_surfaces(self):
        surfaces = [
            PlaneX(
                self.__x1, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Left
            PlaneY(
                self.__y2, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Top
            PlaneX(
                self.__x2, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Right
            PlaneY(
                self.__y1, 
                boundary=self.__boundary,
                isClone=self.__isClone
            ), # Bottom
        ]
        return surfaces

    def translate(self, translation_vector):
        x_tr, y_tr = translation_vector
        
        self.__center_x += x_tr
        self.__center_y += y_tr

        self.__surf_left.translate(translation_vector)
        self.__surf_top.translate(translation_vector)
        self.__surf_right.translate(translation_vector)
        self.__surf_bottom.translate(translation_vector)
        
        return 1

    def isPointNegativeSide(self, point):
        x, y = point
        try:
            assert(x >= self.__surf_left.x0)
            assert(x <= self.__surf_right.x0)
            assert(y >= self.__surf_bottom.y0)
            assert(y <= self.__surf_top.y0)
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
        side1 = self.__x2 - self.__x1
        side2 = self.__y2 - self.__y1
        return side1*side2
    
    def evaluate_surface_area(self):
        side1 = self.__x2 - self.__x1
        side2 = self.__y2 - self.__y1
        return {
            self.__surf_left.id: side2,
            self.__surf_top.id: side1,
            self.__surf_right.id: side2,
            self.__surf_bottom.id: side1
        }

    def get_surface_orientation(self):
        return {
            self.__surf_left.id : "left",
            self.__surf_top.id : "top",
            self.__surf_right.id : "right",
            self.__surf_bottom.id : "bottom",
        }

    def get_surface_relation(self):
        return {
            self.__surf_left.id: self.__surf_left,
            self.__surf_top.id: self.__surf_top,
            self.__surf_right.id: self.__surf_right,
            self.__surf_bottom.id:self.__surf_bottom
        }
    
    def get_neutron_current_directions(self):
        # surf T --> outward current = +1 --> inward current = -1
        # surf R --> outward current = +1 --> inward current = -1
        # surf B --> outward current = -1 --> inward current = +1
        # surf L --> outward current = -1 --> inward current = +1
        return {
            self.__surf_left.id: {"inward": "1", "outward": "-1"},
            self.__surf_top.id: {"inward": "-1", "outward": "1"},
            self.__surf_right.id: {"inward": "-1", "outward": "1"},
            self.__surf_bottom.id: {"inward": "1", "outward": "-1"},
        }

    def clone(self, center_x, center_y, clone_vector=None):
        """
            It clones the surface: same id, but in a new center
        """
        length_x = self.__x2 - self.__x1
        length_y = self.__y2 - self.__y1
        
        new_x1 = center_x - length_x/2
        new_x2 = center_x + length_x/2
        new_y1 = center_y - length_y/2
        new_y2 = center_y + length_y/2

        clone_rectangle = InfiniteRectangleCylinderZ(new_x1, new_x2, new_y1, new_y2, isClone=True)
        clone_rectangle.surf_left.id = self.__surf_left.id
        clone_rectangle.surf_right.id = self.__surf_right.id
        clone_rectangle.surf_top.id = self.__surf_top.id
        clone_rectangle.surf_bottom.id = self.__surf_bottom.id
        clone_rectangle.id = super().id

        return clone_rectangle
    
    def get_surface_for_detectors_serpent_syntax(self):
        serpent_syntax = f"surf {self.__surf_left.id} px 0.00000\n"
        serpent_syntax += f"surf {self.__surf_top.id} py {self. __height}\n"
        serpent_syntax += f"surf {self.__surf_right.id} px {self.__width}\n"
        serpent_syntax += f"surf {self.__surf_bottom.id} py 0.00000\n"


        return serpent_syntax
    
    @property
    def serpent_syntax_exact_position(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"rect {format(self.__x1, '.8f')} " 
        serpent_syntax += f"{format(self.__x2, '.8f')} "
        serpent_syntax += f"{format(self.__y1, '.8f')} "
        serpent_syntax += f"{format(self.__y2, '.8f')}\n"

        return serpent_syntax

    @property
    def serpent_syntax_standard_position(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"rect {format(self.__x1, '.8f')} " 
        serpent_syntax += f"{format(self.__x2, '.8f')} "
        serpent_syntax += f"{format(self.__y1, '.8f')} "
        serpent_syntax += f"{format(self.__y2, '.8f')}\n"
        return serpent_syntax

    @property
    def x1(self):
        return self.__x1

    @property
    def x2(self):
        return self.__x2
    
    @property
    def y1(self):
        return self.__y1
    
    @property
    def y2(self):
        return self.__y2
     
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
    def boundary(self):
        return self.__boundary

    @property
    def vertex_points(self):
        points = [
            (self.__x1, self.__y1),
            (self.__x1, self.__y2),
            (self.__x2, self.__y1),
            (self.__x2, self.__y2),
        ]

        return points

    @property
    def volume(self):
        return self.evaluate_enclosed_volume()
    
    @property
    def center(self):
        xc = (self.__x2 - self.__x1) / 2
        yc = (self.__y2 - self.__y1) / 2
        return (xc,yc)
    

class PlaneParametric(Surface):

    def __init__(self, x0, y0, z0, x1, y1, z1, x2, y2, z2, type_surface="", name="", isClone=False):
        super().__init__(type_surface, name, isClone)
        self.__x0 = x0
        self.__y0 = y0
        self.__z0 = z0
        self.__x1 = x1
        self.__y1 = y1
        self.__z1 = z1
        self.__x2 = x2
        self.__y2 = y2
        self.__z2 = z2
    
    def clone(self, clone_vector=None):
        # new_y0 = self.__y0
        # if clone_vector:
        #     new_y0 = self.__y0 + clone_vector[1]
        surf_clone = PlaneParametric(
            self.__x0, self.__y0, self.__z0, 
            self.__x1, self.__y1, self.__z1, 
            self.__x2, self.__y2, self.__z2, 
            isClone=True
        )
        surf_clone.id = super().id
        return surf_clone
        
    @property
    def serpent_syntax_exact_position(self):
        serpent_syntax = f"surf {self.id} plane "
        serpent_syntax += f"{format(self.__x0, '.8f')} {format(self.__y0, '.8f')} {format(self.__z0, '.8f')} "
        serpent_syntax += f"{format(self.__x1, '.8f')} {format(self.__y1, '.8f')} {format(self.__z1, '.8f')} "
        serpent_syntax += f"{format(self.__x2, '.8f')} {format(self.__y2, '.8f')} {format(self.__z2, '.8f')}\n"
        return serpent_syntax


class InfiniteCylinderZ(Surface):

    """
    Class for an Infinite Cylinder parallel to Z-axis

    Surface equation: S(x, y) =  (y - y0)**2 + (x - x0)**2 - r**2
    """

    def __init__(self, center_x, center_y, radius, name="", boundary=None, isClone=False):
        super().__init__(type_surface="cylinder_z", name=name, isClone=isClone)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius
        self.__isClone = isClone
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

    def scale(self, scale_f):
        self.__radius *= scale_f

    def clone(self, new_center_x, new_center_y, clone_vector=None):
        surf_clone = InfiniteCylinderZ(new_center_x, new_center_y, self.__radius, isClone=True)
        surf_clone.id = super().id
        return surf_clone

    def eval_point(self, x, y):
        return self.__function(x, y)

    def isPointNegativeSide(self, point):
        x, y = point
        try:
            assert self.eval_point(x, y) < 0
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
    def center_x(self):
        return self.__center_x
    
    @property
    def center_y(self):
        return self.__center_y
    

    @property
    def center(self):
        return (self.__center_x, self.__center_y)
    
    @property
    def volume(self):
        return self.evaluate_enclosed_volume()
    
    @center.setter
    def center(self, center):
        self.__center_x = center[0]
        self.__center_y = center[1]

    @property
    def radius(self):
        return self.__radius
    
    @property
    def serpent_syntax_exact_position(self):
        serpent_syntax = f"surf {self.id} " 
        serpent_syntax += f"cyl {format(self.__center_x, '.8f')} " 
        serpent_syntax += f"{format(self.__center_y, '.8f')} "
        serpent_syntax += f"{format(self.__radius, '.8f')}\n"
        return serpent_syntax

    @property
    def serpent_syntax_standard_position(self):
        serpent_syntax = f"surf {self.id} cyl 0.0000 0.0000 " 
        serpent_syntax += f"{format(self.__radius, '.8f')}\n"
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
       

class PieQuadrant(Surface):
    
    def __init__(self, circle, v_plane, h_plane, quadrant, boundary=None, name="", isClone=False):
        super().__init__(type_surface="pie_surface", name=name, isClone=isClone)
        self.__surf_circle = circle
        self.__surf_v_plane = v_plane
        self.__surf_h_plane = h_plane
        self.__quadrant = quadrant
        self.__boundary = boundary
        self.__isClone = isClone

    def clone(self, center_x, center_y, clone_vector=None):
        """
            It clones the surface: same id, but in a new center
        """
        center_x, center_y = self.__surf_circle.center
        clone_circle = self.__surf_circle.clone(center_x, center_y, clone_vector=clone_vector)
        clone_v_plane = self.__surf_v_plane.clone(clone_vector=clone_vector)
        clone_h_plane = self.__surf_h_plane.clone(clone_vector=clone_vector)

        clone_pie = PieQuadrant(clone_circle, clone_v_plane, clone_h_plane, self.__quadrant, isClone=True)
        clone_pie.surf_circle.id = self.__surf_circle.id
        clone_pie.surf_v_plane.id = self.__surf_v_plane.id
        clone_pie.surf_h_plane.id = self.__surf_h_plane.id
        clone_pie.id = super().id

        return clone_pie
    
    def get_surface_relation(self):
        return {
            self.__surf_circle.id: self.__surf_circle,
            self.__surf_v_plane.id: self.__surf_v_plane,
            self.__surf_h_plane.id: self.__surf_h_plane,
        }

    def get_surface_sides(self):
        if self.__quadrant == "top_left":
            return {
                self.__surf_circle.id:  -self.__surf_circle,
                self.__surf_v_plane.id: -self.__surf_v_plane,
                self.__surf_h_plane.id: +self.__surf_h_plane,
            }
        elif self.__quadrant == "top_right":
            return {
                self.__surf_circle.id: -self.__surf_circle,
                self.__surf_v_plane.id: +self.__surf_v_plane,
                self.__surf_h_plane.id: -self.__surf_h_plane,
            }
        elif self.__quadrant == "bottom_right":
            return {
                self.__surf_circle.id: -self.__surf_circle,
                self.__surf_v_plane.id: -self.__surf_v_plane,
                self.__surf_h_plane.id: +self.__surf_h_plane,
            }
        elif self.__quadrant == "bottom_left":
            return {
                self.__surf_circle.id: -self.__surf_circle,
                self.__surf_v_plane.id: +self.__surf_v_plane,
                self.__surf_h_plane.id: -self.__surf_h_plane,
            }
        else:
            return {}
        

    def get_neutron_current_directions(self):
        if self.__quadrant == "top_left":
            return {
                self.__surf_circle.id: {"inward": "-1", "outward": "1"},
                self.__surf_v_plane.id: {"inward": "-1", "outward": "1"},
                self.__surf_h_plane.id: {"inward": "1", "outward": "-1"},
            }
        elif self.__quadrant == "top_right":
            return {
                self.__surf_circle.id: {"inward": "-1", "outward": "1"},
                self.__surf_v_plane.id: {"inward": "1", "outward": "-1"},
                self.__surf_h_plane.id: {"inward": "-1", "outward": "1"},
            }
        elif self.__quadrant == "bottom_right":
            return {
                self.__surf_circle.id: {"inward": "-1", "outward": "1"},
                self.__surf_v_plane.id: {"inward": "-1", "outward": "1"},
                self.__surf_h_plane.id: {"inward": "1", "outward": "-1"},
            }
        elif self.__quadrant == "bottom_left":
            return {
                self.__surf_circle.id: {"inward": "-1", "outward": "1"},
                self.__surf_v_plane.id: {"inward": "1", "outward": "-1"},
                self.__surf_h_plane.id: {"inward": "-1", "outward": "1"},
            }
        else:
            return {}


    @property
    def serpent_syntax_exact_position(self):
        serpent_syntax = f"surf {self.__surf_circle.id} cyl {format(self.__surf_circle.center_x, '.8f')} " 
        serpent_syntax += f"{format(self.__surf_circle.center_y, '.8f')} "
        serpent_syntax += f"{format(self.__surf_circle.radius, '.8f')}\n" 
        serpent_syntax += self.__surf_v_plane.serpent_syntax_exact_position()
        serpent_syntax += self.__surf_h_plane.serpent_syntax_exact_position()
        return serpent_syntax


    @property
    def center_x(self):
        return self.__center_x
    
    @property
    def center_y(self):
        return self.__center_y
    
    @property
    def center(self):
        return (self.__center_x, self.__center_y)
    
    @center.setter
    def center(self, center):
        self.__center_x = center[0]
        self.__center_y = center[1]

    @property
    def quadrant(self):
        return self.__quadrant

    @property
    def surf_circle(self):
        return self.__surf_circle

    @property
    def surf_v_plane(self):
        return self.__surf_v_plane

    @property
    def surf_h_plane(self):
        return self.__surf_h_plane

    @property
    def boundary(self):
        return self.__boundary


class CylinderPad(Surface):
    
    def __init__(self, x0, y0, r1, r2, th1, th2, boundary=None, name="", isClone=False):
        super().__init__(type_surface="pie_surface", name=name, isClone=isClone)
        self.__x0 = x0
        self.__y0 = y0
        self.__r1 = r1
        self.__r2 = r2
        self.__th1 = th1
        self.__th2 = th2

        self.__boundary = boundary
        self.__isClone = isClone

        self.volume = self.__calculateVolume()

    def __calculateVolume(self):
        vol_inner_circle = math.pi * self.__r1 * self.__r1
        vol_outer_circle = math.pi * self.__r2 * self.__r2

        angle_piece = self.__th2 - self.__th1
        volume_factor = angle_piece / 360

        return (vol_outer_circle - vol_inner_circle) * volume_factor

    def clone(self, center_x, center_y, clone_vector=None):
        """
            It clones the surface: same id, same radius, same angles but in a new center
        """
    
        clone_pad = CylinderPad(
            self.__x0, self.__y0, self.__r1, self.__r2, self.__th1, self.__th2,
            isClone=True
        )
        
        clone_pad.id = super().id

        
        return clone_pad
    


    @property
    def serpent_syntax_exact_position(self):
        serpent_syntax = f"surf {self.id} pad "
        serpent_syntax += f"{format(self.__x0, '.8f')} {format(self.__y0, '.8f')} " 
        serpent_syntax += f"{format(self.__r1, '.8f')} {format(self.__r2, '.8f')} " 
        serpent_syntax += f"{format(self.__th1, '.8f')} {format(self.__th2, '.8f')}\n" 
        return serpent_syntax

    @property
    def serpent_syntax_standard_position(self):
        serpent_syntax = f"surf {self.id} pad "
        serpent_syntax += f"0.0000 0.0000 " 
        serpent_syntax += f"{format(self.__r1, '.8f')} {format(self.__r2, '.8f')} " 
        serpent_syntax += f"{format(self.__th1, '.8f')} {format(self.__th2, '.8f')}\n" 
        return serpent_syntax


    @property
    def center_x(self):
        return self.__center_x
    
    @property
    def center_y(self):
        return self.__center_y
    
    @property
    def center(self):
        return (self.__center_x, self.__center_y)
    
    @property
    def boundary(self):
        return self.__boundary


class Hexagon(Surface):

    def __init__(self, type_surface="", name="", isClone=False):
        super().__init__(type_surface, name, isClone=isClone)


class InfiniteHexagonalCylinderXtype(Hexagon):
    """
        surf_A   --> cell in - side
        surf_B   --> cell in - side
        surf_C   --> cell in + side
        surf_D   --> cell in + side
        surf_E   --> cell in + side
        surf_F   --> cell in - side
    """

    def __init__(self, center_x, center_y, half_width, name="", boundary=None, isClone=False):
        super().__init__(name=name, type_surface="inf hex_x", isClone=isClone)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__boundary = boundary
        self.__isClone = isClone

        self.__radius = round(2 * self.__half_width / math.sqrt(3),8)
        self.__side = self.__radius
        self.__surf_A, self.__surf_B, self.__surf_C, self.__surf_D, self.__surf_E, self.__surf_F = self.__generate_surfaces()

    def __generate_surfaces(self):
        """
            To rotate the plane-Y we consider the rotation of a vector with unitary length
            pointing in the positive x-direction
        
        """
        hw = self.__half_width
        rot_ref_transformation_x = round(hw - (2*hw*hw/self.__radius - hw),8)

        rot_ref_A = (self.__center_x + rot_ref_transformation_x, self.__center_y + self.__radius)
        rot_ref_C = (self.__center_x + rot_ref_transformation_x, self.__center_y - self.__radius)
        rot_ref_D = (self.__center_x - rot_ref_transformation_x, self.__center_y - self.__radius)
        rot_ref_F = (self.__center_x - rot_ref_transformation_x, self.__center_y + self.__radius)

        _A = PlaneY(round(self.__center_y + hw,8), boundary=self.__boundary, isClone=self.__isClone)
        _B = PlaneX(round(self.__center_x + hw,8), boundary=self.__boundary, isClone=self.__isClone)
        _C = PlaneY(round(self.__center_y - hw,8), boundary=self.__boundary, isClone=self.__isClone)
        _D = PlaneY(round(self.__center_y - hw,8), boundary=self.__boundary, isClone=self.__isClone)
        _E = PlaneX(round(self.__center_x - hw,8), boundary=self.__boundary, isClone=self.__isClone)
        _F = PlaneY(round(self.__center_y + hw,8), boundary=self.__boundary, isClone=self.__isClone)
        _A.rotate(-30, rot_ref_A)
        _C.rotate(+30, rot_ref_C)
        _D.rotate(-30, rot_ref_D)
        _F.rotate(+30, rot_ref_F)
        
        surfaces = [_A, _B, _C, _D, _E, _F ]

        return surfaces
    
    def clone(self, center_x, center_y, clone_vector=None):
        """
            It clones the surface: same id, but in a new center
        """
        clone_hexagon = InfiniteHexagonalCylinderXtype(center_x, center_y, self.__half_width, boundary=self.__boundary, isClone=True)
        clone_hexagon.surf_A.id = self.__surf_A.id
        clone_hexagon.surf_B.id = self.__surf_B.id
        clone_hexagon.surf_C.id = self.__surf_C.id
        clone_hexagon.surf_D.id = self.__surf_D.id
        clone_hexagon.surf_E.id = self.__surf_E.id
        clone_hexagon.surf_F.id = self.__surf_F.id
        clone_hexagon.id = super().id

        return clone_hexagon

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
    
    def scale(self, scale_f):
        new_half_width = self.__half_width * scale_f
        plane_move = new_half_width - self.__half_width

        self.__surf_A.translate((plane_move,plane_move))
        self.__surf_B.translate((plane_move,0))
        self.__surf_C.translate((plane_move,-plane_move))
        self.__surf_D.translate((-plane_move,-plane_move))
        self.__surf_E.translate((-plane_move,0))
        self.__surf_F.translate((-plane_move,plane_move))

        self.__half_width = new_half_width
        self.__radius *= scale_f


    def isPointNegativeSide(self, point):
        x, y = point
        try:
            assert self.__surf_A.isPointNegativeSide(point)
            assert self.__surf_B.isPointNegativeSide(point)
            assert self.__surf_C.isPointPositiveSide(point)
            assert self.__surf_D.isPointPositiveSide(point)
            assert self.__surf_E.isPointPositiveSide(point)
            assert self.__surf_F.isPointNegativeSide(point)
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
            (self.__center_x, self.__center_y + self.__radius),         # vertex F - A
            (self.__center_x+self.__half_width, self.__center_y + 0.5*self.__radius),    # vertex A - B
            (self.__center_x+self.__half_width, self.__center_y - 0.5*self.__radius),    # vertex B - C
            (self.__center_x, self.__center_y - self.__radius),         # vertex C - D
            (self.__center_x-self.__half_width, self.__center_y - 0.5*self.__radius),    # vertex D - E
            (self.__center_x-self.__half_width, self.__center_y + 0.5*self.__radius),    # vertex E - F    
        ]        
        return points

    def get_side_middle_points(self):
        sx = round(0.5 * self.__half_width,8)
        sy = round(math.cos(math.radians(30)) * self.__half_width,8)
        points = [
            (self.__center_x + sx, self.__center_y + sy),   # A
            (self.__surf_B.x0, self.__center_y),            # B
            (self.__center_x + sx, self.__center_y - sy),   # C
            (self.__center_x - sx, self.__center_y - sy),   # D
            (self.__surf_E.x0, self.__center_y),            # E
            (self.__center_x - sx, self.__center_y + sy),   # F
        ]

        return points

    @property
    def serpent_syntax_exact_position(self):
        serp_syn = f"surf {self.id} hexxc {format(self.__center_x, '.8f')} "
        serp_syn += f" {format(self.__center_y, '.8f')} {format(self.__half_width, '.8f')}\n"
        return serp_syn
    

    @property
    def serpent_syntax_standard_position(self):
        return f"surf {self.id} hexxc {0.0000} {0.0000} {format(self.__half_width, '.8f')}\n"

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
    def half_width(self):
        return self.__half_width

    @property
    def center_x(self):
        return self.__center_x
    
    @property
    def center_y(self):
        return self.__center_y
    

    @property
    def center(self):
        return (self.__center_x, self.__center_y)
    
    @center.setter
    def center(self, point):
        self.__center_x = point[0]
        self.__center_y = point[1]
    
    @property
    def vertex_points(self):
        return self.get_vertex_points()


class InfiniteHexagonalCylinderYtype(Hexagon):
    """
    
        surf_A   --> cell in - side
        surf_B   --> cell in - side
        surf_C   --> cell in - side
        surf_D   --> cell in + side
        surf_E   --> cell in + side
        surf_F   --> cell in + side

    """

    def __init__(self, center_x, center_y, half_width, name="", boundary=None, isClone=False):
        super().__init__(name=name, type_surface="inf hex_x", isClone=isClone)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__boundary = boundary
        self.__isClone = isClone

        # self.__side = 2 * self.__half_width * math.tan(math.radians(30))
        self.__radius = 2 * self.__half_width / math.sqrt(3)
        self.__side = self.__radius
        # self.__radius = self.__half_width * math.sqrt(5) / 2
        self.__surf_A, self.__surf_B, self.__surf_C, self.__surf_D, self.__surf_E, self.__surf_F = self.__generate_surfaces()

    def __generate_surfaces(self):
        """
            To rotate the plane-Y we consider the rotation of a vector with unitary length
            pointing in the positive x-direction
        
        """
        rot_ref_B = (self.__center_x + self.__radius, self.__center_y)
        rot_ref_C = (self.__center_x + self.__radius, self.__center_y)
        rot_ref_E = (self.__center_x - self.__radius, self.__center_y)
        rot_ref_F = (self.__center_x - self.__radius, self.__center_y)

        _A = PlaneY(self.__center_y + self.__half_width, boundary=self.__boundary, isClone=self.__isClone)
        _B = PlaneX(self.__center_x + self.__radius, boundary=self.__boundary, isClone=self.__isClone)
        _C = PlaneX(self.__center_x + self.__radius, boundary=self.__boundary, isClone=self.__isClone)
        _D = PlaneY(self.__center_y - self.__half_width, boundary=self.__boundary, isClone=self.__isClone)
        _E = PlaneX(self.__center_x - self.__radius, boundary=self.__boundary, isClone=self.__isClone)
        _F = PlaneX(self.__center_x - self.__radius, boundary=self.__boundary, isClone=self.__isClone)

        _B.rotate(+30, rot_ref_B)
        _C.rotate(-30, rot_ref_C)
        _E.rotate(+30, rot_ref_E)
        _F.rotate(-30, rot_ref_F)
        
        surfaces = [_A, _B, _C, _D, _E, _F ]

        return surfaces
    
    def clone(self, center_x, center_y, clone_vector=None):
        """
            It clones the surface: same id, but in a new center
        """
        clone_hexagon = InfiniteHexagonalCylinderYtype(center_x, center_y, self.__half_width, boundary=self.__boundary, isClone=True)
        clone_hexagon.surf_A.id = self.__surf_A.id
        clone_hexagon.surf_B.id = self.__surf_B.id
        clone_hexagon.surf_C.id = self.__surf_C.id
        clone_hexagon.surf_D.id = self.__surf_D.id
        clone_hexagon.surf_E.id = self.__surf_E.id
        clone_hexagon.surf_F.id = self.__surf_F.id
        clone_hexagon.id = super().id

        return clone_hexagon

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
    
    def scale(self, scale_f):
        new_half_width = self.__half_width * scale_f
        plane_move = new_half_width - self.__half_width

        self.__surf_A.translate((0,plane_move))
        self.__surf_B.translate((plane_move,plane_move))
        self.__surf_C.translate((plane_move,-plane_move))
        self.__surf_D.translate((0,-plane_move))
        self.__surf_E.translate((-plane_move,-plane_move))
        self.__surf_F.translate((-plane_move,plane_move))

        self.__half_width = new_half_width
        self.__radius *= scale_f

    def isPointNegativeSide(self, point):
        x, y = point
        try:
            assert self.__surf_A.isPointNegativeSide(point)
            assert self.__surf_B.isPointNegativeSide(point)
            assert self.__surf_C.isPointNegativeSide(point)
            assert self.__surf_D.isPointPositiveSide(point)
            assert self.__surf_E.isPointPositiveSide(point)
            assert self.__surf_F.isPointPositiveSide(point)
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
            (self.__center_x - 0.5*self.__radius, self.__surf_A.y0),    # vertex F - A    
            (self.__center_x + 0.5*self.__radius, self.__surf_A.y0),    # vertex A - B
            (self.__center_x + self.__radius, self.__center_y),         # vertex B - C
            (self.__center_x + 0.5*self.__radius, self.__surf_D.y0),    # vertex C - D
            (self.__center_x - 0.5*self.__radius, self.__surf_D.y0),    # vertex D - E
            (self.__center_x - self.__radius, self.__center_y),         # vertex E - F
        ]        
        return points

    def get_side_middle_points(self):
        sx = round((math.cos(math.radians(30)) * self.__half_width),8)
        sy = round(0.5 * self.__half_width,8)
        points = [
            (self.__center_x, self.__surf_A.y0),            # A
            (self.__center_x + sx, self.__center_y + sy),   # B
            (self.__center_x + sx, self.__center_y - sy),   # C
            (self.__center_x, self.__surf_D.y0),            # D
            (self.__center_x - sx, self.__center_y - sy),   # E
            (self.__center_x - sx, self.__center_y + sy),   # F
        ]
        return points

    def get_x_coord_in_line_y(self, y0):
        """
            
            Returns a the x-coordinates x1 & x2
            of a y_line crossing the hexagon

        """
    
        if y0 <= self.__center_y:
            surf_f_point = round(self.__surf_F.useFunction(y0),8)
            surf_b_point = round(self.__surf_B.useFunction(y0),8)
            return surf_f_point, surf_b_point
        elif y0 > self.__center_y:
            surf_e_point = round(self.__surf_E.useFunction(y0),8)
            surf_c_point = round(self.__surf_C.useFunction(y0),8)
            return surf_e_point, surf_c_point
        pass

    @property
    def serpent_syntax_exact_position(self):
        return f"surf {self.id} hexyc {self.__center_x} {self.__center_y} {self.__half_width}\n"

    @property
    def serpent_syntax_standard_position(self):
        return f"surf {self.id} hexyc {0.0000} {0.0000} {self.__half_width}\n"

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
    def half_width(self):
        return self.__half_width

    @property
    def vertex_points(self):
        return self.get_vertex_points()

    @property
    def center(self):
        return self.__center_x, self.__center_y
    
    @center.setter
    def center(self, point):
        self.__center_x = point[0]
        self.__center_y = point[1]


    @property
    def center_x(self):
        return self.__center_x

    @property
    def center_y(self):
        return self.__center_y
    

def reset_surface_counter():
    surf_ids = []
    return 0
        