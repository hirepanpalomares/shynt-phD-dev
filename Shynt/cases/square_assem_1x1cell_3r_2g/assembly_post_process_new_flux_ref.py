import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from assembly import model_universe
from assembly_generate_serp_root_file import serp_root_input_file
from Shynt.api_py.Postprocess import process_files as postprocess
from Shynt.api_py.Postprocess import normalize as norm

"""
    This script generates the plots of the scalar flux along the diagonal
    of the square assembly problem. 

    It compares the fluxes between Hynt and  Serpent
"""
def order_serp_flux(flux, errors, energy_g):    
    """
        This function orders the serpent flux and errors extracted from 
        a detector output file that was obtained wiht a lattice detector 
        (det dl) each key of detectors is a reference to the material

        Fluxes in the detector output are written from left to right and
        from top to bottom
    """
    assembly = [
        [2, 2, 3, 5, 5, 5, 5, 3, 2, 2],
        [2, 3, 5, 6, 6, 6, 6, 5, 3, 2],
        [3, 5, 6, 6, 6, 6, 6, 6, 5, 3],
        [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [3, 5, 6, 6, 6, 6, 6, 6, 5, 3],
        [2, 3, 5, 6, 6, 6, 6, 5, 3, 2],
        [2, 2, 3, 5, 5, 5, 5, 3, 2, 2],
    ]
    detectors_material_ratio = {
        'coolant': '1',
        'fuel2': '2',
        'fuel3': '3',
        'fuel5': '4',
        'fuel6': '5'
    }

    pin_fuel_ratio = {
        2: "fuel2",
        3: "fuel3",
        5: "fuel5",
        6: "fuel6",
    }
    new_flux = [
        [],
        []
    ]

    new_error = [
        [],
        []
    ]

    for g in range(2):
        f_index= 0
        for r in range(10):
            for c in range(10):
                pin = assembly[r][c]
                fuel_type = pin_fuel_ratio[pin]
                det_fuel = detectors_material_ratio[fuel_type]

                coolant_f = flux['1'][g][f_index]
                fuel_f = flux[det_fuel][g][f_index]
                coolant_e = errors['1'][g][f_index]
                fuel_e = errors[det_fuel][g][f_index]

                new_flux[g].append(fuel_f)
                new_flux[g].append(coolant_f)
                new_error[g].append(fuel_e)
                new_error[g].append(coolant_e)

                f_index += 1

    return np.array(new_flux), np.array(new_error)


energy_g = model_universe.energy_grid.energy_groups

# serpent stuff for comparing fluxes -------------------------------------------------

cells_ids_in_detectors = list(serp_root_input_file.cells_for_flux.keys())

detector_out_file = "/home/hirepan/Documents/chalmers/benchmarck-cases/shynt/single_assem_1x1cell/assembly_2000n/serpent_files/ref_flux/root_universe.serp_det0.m"
serp_flux, serp_errors = postprocess.get_flux_from_detector_file(detector_out_file, '1', '2', '3', '4', '5')
new_serp_flux, new_serp_errors = order_serp_flux(serp_flux, serp_errors, energy_g)
serp_flux_normalized = norm.normalize_serpent_flux(new_serp_flux, energy_g)


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
for r in regions_diagonal_serp:
    # get index in serpent results
    s_idx = cells_ids_in_detectors.index(r)
    for g in range(energy_g):
        serp_array_to_plot[g].append(serp_flux_normalized[g][s_idx])
        serp_errors_to_plot[g].append(new_serp_errors[g][s_idx])


for r in regions_diagonal_hybrid:
    # get index in serpent results
    s_idx = cells_ids_in_detectors.index(r)
    for g in range(energy_g):
        shynt_array_to_plot[g].append(shynt_flux_normalized[g][r])

difference_shynt_serpent = {

}
for g in range(energy_g):
    diff = np.abs(np.array(shynt_array_to_plot[g]) - np.array(serp_array_to_plot[g])) / np.array(serp_array_to_plot[g])
    difference_shynt_serpent[g] = diff * 100

x = np.arange(len(serp_array_to_plot[0]))

fig, ax = plt.subplots()
ax.plot(shynt_array_to_plot[0], label="Hynt")
ax.plot(serp_array_to_plot[0], label="Serpent")
ax2 = ax.twinx()
ax2.plot(difference_shynt_serpent[0], marker="o", color="green")
ax2.set_ylim([0, 2])
ax2.set_ylabel("% diff")
plt.title("Thermal group - Shynt vs Serpent")
ax.legend()
fig.savefig("Termal group - Hynt vs Serpent")


fig, ax = plt.subplots()
ax.plot(shynt_array_to_plot[1], label="Hynt")
ax.plot(serp_array_to_plot[1], label="Serpent")
ax2 = ax.twinx()
ax2.plot(difference_shynt_serpent[1], marker="o", color="green")
ax2.set_ylim([0, 3])
ax2.set_ylabel("% diff")
plt.title("Fast group - Hynt vs Serpent")
ax.legend()
fig.savefig("Fast group - Hynt vs Serpent")


