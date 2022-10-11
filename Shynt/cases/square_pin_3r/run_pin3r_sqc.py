
import Shynt
from Shynt.api_py.main.run import run, run_RMM
from Shynt.api_py.montecarlo import MontecarloParams

from pin import model_universe
import numpy as np

import matplotlib.pyplot as plt


base_dir = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/square_pin_3r/"
files_dirs = {
  "10_000": "serpent_files_10_000-1500-500",
  "30_000": "serpent_files_30_000-1500-500",
  "50_000": "serpent_files_50_000-1500-500",
  "100_000": "serpent_files_100_000-1500-500",
  "300_000": "serpent_files_300_000-1500-500"
}
mc_params = {
  "10_000": MontecarloParams(10_000, 1500, 500),
  "30_000": MontecarloParams(30_000, 1500, 500),
  "50_000": MontecarloParams(50_000, 1500, 500),
  "100_000": MontecarloParams(100_000, 1500, 500),
  "300_000": MontecarloParams(300_000, 1500, 500)
}
# det_files = [
#   "det_local_problem_inner_fuel.serp", "det_local_problem_na_coolant.serp",
#   "det_local_problem_surfaces.serp"
# ]
# xs_files = ["XS_generation.serp"]
serpent_files = {}
for np_case, mc in mc_params.items():
  model_universe.mcparams = mc
  run(model_universe, name_out=np_case, serp_dir=files_dirs[np_case])

  



# plot_cell(assembly_cell)
