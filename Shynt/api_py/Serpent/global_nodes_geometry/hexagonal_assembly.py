
def edge_with_void(geom_info):
  rect_width = geom_info["rectangle_width"]
  rect_height = geom_info["rectangle_height"]
  height_to_width = rect_height / rect_width
  radius = geom_info["radius"]
  cells = geom_info["cells"]
  fuel_cell_id = geom_info["fuel_relation"]["fuel"]
  coolant_cell_id = geom_info["fuel_relation"]["non_fuel"]
  # cell_void = cells["void"]
  cell_fuel = cells[fuel_cell_id]
  cell_coolant = cells[coolant_cell_id]

  x1 = 0.0
  x2 = rect_width
  y1 = 0.0
  y2 = rect_height

  serpent_syntax = f"\n\nsurf 1 rect {x1} {x2} {y1} {y2}\n"
  serpent_syntax += f"surf 2 pad {x2} {y1} 0.0000 {radius} 180  270\n"
  serpent_syntax += f"surf 3 px {0.0}\n"
  serpent_syntax += f"trans s 3 0.0 0.0 0.0 0.0 0.0 30\n\n"
  
  
  serpent_syntax += f"cell {100000} edge_hex void -1  -3\n"
  serpent_syntax += f"cell {cell_fuel.id} edge_hex {cell_fuel.content.name} -2\n"
  serpent_syntax += f"cell {cell_coolant.id} edge_hex {cell_coolant.content.name} -1  2 3\n"
  serpent_syntax += "cell 999999  0  fill edge_hex  -1\n"
  serpent_syntax += "cell 999998  0  outside  1\n\n\n"
  serpent_syntax += f"plot 3 500 {int(500*height_to_width)}\n\n"
  

  return serpent_syntax

def top_edge(geom_info):
  rect_width = geom_info["rectangle_width"]
  rect_height = geom_info["rectangle_height"]
  circle_radius = geom_info["radius"]
  cells = geom_info["cells"]
  fuel_cell_id = geom_info["fuel_relation"]["fuel"]
  coolant_cell_id = geom_info["fuel_relation"]["non_fuel"]
  cell_fuel = cells[fuel_cell_id] 
  cell_coolant = cells[coolant_cell_id]
  x1 = 0.0
  x2 = rect_width
  y1 = 0.0
  y2 = rect_height
  height_to_width = rect_height / rect_width

  serpent_syntax = f"\n\nsurf 1 rect {x1} {x2} {y1} {y2}\n"
  serpent_syntax += f"surf 2 pad {x1} {y1} 0.000 {circle_radius}  270  360\n\n"
  
  serpent_syntax += f"cell {cell_fuel.id} top_edge_hex {cell_fuel.content.name} -2 \n"
  serpent_syntax += f"cell {cell_coolant.id} top_edge_hex {cell_coolant.content.name} -1  2\n"
  serpent_syntax += "cell 999999  0  fill top_edge_hex  -1\n"
  serpent_syntax += "cell 999998  0  outside  1\n\n\n"
  serpent_syntax += f"plot 3 500 {int(500*height_to_width)}\n\n"



  return serpent_syntax

def inside(geom_info):
  rect_width = geom_info["rectangle_width"]
  rect_height = geom_info["rectangle_height"]
  height_to_width = rect_height / rect_width
  circle_radius = geom_info["radius"]
  hexagon_radius = geom_info["hexagon_radius"]
  cells = geom_info["cells"]
  fuel_cell_1_id = geom_info["fuel_relation"]["fuel1"]
  fuel_cell_2_id = geom_info["fuel_relation"]["fuel2"]

  coolant_cell_1_id = geom_info["fuel_relation"]["non_fuel1"]
  coolant_cell_2_id = geom_info["fuel_relation"]["non_fuel2"]

  cell_fuel_1 = cells[fuel_cell_1_id]
  cell_fuel_2 = cells[fuel_cell_2_id]
  cell_coolant_1 = cells[coolant_cell_1_id]
  cell_coolant_2 = cells[coolant_cell_2_id]

  x1 = 0.0
  x2 = rect_width
  y1 = 0.0
  y2 = rect_height
  serpent_syntax = f"\n\nsurf 1 rect {x1} {x2} {y1} {y2}\n"
  serpent_syntax += f"surf 2 pad {x1} {y1} 0.00 {circle_radius}  270  360\n"
  serpent_syntax += f"surf 3 pad {x2} {y2} 0.00 {circle_radius}   90  180\n"

  serpent_syntax += f"surf 4 py {hexagon_radius}\n"
  serpent_syntax += f"trans s 4 0.0 0.0 0.0 0.0 0.0 30\n\n"

  serpent_syntax += f"cell {cell_fuel_1.id} inside_hex {cell_fuel_1.content.name} -2  -1\n"
  serpent_syntax += f"cell {cell_fuel_2.id} inside_hex {cell_fuel_2.content.name} -3  -1 \n"
  serpent_syntax += f"cell {cell_coolant_1.id} inside_hex {cell_coolant_1.content.name} -1  2  3 -4\n"
  serpent_syntax += f"cell {cell_coolant_2.id} inside_hex {cell_coolant_2.content.name} -1  2  3  4\n"

  serpent_syntax += "cell 999999  0  fill inside_hex  -1\n"
  serpent_syntax += "cell 999998  0  outside  1\n\n\n"
  serpent_syntax += f"plot 3 500 {int(500*height_to_width)}\n\n"
  


  return serpent_syntax



def xs_generation_edge_with_void(geom_info):
  rect_width = geom_info["rectangle_width"]
  rect_height = geom_info["rectangle_height"]
  height_to_width = rect_height / rect_width
  circle_radius = geom_info["radius"]
  cells = geom_info["cells"]
  fuel_cell_id = geom_info["fuel_relation"]["fuel"]
  coolant_cell_id = geom_info["fuel_relation"]["non_fuel"]
  # cell_void = cells["void"]
  cell_fuel = cells[fuel_cell_id]
  cell_coolant = cells[coolant_cell_id]

  x1 = 0.0
  x2 = rect_width
  y1 = 0.0
  y2 = rect_height
  serpent_syntax = f"\n\nsurf 1 rect {x1} {x2} {y1} {y2}\n"
  serpent_syntax += f"%surf 2 pad  {x2} {y1} 0.0000 {circle_radius} 180 270\n"
  serpent_syntax += f"surf 2 cyl  {x2} {y1} {circle_radius} \n"

  serpent_syntax += f"surf 3 px {0.0}\n"
  serpent_syntax += f"trans s 3 0.0 0.0 0.0 0.0 0.0 30\n\n"
  
  
  serpent_syntax += f"cell {100000}    u4gcu_1 void -1  -3\n"
  serpent_syntax += f"cell {100001} coarse_node fill u4gcu_1 -1  -3\n"

  serpent_syntax += f"cell {cell_fuel.id}      u4gcu_2 {cell_fuel.content.name} -2\n"
  serpent_syntax += f"cell {cell_fuel.id+10}   coarse_node fill u4gcu_2 -2\n"

  serpent_syntax += f"cell {cell_coolant.id}    u4gcu_3 {cell_coolant.content.name} -1  2  3\n"
  serpent_syntax += f"cell {cell_coolant.id+10} coarse_node fill u4gcu_3  -1  2   3\n"

  serpent_syntax += "cell 999999  0  fill coarse_node  -1\n"
  serpent_syntax += "cell 999998  0  outside  1\n\n\n"

  serpent_syntax += "set gcu u4gcu_2 u4gcu_3 \n\n"
  serpent_syntax += f"plot 3 500 {int(500*height_to_width)}\n\n"
  


  gcu_rel = {
    cell_fuel.id: "u4gcu_2",
    cell_coolant.id: "u4gcu_3",
  }
  return serpent_syntax, gcu_rel

def xs_generation_top_edge(geom_info):
  rect_width = geom_info["rectangle_width"]
  rect_height = geom_info["rectangle_height"]
  height_to_width = rect_height / rect_width
  circle_radius = geom_info["radius"]
  cells = geom_info["cells"]
  fuel_cell_id = geom_info["fuel_relation"]["fuel"]
  coolant_cell_id = geom_info["fuel_relation"]["non_fuel"]
  # cell_void = cells["void"]
  cell_fuel = cells[fuel_cell_id]
  cell_coolant = cells[coolant_cell_id]

  x1 = 0.0
  x2 = rect_width
  y1 = 0.0
  y2 = rect_height
  serpent_syntax = f"\n\nsurf 1 rect {x1} {x2} {y1} {y2}\n"
  serpent_syntax += f"%surf 2 pad {x2} {y1} 0.000 {circle_radius}  180  270\n\n"
  serpent_syntax += f"surf 2 cyl  {x2} {y1} {circle_radius} \n"


  serpent_syntax += f"cell {cell_fuel.id}      u4gcu_1 {cell_fuel.content.name} -2\n"
  serpent_syntax += f"cell {cell_fuel.id+10}   coarse_node fill u4gcu_1 -2\n"
  serpent_syntax += f"cell {cell_coolant.id}    u4gcu_2 {cell_coolant.content.name} -1  2 \n"
  serpent_syntax += f"cell {cell_coolant.id+10} coarse_node fill u4gcu_2  -1  2 \n"
  serpent_syntax += "cell 999999  0  fill coarse_node  -1\n"
  serpent_syntax += "cell 999998  0  outside  1\n\n\n"
  serpent_syntax += "set gcu u4gcu_1 u4gcu_2\n\n"
  serpent_syntax += f"plot 3 500 {int(500*height_to_width)}\n\n"
  

  gcu_rel = {
    cell_fuel.id: "u4gcu_1",
    cell_coolant.id: "u4gcu_2",
  }

  return serpent_syntax, gcu_rel

def xs_generation_inside(geom_info):
  rect_width = geom_info["rectangle_width"]
  rect_height = geom_info["rectangle_height"]
  height_to_width = rect_height / rect_width
  circle_radius = geom_info["radius"]
  hexagon_radius = geom_info["hexagon_radius"]
  cells = geom_info["cells"]
  fuel_cell_1_id = geom_info["fuel_relation"]["fuel1"]
  fuel_cell_2_id = geom_info["fuel_relation"]["fuel2"]

  coolant_cell_1_id = geom_info["fuel_relation"]["non_fuel1"]
  coolant_cell_2_id = geom_info["fuel_relation"]["non_fuel2"]

  cell_fuel_1 = cells[fuel_cell_1_id]
  cell_fuel_2 = cells[fuel_cell_2_id]
  cell_coolant_1 = cells[coolant_cell_1_id]
  cell_coolant_2 = cells[coolant_cell_2_id]

  x1 = 0.0
  x2 = rect_width
  y1 = 0.0
  y2 = rect_height

  serpent_syntax = f"\n\nsurf 1 rect {x1} {x2} {y1} {y2}\n"
  serpent_syntax += f"surf 2 pad {x1} {y1} 0.00 {circle_radius}  270 360\n"
  serpent_syntax += f"surf 3 pad {x2} {y2} 0.00 {circle_radius}   90 180\n"

  serpent_syntax += f"surf 4 py {hexagon_radius}\n"
  serpent_syntax += f"trans s 4 0.0 0.0 0.0 0.0 0.0 30\n\n"

  serpent_syntax += f"cell {cell_fuel_1.id}      u4gcu_1 {cell_fuel_1.content.name} -2  -1\n"
  serpent_syntax += f"cell {cell_fuel_1.id+10}   coarse_node fill u4gcu_1 -2\n"
  serpent_syntax += f"cell {cell_fuel_2.id}      u4gcu_2 {cell_fuel_2.content.name} -3  -1\n"
  serpent_syntax += f"cell {cell_fuel_2.id+10}   coarse_node fill u4gcu_2 -3\n"
  serpent_syntax += f"cell {cell_coolant_1.id}    u4gcu_3 {cell_coolant_1.content.name} -1  2  3 -4\n"
  serpent_syntax += f"cell {cell_coolant_1.id+10} coarse_node fill u4gcu_3  -1  2  3  -4\n"
  serpent_syntax += f"cell {cell_coolant_2.id}    u4gcu_4 {cell_coolant_2.content.name} -1  2  3  4\n"
  serpent_syntax += f"cell {cell_coolant_2.id+10} coarse_node fill u4gcu_4  -1  2  3  4\n"
  serpent_syntax += "cell 999999  0  fill coarse_node  -1\n"
  serpent_syntax += "cell 999998  0  outside  1\n\n\n"
  serpent_syntax += f"plot 3 500 {int(500*height_to_width)}\n\n"
  serpent_syntax += "set gcu u4gcu_1 u4gcu_2 u4gcu_3 u4gcu_4\n\n"


  gcu_rel = {
    cell_fuel_1.id: "u4gcu_1",
    cell_fuel_2.id: "u4gcu_2",
    cell_coolant_1.id: "u4gcu_3",
    cell_coolant_2.id: "u4gcu_4",
  }

  return serpent_syntax, gcu_rel


def edge_with_void_detectors_fuel(geom_info, ene, file_reg_id):
  detectors_syntax = ""
  fuel_surf = geom_info["surfaces_for_detectors"]["fuel"]
  fuel_reg_id = file_reg_id
  fuel_mat = geom_info["cells"][fuel_reg_id].content.name
  regions = list(geom_info["cells"].keys())
  surfaces = list(geom_info["surfaces_for_detectors"]["boundary"].keys())

  detectors_syntax += f"det j_in_reg{fuel_reg_id} ds {fuel_surf} -1 de {ene} dfl 1 1\n"
  detectors_syntax += f"det j_out_reg{fuel_reg_id} ds {fuel_surf} 1 de {ene} dfl 1 3  dfl 2 1\n"
  detectors_syntax += f"det all_to_reg{fuel_reg_id} de {ene} dr -1 {fuel_mat} dc {fuel_reg_id} dfl 1 2 dfl 1 0\n"
  for r_id in regions:
    detectors_syntax += f"det reg{fuel_reg_id}_to_reg{r_id} de {ene} dr -1 {fuel_mat} dc {r_id} dfl 2 2 dfl 2 0\n"
  for s_id in surfaces:
    j_out_dir = geom_info["surf_for_detectors"]["current_dir"][s_id]["outward"]
    detectors_syntax += f"det reg{fuel_reg_id}_surface{s_id} de {ene} ds {s_id} {j_out_dir} dfl 2 2 dfl 2 0\n"

  return detectors_syntax

def edge_with_void_detectors_non_fuel(geom_info, ene, file_reg_id):
  detectors_syntax = ""
  regions = list(geom_info["cells"].keys())
  surfaces = list(geom_info["surfaces_for_detectors"]["boundary"].keys())

  file_reg_mat = geom_info["cells"][file_reg_id].content.name

  detectors_syntax += f"det reg{file_reg_id}_reg{file_reg_id} de {ene} dr -1 {file_reg_mat} dc {file_reg_id} dfl 1 2  dfl 1 0  dfl 1 1\n"
  detectors_syntax += f"det total_rate_reg{file_reg_id} de {ene} dr -1 {file_reg_mat} dc {file_reg_id} dfl 1 1\n"
  for r_id in regions:
    r_mat = geom_info["cells"][r_id].content.name
    detectors_syntax += f"det reg{file_reg_id}_reg{r_id} de {ene} dr -1 {r_mat} dc {r_id} dfl 1 2 dfl 1 0\n"
  for s_id in surfaces:
    j_out_dir = geom_info["surf_for_detectors"]["current_dir"][s_id]
    detectors_syntax += f"det reg{file_reg_id}_surface{s_id} de {ene} ds {s_id} {j_out_dir} dfl 1 2 dfl 1 0\n"
  
  return detectors_syntax

def edge_with_void_detectors_surfaces(geom_info, ene):
  detectors_syntax = ""
  surfaces = list(geom_info["surfaces_for_detectors"]["boundary"].keys())
  regions = list(geom_info["cells"].keys())
  plane_id = geom_info["plane_void_id"]

  s_flag = 1
  for s_id in surfaces:
    j_in_dir = geom_info["surf_for_detectors"]["current_dir"][s_id]["inward"]
    detectors_syntax += f"det surface_{s_id}_jin ds {s_id} {j_in_dir} de {ene} dfl {s_flag} 1\n"
    for r_id in regions:
      r_id_mat = geom_info["cells"][r_id].content.name
      detectors_syntax += f"det surface_{s_id}_to_reg{r_id} de {ene} dr -1 {r_id_mat} dc {r_id} dfl {s_flag} 2  dfl {s_flag} 0\n"
    for sp_id in surfaces:
      j_out_dir = geom_info["surf_for_detectors"]["current_dir"][sp_id]["outward"]
      detectors_syntax += f"det surface_{s_id}_to_surf{sp_id} ds {sp_id} {j_out_dir} de {ene} dfl {s_flag} 2  dfl {s_flag} 0\n"
    s_flag += 1

  return detectors_syntax
  

def top_edge_detectors():
  pass

def inside_detectors():
  pass
