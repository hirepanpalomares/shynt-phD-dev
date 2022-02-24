import os
from collections import namedtuple
import numpy as np

import Shynt
from Shynt.api_py.Probabilities.p_calc import calculate_probabilities
from Shynt.api_py.Serpent.detector_output import read_detector_file



from Shynt.api_py.ResponseMatrix.iterations import solveKeff

import serpentTools
from serpentTools.settings import rc
rc['serpentVersion'] = '2.1.32'



def run(root):
    Shynt.surfaces.reset_surface_counter()
    Shynt.cells.reset_cell_counter()

    model_cell, outside_cell = root.cells # Here it is assumed that model_cell is already meshed
    # Generate local problems files, and file for cross section generation
    det_inputs, xs_inputs, equality_bins =  Shynt.generator.generate_serpent_files(root)
    coarse_nodes = model_cell.global_mesh.coarse_nodes
    fine_nodes = model_cell.local_mesh.fine_nodes
    
   

    # Run detector files and it will generate an output file for each local problem 
    # input file
    for id_coarse, inp in det_inputs.items():
        for file_ in inp:
            # print(file_.name)
            # command = f"gnome-terminal -x sh -c \"sss2.1.32 {file_.name} -omp 10; bash\" " # To run in another terminal (testing it)
            command = f"sss2.1.32 {file_.name} -omp 18"
            # os.system(command)


    # Run cross sections file
    for id_coarse, xs_inp in xs_inputs.items():
        command_xs_gen = f"sss2.1.32 {xs_inp.name} -omp 18"
        # os.system(command)



    # Extract data from detectors
    coarse_node_scores = {}
    detector_relation = {}
    for id_, inp in det_inputs.items():
        coarse_node_scores[id_] = {}
        detector_relation[id_] = {}
        for file_ in inp:
            det_file_name = file_.name + "_det0.m"
            data_detector = read_detector_file(det_file_name) # This is data of the detectors
            coarse_node_scores[id_][file_.specific] = data_detector
            detector_relation[id_][file_.specific] = file_.detectors_relation
    
    
    
    """
        Extract XS data  
        An open source library is used
        see (https://github.com/drewejohnson/serpent-tools)

        The XS are ordered from FAST ---> THERMAL
    """
    xs = {}

    energy_g = root.energy_grid.energy_groups
    for id_coarse, xs_inp in xs_inputs.items():
        resFile = xs_inp.name + "_res.m"
        res = serpentTools.read(resFile)
        xs[id_coarse] = {}
        for c in range(len(fine_nodes[id_coarse])):
            cell = fine_nodes[id_coarse][c].cell
            universe = res.getUniv(cell.gcuName, burnup=0)

            xs_total = universe["infTot"]
            xs_nuFiss = universe["infNsf"]
            xs_chi = universe["infChit"]
            scatter_data = universe["infS0"]
            xs_scatterMatrix = scatter_data.reshape((energy_g, energy_g))
            xs[id_coarse][cell.id] = {
                "total": xs_total,
                "nuSigFission": xs_nuFiss,
                "chi": xs_chi,
                "scatter": xs_scatterMatrix
            }    
        
    
    # Calculate probabilities for each node of the coarse mesh -------------------
    probabilities = {}
    try: 
        for id_ in det_inputs:
            prob_id = calculate_probabilities(
                coarse_node_scores[id_], 
                detector_relation[id_], 
                energy_g, id_
            )
            probabilities[id_] = prob_id
    except KeyError:
        Shynt.surfaces.reset_surface_counter()
        Shynt.cells.reset_cell_counter()
    

    


    # print(xs[1])
    # print()
    # print(3)
    # print(probabilities[1]["surface"][3]["surfaces"])
    # print()
    # print(4)
    # print(probabilities[1]["surface"][4]["surfaces"])
    # print()
    # print(6)
    # print(probabilities[1]["surface"][6]["surfaces"])
    # print()
    # print(5)
    # print(probabilities[1]["surface"][5]["surfaces"])
    # print()
    # print()
    # print(probabilities[1]["coolant"])


    Shynt.surfaces.reset_surface_counter()
    Shynt.cells.reset_cell_counter()
    
    # Ordering nodes, regions and surfaces --------------------------------------
    coarse_node_array = list(coarse_nodes.keys())
    all_regions = []
    region_coarse_rel = {}
    coarse_region_rel = {}
    coarse_surf_rel = {}
    regions_vol = {}
    all_surfaces = []
    for n_id in coarse_node_array:
        regions = coarse_nodes[n_id].fine_nodes_ids
        surfaces = coarse_nodes[n_id].surface_ids
        vols = coarse_nodes[n_id].fine_nodes_volume
        regions_vol.update(vols)
        all_regions += regions
        all_surfaces += surfaces
        coarse_region_rel[n_id] = regions
        for r in regions:
            region_coarse_rel[r] = n_id
        for s in surfaces:
            coarse_surf_rel[s] = n_id

    # print(coarse_node_array)
    # print(all_regions)
    # print(region_coarse_rel)
    # print(coarse_surf_rel)
    # print(regions_vol)
    # print(all_surfaces)

    MeshInfo = namedtuple(
        "MeshInfo", 
        [
            "coarse_order", 
            "all_regions_order", 
            "all_regions_vol", 
            "all_surfaces_order",
            "region_coarse_rel",
            "coarse_region_rel",
            "coarse_surface_rel"
        ]
    )
    mesh_info = MeshInfo(
        coarse_node_array,
        all_regions,
        regions_vol,
        all_surfaces,
        region_coarse_rel,
        coarse_region_rel,
        coarse_surf_rel
    )


    # Solve response matrix ----------------------------------------------------
    solution = solveKeff(
        coarse_nodes, 
        fine_nodes, 
        energy_g, 
        xs, 
        probabilities, 
        mesh_info
    )
    
    
    #    Post processing data
    pass


    # Reset counters and delete counter files Probably store it in some memory
    # location that can be readable from every part of the code.
    Shynt.surfaces.reset_surface_counter()
    Shynt.cells.reset_cell_counter()
