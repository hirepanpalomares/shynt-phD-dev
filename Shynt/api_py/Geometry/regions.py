

class Region:
    """ Class used to represent the euclidean space generated
    by the intersection of two SurfaceSides.

    The Region is respresented as a binary tree having as childs
    two different SurfaceSide classes and boolean operation as 
    atribute

    Parameters
    -----------------
    child1      :   Child SurfaceSide of the binary tree
    child2      :   Child SurfaceSide of the binary tree
    operation   :   Atribute of the root of the binary tree, is the
                    boolean operation involving the 2 childs
    -----------------
    # TODO: -------------------------------------------------------
    # TODO:     Implement the case when the two childs are already
    # TODO:     region instances
    # TODO: -------------------------------------------------------
    # TODO:     Implement A or B ----> Boolean union  __or__
    # TODO: -------------------------------------------------------
    # TODO:     Implement A xor B ----> Boolean opposite to or __xor__
    # TODO:     (Might not be used in reactor physics)
    # TODO: -------------------------------------------------------
    # TODO:     Implement A - B ----> Boolean negation


    """
    def __init__(self, child1, child2, operation):
        self.__child1 = child1
        self.__child2 = child2
        self.__operation = operation
    


    def __str__(self):
        return "Region class"

    def __and__(self, other):
        """Class method to add to create the intersection of two Regions

        Parameters
        ----------
        self    :   Region type
        other   :   Region type
        ----------
        # TODO: Implement when the two instances are already regions
        """
        pass
    
    @property
    def child1(self):
        return self.__child1
    
    @property
    def child2(self):
        return self.__child2

    @property
    def operation(self):
        return self.__operation
    

class SurfaceSide():

    def __init__(self, surface, side):
        self.surface = surface
        self.side = side

        #print(f'Surface side: {side}')
        #print(surface)
    

    def __and__(self, other):
        """Class overloading operator __and__

        This overwrites the parent class method so it performs the
        sum of two SurfaceSide classes.

        It returns an instance of the Region Class by merging the euclidean
        space between the two instances 'self' and 'other'

        Parameters
        ---------------------------------------------------------------
        self        :   It is an instance of the class SurfaceSide
        other       :   It is an instance of the class SurfaceSide
        ---------------------------------------------------------------
        
        
        
        """
        
        return Region(self, other, operation="and")
    
    def __str__(self):
        return_string = """
        Surface side:  (%s)
        Surface: 
        %s
        """%(self.side, self.surface)
        return return_string


