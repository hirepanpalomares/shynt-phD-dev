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

    # Then the regions of the node ..................................................
    regions_to_plot = []
    for c_id in coarse_nodes_to_plot:
        regions_mat_rel = mesh_info.region_type_rel[c_id]
        coarse_nodes[c_id].getDiagonalRegions()
        # if code == "serp":
        regions_to_plot.append(regions_mat_rel["coolant"])
        regions_to_plot.append(regions_mat_rel["cladding"])
        if "fuel2" in regions_mat_rel:
            regions_to_plot.append(regions_mat_rel["fuel2"])
        if "fuel3" in regions_mat_rel:
            regions_to_plot.append(regions_mat_rel["fuel3"])
        if "fuel5" in regions_mat_rel:
            regions_to_plot.append(regions_mat_rel["fuel5"])
        if "fuel6" in regions_mat_rel:
            regions_to_plot.append(regions_mat_rel["fuel6"])
        regions_to_plot.append(regions_mat_rel["cladding"])
        regions_to_plot.append(regions_mat_rel["coolant"])
    
        # elif code == "hybrid":
        #     regions_to_plot.append(regions_mat_rel["fuel"])
        #     regions_to_plot.append(regions_mat_rel["other"])
        #     regions_to_plot.append(regions_mat_rel["fuel"])

    return coarse_nodes_to_plot


dir_case = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/square_assem_1x1cell_3r_2g/"
# Serpent flux  --------------------------------------------------------------------
detector_out_file = dir_case + "reference/1e5_3000_500/assembly.serp_det0.m"
serp_cool_flux, serp_errors_cool = postprocess.get_flux_from_detector_file(detector_out_file, "1")
serp_clad_flux, serp_errors_clad = postprocess.get_flux_from_detector_file(detector_out_file, "2")
serp_fuel2_flux, serp_errors_fuel2 = postprocess.get_flux_from_detector_file(detector_out_file, "3")
serp_fuel3_flux, serp_errors_fuel3 = postprocess.get_flux_from_detector_file(detector_out_file, "4")
serp_fuel5_flux, serp_errors_fuel5 = postprocess.get_flux_from_detector_file(detector_out_file, "5")
serp_fuel6_flux, serp_errors_fuel6 = postprocess.get_flux_from_detector_file(detector_out_file, "6")


flux = {
    "cool": serp_cool_flux["1"],
    "clad": serp_clad_flux["2"],
    "fuel2": serp_fuel2_flux["3"],
    "fuel3": serp_fuel3_flux["4"], 
    "fuel5": serp_fuel5_flux["5"], 
    "fuel6": serp_fuel6_flux["6"], 
}
sigma = {
    "cool": serp_errors_cool["1"],
    "clad": serp_errors_clad["2"],
    "fuel2": serp_errors_fuel2["3"],
    "fuel3": serp_errors_fuel3["4"], 
    "fuel5": serp_errors_fuel5["5"], 
    "fuel6": serp_errors_fuel6["6"], 
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



# Ordering arrays to plot ------------------------------------------------------------
serp_array_to_plot = { g:[] for g in range(energy_g)}
serp_errors_to_plot = { g:[] for g in range(energy_g)}

shynt_array_to_plot = { g:[] for g in range(energy_g)}

serpent_idx_in_lattice = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
seprent_pin_list_to_plot = [2, 3, 6, 6, 6, 6, 6, 6, 3, 2]
fuel_diagonal = ['fuel2', 'fuel3', 'fuel6', 'fuel6', 'fuel6', 'fuel6', 'fuel6', 'fuel6', 'fuel3', 'fuel2']
for g in range(energy_g):
    for s in range(10):
        fuel = fuel_diagonal[s]
        s_idx = serpent_idx_in_lattice[s]
        # FLUX --------------------------------------------------
        serp_array_to_plot[g].append(serp_flux_normalized['cool'][g][s_idx])
        serp_array_to_plot[g].append(serp_flux_normalized['clad'][g][s_idx])
        serp_array_to_plot[g].append(serp_flux_normalized[fuel][g][s_idx])
        serp_array_to_plot[g].append(serp_flux_normalized['clad'][g][s_idx])
        serp_array_to_plot[g].append(serp_flux_normalized['cool'][g][s_idx])
        # STD DEV ----------------------------------------------
        serp_errors_to_plot[g].append(sigma['cool'][g][s_idx])
        serp_errors_to_plot[g].append(sigma['clad'][g][s_idx])
        serp_errors_to_plot[g].append(sigma[fuel][g][s_idx])
        serp_errors_to_plot[g].append(sigma['clad'][g][s_idx])
        serp_errors_to_plot[g].append(sigma['cool'][g][s_idx])
    serp_array_to_plot[g] = np.array(serp_array_to_plot[g])
    serp_errors_to_plot[g] = np.array(serp_errors_to_plot[g])


coarse_nodes_to_plot = regions_to_plot(model_universe)
regions_to_plot = []
regions_diagonal = [
    21,20,19,20,21,
    65,64,63,64,65,
    109,108,107,108,109,
    153,152,151,152,153,
    197,196,195,196,197,
    241,240,239,240,241,
    285,284,283,284,285,
    329,328,327,328,329,
    373,372,371,372,373,
    417,416,415,416,417
    # 19, 
    # 63, 
    # 107, 
    # 151, 
    # 195, 
    # 239, 
    # 283, 
    # 327, 
    # 371, 
    # 415, 
]
for r in regions_diagonal:
    for g in range(energy_g):
        shynt_array_to_plot[g].append(shynt_flux_normalized[g][r])

x = np.arange(50)


# % difference vs Serpent
difference_shynt_serp = {}
for g in range(energy_g):
    diff = np.abs(np.array(shynt_array_to_plot[energy_g-1-g]) - np.array(serp_array_to_plot[g])) / np.array(serp_array_to_plot[g])
    difference_shynt_serp[g] = diff * 100


# Thermal -group --------------------------------------------------------------
# plt.figure()
fig, ax = plt.subplots()
ax.errorbar(x, serp_array_to_plot[0], yerr=serp_errors_to_plot[0]*serp_array_to_plot[0], label="Serpent")
ax.plot(shynt_array_to_plot[1], label="SHYNT")
ax.legend()
fig.savefig(dir_case + "Thermal-SHYNTvsSerpent")
# plt.show()

plt.figure()
plt.plot(difference_shynt_serp[0], marker="o", color="green")
plt.ylabel("% err")
plt.savefig(dir_case + "Thermal-SHYNTvsSerpent_difference")


# Fast group ---------------------------------------
fig, ax = plt.subplots()
ax.errorbar(x, serp_array_to_plot[1], yerr=serp_errors_to_plot[1]*serp_array_to_plot[1], label="Serpent")
ax.plot(shynt_array_to_plot[0], label="SHYNT")
ax.legend()
fig.savefig(dir_case+ "Fast-SHYNTvsSerpent")


plt.figure()
plt.plot(difference_shynt_serp[1], marker="o", color="green")
plt.ylabel("% err")
plt.savefig(dir_case + "Fast-SHYNTvsSerpent_difference")

