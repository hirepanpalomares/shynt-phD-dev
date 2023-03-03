import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Shynt.api_py.Postprocess import process_files as postprocess

base_dir = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hex_pin_pie/pie_cladding/'
# HYBRID ---------------------------------------------------------------------------------------------
flux_df_1_000 = pd.read_csv(base_dir + 'output_RMM_1_000/_rmm_flux.csv')
# print(flux_df_1_000)
flux_hyb_1_000 = {}
for g in range(1,9):
  flux_hyb_1_000[g] = flux_df_1_000[flux_df_1_000["Energy_group"] == g]['scalar_flux'].to_numpy()

norm_factor_hyb = flux_hyb_1_000[1].max()
for g in range(1,9):
  flux_hyb_1_000[g] /= norm_factor_hyb

#################################
flux_df_50_000 = pd.read_csv(base_dir + 'output_RMM_50_000/50_000_rmm_flux.csv')
# print(flux_df_50_000)
flux_hyb_50_000 = {}
norm_factor_hyb = 0
for g in range(1,9):
  flx_arr_g = flux_df_50_000[flux_df_50_000["Energy_group"] == g]['scalar_flux'].to_numpy()
  flux_hyb_50_000[g] = flx_arr_g
  if flx_arr_g.max() > norm_factor_hyb:
    norm_factor_hyb = flx_arr_g.max()

print(norm_factor_hyb)
for g in range(1,9):
  flux_hyb_50_000[g] /= norm_factor_hyb

# Serpent --------------------------------------------------------------------------------------------
detector_out_file = base_dir + "reference/10_000/ref.serp_det0.m"
det_names = [
  'fuel',
  'cl_tl',
  'cl_tr',
  'cl_br',
  'cl_bl',
  'coolant',
]
flux_serp = {}
sigma_serp = {}

norm_factor_serp = 0
for dn in det_names:
  fl, err = postprocess.get_flux_from_detector_file(detector_out_file, dn)
  flux_serp[dn] = np.zeros(8)
  sigma_serp[dn] = np.zeros(8)

  fl_array = np.flip(fl[dn],0)
  max_ = fl_array.max()
  if max_ > norm_factor_serp: norm_factor_serp = max_
  fl[dn] = fl_array
  err[dn] = np.flip(err[dn],0)

  for g in range(8):
    flux_serp[dn][g] = fl[dn][g]
    sigma_serp[dn][g] = err[dn][g]

print(norm_factor_serp)
for dn in det_names:
  flux_serp[dn] /= norm_factor_serp

# ---------------------------------------------------------------------------------------------------

diag1 = [5,1,0,3,5]
diag2 = [5,2,0,4,5]

for g in range(8):
  diag1_hyb = [flux_hyb_50_000[g+1][idx] for idx in diag1]
  diag2_hyb = [flux_hyb_50_000[g+1][idx] for idx in diag2]

  diag1_serp = [flux_serp[det_names[idx]][g] for idx in diag1]
  diag2_serp = [flux_serp[det_names[idx]][g] for idx in diag2]


  plt.figure()
  plt.plot(diag1_hyb, '-o', label='hybrid')
  plt.plot(diag1_serp, '--o', label='serpent')
  plt.title(f'Diagonal left-top --> right-down (G{g})')
  plt.legend()
  plt.savefig(f"diag1_G{g}.png")


  plt.figure()
  plt.plot(diag2_hyb, '-o', label='hybrid')
  plt.plot(diag2_serp, '--o', label='serpent')
  plt.title(f'Diagonal left-right --> left-down (G{g})')
  plt.legend()
  plt.savefig(f"diag2_G{g}.png")


