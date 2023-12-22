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
        worksheet.write(row_idx, col_idx, f"{mat}-{r_id}")
        col_idx += 1
      for s in surfaces:
        worksheet.write(row_idx, col_idx, s)
        col_idx += 1
      col_idx = 0
      row_idx += 1
      # write region to x prob values ---------------------------
      for r_id, cell in regions.items():
        mat = cell.content.name
        worksheet.write(row_idx, col_idx, f"{mat}-{r_id}")
        col_idx = 1
        for rp_id, cell in regions.items():
          mat = cell.content.name
          prob_val = probabilities["regions"][r_id]["regions"][rp_id][g]
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        for s in surfaces:
          prob_val = probabilities["regions"][r_id]["surfaces"][s][g]
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        col_idx = 0
        row_idx += 1
      # write surface to x prob values ---------------------------
      col_idx = 0
      for s in surfaces:
        worksheet.write(row_idx, col_idx, s)
        col_idx = 1
        for rp_id, cell in regions.items():
          mat = cell.content.name
          prob_val = probabilities["surfaces"][s]["regions"][rp_id][g]
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        for sp in surfaces:
          prob_val = probabilities["surfaces"][s]["surfaces"][sp][g]
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        row_idx += 1
        col_idx = 0
      row_idx += 4
      

  print("workbook closed")
  workbook.close()
