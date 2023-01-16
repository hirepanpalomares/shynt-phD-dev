import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from Shynt.api_py.Postprocess import process_files as postprocess



energy_g = 8


def pin3r():
 

  dir_base = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_3r_8g/"

  detector_out_file = dir_base + "reference/reference_calc_3r_8g.serp_det0.m"
  serp_fuel_flux, serp_errors_fuel = postprocess.get_flux_from_detector_file(detector_out_file, "1")
  serp_clad_flux, serp_errors_clad = postprocess.get_flux_from_detector_file(detector_out_file, "2")
  serp_cool_flux, serp_errors_cool = postprocess.get_flux_from_detector_file(detector_out_file, "3")


  flux = {"fuel": serp_fuel_flux["1"], "clad": serp_clad_flux["2"], "cool": serp_cool_flux["3"]}
  sigma = {"fuel": serp_errors_fuel["1"], "clad": serp_errors_clad["2"], "cool": serp_errors_cool["3"]}

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
    serpent_arrays_to_plot[g].append(serp_flux_normalized["clad"][g])
    serpent_arrays_to_plot[g].append(serp_flux_normalized["fuel"][g])
    serpent_arrays_to_plot[g].append(serp_flux_normalized["clad"][g])
    serpent_arrays_to_plot[g].append(serp_flux_normalized["cool"][g])

    serpent_sigma_to_plot[g].append(sigma["cool"][g])
    serpent_sigma_to_plot[g].append(sigma["clad"][g])
    serpent_sigma_to_plot[g].append(sigma["fuel"][g])
    serpent_sigma_to_plot[g].append(sigma["clad"][g])
    serpent_sigma_to_plot[g].append(sigma["cool"][g])
  
  return serpent_arrays_to_plot


def pin2r():
  dir_base = "/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_2r_8g/"

  detector_out_file = dir_base + "reference_calculation/moreParticles_test/2e6.serp_det0.m"
  serp_fuel_flux, serp_errors_fuel = postprocess.get_flux_from_detector_file(detector_out_file, "1")
  serp_cool_flux, serp_errors_cool = postprocess.get_flux_from_detector_file(detector_out_file, "2")

  flux = {"fuel": serp_fuel_flux["1"], "cool": serp_cool_flux["2"]}
  sigma = {"fuel": serp_errors_fuel["1"], "cool": serp_errors_cool["2"]}

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
  
  return serpent_arrays_to_plot


serp_flx_pin_3r = pin3r()
serp_flx_pin_2r = pin2r()


for g in range(energy_g):
  plt.figure()
  plt.plot(serp_flx_pin_3r[g], label="3r")
  plt.plot([0,2,4], np.array(serp_flx_pin_2r[g]), label="2r")
 
  plt.legend()
  plt.savefig(f"/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hexagonal_pin_no_hollow_3r_8g/comparing_3r_2r/g{g}_serpent_2r_3r")