from Shynt.api_py.Serpent.input_file import SerpentInputFile
import os
import sys
from pathlib import Path



def generate_serpent_files(model):
    """
    Parameters
    -------------
    model   :   Model already meshed of type <class Universe> with the attributes
                <class Universe>.global_mesh and <class Universe>.local_mesh already 
                defined
    """
    model_cell, outside_cell = model.cells # Here it is assumed that model_cell is already meshed
    # print(model_cell)
    #print(outside_cell)

    global_cells = model_cell.global_mesh.coarse_nodes
    local_cells = model_cell.local_mesh.fine_nodes

    different_node_bins = different_global_nodes(global_cells, local_cells)

    print("\nGlobal cells... ")
    # print(global_cells)
    print("\nLocal cells...")
    # print(local_cells)
    print("\nNodes grouped...")
    # print(different_node_bins)
    # print("\n")
    
    cells_to_files = {bin_[0] : global_cells[bin_[0]] for bin_ in different_node_bins}
    # print(cells_to_files)
    
    det_files, xs_files = input_generator(cells_to_files, local_cells, model)
    return det_files, xs_files, different_node_bins


def is_pin_in_array(pin, arr, global_nodes, local_nodes):
    """
        Function that tells if a pin is in an array 
        returns True if in the array exist a similar pin
        and False if it does not

        Parameters
        ---------------------------------
        
        pin     :   <class Cell> and it hast be filled with the Pin universe
        arr     :   <class list> array of cells
        
        ---------------------------------
    """
    for other in arr:
        # check number of total local problems
        num_local_other = len(local_nodes[other])
        num_local_pin = len(local_nodes[pin])
        if num_local_other == num_local_pin:
            # check that the pin is the same
            pin_array = global_nodes[other].content
            pin_compare = global_nodes[pin].content
            if pin_array == pin_compare:
                return True
    
    return False


def different_global_nodes(global_nodes, local_nodes):
    """
    
        Ways that could be used to check if are different:
            
            - Amount of local problems
            - Material of local problems 
            - Shape of local problems (surface)
            - Size of the local problems

        ****************************************************************

            At the moment it only works when the global cells are
            cells with a Pin universe as content
        
        ****************************************************************
    """

    bins = []
    for id_, cell in global_nodes.items():
        # sweep cells
        found = False
        for b in range(len(bins)):
            # sweep bins
            if is_pin_in_array(id_, bins[b], global_nodes, local_nodes):
                bins[b].append(id_)
                found = True
                break
        if not found:
            # add new bin
            bins.append([id_])
        
    
    return bins


def input_generator(global_cells, local_cells, model):
    """
    
    Function to generate the input files from a given set of cells,
    each one with a different file.

    """

    
    input_file_argument = sys.argv[0]
    input_file_absolute = str(Path(input_file_argument).absolute())
    input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"

    serpent_dir = input_file_dir + "serpent_files"
    # print("*"*60)
    # print(os.getcwd())
    # print("*"*60)

    try:
        assert(os.path.isdir(serpent_dir))
    except AssertionError:
        os.mkdir(serpent_dir)


    det_files = {}
    xs_files = {}
    
    for id_, global_cell in global_cells.items():
        # Loop for every global_cell
        det_files[id_] = []
        global_cell_dir = f"{serpent_dir}/global_cell_type{id_}"
        try:
            assert(os.path.isdir(global_cell_dir))
        except AssertionError:
            os.mkdir(global_cell_dir)
        
        for local_cell in local_cells[id_]:
            # Loop for local cells (a different file for every material or, in this case, each local cell to write the detectors)
            cell = local_cell.cell
            material = cell.content.name
            name_file = f"{global_cell_dir}/det_local_problem_{material}.serp"
            serpent_input = SerpentInputFile(
                global_cell, 
                id_, 
                local_cells[id_], 
                name_file,
                model.libraries, 
                model.energy_grid, 
                model.mcparams,
                type_detectors="local_cell",
                local_cell_id=local_cell.cell.id,
                specific=material

            )
            det_files[id_].append(serpent_input)

        # Additional file for the surfaces
        name_surfaces_file = f"{global_cell_dir}/det_local_problem_surfaces.serp"
        det_files[id_].append(
            SerpentInputFile(
                global_cell, 
                id_, 
                local_cells[id_], 
                name_surfaces_file,
                model.libraries, 
                model.energy_grid, 
                model.mcparams,
                type_detectors="surfaces",
                specific="surfaces"
            )
        )
        # Additional file for cross section generation
        name_file = f"{global_cell_dir}/XS_generation.serp"
        xs_files[id_] = SerpentInputFile(
            global_cell, 
            id_, 
            local_cells[id_], 
            name_file,
            model.libraries, 
            model.energy_grid, 
            model.mcparams,
            type_detectors="xs_generation",
        )
    return det_files, xs_files



if __name__=="__main__":
    pass
