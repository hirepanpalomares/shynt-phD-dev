import os
import sys
from pathlib import Path

import xlsxwriter


def write_excel(probabilities, mesh_info, root, dir_):
  energy_g = root.energy_grid.energy_groups

  input_file_argument = sys.argv[0]
  input_file_absolute = str(Path(input_file_argument).absolute())
  input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"

  name_prob_file = dir_ + "/probabilities.xlsx"
  workbook = xlsxwriter.Workbook(name_prob_file)
  unique_nodes = [arr[0] for arr in mesh_info.equal_nodes]
  for c_id in unique_nodes:
    regions_mat = mesh_info.region_type_rel_switched[c_id]
    worksheet = workbook.add_worksheet(f"Node type {c_id}")

    start_row = 0
    start_col = 0

    regions = list(regions_mat.keys())
    surfaces = list(mesh_info.coarse_surface_rel[c_id])
    col_idx  = 0
    row_idx = 0
    for g in range(energy_g):
      # write headers ------------------------------------
      worksheet.write(row_idx, col_idx, f"g = {g}")
      col_idx += 1
      for r in regions:
        mat = regions_mat[r]
        worksheet.write(row_idx, col_idx, mat)
        col_idx += 1
      for s in surfaces:
        worksheet.write(row_idx, col_idx, s)
        col_idx += 1
      col_idx = 0
      row_idx += 1
      # write region to x prob values ---------------------------
      for r in regions:
        mat = regions_mat[r]
        worksheet.write(row_idx, col_idx, mat)
        col_idx = 1
        for rp in regions:
          prob_val = probabilities["regions"][r]["regions"][rp][g]
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        for s in surfaces:
          prob_val = probabilities["regions"][r]["surfaces"][s][g]
          worksheet.write(row_idx, col_idx, prob_val)
          col_idx += 1
        col_idx = 0
        row_idx += 1
      # write surface to x prob values ---------------------------
      col_idx = 0
      for s in surfaces:
        worksheet.write(row_idx, col_idx, s)
        col_idx = 1
        for rp in regions:
          prob_val = probabilities["surfaces"][s]["regions"][rp][g]
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
