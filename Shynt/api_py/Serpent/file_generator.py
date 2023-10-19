from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Serpent.input_file import SerpentInputFileReferenceFlux
from Shynt.api_py.Serpent.input_file import SerpentInputFileDetectorsRegion
from Shynt.api_py.Serpent.input_file import SerpentInputFileDetectorsSurface
from Shynt.api_py.Serpent.input_file import SerpentInputFileDetectorsXsGeneration

import os
import sys
import numpy as np
from pathlib import Path


# 
def generate_serpent_files(root, different_node_bins, serp_dir="serpent_files"):
    """
    Parameters
    -------------
    root        :   Model already meshed of type <class Universe> with the attributes
                    <class Universe>.global_mesh and <class Universe>.local_mesh already 
                    defined
    """

    global_cells = root.model_cell.global_mesh.coarse_nodes
    local_cells = root.model_cell.local_mesh.fine_nodes

    map_mesh = root.model_cell.global_mesh.coarse_nodes_map
    # print(map_mesh)

    # print_different_node_bins = [print(bb) for bb in different_node_bins]
    coarse_nodes_to_files = [global_cells[bin_[0]] for bin_ in different_node_bins]
    
    # print_coarse_nodes_to_files = [print(i) for i in coarse_nodes_to_files  ]

    
    """
        The cells in cells_to_files are generated with a new geometry, i.e. 
        new surfaces with new coordinates. 
        This is to avoid problems with the surfaces that are used in the 
        detectors
    """
    coarse_nodes_clones = {}
    
    # ! The proccess of cloning is taking too much time debugging it, SO NO CLONES
    # for coarse_node in coarse_nodes_to_files:
    #     print()
    #     # print(coarse_node.)
    #     print(coarse_node.cell.content.cells)
    #     cell_center = coarse_node.cell.center
    #     clone_vector = (0.0 - cell_center[0], 0.0 - cell_center[1])
    #     cell_clone = coarse_node.cell.clone(0.0, 0.0, clone_vector=clone_vector) # New center in 0.0, 0.0
    #     coarse_node.cell = cell_clone
    #     coarse_nodes_clones[coarse_node.id] = coarse_node
        
    # raise SystemExit

    det_files, xs_files = input_generator(coarse_nodes_to_files, local_cells, root, serp_dir=serp_dir)

    return det_files, xs_files


def input_generator(coarse_nodes, fine_nodes, root, serp_dir="serpent_files"):
    """
    
    Function to generate the input files from a given set of cells,
    each one with a different file.

    """

    
    input_file_argument = sys.argv[0]
    input_file_absolute = str(Path(input_file_argument).absolute())
    input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"

    serpent_dir = input_file_dir + serp_dir
  

    try:
        assert(os.path.isdir(serpent_dir))
    except AssertionError:
        os.mkdir(serpent_dir)


    det_files = {}
    xs_files = {}
    
    for coarse_n in coarse_nodes:
        # Loop for every coarse_node
        # print("-"*100)
        # print(coarse_n.cell.content.cells)
        det_files[coarse_n.id] = []

        coarse_n.cell.universe = 0 # To adjust the root universe to the cell under study
        global_cell_dir = f"{serpent_dir}/global_cell_type{coarse_n.id}"
        try:
            assert(os.path.isdir(global_cell_dir))
        except AssertionError:
            os.mkdir(global_cell_dir)
        
        for reg_id, reg in fine_nodes[coarse_n.id].items():
            """
                Loop for local cells (a different file for every 
                material or, in this case, each local cell to write 
                the detectors.

                The detectors for each local cell have to be defined
                in different serpent files to avoid calculation error 
                with the flags
            """
            cell = reg.cell
            material = cell.content.name
            if material == "void": continue
            # print("file")
            # print(material)
            name_file = f"{global_cell_dir}/det_local_problem_{material}_{reg_id}.serp"
            
            serpent_input = SerpentInputFileDetectorsRegion(
                coarse_n, fine_nodes[coarse_n.id], name_file, root, reg_id
            )
            
            det_files[coarse_n.id].append(serpent_input)

        # print("-----"*50)
        # Additional file for the surfaces
        name_surfaces_file = f"{global_cell_dir}/det_local_problem_surfaces.serp"
        surf_serpent_input = SerpentInputFileDetectorsSurface(coarse_n, fine_nodes[coarse_n.id], name_surfaces_file, root)
        det_files[coarse_n.id].append(surf_serpent_input)
        # print(name_surfaces_file)
        # Additional file for cross section generation
        name_file = f"{global_cell_dir}/XS_generation.serp"
        xs_serpent_input = SerpentInputFileDetectorsXsGeneration(coarse_n, fine_nodes[coarse_n.id], name_file, root)    
        xs_files[coarse_n.id] = xs_serpent_input
        # print(name_file)
    
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
    serp_file = SerpentInputFileReferenceFlux(root, name_file)

    return serp_file


if __name__=="__main__":
    pass
