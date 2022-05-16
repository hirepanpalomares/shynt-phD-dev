

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
        return Region(self, other, operation="and")

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
        

    def destructure_region(self, surfaces_sides=[]):
        """
            Recursive function to destructurate a region in its surfaces sides

            returns:
                Array(<SurfaceSide class>)
            #TODO Complete this function such that it is a method of the class
        """
        if isinstance(self, SurfaceSide):
            # Base case
            if self not in surfaces_sides:
                surfaces_sides.append(self)
            return surfaces_sides
        elif isinstance(self, Region):
            surfaces_sides = destructure_region(self.child1, surfaces_sides)
            surfaces_sides =  destructure_region(self.child2, surfaces_sides)
        
            return surfaces_sides

    def translate(self, trans_vector):
        self.child1.translate(trans_vector)
        self.child2.translate(trans_vector)
        
    

    @property
    def operation(self):
        return self.__operation
    

class SurfaceSide(Region):

    def __init__(self, surface, side):
        self.surface = surface
        self.side = side

        #print(f'Surface side: {side}')
        #print(surface)
    

    def __and__(self, other):
        """Class overloading operator __and__

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
    
    # def __str__(self):
    #     # return_string = """
    #     # # Surface side:  (%s)
    #     # # Surface: 
    #     # # %s
    #     # # """%(self.side, self.surface)
    #     # return return_string
    #     return ""
    
    def encloses(self, other):
        others_vertex = other.surface.vertex_points
        for point in others_vertex:
            if not self.surface.is_point(point):
                return False
        return True
    
    def translate(self, trans_vector):
        self.surface.translate(trans_vector)
        
    
    # @property
    # def child1(self):
    #     return self.child1
    
    # @property
    # def child2(self):
    #     return self.child2


def destructure_region(region, surfaces_sides=[]):
    """
    Recursive function to destructurate a region in its surfaces sides

    returns:
        Array(<SurfaceSide class>)
    """
    if isinstance(region, SurfaceSide):
        # Base case
        if region not in surfaces_sides:
            surfaces_sides.append(region)
        return surfaces_sides
    elif isinstance(region, Region):
        surfaces_sides = destructure_region(region.child1, surfaces_sides)
        surfaces_sides =  destructure_region(region.child2, surfaces_sides)
    
        return surfaces_sides


