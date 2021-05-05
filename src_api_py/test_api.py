import numpy as np
import scipy.io
import shynt.input_handler as shynt_input

pin_radius = 0.4335 # cm
pitch = 1.2950 # cm

serpent_res_files = [
    'GroupConst1_res.m',
    'GroupConst2_res.m',
    'GroupConst3_res.m',
    'GroupConst4_res.m',
    'GroupConst5_res.m',
    'GroupConst6_res.m',
]


energy_groups = 2
regions_by_cell = 2
cell_number = 100

assembly = np.array([
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

xs = shynt_input.getSerpentXS(serpent_res_files).getData()


#print(xs['GroupConst1_res.m'][0.0]['XS']['11']['total']['xs'])
