from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Serpent.input_file import (
  SerpentInputFileReferenceFlux,
  SerpentInputFileDetectorsRegion,
  SerpentInputFileDetectorsSurface,
  SerpentInputFileDetectorsXsGeneration,
  SerpentInputFile,
)


import os
import sys
import numpy as np
from pathlib import Path
import os

# 
def generate_serpent_files(root, serp_dir="serpent_files"):
  """

  Parameters
  ----------
  root : <class Universe>
    Root universe 
  """
  

  coarse_mesh = root.mesh.coarse_mesh
  coarse_nodes_to_files = coarse_mesh.equivalent_nodes.keys()
  

  # input_file_argument = sys.argv[0]
  # input_file_absolute = str(Path(input_file_argument).absolute())
  # input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"
  input_file_dir = os.getcwd() + '/'
  serpent_dir = input_file_dir + serp_dir
  try:
    assert(os.path.isdir(serpent_dir))
  except AssertionError:
    os.mkdir(serpent_dir)
  for n_id in coarse_nodes_to_files:
    global_cell_dir = f"{serpent_dir}/coarse_node_type_{n_id}"
    try:
      assert(os.path.isdir(global_cell_dir))
    except AssertionError:
      os.mkdir(global_cell_dir)

  det_files = {}
  xs_files = {}
  for n_id in coarse_nodes_to_files:
    global_cell_dir = f"{serpent_dir}/coarse_node_type_{n_id}"
    print(global_cell_dir)
    coarse_node = coarse_mesh.coarse_nodes[n_id]
    fine_mesh = coarse_node.fine_mesh.regions
    
    det_files[n_id] = []
    
    for reg_id, cell in fine_mesh.items():
      
      material = cell.content
      if material.name == "void": continue
      is_material_fuel = material.isFuel

      name_file = f"{global_cell_dir}/det_cell_{material.name}_{reg_id}.serp"
      
      # serpent_input = SerpentInputFileDetectorsRegion(
      #   coarse_node, fine_mesh, name_file, root, reg_id
      # )
      
      serpent_input = SerpentInputFile(
        coarse_node, fine_mesh, name_file, root
      )
      serpent_input.write_detectors(
        type_="region", is_material_fuel=is_material_fuel, reg_id=reg_id
      )
      det_files[n_id].append(serpent_input)

    # Additional file for the surfaces
    name_surfaces_file = f"{global_cell_dir}/det_surfaces.serp"
    surf_serpent_input = SerpentInputFile(
      coarse_node, fine_mesh, name_surfaces_file, root
    )
    surf_serpent_input.write_detectors(type_="surfaces")
    det_files[n_id].append(surf_serpent_input)

    # Additional file for cross section generation
    name_file = f"{global_cell_dir}/XS_generation.serp"
    xs_serpent_input = SerpentInputFile(
      coarse_node, fine_mesh, name_file, root, xs_generation=True
    )    
    xs_files[n_id] = xs_serpent_input
  
  return det_files, xs_files


# def get_serpent_geometry(self):
#   from Shynt.api_py.Geometry.universes import Pin
#   serpent_syntax = ""
#   node_universe = super().universe

#   try:
#     assert isinstance(node_universe, Pin)
#     pin_levels = node_universe.pin_levels

#     assert len(pin_levels) > 1
#     # regions = {
#     #   cell_id: {
#     #     "material":mat_name,
#     #     "surf-": id_,
#     #     "surf+": id_,
#     #   }
#     # }

#     # cylinders = {
#     #   s_id: radius
#     # }
#     # Closing surface: square with  id = 100

#     half_pitch = self.pitch / 2
#     closing_square_id = 101
#     closing_square = f"surf {closing_square_id} "
#     closing_square += f"sqc 0.0000 0.0000 {half_pitch}\n\n\n"

#     cylinders = {}
#     regions = {}
#     num_surf = 1

#     # surfaces ---------------------------------------
#     for l, level in enumerate(pin_levels):
#       num_cell = level.cell_id
#       if level.radius is not None:
#         cylinders[f"{num_surf}_geom"] = level.radius
#         regions[num_cell] = {
#           "material": level.material.name,
#           "surf(-)": f"{num_surf}_geom",
#           "surf(+)": ""
#         }
#         if l >= 1:
#           regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
#       else:
#         # is surroundings of pin
#         regions[num_cell] = {
#           "material": level.material.name,
#           "surf(-)": closing_square_id,
#           "surf(+)": f"{num_surf-1}_geom"
#         }
#       num_surf += 1
      
  
#     serpent_syntax += "\n\n\n"
#     for s_id, rad in cylinders.items():
#       serpent_syntax += f"surf {s_id} cyl 0.0000 0.0000 {rad}\n"
#     serpent_syntax += closing_square
    
    
#     # cells ---------------------------------------
#     for r_id, reg_info in regions.items():
#       serpent_syntax += f"cell {r_id} pin_fuel{self.id} "
#       serpent_syntax += f"{reg_info['material']} -{reg_info['surf(-)']} "
#       serpent_syntax += f"{reg_info['surf(+)']}\n"
      
#     serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
#     serpent_syntax += f"-{closing_square_id}\n"

#     serpent_syntax += f"cell root_out 0 outside {closing_square_id}\n"
    
#     boundary_ids = list(self.surfaces.keys()) 

#     serpent_syntax += "\n\n% ----- Surface for detectors --------\n"
#     detectors_surfaces = {
#       boundary_ids[0]: {
#         "syntax": f"surf {boundary_ids[0]} px -{half_pitch}\n",
#         "j_in_dir": 1
#       },
#       boundary_ids[1]: {
#         "syntax": f"surf {boundary_ids[1]} py {half_pitch}\n",
#         "j_in_dir": -1
#       },
#       boundary_ids[2]: {
#         "syntax": f"surf {boundary_ids[2]} px {half_pitch}\n",
#         "j_in_dir": -1
#       },
#       boundary_ids[3]: {
#         "syntax": f"surf {boundary_ids[3]} py -{half_pitch}\n",
#         "j_in_dir": 1
#       }
#     }
    

#     for surf_serpent in detectors_surfaces.values():
#       serpent_syntax += surf_serpent["syntax"]

    
#     self.detectors_surfaces = detectors_surfaces

#     return serpent_syntax, detectors_surfaces
#   except AssertionError:
#     raise NotImplementedError

# def get_gcu_geometry(self):
#     from Shynt.api_py.Geometry.universes import Pin
#     serpent_syntax = ""
#     node_universe = super().universe

#     try:
#       assert isinstance(node_universe, Pin)
#       pin_levels = node_universe.pin_levels

#       assert len(pin_levels) > 1
#       # regions = {
#       #   cell_id: {
#       #     "material":mat_name,
#       #     "surf-": id_,
#       #     "surf+": id_,
#       #   }
#       # }

#       # cylinders = {
#       #   s_id: radius
#       # }
#       # Closing surface: square with  id = 100

#       half_pitch = self.pitch / 2
#       closing_square_id = 101
#       closing_square = f"surf {closing_square_id} "
#       closing_square += f"sqc 0.0000 0.0000 {half_pitch}\n\n\n"

#       cylinders = {}
#       regions = {}
#       num_surf = 1

#       # surfaces ---------------------------------------
#       for l, level in enumerate(pin_levels):
#         num_cell = level.cell_id
#         if level.radius is not None:
#           cylinders[f"{num_surf}_geom"] = level.radius
#           regions[num_cell] = {
#             "material": level.material.name,
#             "surf(-)": f"{num_surf}_geom",
#             "surf(+)": ""
#           }
#           if l >= 1:
#             regions[num_cell]["surf(+)"] = f"{num_surf-1}_geom"
#         else:
#           # is surroundings of pin
#           regions[num_cell] = {
#             "material": level.material.name,
#             "surf(-)": closing_square_id,
#             "surf(+)": f"{num_surf-1}_geom"
#           }
#         num_surf += 1
        
     
#       serpent_syntax += "\n\n\n"
#       for s_id, rad in cylinders.items():
#         serpent_syntax += f"surf {s_id} cyl 0.0000 0.0000 {rad}\n"
#       serpent_syntax += closing_square
      
      
#       # cells ---------------------------------------
#       u4gcu = []
#       gcu_id = 1
#       for r_id, reg_info in regions.items():
#         serpent_syntax += f"cell {r_id+1000}  u4gcu{gcu_id} "
#         serpent_syntax += f"{reg_info['material']} "
#         serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

#         serpent_syntax += f"cell {r_id+1001} pin_fuel{self.id} fill "
#         serpent_syntax += f"u4gcu{gcu_id}"
#         serpent_syntax += f"-{reg_info['surf(-)']} {reg_info['surf(+)']}\n"

#         u4gcu.append(f"u4gcu{gcu_id}")
#         gcu_id += 1

#       serpent_syntax += f"cell root_in 0 fill pin_fuel{self.id} "
#       serpent_syntax += f"-{closing_square_id}\n"

#       serpent_syntax += f"cell root_out 0 outside {closing_square_id}\n"
      
      

#       return serpent_syntax
#     except AssertionError:
#       raise NotImplementedError
  
