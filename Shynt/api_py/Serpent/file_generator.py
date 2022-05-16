from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Serpent.input_file import SerpentInputFile, SerpentInputFileRmm
import os
import sys
from pathlib import Path



def generate_serpent_files(root, different_node_bins):
    """
    Parameters
    -------------
    root        :   Model already meshed of type <class Universe> with the attributes
                    <class Universe>.global_mesh and <class Universe>.local_mesh already 
                    defined
    """

    global_cells = root.model_cell.global_mesh.coarse_nodes
    local_cells = root.model_cell.local_mesh.fine_nodes


    
    cells_to_files = {bin_[0] : global_cells[bin_[0]] for bin_ in different_node_bins}
    # print(cells_to_files)
    
    det_files, xs_files = input_generator(cells_to_files, local_cells, root)

    return det_files, xs_files


def input_generator(coarse_nodes, regions, root):
    """
    
    Function to generate the input files from a given set of cells,
    each one with a different file.

    """

    
    input_file_argument = sys.argv[0]
    input_file_absolute = str(Path(input_file_argument).absolute())
    input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"

    serpent_dir = input_file_dir + "serpent_files"
  

    try:
        assert(os.path.isdir(serpent_dir))
    except AssertionError:
        os.mkdir(serpent_dir)


    det_files = {}
    xs_files = {}
    
    for id_, global_cell in coarse_nodes.items():
        # Loop for every global_cell
        # print("-"*100)
        det_files[id_] = []
        # print("", id_)

        global_cell.cell.universe = 0 # To adjust the root universe to the cell under study
        global_cell_dir = f"{serpent_dir}/global_cell_type{id_}"
        try:
            assert(os.path.isdir(global_cell_dir))
        except AssertionError:
            os.mkdir(global_cell_dir)
        
        for reg_id, reg in regions[id_].items():
            # Loop for local cells (a different file for every material or, 
            # in this case, each local cell to write the detectors)
            cell = reg.cell
            material = cell.content.name
            name_file = f"{global_cell_dir}/det_local_problem_{material}.serp"
            type_reg = ""
            if cell.content.isFuel:
                type_reg = "fuel"
            else:
                type_reg = "coolant"
            serpent_input = SerpentInputFileRmm(
                global_cell, 
                id_, 
                regions[id_], 
                name_file,
                root.libraries, 
                root.energy_grid, 
                root.mcparams,
                type_detectors="region",
                region_id=reg_id,
                specific=f"region_{type_reg}"

            )
            det_files[id_].append(serpent_input)

        # Additional file for the surfaces
        name_surfaces_file = f"{global_cell_dir}/det_local_problem_surfaces.serp"
        surf_serpent_input = SerpentInputFileRmm(
                global_cell, 
                id_, 
                regions[id_], 
                name_surfaces_file,
                root.libraries, 
                root.energy_grid, 
                root.mcparams,
                type_detectors="surfaces",
                specific="surfaces"
            )
        det_files[id_].append(surf_serpent_input)
        # Additional file for cross section generation
        name_file = f"{global_cell_dir}/XS_generation.serp"
        xs_serpent_input = SerpentInputFileRmm(
            global_cell, 
            id_, 
            regions[id_], 
            name_file,
            root.libraries, 
            root.energy_grid, 
            root.mcparams,
            type_detectors="xs_generation",
        )
    
        xs_files[id_] = xs_serpent_input
    
    return det_files, xs_files


def generate_root_serpent_file(root, ask_flux="cell"):

    input_file_argument = sys.argv[0]
    input_file_absolute = str(Path(input_file_argument).absolute())
    input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"

    serpent_dir = input_file_dir + "serpent_files"
  
    serpent_root_dir =  serpent_dir + "/root_universe"
    try:
        assert(os.path.isdir(serpent_dir))
    except AssertionError:
        os.mkdir(serpent_dir)
    try:
        assert(os.path.isdir(serpent_root_dir))
    except AssertionError:
        os.mkdir(serpent_root_dir)
    
    name_file = f"{serpent_root_dir}/root_universe.serp"
    serp_file = SerpentInputFile(
        root.model_cell,
        name_file,
        root.libraries,
        root.energy_grid,
        root.mcparams,
        type_detectors="flux",
    )


if __name__=="__main__":
    pass
