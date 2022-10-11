import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from hex_assem import assembly_cell
from hex_assem import root_universe
from hex_assem import energy_grid

import Shynt
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm
from Shynt.api_py.Drawer.cell_drawing import plot_cell
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice


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


energy_g = energy_grid.energy_groups


dir_case = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_assem_no_hollow_2r_2g"


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

# SHYNT fluxes --------------------------------
input_file_argument = sys.argv[0]
input_file_absolute = str(Path(input_file_argument).absolute())
input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"
shynt_output_file = input_file_dir + "output_RMM/run_hex_assem_rmm_flux.csv"
shynt_flux = postprocess.get_flux_from_shynt_output(shynt_output_file)
shynt_flux_normalized = norm.normalize_hybrid_flux(shynt_flux, energy_g)


# Serpent flux  --------------------------------------------------------------------
# detector_out_file = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_assem_no_hollow/reference_calc_hexagon_assembly_noHollow_8g/if_assembly_noHollow_det0.m"
# serp_fuel_flux, serp_errors_fuel = postprocess.get_flux_from_detector_file(detector_out_file, "1")
# serp_He_flux, serp_errors_He = postprocess.get_flux_from_detector_file(detector_out_file, "2")
# serp_clad_flux, serp_errors_clad = postprocess.get_flux_from_detector_file(detector_out_file, "3")
# serp_Na_flux, serp_errors_Na = postprocess.get_flux_from_detector_file(detector_out_file, "4")

# flux = {"fuel": serp_fuel_flux["1"], "gap": serp_He_flux["2"], "clad": serp_clad_flux["3"], "cool": serp_Na_flux["4"]}
# normalize_factor = -1000
# for type_flux, f in flux.items():
#   # Fastest flux = [-1]
#   fast_flux = f[energy_g-1]
#   max_ = np.max(fast_flux)
#   if max_ > normalize_factor:
#     normalize_factor = max_
# for type_flux, f in flux.items():
#   flux[type_flux] = f/normalize_factor
# # flux is now normalized
# serp_flux_normalized = flux


# mmm = np.arange(0,441).reshape((21,21))
# coarse_node_to_plot_serpent = [mmm[c][10] for c in range(1,len(mmm)-1)]

# serpent_arrays_to_plot = { g:[] for g in range(energy_g)}
# for g in range(energy_g):
#   for c_id in coarse_node_to_plot_serpent:
    # serpent_arrays_to_plot[g].append(serp_flux_normalized["cool"][g][c_id])
    # serpent_arrays_to_plot[g].append(serp_flux_normalized["clad"][g][c_id])
    # serpent_arrays_to_plot[g].append(serp_flux_normalized["gap"][g][c_id])
    # serpent_arrays_to_plot[g].append(serp_flux_normalized["fuel"][g][c_id])
    # serpent_arrays_to_plot[g].append(serp_flux_normalized["gap"][g][c_id])
    # serpent_arrays_to_plot[g].append(serp_flux_normalized["clad"][g][c_id])
    # serpent_arrays_to_plot[g].append(serp_flux_normalized["cool"][g][c_id])

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
coarse_nodes_diagonal_hybrid = [map_system[c][10] for c in range(1,len(map_system)-1)]
regions_to_plot = []
for c_id in coarse_nodes_diagonal_hybrid:
  regions_mat_rel = mesh_info.region_type_rel[c_id]
  regions_to_plot.append(regions_mat_rel["na_coolant"])
  regions_to_plot.append(regions_mat_rel["inner_fuel"])
  regions_to_plot.append(regions_mat_rel["na_coolant"])


shynt_arrays_to_plot = { g:[] for g in range(energy_g)}
for r in regions_to_plot:
    for g in range(energy_g):
        shynt_arrays_to_plot[g].append(shynt_flux_normalized[g][r])


for g in range(energy_g):
  plt.figure()
  plt.plot(shynt_arrays_to_plot[g])
  plt.savefig(f"g{g}_diagonal")

# flux_colors, normalize, cmap = norm.normalized_flux_colors_by_group(shynt_flux_normalized, energy_g)

# print(flux_colors)


# raise SystemExit

# g_plot = 0
# plot_cell(
#   assembly_cell,
#   dimensions=(7000,7000),
#   name=f"hex_lattice_noHollow_HYBRID_2r_g{g_plot}",
#   cell_colors=flux_colors[g_plot]
# )

# fig=mpl.pyplot.figure(figsize=(8,3))
# ax=fig.add_subplot(111)
# cb = mpl.colorbar.ColorbarBase(
#   ax, 
#   cmap=cmap,   
#   norm=normalize[g_plot],
#   spacing='uniform',
#   orientation='horizontal',
#   extend='neither',
# )
# mpl.pyplot.savefig(f"hex_lattice_noHollow_HYBRID_2r_g{g_plot}_COLORMAP.png")
  
