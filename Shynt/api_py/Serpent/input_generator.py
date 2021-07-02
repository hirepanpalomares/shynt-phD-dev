from Shynt.api_py.Serpent.input_syntax import print_cell
from Shynt.api_py.Geometry.regions import SurfaceSide
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.universes import Universe


def generate_serpent_input(arg, file):
    # Make a recursive tree to generate the output
    if not (isinstance(arg, Cell) or isinstance(arg, Universe)):
        return 0

    elif isinstance(arg, Cell):
        
        file.write(print_cell(arg))
        if arg.filled_by_universe:
            #cell was filled with universe 
            # RECURSIVE CALL 
            pass
        else:
            #cell was filled with material
            # print directly Serpent cell definition
            material = arg.material
    elif isinstance(arg, Universe):
        pass


def input_generator(cell):
    """
    Function to call the recursive serpent cards generator over all
    the geometry, starting from the root cell.
    """
    with open('serp_inp', 'w') as file:
        generate_serpent_input(cell, file)
    return []



"""
Para imprimir los materiales quizás sea bueno
irlos impriendo en otro documento conforme vayan 
apareciendo

La recursion servira para imprimir los universos 
con los que son llenadas las celdas y las demas
superficies

"""