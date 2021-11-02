import os

import Shynt
from Shynt.api_py.Probabilities.p_calc import calculate_probabilities
from Shynt.api_py.Serpent.detector_output import read_detector_file


def run(root):
    # Generate Serpent detector Files
    inputs, coarse_nodes, fine_nodes, equality_bins =  Shynt.generator.generate_serpent_files(root)
    print("-"*100)

    # print(inputs)
    # print(global_p)
    # print(coarse_nodes)
    # print(equality_bins)
    
    # -------------------------------------------------------------------------------------------

    # Then run every file and it will generate a detector file for each input file
    for id_, inp in inputs.items():
        command = f"sss2.32 {inp.name} -omp 10"
        # os.system(command)

    # -------------------------------------------------------------------------------------------

    # Then extract data from detectors
    coarse_node_scores = {}
    detector_relation = {}
    for id_, inp in inputs.items(): 
        det_file_name = inp.name + "_det0.m"
        data_detector = read_detector_file(det_file_name) # This is data of the detectors
        coarse_node_scores[id_] = data_detector
        detector_relation[id_] = inp.detectors_relation
        

    # -------------------------------------------------------------------------------------------

    # Then calculate probabilities for each node of the coarse mesh
    probabilities = {}
    for id_ in inputs:
        prob_id = calculate_probabilities(coarse_node_scores[id_], detector_relation[id_])
        probabilities[id_] = prob_id

    # Build response matrix

    # Solve response matrix

    # Post processing data

    Shynt.surfaces.reset_surface_counter()
    Shynt.cells.reset_cell_counter()

