
import Shynt

from hex_pin import root_universe
import numpy as np

import matplotlib.pyplot as plt

mc_params = Shynt.montecarlo.MontecarloParams(10_000, 3_000, 1_500) 
# mc_params = Shynt.montecarlo.MontecarloParams(1_000, 3_000, 1_500) 

root_universe.mcparams = mc_params
Shynt.run(
    root_universe,
    serp_dir=f'serp_files_{mc_params.histories}p_{mc_params.active_cycles}_{mc_params.unactive_cycles}', 
    name_out=f'{mc_params.histories}_{mc_params.active_cycles}_{mc_params.unactive_cycles}'
)


