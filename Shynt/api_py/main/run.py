import os
from platform import node
import numpy as np

import Shynt
from Shynt.api_py.Probabilities.p_calc import calculate_probabilities
from Shynt.api_py.Serpent.detector_output import read_detector_file

from Shynt.api_py.ResponseMatrix.build_matrix import getInitializedPhi_byNode
from Shynt.api_py.ResponseMatrix.build_matrix import getM_matrix
from Shynt.api_py.ResponseMatrix.build_matrix import getMatrixS_byGlobalNode
from Shynt.api_py.ResponseMatrix.build_matrix import getMatrixT_byGlobalNode
from Shynt.api_py.ResponseMatrix.build_matrix import getMatrixU_byGlobalNode
from Shynt.api_py.ResponseMatrix.build_matrix import getResponseMatrix_system

from Shynt.api_py.ResponseMatrix.iterations import solveKeff

import serpentTools
from serpentTools.settings import rc
rc['serpentVersion'] = '2.1.32'



def run(root):
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

    
    # Guessing of phi and k
    phi_guess = getInitializedPhi_byNode(coarse_nodes, energy_g)
    keff = 1


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

    # Build matrixes
    matrixS_byNode = getMatrixS_byGlobalNode(coarse_nodes, energy_g, xs, probabilities) # ready
    matrixT_byNode = getMatrixT_byGlobalNode(coarse_nodes, energy_g, xs, probabilities) # ready
    matrixU_byNode = getMatrixU_byGlobalNode(coarse_nodes, energy_g, probabilities) # ready
    matrixR_system, node_order = getResponseMatrix_system(coarse_nodes, energy_g, probabilities) # ready
    matrixM_system = getM_matrix(coarse_nodes, energy_g) # ready 

    matrixes = {
        "S": matrixS_byNode,
        "T": matrixT_byNode,
        "U": matrixU_byNode,
        "R": matrixR_system,
        "M": matrixM_system
    }


    # Solve response matrix
    solution = solveKeff(keff, phi_guess, coarse_nodes, fine_nodes, energy_g, xs, matrixes, node_order, probabilities)
    
    
    #    Post processing data
    pass


    # Reset counters and delete counter files Probably store it in some memory
    # location that can be readable from every part of the code.
    Shynt.surfaces.reset_surface_counter()
    Shynt.cells.reset_cell_counter()
