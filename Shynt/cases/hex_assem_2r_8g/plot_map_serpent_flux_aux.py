from locale import normalize
import numpy as np
import matplotlib as mpl
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Geometry.mesh_info import MeshInfo
from hex_assem import root_universe
from Shynt.api_py.Postprocess import normalize as norm
from Shynt.api_py.Drawer.cell_drawing import plot_cell
from hex_assem import assembly_cell


energy_g = 8
# Serpent flux  --------------------------------------------------------------------
detector_out_file = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_assem_no_hollow/reference_calc_hexagon_assembly_noHollow_8g/if_assembly_noHollow_det0.m"
serp_fuel_flux, serp_errors_fuel = postprocess.get_flux_from_detector_file(detector_out_file, "1")
serp_He_flux, serp_errors_He = postprocess.get_flux_from_detector_file(detector_out_file, "2")
serp_clad_flux, serp_errors_clad = postprocess.get_flux_from_detector_file(detector_out_file, "3")
serp_Na_flux, serp_errors_Na = postprocess.get_flux_from_detector_file(detector_out_file, "4")

flux = {"inner_fuel": serp_fuel_flux["1"], "helium_gas": serp_He_flux["2"], "cladding": serp_clad_flux["3"], "na_coolant": serp_Na_flux["4"]}
uncertainties = {"inner_fuel": serp_errors_fuel["1"], "helium_gas": serp_errors_He["2"], "cladding": serp_errors_clad["3"], "na_coolant": serp_errors_Na["4"]}

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


map_serpent = np.arange(0,441).reshape((21,21))
map_system = mesh_info.coarse_nodes_map

serp_flux_plot = {g: {} for g in range(energy_g)}
serp_uncert_plot = {g: {} for g in range(energy_g)}
for row in range(21):
  for col in range(21):
    c_id = map_system[row][col]
    if c_id is not None:
      serp_c_id = map_serpent[row][col]
      regions_mat_rel = mesh_info.region_type_rel[c_id]
      for material, r_id in regions_mat_rel.items():
        for g in range(energy_g):
          serp_f = serp_flux_normalized[material][g][serp_c_id]
          serp_uncert = uncertainties[material][g][serp_c_id]
          serp_flux_plot[g][r_id] = serp_f
          serp_uncert_plot[g][r_id] = serp_uncert

a = 0

flux_colors, normalize, cmap = norm.normalized_flux_colors_by_group(serp_flux_plot, energy_g)
uncert_colors, normalize_uncert, cmap_uncert = norm.normalized_flux_colors_by_whole(serp_uncert_plot, energy_g, color_map="inferno")

print(flux_colors)


# raise SystemExit
# for g in range(1):

g_plot = 1


# Fluxc plots- -------------------------------------------------------------
plot_cell(
  assembly_cell,
  dimensions=(7000,7000),
  name=f"hex_lattice_noHollow_g{g_plot}_serp",
  cell_colors=flux_colors[g_plot]
)

fig=mpl.pyplot.figure(figsize=(8,3))
ax=fig.add_subplot(111)
cb = mpl.colorbar.ColorbarBase(
  ax, 
  cmap=cmap,   
  norm=normalize[g_plot],
  spacing='uniform',
  orientation='horizontal',
  extend='neither',
)
mpl.pyplot.savefig(f"hex_lattice_noHollow_g{g_plot}_serp_COLORMAP.png")



