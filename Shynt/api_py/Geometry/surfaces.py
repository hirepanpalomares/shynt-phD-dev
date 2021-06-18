import os

class Surface:

    def __init__(self, name, type_surface):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :       String to name the surface
            id          :       Integer numering the surface
            ----------------------------------------------------------------
        """
        
        self._name = name
        self._type = type_surface
        self._id = None
        self.calculateId()
    
    def calculateId(self):
        try:
            id = None
            with open("id-counter", "r") as fileCounter:
                for line in fileCounter:
                    id = int(line.split()[0]) + 1
                    self._id = id
                    break
            with open("id-counter", "w") as fileCounter:
                fileCounter.write(str(id))
            
        except FileNotFoundError:
            self._id = 0
            with open("id-counter", "w") as fileCounter:
                fileCounter.write("0")
    
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def surface_type(self):
        return self._type

    @name.setter
    def id(self, id):
        self._id = id
            
    def __neg__(self):
        return SurfaceSide(self, "-")

    def __pos__(self):
        return SurfaceSide(self, "+")


class InfiniteCylinder(Surface):

    def __init__(self, name, center_x, center_y, radius, orientation="z"):
        super().__init__(name, type_surface="cylinder_%s"%orientation)
        self._center_x = center_x
        self._center_y = center_y
        self._radius = radius
        self._orientation = orientation
    
    def __str__(self):    
        return """
        Surface of infinite cylinder:
            - name: %s
            - id: %s
            - radius: %s
        """%(self._name, self._id, self._radius)
    
    @property
    def center_x(self):
        return self._center_x
    
    @property
    def center_y(self):
        return self._center_y
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def orientation(self):
        return self._orientation
    


class SquareCylinder(Surface):

    def __init__(self, name, center_x, center_y, half_width, orientation="z"):
        super()._init__(name, type_surf="square cylinder")
        self._center_x = center_x
        self._center_y = center_y
        self._half_width= half_width
        self._orientation = orientation
    
    def __str__(self):    
        return """
        Surface of infinite square cylinder:
            - name: %s
            - center (x,y): (%s,%s)
            - half width: %s
            - width: %s
        """%(self._name, self._center_x, self._center_y, self._half_width, 2*self._half_width)

    @property
    def center_x(self):
        return self._center_x
    
    @property
    def center_y(self):
        return self._center_y
    
    @property
    def half_width(self):
        return self._half_width
    
    @property
    def orientation(self):
        return self._orientation


class HexagonalCylinderX(Surface):

    def __init__(self, name, half_width):
        super()._init__(name, type_surf="inf hex_x")


class HexagonalCylinderY(Surface):

    def __init__(self, name, half_width):
        super()._init__(name, type_surf="inf hex_y")


class SurfaceSide():

    def __init__(self, surface, side):
        self.surface = surface
        self.side = side

        print(surface)
        print(side)






def reset_surface_counter():
    try:
        os.remove("id-counter")
    except FileNotFoundError:
        pass