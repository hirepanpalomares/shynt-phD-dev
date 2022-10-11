import numpy as np
import matplotlib.pyplot as plt

from Shynt.cases.square_pin_3r.pin import model_cell
from Shynt.cases.square_pin_3r.pin import model_universe
from Shynt.cases.square_pin_3r.pin import energy_grid


from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm
from Shynt.api_py.Drawer.cell_drawing import plot_cell
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice

energy_g = energy_grid.energy_groups


# Extracting cells from root model
model_cell = model_universe.model_cell
outside_cell = model_universe.outside_cell
lattice = model_cell.content

coarse_nodes = model_cell.global_mesh.coarse_nodes
coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
fine_nodes = model_cell.local_mesh.fine_nodes

# Generating mesh info
mesh_info = MeshInfo(coarse_nodes, fine_nodes, coarse_nodes_map)
mesh_info.type_system = "square"
map_system = mesh_info.coarse_nodes_map


# Extracting serpent fluxes
base_dir = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/square_pin_3r"
output_files = {
  "50_000" : f"{base_dir}/reference/50_000-1500-500/reference_pin3r.serp_det0.m",
  "75_000" : f"{base_dir}/reference/75_000-1500-500/reference_pin3r.serp_det0.m",
  "100_000" : f"{base_dir}/reference/100_000-1500-500/reference_pin3r.serp_det0.m",
  "200_000" : f"{base_dir}/reference/200_000-1500-500/reference_pin3r.serp_det0.m",
  "500_000" : f"{base_dir}/reference/500_000-1500-500/reference_pin3r.serp_det0.m",
  "750_000" : f"{base_dir}/reference/750_000-1500-500/reference_pin3r.serp_det0.m",
}

flux = {}
sigma = {}

for key, det_file in output_files.items():
  serp_fuel_flux, serp_errors_fuel = postprocess.get_flux_from_detector_file(det_file, "1")
  serp_cladd_flux, serp_errors_cladd = postprocess.get_flux_from_detector_file(det_file, "2")
  serp_Na_flux, serp_errors_Na = postprocess.get_flux_from_detector_file(det_file, "3")

  flux[key] = {"fuel": serp_fuel_flux["1"], "cladd": serp_cladd_flux["2"], "cool": serp_Na_flux["3"]}
  sigma[key] = {"fuel": serp_errors_fuel["1"], "cladd": serp_errors_cladd["2"], "cool": serp_errors_Na["3"]}

  normalize_factor = -1000
  for type_flux, f in flux[key].items():
    # Fastest flux[key] = [-1]
    fast_flux = f[energy_g-1]
    max_ = np.max(fast_flux)
    if max_ > normalize_factor:
      normalize_factor = max_
  for type_flux, f in flux[key].items():
    flux[key][type_flux] = f/normalize_factor
  # flux is now normalized


serp_flux_normalized = flux

serpent_arrays_to_plot = { }
serpent_sigma_to_plot = { }

for key, det_file in output_files.items():
  serpent_arrays_to_plot[key] = { g:[] for g in range(energy_g)}
  serpent_sigma_to_plot[key] = { g:[] for g in range(energy_g)}

  for g in range(energy_g):
    serpent_arrays_to_plot[key][g].append(serp_flux_normalized[key]["cool"][g])
    serpent_arrays_to_plot[key][g].append(serp_flux_normalized[key]["cladd"][g])
    serpent_arrays_to_plot[key][g].append(serp_flux_normalized[key]["fuel"][g])
    serpent_arrays_to_plot[key][g].append(serp_flux_normalized[key]["cladd"][g])
    serpent_arrays_to_plot[key][g].append(serp_flux_normalized[key]["cool"][g])

    serpent_sigma_to_plot[key][g].append(sigma[key]["cool"][g])
    serpent_sigma_to_plot[key][g].append(sigma[key]["cladd"][g])
    serpent_sigma_to_plot[key][g].append(sigma[key]["fuel"][g])
    serpent_sigma_to_plot[key][g].append(sigma[key]["cladd"][g])
    serpent_sigma_to_plot[key][g].append(sigma[key]["cool"][g])


for g in range(energy_g):
  fig, ax = plt.subplots()
  for key, det_file in output_files.items():
    serp_arr = np.array(serpent_arrays_to_plot[key][g])
    yerr = serp_arr*np.array(serpent_sigma_to_plot[key][g])
    # ax.errorbar([0,1,2], serp_arr, yerr=yerr, label=key)
    ax.plot(serp_arr, label=key)
    
    # ax2.set_ylim([0, 2])
    # ax2.set_ylabel("% diff")
    plt.title(f"Reference solution analysis g{g}")
    ax.legend()
  fig.savefig(f"{base_dir}/ref_solution_analysis_plots/ref_compare_g{g}")
  # plt.show()
a = 0