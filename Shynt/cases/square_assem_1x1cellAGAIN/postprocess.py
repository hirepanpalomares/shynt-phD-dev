import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from assembly import model_universe

from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import SquareLattice, HexagonalLatticeTypeX

from Shynt.cases.square_assem_1x1cellAGAIN.hy_fluxes import getHYFlux
from Shynt.cases.square_assem_1x1cell_3r_2g.assembly import assembly_10x10
from Shynt.cases.square_assem_1x1cell_3r_2g.assembly import model_universe
from Shynt.cases.square_assem_1x1cell_3r_2g.assembly import energy_grid

energy_g = energy_grid.energy_groups

def regions_to_plot(root_universe, line="diagonal", code=""):
    # Extracting cells from root model
    model_cell = root_universe.model_cell
    outside_cell = root_universe.outside_cell
    lattice = model_cell.content

    coarse_nodes = model_cell.global_mesh.coarse_nodes
    coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
    fine_nodes = model_cell.local_mesh.fine_nodes

    # Generating mesh info
    mesh_info = MeshInfo (coarse_nodes, fine_nodes, coarse_nodes_map)
    if isinstance(model_cell.content, SquareLattice):
        mesh_info.type_system = "square"
    elif isinstance(model_cell.content, HexagonalLatticeTypeX):
        mesh_info.type_system = "hexagonal"
    elif isinstance(model_cell.content, HexagonalLatticeTypeX):
        mesh_info.type_system = "hexagonal"
            

    map_system = mesh_info.coarse_nodes_map

    # First the coarse nodes ........................................................
    coarse_nodes_to_plot = []
    if mesh_info.type_system == "square":
        coarse_nodes_to_plot = [map_system[c][c] for c in range(len(map_system))]
    elif mesh_info.type_system == "hexagonal":
        coarse_nodes_to_plot = [map_system[c][10] for c in range(1,len(map_system)-1)]


    return coarse_nodes_to_plot

dir_case = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/square_assem_1x1cellAGAIN"

# Serpent flux  --------------------------------------------------------------------
detector_out_file = dir_case + "/reference/root_universe.serp_det0.m"
serp_cool_flux, serp_errors_cool = postprocess.get_flux_from_detector_file(detector_out_file, "1")
serp_fuel2_flux, serp_errors_fuel2 = postprocess.get_flux_from_detector_file(detector_out_file, "2")
serp_fuel3_flux, serp_errors_fuel3 = postprocess.get_flux_from_detector_file(detector_out_file, "3")
serp_fuel5_flux, serp_errors_fuel5 = postprocess.get_flux_from_detector_file(detector_out_file, "4")
serp_fuel6_flux, serp_errors_fuel6 = postprocess.get_flux_from_detector_file(detector_out_file, "5")


flux = {
    "cool": serp_cool_flux["1"],
    "fuel2": serp_fuel2_flux["2"],
    "fuel3": serp_fuel3_flux["3"], 
    "fuel5": serp_fuel5_flux["4"], 
    "fuel6": serp_fuel6_flux["5"], 
}
sigma = {
    "cool": serp_errors_cool["1"],
    "fuel2": serp_errors_fuel2["2"],
    "fuel3": serp_errors_fuel3["3"], 
    "fuel5": serp_errors_fuel5["4"], 
    "fuel6": serp_errors_fuel6["5"], 
}

normalize_factor = -1000
for type_flux, f in flux.items():
  # Fastest flux = [-1]
  fast_flux = f[energy_g-1].max()
  if fast_flux > normalize_factor:
    normalize_factor = fast_flux

for type_flux, f in flux.items():
  flux[type_flux] = f/normalize_factor
# flux is now normalized
serp_flux_normalized = flux



# shynt flux -------------------------------------------------------------------------
shynt_output_file = dir_case + "/output_RMM/_rmm_flux.csv"
shynt_flux = postprocess.get_flux_from_shynt_output(shynt_output_file)
shynt_flux_normalized = norm.normalize_hybrid_flux(shynt_flux, energy_g)


# Huaiqian flux ----------------------------------------------------------------------
hy_flux = getHYFlux()


# Ordering arrays to plot ------------------------------------------------------------

# SERPENT ---
serp_array_to_plot = { g:[] for g in range(energy_g)}
serp_errors_to_plot = { g:[] for g in range(energy_g)}
serpent_idx_in_lattice = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
seprent_pin_list_to_plot = [2, 3, 6, 6, 6, 6, 6, 6, 3, 2]
fuel_diagonal = ['fuel2', 'fuel3', 'fuel6', 'fuel6', 'fuel6', 'fuel6', 'fuel6', 'fuel6', 'fuel3', 'fuel2']
for g in range(energy_g):
    for s in range(10):
        fuel = fuel_diagonal[s]
        s_idx = serpent_idx_in_lattice[s]
        # FLUX --------------------------------------------------
        serp_array_to_plot[g].append(serp_flux_normalized['cool'][g][s_idx])
        serp_array_to_plot[g].append(serp_flux_normalized[fuel][g][s_idx])
        serp_array_to_plot[g].append(serp_flux_normalized['cool'][g][s_idx])
        # STD DEV ----------------------------------------------
        serp_errors_to_plot[g].append(sigma['cool'][g][s_idx])
        serp_errors_to_plot[g].append(sigma[fuel][g][s_idx])
        serp_errors_to_plot[g].append(sigma['cool'][g][s_idx])
    serp_array_to_plot[g] = np.array(serp_array_to_plot[g])
    serp_errors_to_plot[g] = np.array(serp_errors_to_plot[g])


# SHYNT ---
shynt_array_to_plot = { g:[] for g in range(energy_g)}
coarse_nodes_to_plot = regions_to_plot(model_universe)
regions_to_plot = []
regions_diagonal = [
    14,13,14,
    47,46,47,
    80,79,80,
    113,112,113,
    146,145,146,
    179,178,179,
    212,211,212,
    245,244,245,
    278,277,278,
    311,310,311
]
for r in regions_diagonal:
    for g in range(energy_g):
        shynt_array_to_plot[g].append(shynt_flux_normalized[g][r])

# MATLAB ---
matlab_array_to_plot = { g:[] for g in range(energy_g)}
for g in range(energy_g):
    for p in range(10):
        matlab_pin_flux = hy_flux[g][p][p]
        fuel_flx = matlab_pin_flux[0]
        cool_flx = matlab_pin_flux[1]
        matlab_array_to_plot[g].append(cool_flx)
        matlab_array_to_plot[g].append(fuel_flx)
        matlab_array_to_plot[g].append(cool_flx)




x = np.arange(30)


# for g in range(energy_g):
#     diff = np.abs(np.array(shynt_array_to_plot[g]) - np.array(huaqian_array_to_plot[g])) / np.array(shynt_array_to_plot[g])
#     difference_shynt_matlab[g] = diff * 100

plt.figure()
plt.errorbar(x, serp_array_to_plot[0], yerr=serp_errors_to_plot[0]*serp_array_to_plot[0], label="Serpent")
# plt.plot(shynt_array_to_plot[1], label="SHYNT")
# plt.ylim([0.02, 0.17])
plt.title("Thermal group SHYNT vs SERPENT")
plt.legend()
plt.savefig(dir_case + "/Thermal_group-Serpent")
# plt.show()

plt.figure()
plt.errorbar(x, serp_array_to_plot[1], yerr=serp_errors_to_plot[1]*serp_array_to_plot[1], label="Serpent")
# plt.plot(shynt_array_to_plot[0], label="SHYNT")
# plt.ylim([0.2, 1.4])
plt.title("Fast group SHYNT vs SERPENT")
plt.legend()
plt.savefig(dir_case + "/Fast_group-Serpent")
# plt.show()


# Comparison with HY -------------------------------------------------------------------------
fig, ax = plt.subplots()
ax.plot(shynt_array_to_plot[0], label="Shynt")
ax.plot(matlab_array_to_plot[0], label="Matlab")
# ax2 = ax.twinx()
# ax2.plot(difference_shynt_matlab[0], marker="o", color="green")
# ax2.set_ylim([0, 2])
# ax2.set_ylabel("% diff")
plt.title("Fast group - Shynt vs Matlab")
ax.legend()
fig.savefig(dir_case +"/Fast_group-Shynt_vs_Matlab")
# plt.show()


fig, ax = plt.subplots()
ax.plot(shynt_array_to_plot[1], label="Shynt")
ax.plot(matlab_array_to_plot[1], label="Matlab")
# ax2 = ax.twinx()
# ax2.plot(difference_shynt_matlab[1], marker="o", color="green")
# ax2.set_ylim([0, 2])
# ax2.set_ylabel("% diff")
plt.title("Thermal group - Shynt vs Matlab")
ax.legend()
fig.savefig(dir_case +"/Thermal_group-Shynt_vs_Matlab")
# plt.show()
