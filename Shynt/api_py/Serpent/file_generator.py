from Shynt.api_py.Geometry.regions import Region
from Shynt.api_py.Serpent.input_file import (
  SerpentInputFile
)


import os
import sys
import numpy as np
from pathlib import Path
import os

# 
def generate_serpent_files(
  root, sdir='', add_to_dir='', in_folder=None, run_command='', exclude_nodes=[]
):
  """

  Parameters
  ----------
  root : <class Universe>
    Root universe 
  """
  coarse_mesh = root.mesh.coarse_mesh
  coarse_nodes_to_files = coarse_mesh.equivalent_nodes.keys()
  mc = root.mcparams

  
  for n_id in coarse_nodes_to_files:
    if n_id in exclude_nodes:
      continue
    coarse_node = coarse_mesh.coarse_nodes[n_id]
    fine_mesh = coarse_node.fine_mesh.regions
    for reg_id, cell in fine_mesh.items():
      material = cell.content
      if material.type_calculation == 'source':
        mc.src_calc = True


  serp_dir = ''
  if in_folder is not None:
    serp_dir = f'{in_folder}/serpent_files_{mc.dir_name}'
  else:
    serp_dir = f'serpent_files_{mc.dir_name}'

  if sdir != '':
    serp_dir += f'_{sdir}'
  
  if add_to_dir != '': 
    serp_dir += f'_{add_to_dir}'
  

  

  # input_file_argument = sys.argv[0]
  # input_file_absolute = str(Path(input_file_argument).absolute())
  # input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"
  command_to_run = ''
  input_file_dir = os.getcwd() + '/'
  # serpent_dir = input_file_dir + serp_dir

  serpent_dir = serp_dir

  try:
    assert(os.path.isdir(serpent_dir))
  except AssertionError:
    os.mkdir(serpent_dir)
  for n_id in coarse_nodes_to_files:
    if n_id in exclude_nodes:
      continue
    global_cell_dir = f"{serpent_dir}/coarse_node_type_{n_id}"
    try:
      assert(os.path.isdir(global_cell_dir))
    except AssertionError:
      os.mkdir(global_cell_dir)

  det_files = {}
  xs_files = {}
  regs = []
  nodes = []
  surfs = []
  for n_id in coarse_nodes_to_files:
    if n_id in exclude_nodes:
      continue
    nodes.append(n_id)
    global_cell_dir = f"{serpent_dir}/coarse_node_type_{n_id}"
    print(global_cell_dir)
    coarse_node = coarse_mesh.coarse_nodes[n_id]
    fine_mesh = coarse_node.fine_mesh
    print(fine_mesh.regions_symmetry)
    det_files[n_id] = []
    type_detectors = ""
    isThereCriticality = False
    last_cell = None
    print(fine_mesh.regions)
    for reg_id, cell in fine_mesh.regions.items():
      last_cell = cell
      regs.append(reg_id)
      material = cell.content
      name_file = f"{global_cell_dir}/det_cell_{material.name}_{reg_id}.serp"
      print(reg_id, material)
      if material.name == "void": continue
      if fine_mesh.symmetry != "":
        if reg_id not in fine_mesh.regions_symmetry:
          continue
      if material.type_calculation == 'source':
        serpent_input = SerpentInputFile(
          coarse_node, fine_mesh.regions, name_file, root, cell=cell,
          type_calculation='source'
        )
        serpent_input.write_detectors(
          material.type_detectors, reg_id=reg_id
        )
      elif material.type_calculation == 'criticality':
        isThereCriticality = True
        if material.isFuel: 
          material.type_detectors = "region_fuel"
        else:
          material.type_detectors = "region_nonFuel"
        serpent_input = SerpentInputFile(
          coarse_node, fine_mesh.regions, name_file, root, cell=cell
        )
        serpent_input.write_detectors(
          material.type_detectors, reg_id=reg_id
        )
      det_files[n_id].append(serpent_input)
      
      command_to_run += f'{run_command} {name_file}\n'
     
    
    # ------------------------------------------------------------------

    # Additional file for the surfaces ----------------------------------
      

    name_surfaces_file = f"{global_cell_dir}/det_surfaces.serp"
    command_to_run += f'{run_command} {name_surfaces_file}\n'



    if isThereCriticality:
      # normal
      surf_serpent_input = SerpentInputFile(
        coarse_node, fine_mesh.regions, name_surfaces_file, root,
      )
      surf_serpent_input.write_detectors("surfaces")
      det_files[n_id].append(surf_serpent_input)
      surfs += list(
        surf_serpent_input.detectors_relation['surface_to_region'].keys()
      )
    else:
      # surface detectors with src_calc in the last cell 
      surf_serpent_input = SerpentInputFile(
        coarse_node, fine_mesh.regions, name_surfaces_file, root, 
        cell=last_cell, # last_cell
        type_calculation='source'
      )
      surf_serpent_input.write_detectors("surfaces")
      det_files[n_id].append(surf_serpent_input)
    
      surfs += list(
        surf_serpent_input.detectors_relation['surface_to_region'].keys()
      )

    # Additional file for cross section generation ---------------------
    name_xs_file = f"{global_cell_dir}/XS_generation.serp"
    command_to_run += f'{run_command} {name_xs_file}\n'
    
    if isThereCriticality:
      # normal
      xs_serpent_input = SerpentInputFile(
        coarse_node, fine_mesh.regions, name_xs_file, root, xs_generation=True
      )
      xs_files[n_id] = xs_serpent_input

    else:
      # surface detectors with src_calc in the last cell 
      xs_serpent_input = SerpentInputFile(
        coarse_node, fine_mesh.regions, name_xs_file, root, xs_generation=True,
        cell=cell, # last_cell
        type_calculation='source'
      )
      xs_files[n_id] = xs_serpent_input
    # ------------------------------------------------------------------

    
  print()
  print()
  print()
  print(nodes)
  print(surfs)
  print(regs)

  return det_files, xs_files, command_to_run

