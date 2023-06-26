
def square_pin_cell(geom_info):
  half_width = geom_info["half_width"]
  radius = geom_info["radius"]
  cells = geom_info["cells"]
  fuel_cell_id = geom_info["fuel_relation"]["fuel"][0]
  coolant_cell_id = geom_info["fuel_relation"]["non_fuel"][0]
  
  cell_fuel = cells[fuel_cell_id]
  cell_coolant = cells[coolant_cell_id]


  serpent_syntax = f"\n\nsurf 1001 sqc 0.0000  0.0000 {half_width}\n"
  serpent_syntax += f"surf 1002 cyl  0.0000  0.0000 {radius}\n"
  
  
  serpent_syntax += f"cell {cell_fuel.id} sqc_pin {cell_fuel.content.name} -1002\n"
  serpent_syntax += f"cell {cell_coolant.id} sqc_pin {cell_coolant.content.name} 1002  -1001\n"
  serpent_syntax += "cell 999999  0  fill sqc_pin  -1001\n"
  serpent_syntax += "cell 999998  0  outside  1001\n\n\n"
  serpent_syntax += f"plot 3 500 500\n\n"
  

  return serpent_syntax


def xs_generation_square_pin_cell(geom_info):
  half_width = geom_info["half_width"]
  radius = geom_info["radius"]
  cells = geom_info["cells"]
  fuel_cell_id = geom_info["fuel_relation"]["fuel"][0]
  coolant_cell_id = geom_info["fuel_relation"]["non_fuel"][0]
  cell_fuel = cells[fuel_cell_id]
  cell_coolant = cells[coolant_cell_id]


  serpent_syntax = f"\n\nsurf 1001 sqc 0.0000  0.0000 {half_width}\n"
  serpent_syntax += f"surf 1002 cyl  0.0000  0.0000 {radius}\n"
  
  
  

  serpent_syntax += f"cell {cell_fuel.id}      u4gcu_1001 {cell_fuel.content.name} -1002\n"
  serpent_syntax += f"cell {cell_fuel.id+10}   coarse_node fill u4gcu_1001 -1002\n"

  serpent_syntax += f"cell {cell_coolant.id}    u4gcu_1002 {cell_coolant.content.name} -1001  1002\n"
  serpent_syntax += f"cell {cell_coolant.id+10} coarse_node fill u4gcu_1002  -1001  1002 \n"

  serpent_syntax += "cell 999999  0  fill coarse_node  -1001\n"
  serpent_syntax += "cell 999998  0  outside  1001\n\n\n"

  serpent_syntax += "set gcu u4gcu_1001 u4gcu_1002 \n\n"
  serpent_syntax += f"plot 3 500 500\n\n"
  


  gcu_rel = {
    cell_fuel.id: "u4gcu_1001",
    cell_coolant.id: "u4gcu_1002",
  }
  return serpent_syntax, gcu_rel