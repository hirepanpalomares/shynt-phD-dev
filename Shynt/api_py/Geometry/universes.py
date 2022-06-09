
from Shynt.api_py.Geometry.regions import Region
from collections import namedtuple

from Shynt.api_py.Geometry.utilities_geometry import get_all_surfaces_in_a_cell, get_all_surfaces_in_a_universe
from Shynt.api_py.Geometry.utilities_geometry import declaring_pin_by_cells

from .surfaces import *
from Shynt.api_py.materials import Material

from Shynt.api_py.Geometry import surfaces



class Universe(object):
    """
        Universe class
    """
    def __init__(self, name="") :
        self.__name = name
        self.__cells = {}        
    
    def mark_cells(self):
        for id_, cell in self.__cells.items():
            cell.universe = self.__name

    def add_cell(self, cell):
        self.__cells[cell.id] = cell
    
    def translate(self, trans_vector):
        surfaces_universe = get_all_surfaces_in_a_universe(self)
        for id_, surf in surfaces_universe.items():
            surf.translate(trans_vector)
            
    def __eq__(self, __o: object) -> bool:
        """
            Comparaison of a universe:

            1.- It compares first the number of cells
            2.- It compares each of the cells

            Criteria:
            For a universe to be equal:
            1. Number of cells should be the same
            2. Each cell has to be equal to at least one of the cells in "__o" param
        """
        try:
            assert isinstance(__o, Universe)
            assert len(self.__cells) == len(__o.cells)
            compare_ = {c_id:False for c_id in self.__cells.keys()}
            for c_id, cell in self.__cells.items():
                for cell_other in __o.cells.values():
                    if cell == cell_other:
                        compare_[c_id] = True
            for key_, hasEqual in compare_.items():
                assert(hasEqual)
            return True
        except AssertionError:
            return False

    
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        for cell in self.cells.values():
            cell.universe = name

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, new_cells):
        self.__cells = new_cells


class Root(Universe):

    def __init__(self, model, outside, energy_grid=None, mcparams=None, libraries=""):
        super().__init__(name="0")
        self.add_cell(model)
        self.add_cell(outside)
        self.model_cell = model
        self.outside_cell = outside
        self.energy_grid = energy_grid  # Grid type
        self.mcparams = mcparams        # MontecarloParams type
        self.libraries = libraries      # Libraries for Serpent
        self.add_universe_to_cells()
    
    def add_universe_to_cells(self):
        for cell in self.cells.values():
            cell.universe = self.name


class Pin(Universe):

    """
        Pin universe composed by concentric cylinders and
        its respective materials

    """
    def __init__(self, name=""):#material=None, radius=None, surroundings=None):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :   A string with the name of the pin universe

            material    :   An object or a list of objects of class Meterial 
                            corresponding to the cylinder levels of the pincell
                            in case of provided
            
            radius      :   An number or a lis of numbers corresponding to the 
                            radius of the  levels of the fuel pin universe.
            ----------------------------------------------------------------
        """
        super().__init__(name)
        self.__pin_levels = [] # These are the cells of the universe Pin
        self.__clone = False
        self.__outer_most_surface = None
        self.__last_region = None
        # self.__check_init_levels(material, radius, surroundings)
        
    def __check_init_levels(self, mat, radius, surroundings):
        """
            Checks the first material and radius given to the pin

            --------------------------------------------------------

            It has a bug: generates more cells than expected

            cancelled on May 27 2022

            If restored fix the bug!!!!
        """
        if mat and radius: # both are not None
            # single level is declared
            if isinstance(mat, Material) and (isinstance(radius, float) or isinstance(radius, int)):
                # a single level is declared
                self.add_level(mat, radius)
                if surroundings:
                    self.add_level(surroundings)
            else:
                try:
                    assert(isinstance(mat, list) and isinstance(radius, list))
                    if len(mat) != len(radius):
                        print(f"*** Error while difining either materials or radius for pin '{self.name}'")
                        print("material and radius arrays must have the same length")
                        raise SystemExit
                    for m in range(len(mat)):
                        self.add_level(mat[m], radius[m])
                    if surroundings:
                        self.add_level(surroundings)
                except AssertionError:
                    print(f"*** Error while difining either materials or radius for pin '{self.name}'")
                    print("material and radius must be introduced in an array")
                    raise SystemExit
            # print("--- Warning --- Do not forget to declare the levels for the pin")
        elif mat is None and radius is None:
            if surroundings is not None:
                # Empty Pin declared
                # surroundings is a material
                self.add_level(surroundings) # Adding a material as a level for a void Pin
            else:
                print(f"*** Warning *** Remember to declare materials for the pin '{self.name}'")
        else:
            print(f"*** Error while difining either materials or radius for pin '{self.name}'")
            print("material and radius must be introduced either both or none")
            # Error: material and radius have to be declared either both or none
            raise SystemExit
            
    def add_level(self, material, radius=None):
        """
            Adds a concentric pin level

            Parameters
            ------------------------------------------------------------------------
            material    :   An object of the class Material

            radius      :   A float or integer, radius of the concentric cylinder 
                            from the center of the first level, if it is False, 
                            assumes that is the last material of the pin, i.e. 
                            surroundings of the pin
            ------------------------------------------------------------------------
        """
        from .cells import Cell
        

        Level = namedtuple("Level", ["cell_id", "radius"])
        corresponding_cyl = None
        if radius:
            corresponding_cyl = InfiniteCylinderZ(0.0, 0.0, radius)
            if len(self.__pin_levels) == 0:
                # First level to be declared
                self.__last_region = -corresponding_cyl # SurfaceSide type
            else:
                self.__last_region = +self.__outer_most_surface & -corresponding_cyl  # Region type
            self.__outer_most_surface = corresponding_cyl
            cell = Cell(
                "%s_level_%s"%(self.name,len(self.__pin_levels)), 
                fill=material,
                region=self.__last_region,
                universe=self.name
            )
            
            level = Level(cell.id, radius)
            super().add_cell(cell)
            self.__pin_levels.append(level)
        else:
            #surroundings
            if self.__outer_most_surface is None:
                # surroundnigs for a void pin
                cell = Cell(
                    "%s_level_%s"%(self.name,len(self.__pin_levels)), 
                    fill=material,
                    universe=self.name
                )
                level = Level(cell.id, None)
                super().add_cells(cell)
                self.__pin_levels.append(level)
            else:
                # surroundings of a pin with levels in it already
                cell_region = +self.__outer_most_surface
                cell = Cell(
                    "%s_level_%s"%(self.name,len(self.__pin_levels)), 
                    fill=material,
                    region=cell_region,
                    universe=self.name
                )
                level = Level(cell.id, None)
                super().add_cell(cell)
                self.__pin_levels.append(level)

    def close_last_level(self, region): #region
        last_level = self.__pin_levels[-1]
        first_level = self.__pin_levels[0]
        ll_id = last_level.cell_id
        num_levels = len(self.__pin_levels)
        if num_levels == 0:
            # Void pin with no materials inside
            pass
        elif num_levels == 1:
            # The pin has only one level (surroundings)
            if first_level.radius is None:
                # Pin only with the surroundings (no cylinders inside)
                super().cells[ll_id].region = region
            else:
                # It means that there is a cylinder and could be an error
                # because the pin will be closed with a void space (no material)
                pass
        else:
            # The pin has two or more levels
            if last_level.radius is None:
                # the last level is infinite and will be closed with the region
                # Closing the last region, normally the coolant:
                ll_region = super().cells[ll_id].region & region
                super().cells[ll_id].region = ll_region
    
    def add_pin_levels(self, materials, radius, clone=False):
        """
            Setter method for attribute self.__pin_levels

            Params
            -------------------
            levels      |   
        """
        self.__clone = clone
        try:
            assert len(materials) == len(radius)
            for i in range(len(materials)):
                self.add_level(materials[i], radius[i])
        except AssertionError:
            print("**** Error in adding levels, materials and radius arrays must have the same length ****")
            raise SystemExit

    def copy(self):
        """
            It makes a copy of the pin with new surfaces,
            new cells, different ids
        """
        materials = []
        radius = []
        first_level = self.__pin_levels[0]
        cell = super().cells[first_level.cell_id]
        if first_level.radius is None:
            replica = Pin(self.name, surroundings=cell.content)
            return replica
        else:
            for level in self.__pin_levels:
                content = super().cells[level.cell_id].content
                materials.append(content)
                radius.append(level.radius)
            pin_copy = Pin(self.name)
            pin_copy.add_pin_levels(materials, radius)
            return pin_copy

    def clone(self, new_center_x, new_center_y):
        """
            It makes a copy of the pin with surfaces and cells with
            same ids
        """
        pin_cells = super().cells

        pin_clone = Pin(super().name)
        pin_clone.pin_levels = self.__pin_levels

        clone_pin_cells = {}
        for c_id, cell in pin_cells.items():
            clone_level_cell = cell.clone(new_center_x, new_center_y)
            clone_pin_cells[c_id] = clone_level_cell
        
        pin_clone.cells = clone_pin_cells

        return pin_clone

    def get_center(self):
        first_level = self.__pin_levels[0]
        cell = super().cells[first_level.cell_id]
        if first_level.radius is None:
            # center of a void pin
            return (0,0)
        else:
            cell_id = first_level.cell_id
            cell = super().cells[cell_id]
            return cell.region.surface.center

    def serpent_pin_syntax(self):
        syntax = f"pin {self.name}\n"
        for l in self.__pin_levels:
            mat_name = l.cell.content.name
            if l.radius:
                syntax += "%s %E \n"%(mat_name, l.radius)
            else:
                syntax += f"{mat_name}\n\n"
        return syntax

    def serpent_universe_pin_by_cell_syntax(self):
        syntax = []
        # syntax = ""

        cells = super().cells # levels of the pin { }
        
        for l in self.__pin_levels:
            l_id = l.cell_id
            text = cells[l_id].serpent_syntax()
            # syntax += text
            syntax.append(text)

        # syntax += "\n"

        return syntax

    @property
    def pin_levels(self):
        """
            Getter method for attribute self.__pin_levels
        """
        return self.__pin_levels
    
    @pin_levels.setter
    def pin_levels(self, pin_levels):
        """
            Getter method for attribute self.__pin_levels
        """
        self.__pin_levels = pin_levels

    # @property
    # def cells(self):
    #     return super().cells


    @property
    def materials(self):
        return super().get_universe_materials()
        
    def __eq__(self, other) -> bool:
        """
            A pin is only equal to other when they have the same number
            of levels and the materials and radius in each level are similar
        """
        if len(self.__pin_levels) == len(other.pin_levels):
            # check that the levels are the same
            for i in range(len(self.__pin_levels)):
                self_level = self.__pin_levels[i]
                other_level = other.pin_levels[i]
                self_level_cell = super().cells[self_level.cell_id]
                other_level_cell = other.cells[other_level.cell_id]
                if self_level_cell.content != other_level_cell.content or self_level.radius != other_level.radius:
                    return False
            return True
        
        return False


class Lattice(Universe):

    def __init__(self, name=""):
        super().__init__(name)


class SquareLattice(Lattice):
    """
        Square lattice universe composed by an array of fuel pins
        or universes

    """

    def __init__(self, name, left_bottom, pitch, array):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :   A string with the name of lattice universe

            left_bottom :   Point of lattice origin (origin is left bottom corner)

            pitch       :   Pitch of the assembly
            
            array       :   lattice array
            ----------------------------------------------------------------
        """
        super().__init__(name)
        self.__left_bottom = left_bottom
        self.__pitch = pitch
        self.__array = array
        self.__check_rows_cols()
        self.__ny = len(array)
        self.__nx = len(array[0])
        self.__pin_types = self.__get_different_pins()
        self.__num_pin_types = len(self.__pin_types)
        self.__create_cells()
    
    def __check_rows_cols(self):
        init_num_cols = len(self.__array[0])
        for row in self.__array:
            try:
                assert(len(row) == init_num_cols)
            except AssertionError:
                print("****** error ******")
                print("All rows of square lattice must have equal number of pin elements")

    def __create_cells(self):
        from .cells import Cell

        num_rows = len(self.__array)
        num_cols = len(self.__array[0])
        new_array = [[0 for i in range(num_cols)] for j in range(num_rows)]
        
        x_lb, y_lb = self.__left_bottom
        top_left = (x_lb, y_lb + num_rows*self.__pitch)
        x0, y0 = top_left
        top_left_center_x = x0 + self.__pitch/2
        top_left_center_y = y0 - self.__pitch/2
        pin_replacement = None
        for r in range(num_cols):
            new_center_y = top_left_center_y - self.__pitch * r
            for p in range(num_cols):
                new_center_x = top_left_center_x + self.__pitch * p
                # print(f"({r},{p}) ---> center: ({new_center_x},{new_center_y})")
                pin = self.__array[r][p]
                # create a pin with the same characteristics to move the cell
                # pin_replacement = pin.copy()
                materials = []
                radius = []
                for level in pin.pin_levels:
                    mat = pin.cells[level.cell_id].content
                    materials.append(mat)
                    radius.append(level.radius)
                # pin_replacement = Pin(pin.name)
                # pin_replacement.add_pin_levels(materials, radius)

                # if pin_replacement.pin_levels[0].radius is not None:
                #     # assuring that is not a void pin
                #     # moving the pin
                #     center_pin_repl = pin_replacement.get_center()
                #     trans_vector = (
                #         new_center_x - center_pin_repl[0],
                #         new_center_y - center_pin_repl[1]
                #     )
                #     translate_universe(pin_replacement, trans_vector) 
                # -----------------------------------------------------------------------------
                # When this method is applied it changes the other previous pins as well
                # There is a problem with translate method for this case. This case
                # apparently keeps changing the previous pins even though they are in 
                # different memory locations
                # -----------------------------------------------------------------------------
                
    
                closing_surface = InfiniteSquareCylinderZ(new_center_x, new_center_y, self.__pitch*0.5)
                pin_replacement = declaring_pin_by_cells(
                    materials, radius, new_center_x, new_center_y, pin.name, closing_surface
                )
                new_pin = Cell(region=-closing_surface, fill=pin_replacement, universe=self.name)
                super().add_cell(new_pin)
                new_array[r][p] = new_pin.id # order of the cells from column by column
                pin_replacement = None
                # del pin
                # del pin_replacement
                # del new_pin
                # del Cell


        self.array = new_array

    def __get_different_pins(self):
        types = []
        for row in self.__array:
            for pin in row:
                if pin.name not in types:
                    types.append(pin.name)
        return types

    def serpent_syntax_pin_by_cell(self):
        # pin_cells_syntax = []
        pin_cells_syntax = ""
        cells = {}
        pin_cells = super().cells
        array = self.__array
        
        # pin cells by separate --> probably for gcu or flux generation
        for id_, pin_cell in pin_cells.items():
            # The id_ variable is the id of the cell that was created
            # for the pin in the lattice in the specific position
            pin_uni = pin_cell.content
            cells.update(pin_uni.cells)
            pin_uni.name = pin_uni.name + f"_{id_}"
            # pin_cells_syntax += cell_.serpent_syntax()
            cells_in_pin = pin_uni.cells
            pin_cells_syntax += "\n"
            for c_id, cell in pin_uni.cells.items():
                try:
                    assert isinstance(cell.content, Material)
                    region_syntax = cell.region.serpent_syntax()
                    pin_cells_syntax += f"cell {c_id} {pin_uni.name} {cell.content.name} {region_syntax}\n"
                except AssertionError:
                    raise SystemError

        x_lb, y_lb = self.__left_bottom

        lattice_syntax = f"\n\n\nlat {super().name} 1 {x_lb} {y_lb} {self.__nx} {self.__ny} {self.__pitch}\n"
        for row in array:
            for id_ in row:
                lattice_syntax += f"{pin_cells[id_].content.name} "
            lattice_syntax += "\n"
        
        

        return pin_cells_syntax + lattice_syntax, cells

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, array):
        self.__array = array
    
    @property
    def nx(self):
        return self.__nx
    
    @property
    def ny(self):
        return self.__ny

    @property
    def pitch(self):
        return self.__pitch
    
    @property
    def cells(self):
        return super().cells


class HexagonalLatticeTypeX(Lattice):
    """
        Hexagonal Lattice Type X composed by an array of pins, Example:

    """

    def __init__(self, name, center, pitch, array):
        """
            Init method of the class

            Parameters
            ----------------------------------------------------------------
            name        :   A string with the name of lattice universe

            left_bottom :   Point of lattice origin (origin is left bottom corner)

            pitch       :   Pitch of the assembly
            
            array       :   lattice array
            ----------------------------------------------------------------
        """
        super().__init__(name)
        self.__center_x, self.__center_y = center
        self.__pitch = pitch
        self.__array = array
        self.__check_rows_cols()
        self.__ny = len(array)
        self.__nx = len(array[0])
        self.__enclosed_cells = []
        self.__pin_types = self.__get_different_pins()
        self.__num_pin_types = len(self.__pin_types)
        self.__create_cells()

    def __check_rows_cols(self):
        num_cols = len(self.__array[0])
        try:
            for row in self.__array:
                assert(len(row) == num_cols)
            assert(num_cols % 2 == 1)
        except AssertionError:
            print("****** error ******")
            print("All rows of hexagonal lattice type-x must have equal number of pin elements")
            print("Rows and columns of hexagonal lattice type-x must have odd number of pin elements")

    def __create_cells(self):
        from .cells import Cell

        
        new_array = [[0 for i in range(self.__nx)] for j in range(self.__ny)]
        pin_centers = [[0 for i in range(self.__nx)] for j in range(self.__ny)]
        
        half_width = self.__pitch / 2
        self.__radius = 2 * half_width / math.sqrt(3)

        idx_center_row = self.__ny // 2
        idx_center_col = self.__nx // 2

        dy = 1.5*self.__radius
        
        start_x_row = self.__center_x - idx_center_row*half_width - idx_center_row*self.__pitch
        start_y_row = self.__center_y + idx_center_row*dy

        for r in range(self.__ny):
            for c in range(self.__nx):
                x = start_x_row + c * self.__pitch
                # create a pin with the same characteristics to move the cell
                pin_replacement = self.__array[r][c].replicate()
                if pin_replacement.pin_levels[0].radius is not None:
                    # moving the pin
                    trans_vector = (
                        x - pin_replacement.get_center()[0],
                        start_y_row - pin_replacement.get_center()[1]
                    )
                    pin_replacement.translate(trans_vector)

                # new_center
                new_center_x, new_center_y = x, start_y_row
                closing_surface = InfiniteHexagonalCylinderXtype(new_center_x, new_center_y, half_width)
                new_pin = Cell(region=-closing_surface, fill=pin_replacement)
                new_array[r][c] = new_pin.id # order of the cells from column by column
                pin_centers[r][c] = (x,start_y_row) # order of the cells from column by column
                self.add_cells(new_pin)

            start_x_row += half_width
            start_y_row -= dy
        self.array = new_array
 
    def __get_different_pins(self):
        types = []
        for row in self.__array:
            for pin in row:
                if pin.name not in types:
                    types.append(pin.name)
        return types
    
    def translate(self, trans_vector):
        return super().translate(trans_vector)

    def calculate_enclosed_cells(self, region):
        c = 1
        for row in self.__array:
            for c_id in row:
                cell = super().cells[c_id]
                #check cell center coordinates if they are inside the hexagon
                cell_center = cell.region.surface.center
                try:
                    is_inside = False
                    if region.side == "-":
                        is_inside = region.surface.isPointNegativeSide(cell_center)
                    elif region.side == "+":
                        is_inside = region.surface.isPointPositiveSide(cell_center)
                    else:
                        # Check implementation for a union of regions, etc, 
                        # composed by different surfaces
                        raise SystemError
                    assert is_inside
                    self.__enclosed_cells.append(cell)
                    print(c)
                    print(cell.name)
                    c += 1
                except AssertionError:
                    # center of the cell is not inside the lattice
                    #TODO probably check if the corners are inside to include the gaps of coolant
                    continue
        a = 0

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, array):
        self.__array = array
    
    @property
    def nx(self):
        return self.__nx
    
    @property
    def ny(self):
        return self.__ny

    @property
    def pitch(self):
        return self.__pitch

    @property
    def center(self):
        return (self.__center_x, self.__center_y)

    @property
    def cells(self):
        return super().cells


def translate_universe(universe, trans_vector):
    # return super().translate(trans_vector)
    surfaces_universe = get_all_surfaces_in_a_universe(universe)
    for id_, surf in surfaces_universe.items():
        surf.translate(trans_vector)

