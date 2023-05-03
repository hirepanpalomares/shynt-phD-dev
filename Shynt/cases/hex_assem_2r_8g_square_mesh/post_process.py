import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Shynt.api_py.Postprocess import process_files as postprocess

np.set_printoptions(linewidth=np.inf)

base_dir = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hex_assem_2r_8g_square_mesh/'

def shynt_flux():
	nodes_to_plot = [1,23,47,73,101,131,163,197,233,271,310,348,384,418,450,480,508,534,558,580]
	regs_to_plot = [
		1160,1161,1233,1232,1230,1231,1351,1350,1348,1349,
	]
	base_dir = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/Shynt/cases/hex_assem_2r_8g_square_mesh/'
	flux_df = pd.read_csv(base_dir + 'output_RMM_1500_1000_500/1500_1000_500_rmm_flux.csv')
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
		flx_by_n[g].append([])
		n_init = 1
		for arr in flx_g[g]:
			if arr[1] == n_init: 
				flx_by_n[g][-1].append(arr)
			else:
				flx_by_n[g].append([arr])
				n_init = arr[1]
		# Order regions  in the desired order
		for n, node_flx in enumerate(flx_by_n[g]):
			if node_flx[0][1] == 1 or node_flx[0][1] == 580: continue
			else:
				# c1, f1, c2, f2 ---> f2, c2, c1, f1
				new_node_flx_order = [
					node_flx[3],
					node_flx[2],
					node_flx[0],
					node_flx[1],
				]
				flx_by_n[g][n] = new_node_flx_order
		# Getting arrays to plot
		# array_to_plot = np.array(flx_by_n[g])#[:,:,4]
		array_to_plot = []
		for node_array in flx_by_n[g]:
			for region_array in node_array:
				array_to_plot.append(region_array[4])
		flx_to_plot[g] = np.array(array_to_plot)/norm_factor
		
	return flx_to_plot


def serpent_flux():

	detector_out_file = base_dir + "reference_ures_not_set/1e6_3000_1500/1e6_3000_1500.serp_det0.m"
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
	
	
	lat_idx_to_plot = [
		32+21*n for n in range(19)
	]

	print("Normalization factor serpent:", norm_factor_serp)
	print(lat_idx_to_plot)

	flx_to_plot = {}
	for g in range(8):
		flx_arr = []
		for idx in lat_idx_to_plot:
			flx_arr.append(flux_serp[det_names['cool']][g][idx-1])
			flx_arr.append(flux_serp[det_names['fuel']][g][idx-1])	
			flx_arr.append(flux_serp[det_names['fuel']][g][idx-1])	
			flx_arr.append(flux_serp[det_names['cool']][g][idx-1])	
		flx_to_plot[g+1] = np.array(flx_arr)/norm_factor_serp
		print(np.array(flx_arr))
		print()
		print()
		print()

	return flx_to_plot

hyb_flx = shynt_flux()
serp_flx = serpent_flux()


for g in range(1,9):
	plt.figure()
	plt.plot(hyb_flx[g], '--o', label="hybrid")
	# plt.plot(serp_flx[g], '--o', label="serpent")
	
	plt.legend()
	# plt.savefig(f'serpent_flux_g{g}.png')
	plt.savefig(f'hybrid_flux_g{g}.png')

	
	# break
# print(serp_flx)

