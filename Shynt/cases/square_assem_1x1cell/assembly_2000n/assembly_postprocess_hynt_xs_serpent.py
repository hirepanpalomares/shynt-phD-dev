import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
from api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice
from api_py.Mesh.mesh_info import MeshInfo
import numpy as np

from assembly import model_universe
from assembly_generate_serp_root_file import serp_root_input_file
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm

from hy_fluxes import flux_map as hy_flux

"""
    This file generates the plots for the scalar flux
    of Hynt vs Matlab
"""

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


# serp_root_input_file 
energy_g = model_universe.energy_grid.energy_groups

# serpent fluxes for comparing fluxes -------------------------------------------------
cells_ids_in_detectors = list(serp_root_input_file.cells_for_flux.keys())
detector_out_file = serp_root_input_file.name + "_det0.m"
serp_flux, serp_errors = postprocess.get_flux_from_detector_file(detector_out_file, "flux_by_cell_by_group")
serp_flux = serp_flux["flux_by_cell_by_group"]
serp_flux_normalized = norm.normalize_serpent_flux(serp_flux, energy_g)



# shynt flux -------------------------------------------------------------------------
input_file_argument = sys.argv[0]
input_file_absolute = str(Path(input_file_argument).absolute())
input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"
shynt_output_file = input_file_dir + "output_RMM/assembly_rmm_flux.csv"
shynt_flux = postprocess.get_flux_from_shynt_output(shynt_output_file)
shynt_flux_normalized = norm.normalize_hybrid_flux(shynt_flux, energy_g)

# get diagonal regions to plot -------------------------------------------------------
regions_diagonal_serp = postprocess.regions_to_plot(model_universe, line="diagonal", code="serp")
regions_diagonal_hybrid = postprocess.regions_to_plot(model_universe, line="diagonal", code="serp")

# Ordering arrays to plot ------------------------------------------------------------
serp_array_to_plot = { g:[] for g in range(energy_g)}
serp_errors_to_plot = { g:[] for g in range(energy_g)}

shynt_array_to_plot = { g:[] for g in range(energy_g)}
huaqian_array_to_plot  = { g:[] for g in range(energy_g)}

for r in regions_diagonal_serp:
    # get index in serpent results
    s_idx = cells_ids_in_detectors.index(r)
    for g in range(energy_g):
        serp_array_to_plot[g].append(serp_flux_normalized[g][s_idx])
        serp_errors_to_plot[g].append(serp_errors["flux_by_cell_by_group"][g][s_idx])

# for i in range(10):
#     for g in range(energy_g):
#         fuel_flux = hy_flux[g][i][i][0]
#         cool_flux = hy_flux[g][i][i][1]
#         arr = [fuel_flux, cool_flux, fuel_flux]
#         huaqian_array_to_plot[g] += arr


for r in regions_diagonal_hybrid:
    # get index in serpent results
    s_idx = cells_ids_in_detectors.index(r)
    for g in range(energy_g):
        shynt_array_to_plot[g].append(shynt_flux_normalized[g][r])

x = np.arange(len(serp_array_to_plot[0]))

difference_shynt_matlab = {

}

# for g in range(energy_g):
#     diff = np.abs(np.array(shynt_array_to_plot[g]) - np.array(huaqian_array_to_plot[g])) / np.array(shynt_array_to_plot[g])
#     difference_shynt_matlab[g] = diff * 100

plt.figure()
# plt.errorbar(x, serp_array_to_plot[0], yerr=serp_errors_to_plot[0], label="Serpent")
plt.plot(shynt_array_to_plot[0], label="HYNT")
# plt.ylim([0.02, 0.17])
plt.title("Thermal group")
plt.legend()
plt.savefig("Thermal group - HYNT")
# plt.show()

plt.figure()
# plt.errorbar(x, serp_array_to_plot[1], yerr=serp_errors_to_plot[1], label="Serpent")
plt.plot(shynt_array_to_plot[1], label="HYNT")
# plt.ylim([0.2, 1.4])
plt.title("Fast group")
plt.legend()
plt.savefig("Fast group - HYNT")
# plt.show()


# Comparison with HY -------------------------------------------------------------------------
# fig, ax = plt.subplots()
# ax.plot(shynt_array_to_plot[0], label="Shynt")
# ax.plot(huaqian_array_to_plot[0], label="Matlab")
# ax2 = ax.twinx()
# ax2.plot(difference_shynt_matlab[0], marker="o", color="green")
# ax2.set_ylim([0, 2])
# ax2.set_ylabel("% diff")
# plt.title("Fast group - Shynt vs Matlab SP_equisurf")
# ax.legend()
# fig.savefig("Fast group - Shynt vs Matlab SP_equisurf")
# plt.show()


# fig, ax = plt.subplots()
# ax.plot(shynt_array_to_plot[1], label="Shynt")
# ax.plot(huaqian_array_to_plot[1], label="Matlab")
# ax2 = ax.twinx()
# ax2.plot(difference_shynt_matlab[1], marker="o", color="green")
# ax2.set_ylim([0, 2])
# ax2.set_ylabel("% diff")
# plt.title("Thermal group - Shynt vs Matlab SP_equisurf")
# ax.legend()
# fig.savefig("Thermal group - Shynt vs Matlab SP_equisurf")
# plt.show()
