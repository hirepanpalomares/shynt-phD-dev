import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from hex_pin import root_universe, model_cell, energy_grid

import Shynt
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm
from Shynt.api_py.Drawer.cell_drawing import plot_cell
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice

# Extracting cells from root model
energy_g = energy_grid.energy_groups
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


dir_base = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_2r_8g/"

out_files = {
  "2_000": "output_RMM_2_000/2_000_rmm_flux.csv",
  "10_000": "output_RMM_10_000/10_000_rmm_flux.csv",
  "30_000": "output_RMM_30_000/30_000_rmm_flux.csv",
  "50_000": "output_RMM_50_000/50_000_rmm_flux.csv",
  "100_000": "output_RMM_100_000/100_000_rmm_flux.csv",
  "300_000": "output_RMM_300_000/300_000_rmm_flux.csv"
}

shynt_flux_normalized = {}
for n_case, out_file in out_files.items():
  shynt_out = dir_base + out_file
  flux = postprocess.get_flux_from_shynt_output(shynt_out)
  flux_norm = norm.normalize_hybrid_flux(flux, energy_g)
  shynt_flux_normalized[n_case] = flux_norm

a = 0

# get diagonal regions to plot -----------------------------------------------------
coarse_nodes_diagonal_hybrid = [map_system[0][0]]
regions_to_plot = []
for c_id in coarse_nodes_diagonal_hybrid:
  regions_mat_rel = mesh_info.region_type_rel[c_id]

  regions_to_plot.append(regions_mat_rel["na_coolant"])
  regions_to_plot.append(regions_mat_rel["inner_fuel"])
  regions_to_plot.append(regions_mat_rel["na_coolant"])


shynt_arrays_to_plot = { }
for n_case, fl in shynt_flux_normalized.items():
  shynt_arrays_to_plot[n_case] = {g:[] for g in range(energy_g)}
  for r in regions_to_plot:
      for g in range(energy_g):
          shynt_arrays_to_plot[n_case][g].append(shynt_flux_normalized[n_case][g][r])

# Serpent flux  --------------------------------------------------------------------
detector_out_file = dir_base + "reference_calculation/moreParticles_test/2e6.serp_det0.m"
serp_fuel_flux, serp_errors_fuel = postprocess.get_flux_from_detector_file(detector_out_file, "1")
serp_cool_flux, serp_errors_cool = postprocess.get_flux_from_detector_file(detector_out_file, "2")


flux = {"fuel": serp_fuel_flux["1"], "cool": serp_cool_flux["2"]}
sigma = {"fuel": serp_errors_fuel["1"],  "cool": serp_errors_cool["2"]}

normalize_factor = -1000
for type_flux, f in flux.items():
  # Fastest flux = [-1]
  fast_flux = f[energy_g-1]
  if fast_flux > normalize_factor:
    normalize_factor = fast_flux

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

for g in range(energy_g):
  plt.figure()
  plt.errorbar(
    [0,1,2], serpent_arrays_to_plot[g],
    yerr=np.array(serpent_arrays_to_plot[g])*np.array(serpent_sigma_to_plot[g]), 
    label="Serpent", ls='--'
  )
  for n_case, fl in shynt_arrays_to_plot.items():

    # print(serpent_arrays_to_plot[g])
    # print(serpent_sigma_to_plot[g])
    # print(np.array(serpent_arrays_to_plot[g])*np.array(serpent_sigma_to_plot[g]))
    plt.plot(shynt_arrays_to_plot[n_case][energy_g-1-g], label=f"SHYNT_{n_case}")
    # # plt.ylim([0.02, 0.17])
    # current_values = plt.gca().get_yticks()
    # plt.gca().set_yticklabels(['{:.5f}'.format(x) for x in current_values])
    plt.legend()
    # # plt.show()
  plt.savefig(f"{dir_base}det_accuracy_analysis/g{g}_SHYNT")