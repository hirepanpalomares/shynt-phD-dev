import sys

import cases.assem1x1_1x1cell.problem_definition as problem
import Shynt.src_api_py.preprocess.p_calc as probabilities


test = problem.Input()

detector_fuel = test.detector_fuel
detector_moder = test.detector_moder
detector_surf = test.detector_surf


probabilities.calculate(
    detector_fuel, detector_moder, detector_surf, test.absolute_path,
    test.dir_path, test.detector_names, test.number_of_pins
)