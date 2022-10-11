
import Shynt
from Shynt.api_py.main.run import run, run_RMM
from Shynt.api_py.montecarlo import MontecarloParams

from hex_pin import root_universe
import numpy as np

import matplotlib.pyplot as plt


base_dir = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_2r_8g/"
files_dirs = {
  "2_000": "serpent_files_2_000_500_250",
  "10_000": "serpent_files_10_000_1500_250",
  "30_000": "serpent_files_30_000_1500_250",
  "50_000": "serpent_files_50_000_1500_250",
  "100_000": "serpent_files_100_000_1500_250",
  "300_000": "serpent_files_300_000_1500_250"
}
mc_params = {
  "2_000": MontecarloParams(2_000, 500, 250),
  "10_000": MontecarloParams(10_000, 1500, 250),
  "30_000": MontecarloParams(30_000, 1500, 250),
  "50_000": MontecarloParams(50_000, 1500, 250),
  "100_000": MontecarloParams(100_000, 1500, 250),
  "300_000": MontecarloParams(300_000, 1500, 250)
}
# det_files = [
#   "det_local_problem_inner_fuel.serp", "det_local_problem_na_coolant.serp",
#   "det_local_problem_surfaces.serp"
# ]
# xs_files = ["XS_generation.serp"]
serpent_files = {}
for np_case, mc in mc_params.items():
  root_universe.mcparams = mc
  run(root_universe, name_out=np_case, serp_dir=files_dirs[np_case])

  



# plot_cell(assembly_cell)
