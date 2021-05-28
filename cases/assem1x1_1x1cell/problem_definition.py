import numpy as np
import os 



class Input(object):

        def __init__(self):
            self.pin_radius = 0.4335 # cm
            self.volume_fuel = self.pin_radius * self.pin_radius * np.pi

            self.pitch = 1.2950 # cm
            self.volume_moderator = self.pitch * self.pitch - self.volume_fuel

            self.number_of_pins = 6 # different pins
            self.energy_groups = 2
            self.regions_by_cell = 2
            self.cell_number = 100
            self.assembly = np.array([
                [2, 2, 3, 5, 5, 5, 5, 3, 2, 2],
                [2, 3, 5, 6, 6, 6, 6, 5, 3, 2],
                [3, 5, 6, 6, 6, 6, 6, 6, 5, 3],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [3, 5, 6, 6, 6, 6, 6, 6, 5, 3],
                [2, 3, 5, 6, 6, 6, 6, 5, 3, 2],
                [2, 2, 3, 5, 5, 5, 5, 3, 2, 2]
            ])

            self.num_fuel = 1
            self.num_moderator = 1

            self.surface_length = self.pitch          # surfaces through wich the probabilities
            self.num_surfaces = 4*self.cell_number    # are evaluated
            self.dir_path = os.path.dirname(os.path.realpath(__file__))
            self.group_constant_files = [
                './group_constant_generation/GroupConst1_res.m',
                './group_constant_generation/GroupConst2_res.m',
                './group_constant_generation/GroupConst3_res.m',
                './group_constant_generation/GroupConst4_res.m',
                './group_constant_generation/GroupConst5_res.m',
                './group_constant_generation/GroupConst6_res.m',
            ]
            self.absolute_path = '/home/mono/Documents/school/chalmers/phd/codes/Shynt/repo/cases/assem1x1_1x1cell/'
            self.detector_fuel = [
                'detectors/fuel1toX_fixed_det0.m',
                'detectors/fuel2toX_fixed_det0.m',
                'detectors/fuel3toX_fixed_det0.m',
                'detectors/fuel4toX_fixed_det0.m',
                'detectors/fuel5toX_fixed_det0.m',
                'detectors/fuel6toX_fixed_det0.m',
            ]
            self.detector_moder = [
                'detectors/moder1toX_fixed5_det0.m',
                'detectors/moder2toX_fixed5_det0.m',
                'detectors/moder3toX_fixed5_det0.m',
                'detectors/moder4toX_fixed5_det0.m',
                'detectors/moder5toX_fixed5_det0.m',
                'detectors/moder6toX_fixed5_det0.m',
            ]
            self.detector_surf = [
                'detectors/surfacetoX1_det0.m',
                'detectors/surfacetoX2_det0.m',
                'detectors/surfacetoX3_det0.m',
                'detectors/surfacetoX4_det0.m',
                'detectors/surfacetoX5_det0.m',
                'detectors/surfacetoX6_det0.m',
            ]

            self.detector_names = [
                'DETrfueltotfast',
                'DETjinfuelfast',
                'DETrmjinfuelfast',
                'DETjoutfuelfast',
                'DETrfueltomodfast',
                'DETrfueltowfast',
                'DETrfueltoefast',
                'DETrfueltosfast',
                'DETrfueltonfast',
                'DETrfueltotthm',
                'DETjinfuelthm',
                'DETrmjinfuelthm',
                'DETjoutfuelthm',
                'DETrfueltomodthm',
                'DETrfueltowthm',
                'DETrfueltoethm',
                'DETrfueltosthm',
                'DETrfueltonthm'
            ]



