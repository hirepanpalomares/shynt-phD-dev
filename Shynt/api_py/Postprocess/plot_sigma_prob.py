from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


def plot_sigma(sigma, root, name_file):
  print("\n"*10)
  print('--------------------------------')
  print('Plotting standard deviation from probabilities')
  
  energy_g = root.energy_grid.energy_groups

  

  # -----------------------------------------------------------
  # Getting axes names

  mesh = root.mesh
  coarse_nodes = mesh.coarse_mesh.coarse_nodes
  unique_nodes = mesh.coarse_mesh.unique_nodes
  axes_name = []
  for c_id in unique_nodes:
    surfaces = list(coarse_nodes[c_id].surfaces.keys())
    regions = coarse_nodes[c_id].fine_mesh.regions
      
    for r_id, cell in regions.items():
      mat = cell.content.name
      axes_name.append(f"{mat}-{r_id}")
    for s in surfaces:
      axes_name.append(f"surf-{s}")

  # -----------------------------------------------------------

  sigma_to_plot = {}
  for g in range(energy_g): 
    sigma_to_plot[g] = {}
    for c_id in unique_nodes:
      
      surfaces = list(coarse_nodes[c_id].surfaces.keys())
      regions = coarse_nodes[c_id].fine_mesh.regions

      sigma_matrix = []
      for r_id, cell in regions.items():
        
        sigma_region = []
        for rp_id, cell in regions.items():
          mat = cell.content.name
          sigma_val = sigma["regions"][r_id]["regions"][rp_id][g]
          sigma_region.append(sigma_val)
        for sp in surfaces:
          sigma_val = sigma["regions"][r_id]["surfaces"][sp][g]
          sigma_region.append(sigma_val)
        
        sigma_matrix.append(np.array(sigma_region))

      for s in surfaces:
        sigma_surf = []
        for rp_id, cell in regions.items():
          mat = cell.content.name
          sigma_val = sigma["surfaces"][s]["regions"][rp_id][g]
          sigma_surf.append(sigma_val)
        for sp in surfaces:
          sigma_val = sigma["surfaces"][s]["surfaces"][sp][g]
          sigma_surf.append(sigma_val)
        
        sigma_matrix.append(np.array(sigma_surf))

      sigma_to_plot[g][c_id] = sigma_matrix
  # -----------------------------------------------------------
  
  for nid in unique_nodes:
    fig, axs = plt.subplots(4, 2, figsize=(10,8), layout='constrained')
    for g, ax in enumerate(axs.flat):
      # print(sigma_to_plot[0][1])
      for i, name in enumerate(axes_name):
        ax.plot(
          axes_name, sigma_to_plot[g][nid][i]*100, 'o',
          ls='--', label=f'{name}', lw=1,
        )
      ax.set_xticklabels(axes_name, rotation=45)
      y_ticks_log = [0.001, 0.01, 0.1, 1, 10, 100]
      ax.set_ylim(
        top=100, 
        bottom=0.001
      )
      ax.set_yticks(y_ticks_log)
      ax.tick_params(axis='both', which='major', labelsize=7)

      ax.set_yscale('log')
      ax.grid()

    print(f'std_dev_probabilities_{name_file}.png')
    plt.savefig(f'std_dev_probabilities_{name_file}.png')

    legend_fig = plt.figure(figsize=(10, 5))
    handles, labels = ax.get_legend_handles_labels()
    legend_fig.legend(handles, labels, loc='center', ncol=2)
    legend_fig.savefig(f'std_dev_legend_{name_file}.png')
  
  
      
    
  