from locale import normalize
import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt

from assembly import serp_root_input_file, model_universe
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm


# serp_root_input_file 
energy_g = model_universe.energy_grid.energy_groups

# serpent stuff for comparing fluxes -------------------------------------------------
cells_ids_in_detectors = list(serp_root_input_file.cells_for_flux.keys())
detector_out_file = serp_root_input_file.name + "_det0.m"
serp_flux, serp_errors = postprocess.get_flux_from_detector_file(detector_out_file)
serp_flux_normalized = norm.normalize_serpent_flux(serp_flux, energy_g)



# shynt flux -------------------------------------------------------------------------
input_file_argument = sys.argv[0]
input_file_absolute = str(Path(input_file_argument).absolute())
input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"
shynt_output_file = input_file_dir + "output_RMM/assembly_rmm_flux.csv"
shynt_flux = postprocess.get_flux_from_shynt_output(shynt_output_file)
shynt_flux_normalized = norm.normalize_hybrid_flux(shynt_flux, energy_g)

# get diagonal regions to plot -------------------------------------------------------
regions_diagonal = postprocess.regions_to_plot(model_universe, line="diagonal")

# Ordering arrays to plot ------------------------------------------------------------
serp_array_to_plot = { g:[] for g in range(energy_g)}
shynt_array_to_plot = { g:[] for g in range(energy_g)}
for r in regions_diagonal:
    # get index in serpent results
    s_idx = cells_ids_in_detectors.index(r)
    for g in range(energy_g):
        serp_array_to_plot[g].append(serp_flux_normalized[g][s_idx])
        shynt_array_to_plot[g].append(shynt_flux_normalized[g][r])


plt.figure()
plt.plot(serp_array_to_plot[0])
plt.ylim([0, 0.15])
plt.title("Thermal group - serpent")
plt.savefig("Thermal group - serpent")
plt.show()

plt.figure()
plt.plot(serp_array_to_plot[1])
plt.ylim([0.2, 1.4])
plt.title("Fast group - serpent")
plt.savefig("Fast group - serpent")
plt.show()

# plt.plot(shynt_array_to_plot[0])
# # plt.ylim([0, 12])
# plt.title("Thermal group - hybrid")
# plt.savefig("Thermal group - hybrid")
# plt.show()

# plt.plot(shynt_array_to_plot[1])
# # plt.ylim([0, 2])
# plt.title("Fast group - hybrid")
# plt.savefig("Fast group - hybrid")
# plt.show()

