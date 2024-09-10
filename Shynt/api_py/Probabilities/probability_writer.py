import os
import sys
from pathlib import Path

import xlsxwriter


def write_excel(probabilities, root, dir_="", name=""):
  energy_g = root.energy_grid.energy_groups

  input_file_dir = os.getcwd() + '/'
  prob_dir = input_file_dir

  name_prob_file = prob_dir + f"/probabilities_{name}.xlsx"
  workbook = xlsxwriter.Workbook(name_prob_file)

  mesh = root.mesh
  coarse_nodes = mesh.coarse_mesh.coarse_nodes
  unique_nodes = mesh.coarse_mesh.unique_nodes
  print("Printing out probabilities")
  for c_id in unique_nodes:
    worksheet = workbook.add_worksheet(f"Node type {c_id}")

    start_row = 0
    start_col = 0

    surfaces = list(coarse_nodes[c_id].surfaces.keys())
    col_idx  = 0
    row_idx = 0
    
    regions = coarse_nodes[c_id].fine_mesh.regions
    for g in range(energy_g):
      # write headers ------------------------------------
      worksheet.write(row_idx, col_idx, f"g = {g}")
      col_idx += 1
      for r_id, cell in regions.items():
        mat = cell.content.name
        # worksheet.write(row_idx, col_idx, f"{mat}-{r_id}")
        worksheet.write(row_idx, col_idx, f"reg-{r_id}")
        col_idx += 1
      for s in surfaces:
        worksheet.write(row_idx, col_idx, f"surf-{s}")
        col_idx += 1
      col_idx = 0
      row_idx += 1
      # write region to x prob values ---------------------------
      for r_id, cell in regions.items():
        mat = cell.content.name
        # worksheet.write(row_idx, col_idx, f"{mat}-{r_id}")
        worksheet.write(row_idx, col_idx, f"reg-{r_id}")
        col_idx = 1
        for rp_id, cell in regions.items():
          mat = cell.content.name
          prob_val = probabilities[c_id]["regions"][r_id]["regions"][rp_id][g] * 100
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        for s in surfaces:
          prob_val = probabilities[c_id]["regions"][r_id]["surfaces"][s][g] * 100
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        col_idx = 0
        row_idx += 1
      # write surface to x prob values ---------------------------
      col_idx = 0
      for s in surfaces:
        # worksheet.write(row_idx, col_idx, s)
        worksheet.write(row_idx, col_idx, f"surf-{s}")
        col_idx = 1
        for rp_id, cell in regions.items():
          mat = cell.content.name
          prob_val = probabilities[c_id]["surfaces"][s]["regions"][rp_id][g] * 100
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        for sp in surfaces:
          prob_val = probabilities[c_id]["surfaces"][s]["surfaces"][sp][g] * 100
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        row_idx += 1
        col_idx = 0
      row_idx += 4
      

  print("workbook closed")
  workbook.close()


def write_csv(probabilities, root, dir_="", name=""):
  energy_g = root.energy_grid.energy_groups

  input_file_dir = os.getcwd() + '/'
  prob_dir = input_file_dir

  name_prob_file = prob_dir + f"/probabilities_{name}.csv"

  mesh = root.mesh
  coarse_nodes = mesh.coarse_mesh.coarse_nodes
  unique_nodes = mesh.coarse_mesh.unique_nodes
  print("Printing out probabilities csv")

  with open(name_prob_file, 'w') as csv_file:
    csv_file.write(
      "c_id,g,from,to,from_id,to_id,probability\n"
    )
    for c_id in unique_nodes:

      surfaces = list(coarse_nodes[c_id].surfaces.keys())
    
      regions = coarse_nodes[c_id].fine_mesh.regions
      for g in range(energy_g):
        
        # write region to x prob values ---------------------------
        for r_id, cell in regions.items():
          for rp_id, cell in regions.items():
            mat = cell.content.name
            prob_val = probabilities[c_id]["regions"][r_id]["regions"][rp_id][g]
            csv_file.write(f"{c_id},{g},region,region,{r_id},{rp_id},{prob_val}\n")
          for s in surfaces:
            prob_val = probabilities[c_id]["regions"][r_id]["surfaces"][s][g]
            csv_file.write(f"{c_id},{g},region,surface,{r_id},{s},{prob_val}\n")
        # write surface to x prob values ---------------------------
    
        for s in surfaces:
          
          for rp_id, cell in regions.items():
            prob_val = probabilities[c_id]["surfaces"][s]["regions"][rp_id][g]
            csv_file.write(f"{c_id},{g},surface,region,{s},{rp_id},{prob_val}\n")

          for sp in surfaces:
            prob_val = probabilities[c_id]["surfaces"][s]["surfaces"][sp][g]
            csv_file.write(f"{c_id},{g},surface,surface,{s},{sp},{prob_val}\n")

  print("Printing out probabilities csv: Completed")



