import os
from platform import node
import numpy as np

import Shynt
from Shynt.api_py.Probabilities.p_calc import calculate_probabilities
from Shynt.api_py.ResponseMatrix.build_matrix import build_M, buildJsource, getMatrixS_byGlobalNode, getMatrixT_byGlobalNode, getPhiVector_byGlobalNode, getSource_byGllobalNode

from Shynt.api_py.ResponseMatrix.build_matrix import getResponseMatrix_system
from Shynt.api_py.ResponseMatrix.build_matrix import getUMatrix_system

from Shynt.api_py.Serpent.detector_output import read_detector_file

import serpentTools
from serpentTools.settings import rc
rc['serpentVersion'] = '2.1.32'


def run(root):
    model_cell, outside_cell = root.cells # Here it is assumed that model_cell is already meshed

    # Generate local problems files, and file for cross section generation
    det_inputs, xs_inputs, coarse_nodes, fine_nodes, equality_bins =  Shynt.generator.generate_serpent_files(root)
    

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
        
    
    # Extract XS data  
    # An open source library is used
    # see (https://github.com/drewejohnson/serpent-tools)
    xs = {}
    energy_g = root.energy_grid.energy_groups
    for id_coarse, xs_inp in xs_inputs.items():
        resFile = xs_inp.name + "_res.m"
        res = serpentTools.read(resFile)
        cells_fine_nodes = fine_nodes[id_coarse]
        xs[id_coarse] = {}
        for c in range(len(cells_fine_nodes)):
            cell = cells_fine_nodes[c]
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
        
    
    # Calculate probabilities for each node of the coarse mesh

    probabilities = {}
    try: 
        for id_ in det_inputs:
            prob_id = calculate_probabilities(coarse_node_scores[id_], detector_relation[id_], energy_g, id_)
            probabilities[id_] = prob_id
    except KeyError:
        Shynt.surfaces.reset_surface_counter()
        Shynt.cells.reset_cell_counter()
    
    Shynt.surfaces.reset_surface_counter()
    Shynt.cells.reset_cell_counter()

    

    # surfaces relation and areas
    surf_area_relation = model_cell.global_mesh.surface_area_relation
    surf_relation = model_cell.global_mesh.surface_relation
    
    # Guessing of phi and k
    phi_vector = getPhiVector_byGlobalNode(coarse_nodes, fine_nodes, energy_g)
    keff = 1

    # Build matrixes    
    matrixS_byNode = getMatrixS_byGlobalNode(coarse_nodes, fine_nodes, surf_area_relation, energy_g, xs, probabilities)
    matrixT_byNode = getMatrixT_byGlobalNode(coarse_nodes, fine_nodes, energy_g, xs, probabilities)
    matrixR_system = getResponseMatrix_system(coarse_nodes, surf_area_relation, energy_g, probabilities)
    matrixU_system = getUMatrix_system(coarse_nodes, fine_nodes, surf_area_relation, energy_g, probabilities)
    matrixM_system = build_M(surf_relation,energy_g)

    # Calculating source terms
    sourceTerm_QbyNode = getSource_byGllobalNode(coarse_nodes, fine_nodes, energy_g, xs, keff, phi_vector)
    j_source = buildJsource(matrixU_system, sourceTerm_QbyNode)
    
    # Jin_vector_byNode = getJinVector_byNode(coarse_nodes, surf_area_relation, energy_g)
    # Jin_global = getJinVector_global(surf_relation)
    
    
       
    # Solve response matrix







    """
    ------------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------------

        Post processing data
    Shynt.surfaces.reset_surface_counter()
    Shynt.cells.reset_cell_counter()
    ------------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------------
    
    """



    """
    ------------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------------
        # Reset counters and delete counter files

        
        Probably store it in some memory location that can be readable from every part
        of the code.
    ------------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------------
    """
