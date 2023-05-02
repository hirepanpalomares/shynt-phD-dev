import hex_assem
import numpy as np
import Shynt


np.set_printoptions(linewidth=np.inf)

# mc_params = Shynt.montecarlo.MontecarloParams(1500, 1000, 500) 
mc_params = Shynt.montecarlo.MontecarloParams(3_000, 3_000, 1_500) 

hex_assem.root_universe.mcparams = mc_params
Shynt.run(
    hex_assem.root_universe,
    serp_dir=f'serp_files_{mc_params.histories}_{mc_params.active_cycles}_{mc_params.unactive_cycles}', 
    name_out=f'{mc_params.histories}_{mc_params.active_cycles}_{mc_params.unactive_cycles}'
)
