import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Shynt.api_py.Postprocess import process_files as postprocess

np.set_printoptions(linewidth=np.inf)

base_dir = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hex_pin_square_mesh_2r_8g/'

def shynt_flux():
	nodes_to_plot = [1,4]
	regs_to_plot = [7,8,20,19]
	flux_df = pd.read_csv(base_dir + 'output_RMM_10000_3000_1500/10000_3000_1500_rmm_flux.csv')
	# flx = np.array([arr for arr in flux_df.to_numpy() if arr[1] in nodes_to_plot])
	norm_factor = flux_df.to_numpy()[:,4].max()

	flx_g = {
		g: [] for g in range(1,9)
	}

	flux_df = flux_df[flux_df["coarse_node_id"].isin(nodes_to_plot)]
	for g in range(1,9):
		flx_g[g] = flux_df[flux_df["Energy_group"] == g].to_numpy()


	# print(flx_g)
	# for g in range():
	flx_by_n = {
		g: [] for g in range(1,9)
	}

	flx_to_plot = {}


	print("Normalization factor hybrid:", norm_factor)

	for g in range(1,9):
		array_to_plot = np.array([
			flx_g[g][0][4],
			flx_g[g][1][4],
			flx_g[g][3][4],
			flx_g[g][2][4],
		])/norm_factor

		flx_to_plot[g] = array_to_plot
	return flx_to_plot


def serpent_flux():

	detector_out_file = base_dir + "reference_calculation/moreParticles_test/1e6.serp_det0.m"
	det_names = {'fuel':'1', 'cool':'2'}

	
	flux_serp = {}
	sigma_serp = {}

	norm_factor_serp = 0
	for dn in det_names.values():
		fl, err = postprocess.get_flux_from_detector_file(detector_out_file, dn)
		flux_serp[dn] = np.flip(fl[dn], 0)
		for g in range(8):
			max_val = fl[dn][g].max()
			if max_val > norm_factor_serp: norm_factor_serp = max_val
	


	print("Normalization factor serpent:", norm_factor_serp)

	flx_to_plot = {}
	for g in range(8):
		flx_arr = []
		flx_arr.append(flux_serp[det_names['cool']][g])
		flx_arr.append(flux_serp[det_names['fuel']][g])	
		flx_arr.append(flux_serp[det_names['fuel']][g])	
		flx_arr.append(flux_serp[det_names['cool']][g])	
		flx_to_plot[g+1] = np.array(flx_arr)/norm_factor_serp
		print(np.array(flx_arr))
		print()
		print()
		print()

	return flx_to_plot

hyb_flx = shynt_flux()
print(hyb_flx)

serp_flx = serpent_flux()
print(serp_flx)

for g in range(1,9):
	plt.figure()
	plt.plot(hyb_flx[g], '--o', label="hybrid")
	plt.plot(serp_flx[g], '--o', label="serpent")
	
	plt.legend()
	# plt.savefig(f'serpent_flux_g{g}.png')
	plt.savefig(f'hybrid_flux_g{g}.png')
	plt.savefig(f'hybrid_vs_serpent_flux_g{g}.png')

	
	# break
# print(serp_flx)

