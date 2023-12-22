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
    type_detectors = ""
    for reg_id, cell in fine_mesh.items():
      
      material = cell.content
      print(reg_id, material)
      if material.name == "void": continue
      if material.isFuel: 
        type_detectors = "region_fuel"
      else:
        type_detectors = "region_nonFuel"

      name_file = f"{global_cell_dir}/det_cell_{material.name}_{reg_id}.serp"
      
      # serpent_input = SerpentInputFileDetectorsRegion(
      #   coarse_node, fine_mesh, name_file, root, reg_id
      # )
      
      serpent_input = SerpentInputFile(
        coarse_node, fine_mesh, name_file, root
      )
      serpent_input.write_detectors(
        type_detectors, reg_id=reg_id
      )
      det_files[n_id].append(serpent_input)

    # Additional file for the surfaces
    name_surfaces_file = f"{global_cell_dir}/det_surfaces.serp"
    surf_serpent_input = SerpentInputFile(
      coarse_node, fine_mesh, name_surfaces_file, root
    )
    surf_serpent_input.write_detectors("surfaces")
    det_files[n_id].append(surf_serpent_input)

    # Additional file for cross section generation
    name_file = f"{global_cell_dir}/XS_generation.serp"
    xs_serpent_input = SerpentInputFile(
      coarse_node, fine_mesh, name_file, root, xs_generation=True
    )    
    xs_files[n_id] = xs_serpent_input
  
  return det_files, xs_files

