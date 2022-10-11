from array import array
import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from Shynt.cases.hexagonal_pin_no_hollow_2r_8g.hex_pin import assembly_cell
from Shynt.cases.hexagonal_pin_no_hollow_2r_8g.hex_pin import root_universe
from Shynt.cases.hexagonal_pin_no_hollow_2r_8g.hex_pin import energy_grid

import Shynt
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm
from Shynt.api_py.Drawer.cell_drawing import plot_cell
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice

energy_g = energy_grid.energy_groups

# Extracting cells from root model
model_cell = root_universe.model_cell
outside_cell = root_universe.outside_cell
lattice = model_cell.content

coarse_nodes = model_cell.global_mesh.coarse_nodes
coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
fine_nodes = model_cell.local_mesh.fine_nodes

# Generating mesh info
mesh_info = MeshInfo(coarse_nodes, fine_nodes, coarse_nodes_map)
mesh_info.type_system = "hexagonal"
map_system = mesh_info.coarse_nodes_map

# SHYNT fluxes -------------------------------------------------------------------
input_file_argument = sys.argv[0]
input_file_absolute = str(Path(input_file_argument).absolute())
input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"
shynt_output_file = input_file_dir + "output_RMM/hex_pin_rmm_flux.csv"
shynt_flux = postprocess.get_flux_from_shynt_output(shynt_output_file)
shynt_flux_normalized = norm.normalize_hybrid_flux(shynt_flux, energy_g)


# Serpent flux  --------------------------------------------------------------------

detector_out_file = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_2r_8g/reference_calculation/20000p_1500_250/referencecalc.serp_det0.m"
serp_fuel_flux, serp_errors_fuel = postprocess.get_flux_from_detector_file(detector_out_file, "1")
serp_Na_flux, serp_errors_Na = postprocess.get_flux_from_detector_file(detector_out_file, "2")

flux = {"fuel": serp_fuel_flux["1"], "cool": serp_Na_flux["2"]}
sigma = {"fuel": serp_errors_fuel["1"], "cool": serp_errors_Na["2"]}

normalize_factor = -1000
for type_flux, f in flux.items():
  # Fastest flux = [-1]
  fast_flux = f[energy_g-1]
  max_ = np.max(fast_flux)
  if max_ > normalize_factor:
    normalize_factor = max_
for type_flux, f in flux.items():
  flux[type_flux] = f/normalize_factor
# flux is now normalized

serp_flux_normalized = flux

serpent_arrays_to_plot = { g:[] for g in range(energy_g)}
serpent_sigma_to_plot = { g:[] for g in range(energy_g)}

for g in range(energy_g):
  serpent_arrays_to_plot[g].append(serp_flux_normalized["cool"][g])
  serpent_arrays_to_plot[g].append(serp_flux_normalized["fuel"][g])
  serpent_arrays_to_plot[g].append(serp_flux_normalized["cool"][g])

  serpent_sigma_to_plot[g].append(sigma["cool"][g])
  serpent_sigma_to_plot[g].append(sigma["fuel"][g])
  serpent_sigma_to_plot[g].append(sigma["cool"][g])

# for g in range(energy_g):
#   plt.figure()
#   plt.plot(serpent_arrays_to_plot[g])
#   plt.savefig(f"g{g}_diagonal_serp")

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# get diagonal regions to plot -----------------------------------------------------

regions_mat_rel = mesh_info.region_type_rel[1]
regions_to_plot = []
regions_to_plot.append(regions_mat_rel["na_coolant"])
regions_to_plot.append(regions_mat_rel["inner_fuel"])
regions_to_plot.append(regions_mat_rel["na_coolant"])


shynt_arrays_to_plot = { g:[] for g in range(energy_g)}
for r in regions_to_plot:
    for g in range(energy_g):
        shynt_arrays_to_plot[g].append(shynt_flux_normalized[g][r])


# for g in range(energy_g):
#   plt.figure()
#   plt.plot(shynt_arrays_to_plot[g])
#   plt.savefig(f"g{energy_g-1-g}_diagonal")


for g in range(energy_g):
  fig, ax = plt.subplots()
  shynt_arr = np.array(shynt_arrays_to_plot[energy_g-1-g])
  serp_arr = np.array(serpent_arrays_to_plot[g])
  ax.plot(shynt_arr, label="SHYNT")
  yerr = serp_arr*np.array(serpent_sigma_to_plot[g])
  ax.errorbar([0,1,2], serp_arr, yerr=yerr, label="Serpent")
  ax2 = ax.twinx()
  difference = (serp_arr - shynt_arr)/serp_arr
  ax2.plot(difference, marker="o", color="green")
  # ax2.set_ylim([0, 2])
  # ax2.set_ylabel("% diff")
  # plt.title("Thermal group - Shynt vs Matlab SP_equisurf")
  ax.legend()
  fig.savefig(f"/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_2r_8g/g{g}_HYNTvsSerpent")
  plt.show()

pass