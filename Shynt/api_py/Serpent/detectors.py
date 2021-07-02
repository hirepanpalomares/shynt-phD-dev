


from Shynt.api_py.Serpent.input_generator import input_generator


def generate_serpent_files(model):
    """
    Parameters
    -------------
    model   :   Model already meshed of type <class Universe> with the attributes
                <class Universe>.global_mesh and <class Universe>.local_mesh already 
                defined
    """
    model_cell, outside_cell = model.cells # Here it is assumed that model_cell is already meshed
    files = input_generator(model_cell)
    return files

