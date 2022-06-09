



class Region:
    """ Class used to represent the euclidean space generated
    by the intersection of two SurfaceSides.

    The Region is respresented as a binary tree having as childs
    two different SurfaceSide classes and boolean operation as 
    atribute

    Parameters
    -----------------
    child1      :   Child SurfaceSide or Region of the binary tree
    child2      :   Child SurfaceSide or Region of the binary tree
    operation   :   Atribute of the root of the binary tree, is the
                    boolean operation involving the 2 childs
    -----------------
    #TODO:     Implement the case when the two childs are already region instances
    #TODO:     Implement A or B ----> Boolean union  __or__
    #TODO:     Implement A xor B ----> Boolean opposite to or __xor__ (Might not be used in reactor physics)
    #TODO:     Implement A - B ----> Boolean negation


    """
    def __init__(self, child1=None, child2=None, operation=""):
        self.child1 = child1
        self.child2 = child2
        self.__operation = operation
        """
            Checar los child?? yes/no
        """
    


    # def __str__(self):
    #     print_statement = "Region between two surfaces or two regions \n"
    #     print_statement += f"{self.child1}\n"
    #     print_statement += f"{self.child2}\n"
    #     return print_statement

    def __and__(self, other):
        """Class method to add to create the intersection of two Regions

        Parameters
        ----------
        self    :   Region type
        other   :   Region type
        ----------
        
        """
        return Region(child1=self, child2=other, operation="and")

    def __neg__(self):
        pass
    
    def __pos__(self):
        pass

    def invert(self):
        """
            Method to invert the region
        """
        surface_sides = self.destructure_region()
        new_surface_sides = []
        for ss in surface_sides:
            side = ss.side
            new_side = "-"
            if side == "-":
                new_side = "+"
            new_surface_sides.append(SurfaceSide(ss.surface, new_side))
        
        inverted = new_surface_sides[0]
        for ss in range(1, len(new_surface_sides)):
            inverted &= new_surface_sides[ss]
        
        return inverted
        
    def clone(self, new_center_x, new_center_y):
        try: 
            assert isinstance(self.child1, SurfaceSide)
            assert isinstance(self.child2, SurfaceSide)
            child1_clone = self.child1.clone(new_center_x, new_center_y)
            child2_clone = self.child2.clone(new_center_x, new_center_y)
            return child1_clone & child2_clone
        except AssertionError:
            raise SystemError

    def destructure_region(self, surfaces_sides={}):
        """
            Recursive function to destructurate a region in its surfaces sides

            returns:
                Array(<SurfaceSide class>)
        """
        if isinstance(self, SurfaceSide):
            # Base case
            surfaces_sides.update({
                self.surface.id: self
            })

            return surfaces_sides
        elif isinstance(self, Region):
            surfaces_sides.update(self.child1.destructure_region({}))
            surfaces_sides.update(self.child2.destructure_region({}))
            return surfaces_sides

    def translate(self, trans_vector):
        self.child1.translate(trans_vector)
        self.child2.translate(trans_vector)
        
    def surfaces_of_region(self, surfaces={}):
        if isinstance(self, SurfaceSide):
            # base case
            surf = self.surface
            surfaces.update({
                surf.id: surf
            })
            return surfaces
        elif isinstance(self, Region):
            reg1 = self.child1
            reg2 = self.child2
            new_surf_reg1 = reg1.surfaces_of_region(surfaces=surfaces) 
            surfaces.update(new_surf_reg1)
            new_surf_reg2 = reg2.surfaces_of_region(surfaces=surfaces)
            surfaces.update(new_surf_reg2)
            return surfaces

    def serpent_syntax(self):
        """
            It returns the region using serpent syntax for boolean geometry:

            If the region is comprised between the outside of a cylinder->id=2 and 
            the inside of a square->id=3 it will return the following:

            return: "2 -3"
        """
        syntax = ""
        side = lambda s: s if s == "-" else ""
        # # For the regions:
        # if isinstance(self, SurfaceSide):
        #     syntax += f" {side(self.side)}{self.surface.id}"
        # elif isinstance(self, Region):
        #     # find the surfaces sides of the Region
        #     surfaces_sides = self.destructure_region()
        #     for s_id, surf_side in surfaces_sides.items():
        #         syntax += f" {side(surf_side.side)}{surf_side.surface.id}"
        # syntax += ""
        surface_sides = self.destructure_region({})
        for s_id, ss in surface_sides.items():
            syntax += f" {side(ss.side)}{s_id} "
        return syntax


    @property
    def operation(self):
        return self.__operation
    

class SurfaceSide(Region):

    def __init__(self, surface, side):
        self.surface = surface
        self.side = side

    def clone(self, new_center_x, new_center_y):
        surface_clone = self.surface.clone(new_center_x, new_center_y)
        if self.side == "-":
            return -surface_clone
        elif self.side == "+":
            return +surface_clone
        else:
            raise SystemError

    def __and__(self, other):
        """
        Class overloading operator __and__

        This overwrites the parent class method so it performs the
        boolean addition between two SurfaceSide classes.

        It returns an instance of the Region Class by merging the euclidean
        space between the two instances 'self' and 'other'

        Parameters
        ---------------------------------------------------------------
        self        :   It is an instance of the class SurfaceSide
        other       :   It is an instance of the class SurfaceSide
        ---------------------------------------------------------------
        
        
        
        """
        
        return Region(self, other, operation="and")
    
    def encloses(self, other):
        others_vertex = other.surface.vertex_points
        for point in others_vertex:
            if not self.surface.isPointNegativeSide(point):
                return False
        return True
    
    def translate(self, trans_vector):
        self.surface.translate(trans_vector)
        
