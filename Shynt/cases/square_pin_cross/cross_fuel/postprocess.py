import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from square_pin_cross import model_universe, model_cell, energy_grid

import Shynt
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm
from Shynt.api_py.Drawer.cell_drawing import plot_cell
from Shynt.api_py.Mesh.mesh_info import MeshInfo

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


dir_base = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/square_pin_cross/"
# SHYNT fluxes -------------------------------------------------------------------

shynt_output_file = dir_base + "output_RMM_/_rmm_flux.csv"
shynt_flux = postprocess.get_flux_from_shynt_output(shynt_output_file)
shynt_flux_normalized = norm.normalize_hybrid_flux(shynt_flux, energy_g)


# Serpent flux  --------------------------------------------------------------------
detector_out_file = dir_base + "reference/reference_fuel_cross.serp_det0.m"
serp_fuel_tl_flux, serp_errors_fuel_tl = postprocess.get_flux_from_detector_file(detector_out_file, "top_left")
serp_fuel_tr_flux, serp_errors_fuel_tr = postprocess.get_flux_from_detector_file(detector_out_file, "top_right")
serp_fuel_br_flux, serp_errors_fuel_br = postprocess.get_flux_from_detector_file(detector_out_file, "bottom_right")
serp_fuel_bl_flux, serp_errors_fuel_bl = postprocess.get_flux_from_detector_file(detector_out_file, "bottom_left")

serp_cool1_flux, serp_errors_cool1 = postprocess.get_flux_from_detector_file(detector_out_file, "coolant")


flux = {
  "fuel_tl": serp_fuel_tl_flux["top_left"],
  "fuel_tr": serp_fuel_tr_flux["top_right"], 
  "fuel_br": serp_fuel_br_flux["bottom_right"], 
  "fuel_bl": serp_fuel_bl_flux["bottom_left"], 

  "cool1": serp_cool1_flux["coolant"]
}
sigma = {
  "fuel_tl": serp_errors_fuel_tl["top_left"],
  "fuel_tr": serp_errors_fuel_tr["top_right"], 
  "fuel_br": serp_errors_fuel_br["bottom_right"], 
  "fuel_bl": serp_errors_fuel_bl["bottom_left"], 

  "cool1": serp_errors_cool1["coolant"]
}

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


serpent_arrays_to_plot_cross_tl_br = { g:[] for g in range(energy_g)}
serpent_sigma_to_plot_cross_tl_br = { g:[] for g in range(energy_g)}

serpent_arrays_to_plot_cross_tr_bl = { g:[] for g in range(energy_g)}
serpent_sigma_to_plot_cross_tr_bl = { g:[] for g in range(energy_g)}

for g in range(energy_g):
  serpent_arrays_to_plot_cross_tl_br[g].append(serp_flux_normalized["cool1"][g])
  serpent_arrays_to_plot_cross_tl_br[g].append(serp_flux_normalized["fuel_tl"][g])
  serpent_arrays_to_plot_cross_tl_br[g].append(serp_flux_normalized["fuel_br"][g])
  serpent_arrays_to_plot_cross_tl_br[g].append(serp_flux_normalized["cool1"][g])

  serpent_arrays_to_plot_cross_tr_bl[g].append(serp_flux_normalized["cool1"][g])
  serpent_arrays_to_plot_cross_tr_bl[g].append(serp_flux_normalized["fuel_tr"][g])
  serpent_arrays_to_plot_cross_tr_bl[g].append(serp_flux_normalized["fuel_bl"][g])
  serpent_arrays_to_plot_cross_tr_bl[g].append(serp_flux_normalized["cool1"][g])


  serpent_sigma_to_plot_cross_tl_br[g].append(sigma["cool1"][g])
  serpent_sigma_to_plot_cross_tl_br[g].append(sigma["fuel_tl"][g])
  serpent_sigma_to_plot_cross_tl_br[g].append(sigma["fuel_br"][g])
  serpent_sigma_to_plot_cross_tl_br[g].append(sigma["cool1"][g])

  serpent_sigma_to_plot_cross_tr_bl[g].append(sigma["cool1"][g])
  serpent_sigma_to_plot_cross_tr_bl[g].append(sigma["fuel_tr"][g])
  serpent_sigma_to_plot_cross_tr_bl[g].append(sigma["fuel_bl"][g])
  serpent_sigma_to_plot_cross_tr_bl[g].append(sigma["cool1"][g])


# for g in range(energy_g):
#   plt.figure()
#   plt.plot(serpent_arrays_to_plot[g])
#   plt.savefig(f"/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_2r_2g/g{g}_diagonal_serp")

# ---------------------------------------------------------------------------------------



# get diagonal regions to plot -----------------------------------------------------
coarse_nodes_diagonal_hybrid = [map_system[0][0]]
regions_to_plot_tl_br = []
regions_to_plot_tr_bl = []

regions_mat_rel = mesh_info.region_type_rel[1]

regions_to_plot_tl_br.append(regions_mat_rel["coolant_2"])
regions_to_plot_tl_br.append(regions_mat_rel["fuel1_4"])
regions_to_plot_tl_br.append(regions_mat_rel["fuel1_6"])
regions_to_plot_tl_br.append(regions_mat_rel["coolant_2"])

regions_to_plot_tr_bl.append(regions_mat_rel["coolant_2"])
regions_to_plot_tr_bl.append(regions_mat_rel["fuel1_5"])
regions_to_plot_tr_bl.append(regions_mat_rel["fuel1_7"])
regions_to_plot_tr_bl.append(regions_mat_rel["coolant_2"])


shynt_arrays_to_plot_tl_br = { g:[] for g in range(energy_g)}
shynt_arrays_to_plot_tr_bl = { g:[] for g in range(energy_g)}
for r in regions_to_plot_tl_br:
    for g in range(energy_g):
        shynt_arrays_to_plot_tl_br[g].append(shynt_flux_normalized[g][r])

for r in regions_to_plot_tr_bl:
    for g in range(energy_g):
        shynt_arrays_to_plot_tr_bl[g].append(shynt_flux_normalized[g][r])


# for g in range(energy_g):
#   plt.figure()
#   plt.plot(shynt_arrays_to_plot[g])
#   plt.savefig(f"/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_2r_2g/g{energy_g-1-g}_diagonal")

print(serp_flux_normalized)
print(sigma)
print(shynt_flux_normalized)
rr = {"fuel_tl": 4, "fuel_tr": 5, "fuel_br": 6, "fuel_bl": 7, "cool1": 2}
diff = {
  0: {}, 1: {}
}
for reg, flux_n in serp_flux_normalized.items():
  serp_fl_val_fast = flux_n[1]
  shynt_flux_val_fast = shynt_flux_normalized[0][rr[reg]]
  diff_val_fast = (serp_fl_val_fast - shynt_flux_val_fast) / serp_fl_val_fast

  serp_fl_val_therm = flux_n[0]
  shynt_flux_val_therm = shynt_flux_normalized[1][rr[reg]]
  diff_val_therm = (serp_fl_val_therm - shynt_flux_val_therm) / serp_fl_val_therm

  diff[0][reg] = diff_val_fast * 100
  diff[1][reg] = diff_val_therm * 100

raise SystemExit


for g in range(energy_g):
  plt.figure()
  plt.errorbar(
    [0,1,2,3], serpent_arrays_to_plot_cross_tr_bl[g], 
    yerr=np.array(serpent_arrays_to_plot_cross_tr_bl[g])*np.array(serpent_sigma_to_plot_cross_tr_bl[g]), 
    label="Serpent"
  )
  print(serpent_arrays_to_plot_cross_tr_bl[g])
  print(serpent_sigma_to_plot_cross_tr_bl[g])
  print(np.array(serpent_arrays_to_plot_cross_tr_bl[g])*np.array(serpent_sigma_to_plot_cross_tr_bl[g]))
  plt.plot(shynt_arrays_to_plot_tr_bl[energy_g-1-g], label="SHYNT")
  # plt.ylim([0.02, 0.17])
  current_values = plt.gca().get_yticks()
  plt.gca().set_yticklabels(['{:.5f}'.format(x) for x in current_values])
  plt.legend()
  # plt.show()
  plt.savefig(f"{dir_base}g{g}_HYNTvsSerpent_tr_bl")




for g in range(energy_g):
  plt.figure()
  plt.errorbar(
    [0,1,2,3], serpent_arrays_to_plot_cross_tl_br[g], 
    yerr=np.array(serpent_arrays_to_plot_cross_tl_br[g])*np.array(serpent_sigma_to_plot_cross_tl_br[g]), 
    label="Serpent"
  )
  print(serpent_arrays_to_plot_cross_tl_br[g])
  print(serpent_sigma_to_plot_cross_tl_br[g])
  print(np.array(serpent_arrays_to_plot_cross_tl_br[g])*np.array(serpent_sigma_to_plot_cross_tl_br[g]))
  plt.plot(shynt_arrays_to_plot_tl_br[energy_g-1-g], label="SHYNT")
  # plt.ylim([0.02, 0.17])
  current_values = plt.gca().get_yticks()
  plt.gca().set_yticklabels(['{:.5f}'.format(x) for x in current_values])
  plt.legend()
  # plt.show()
  plt.savefig(f"{dir_base}g{g}_HYNTvsSerpent_tl_br")
