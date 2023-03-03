import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Shynt.api_py.Postprocess import process_files as postprocess

base_dir = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hex_pin_pie/pie_cladding_coolant_fuel/'


# Serpent --------------------------------------------------------------------------------------------
detector_out_files = {
  "25_000": base_dir + "reference/25_000/ref.serp_det0.m",
  "50_000": base_dir + "reference/50_000/ref.serp_det0.m",
  "100_000": base_dir + "reference/100_000/ref.serp_det0.m",
  "200_000": base_dir + "reference/200_000/ref.serp_det0.m",
  "300_000": base_dir + "reference/300_000/ref.serp_det0.m",
  "400_000": base_dir + "reference/400_000/ref.serp_det0.m",
  "500_000": base_dir + "reference/500_000/ref.serp_det0.m",
}

det_names = [
  'f_tl',
  'f_tr',
  'f_br',
  'f_bl',
  'cl_tl',
  'cl_tr',
  'cl_br',
  'cl_bl',
  'na_tl',
  'na_tr',
  'na_br',
  'na_bl',
]
flux_serp = {}
sigma_serp = {}


for npart, out_file in detector_out_files.items():
  flux_serp[npart] = {}
  sigma_serp[npart] = {}
  norm_factor_serp = 0
  for dn in det_names:
    fl, err = postprocess.get_flux_from_detector_file(out_file, dn)
    flux_serp[npart][dn] = np.zeros(8)
    sigma_serp[npart][dn] = np.zeros(8)

    fl_array = np.flip(fl[dn],0)
    max_ = fl_array.max()
    if max_ > norm_factor_serp: norm_factor_serp = max_
    fl[dn] = fl_array
    err[dn] = np.flip(err[dn],0)
    for g in range(8):
      flux_serp[npart][dn][g] = fl[dn][g]
      sigma_serp[npart][dn][g] = err[dn][g]


  print(norm_factor_serp)
  for dn in det_names:
    flux_serp[npart][dn] /= norm_factor_serp

# ---------------------------------------------------------------------------------------------------

diag1 = [8,4,0,2,6,10]
diag2 = [9,5,1,3,7,11]

for g in range(8):
  plt.figure()
  for npart, out_file in detector_out_files.items():
    diag1_serp = [flux_serp[npart][det_names[idx]][g] for idx in diag1]
    plt.plot(diag1_serp, '--o', label=npart)
    plt.title(f'Diagonal left-top --> right-down (G{g})')
    plt.legend()
  plt.savefig(f"diag1_G{g}_ref.png")
  
  plt.figure()
  for npart, out_file in detector_out_files.items():
    diag2_serp = [flux_serp[npart][det_names[idx]][g] for idx in diag2]
    plt.plot(diag2_serp, '--o', label=npart)
    plt.title(f'Diagonal right-top --> left-down (G{g})')
    plt.legend()
  plt.savefig(f"diag2_G{g}_ref.png")



