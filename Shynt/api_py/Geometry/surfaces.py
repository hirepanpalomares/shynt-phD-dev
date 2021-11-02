from Shynt.api_py.Geometry.regions import SurfaceSide
import os

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
        self.__id = None
        
        self.serpent_syntax = ""
        self.calculateId()
    
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
        try:
            id = None
            with open("id-counter", "r") as fileCounter:
                for line in fileCounter:
                    id = int(line.split()[0]) + 1
                    self.__id = id
                    break
            with open("id-counter", "w") as fileCounter:
                fileCounter.write(str(id))
            
        except FileNotFoundError:
            self.__id = 1
            with open("id-counter", "w") as fileCounter:
                fileCounter.write("1")
    
    
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
        
        self.serpent_syntax = f"surf {self.id} px {x0}\n"

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
        self.serpent_syntax = f"surf {self.id} py {y0}\n"


    def eval_point(self, y):
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
        self.serpent_syntax = f"surf {self.id} pz {z0}\n"


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
        self.serpent_syntax = f"surf {self.id} cyl {center_x} {center_y} {radius}\n"
        
    def translate(self, dx, dy):
        self.__center_x += dx
        self.__center_y += dy

    def eval_point(self, x, y):
        return self.__function(x, y)

    def is_point(self, x, y):
        return self.eval_point(x, y) < 0

    def __str__(self):    
        return """infinite cylinder:
            - name: %s
            - id: %s
            - radius: %s
        """%(self.name, self.id, self.__radius)
    
    @property
    def center(self):
        return (self.__center_x, self.__center_y)
    
    @property
    def radius(self):
        return self.__radius
    

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
        self.boundary = boundary
        self.__center_x = center_x
        self.__center_y = center_y
        self.__half_width = half_width
        self.__surf_left, self.__surf_right, self.__surf_bottom, self.__surf_top = self.__generate_surfaces()
        self.boundary
        self.serpent_syntax = f"surf {self.id} sqc {center_x} {center_y} {half_width}\n"

        
    def __generate_surfaces(self):
        surfaces = [
            PlaneX(self.__center_x - self.__half_width, self.boundary),
            PlaneX(self.__center_x + self.__half_width, self.boundary),
            PlaneY(self.__center_y - self.__half_width, self.boundary),
            PlaneY(self.__center_y + self.__half_width, self.boundary)
        ]
        return surfaces

    def eval_point(self, x, y):
        return x > self.__surf_left.x0 and x < self.__surf_right.x0 and y > self.__surf_bottom.y0 and y < self.__surf_top.x0

    def __str__(self):    
        return """Surface of infinite square cylinder in z-axis:
            - name: %s
            - center (x,y): (%s,%s)
            - half width: %s
            - width: %s
        """%(self.name, self.__center_x, self.__center_y, self.__half_width, 2*self.__half_width)


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
    

class HexagonalCylinderX(Surface):

    def __init__(self, center_x, center_y, half_width, name="", boundary=None):
        super()._init__(name, type_surf="inf hex_x")


class HexagonalCylinderY(Surface):

    def __init__(self, center_x, center_y, half_width, name="", boundary=None):
        super()._init__(name, type_surf="inf hex_y")
        self.serpent_syntax = f"surf {self.id} hexyc {center_x} {center_y} {half_width}\n"






def reset_surface_counter():
    try:
        os.remove("id-counter")
    except FileNotFoundError:
        pass