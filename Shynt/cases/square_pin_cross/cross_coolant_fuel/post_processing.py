import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Shynt.api_py.Postprocess import process_files as postprocess

# HYBRID ---------------------------------------------------------------------------------------------
flux_df = pd.read_csv('./output_RMM_10_000/10_000_rmm_flux.csv')
print(flux_df)
fast_flux_hyb = flux_df[flux_df["Energy_group"] == 1]['scalar_flux'].to_numpy()
thermal_flux_hyb = flux_df[flux_df["Energy_group"] == 2]['scalar_flux'].to_numpy()

norm_factor_hyb = fast_flux_hyb.max()
fast_flux_hyb /= norm_factor_hyb
thermal_flux_hyb /= norm_factor_hyb
# Serpent --------------------------------------------------------------------------------------------
detector_out_file = "./reference/10_000/ref_10_000.serp_det0.m"
det_names = [
  'top_left_fuel',
  'top_right_fuel',
  'bottom_right_fuel',
  'bottom_left_fuel',
  'top_left_coolant',
  'top_right_coolant',
  'bottom_right_coolant',
  'bottom_left_coolant',
]
flux_fast_serp = []
sigma_fast_serp = []
flux_th_serp = []
sigma_th_serp = []

for dn in det_names:
  fl, err = postprocess.get_flux_from_detector_file(detector_out_file, dn)
  flux_fast_serp.append(fl[dn][1])
  sigma_fast_serp.append(err[dn][1])
  flux_th_serp.append(fl[dn][0])
  sigma_th_serp.append(err[dn][0])

flux_fast_serp = np.array(flux_fast_serp)
flux_th_serp = np.array(flux_th_serp)
norm_factor_serp = flux_fast_serp.max()
flux_fast_serp /= norm_factor_serp
flux_th_serp /= norm_factor_serp

# ---------------------------------------------------------------------------------------------------

diag1 = [4,0,2,6]
diag2 = [5,1,3,7]

diag1_fast_hyb = [fast_flux_hyb[idx] for idx in diag1]
diag1_th_hyb = [thermal_flux_hyb[idx] for idx in diag1]
diag2_fast_hyb = [fast_flux_hyb[idx] for idx in diag2]
diag2_th_hyb = [thermal_flux_hyb[idx] for idx in diag2]

diag1_fast_serp = [flux_fast_serp[idx] for idx in diag1]
diag1_th_serp = [flux_th_serp[idx] for idx in diag1]
diag2_fast_serp = [flux_fast_serp[idx] for idx in diag2]
diag2_th_serp = [flux_th_serp[idx] for idx in diag2]


plt.figure()
plt.plot(diag1_fast_hyb, '-o', label='hybrid')
plt.plot(diag1_fast_serp, '--o', label='serpent')
plt.title('Diagonal left-top --> right-down (FAST)')
plt.legend()
plt.savefig(f"diag1_fast.png")


plt.figure()
plt.plot(diag2_fast_hyb, '-o', label='hybrid')
plt.plot(diag2_fast_serp, '--o', label='serpent')
plt.title('Diagonal left-right --> left-down (FAST)')
plt.legend()
plt.savefig(f"diag2_fast.png")



plt.figure()
plt.plot(diag1_th_hyb, '-o', label='hybrid')
plt.plot(diag1_th_serp, '--o', label='serpent')
plt.title('Diagonal left-top --> right-down (THERMAL)')
plt.legend()
plt.savefig(f"diag1_thermal.png")


plt.figure()
plt.plot(diag2_th_hyb, '-o', label='hybrid')
plt.plot(diag2_th_serp, '--o', label='serpent')
plt.title('Diagonal left-right --> left-down (THERMAL)')
plt.legend()
plt.savefig(f"diag2_thermal.png")

