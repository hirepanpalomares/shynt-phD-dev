from Shynt.api_py.Probabilities.p_calc import (
  calculate_probabilities_main_nodes
)
from Shynt.api_py.Probabilities.p_calc_new import (
  calculate_probabilities_main_nodes_new
)
from Shynt.api_py.Serpent.output_reader import (
  read_detectors_data_serpentTools,
  read_detectors_data_Own,
  read_detectors_data_new,
)

import numpy as np

def get_inputs_data(det_inputs):
  det_inputs_data = {}
  for nid, files in det_inputs.items():
    det_inputs_data[nid] = []
    for serp_file_class in files:
      data = {
        'type': serp_file_class.type_of_detectors,
        'det_relation': serp_file_class.detectors_relation,
        'name': serp_file_class.name,
        'region': serp_file_class.detectors_region
      }
      det_inputs_data[nid].append(data)
  return det_inputs_data


def get_probabilities(root, det_inputs_data):
  # def get_probabilities(root, det_inputs):
  energy_g = root.energy_grid.energy_groups
  coarse_mesh = root.mesh.coarse_mesh

  
  # ------------------------------------------------------------------------
      

  # Calculating probabilities
  
  # coarse_node_scores = read_detectors_data_serpentTools(det_inputs_data)
  coarse_node_scores = read_detectors_data_Own(det_inputs_data)


  prob_nodes, prob_nodes_uncertainties = calculate_probabilities_main_nodes(
    coarse_mesh,
    coarse_node_scores,
    energy_g,
    det_inputs_data 
  )
  
  prob_nodes = apply_symmetry(prob_nodes, root)
  prob_nodes_uncertainties = apply_symmetry(prob_nodes_uncertainties, root)


  return prob_nodes, prob_nodes_uncertainties

def get_probabilities_from_lib(json_file, ids_convert):
  import json

  def convert_keys_to_int(d):
    """
    Recursively convert dictionary keys to integers, if possible.
    
    :param d: The dictionary with string keys.
    :return: A new dictionary with integer keys where applicable.
    """
    new_dict = {}
    
    for key, value in d.items():
      # Try to convert the key to an integer, otherwise keep it as a string

      new_key = None
      if isinstance(key, int):
        new_key = key
      elif isinstance(key, str):
        new_key = int(key) if key.isdigit() else key
      
      # Recursively apply the function if the value is a dictionary
      if isinstance(value, dict):
        new_dict[new_key] = convert_keys_to_int(value)
      else:
        new_dict[new_key] = value
    
    return new_dict


  probabilities = {}
  with open(json_file, 'r') as json_file:
    probabilities = json.load(json_file)
  
  probabilities = convert_keys_to_int(probabilities)

  converted_probabilities = {}
  for c_id in probabilities:
    c_id_conv = ids_convert["nodes"][c_id]
    converted_probabilities[c_id_conv] = {
      "regions": {}, "surfaces": {}
    }
    for r_id in probabilities[c_id]["regions"]:
      r_id_conv = ids_convert["regions"][r_id]
      converted_probabilities[c_id_conv]["regions"][r_id_conv] = {
        "regions": {}, "surfaces": {}
      }
      for r_id_p, probs in probabilities[c_id]["regions"][r_id]["regions"].items():
        r_id_p_conv = ids_convert["regions"][r_id_p]
        converted_probabilities[c_id_conv]["regions"][r_id_conv]["regions"][r_id_p_conv] = probs
      for s_id_p, probs in probabilities[c_id]["regions"][r_id]["surfaces"].items():
        s_id_p_conv = ids_convert["surfaces"][s_id_p]
        converted_probabilities[c_id_conv]["regions"][r_id_conv]["surfaces"][s_id_p_conv] = probs

    for s_id in probabilities[c_id]["surfaces"]:
      s_id_conv = ids_convert["surfaces"][s_id]
      converted_probabilities[c_id_conv]["surfaces"][s_id_conv] = {
        "regions": {}, "surfaces": {}
      }
      for r_id_p, probs in probabilities[c_id]["surfaces"][s_id]["regions"].items():
        r_id_p_conv = ids_convert["regions"][r_id_p]
        converted_probabilities[c_id_conv]["surfaces"][s_id_conv]["regions"][r_id_p_conv] = probs
      for s_id_p, probs in probabilities[c_id]["surfaces"][s_id]["surfaces"].items():
        s_id_p_conv = ids_convert["surfaces"][s_id_p]
        converted_probabilities[c_id_conv]["surfaces"][s_id_conv]["surfaces"][s_id_p_conv] = probs
      


  return converted_probabilities



def apply_symmetry(probabilities, root):
  main_coarse_nodes = root.mesh.coarse_mesh.equivalent_nodes.keys()
  for n_id in main_coarse_nodes:
    coarse_node = root.mesh.coarse_mesh.coarse_nodes[n_id]
    fine_mesh = coarse_node.fine_mesh
    if fine_mesh.symmetry != "":
      print(fine_mesh.regions_symmetry)
      for reg_id, cell in fine_mesh.regions.items():  
        if reg_id in fine_mesh.regions_symmetry:
          # is main region
          prob_main_reg = probabilities[n_id]["regions"][reg_id]

          surfaces = list(prob_main_reg["surfaces"].keys())
          original_surfaces = list(prob_main_reg["surfaces"].keys())

          for reg_symm in fine_mesh.regions_symmetry[reg_id]:
            p_reg_symm = {
              "regions": {}, 
              "surfaces":{}
            }
            p_reg_symm["regions"][reg_symm] = prob_main_reg["regions"][reg_id]
            p_reg_symm["regions"][reg_id] = prob_main_reg["regions"][reg_symm]
            # symmetry on region to region -----------------------------------
            for reg_symm_p in prob_main_reg["regions"]:
              if reg_symm_p in p_reg_symm["regions"]: continue
              if reg_symm_p in fine_mesh.regions_symmetry[reg_id]:
                if reg_symm_p == reg_symm: continue
                p_reg_symm["regions"][reg_symm_p] = prob_main_reg["regions"][reg_symm_p]
              else:
                p_reg_symm["regions"][reg_symm_p] = prob_main_reg["regions"][reg_symm_p]

            # symmetry on region to surface ----------------------------------
            num_surfaces = len(surfaces)
            if num_surfaces == 3:
              surfaces = surfaces[1:num_surfaces] + [surfaces[0]]
            elif num_surfaces == 4:
              surfaces = [surfaces[2],surfaces[1],surfaces[0],surfaces[3]]
            print(surfaces)
            for i, sid in enumerate(surfaces):
              p_reg_symm["surfaces"][sid] = prob_main_reg["surfaces"][original_surfaces[i]]
            probabilities[n_id]["regions"][reg_symm] = p_reg_symm
          continue
        else:
          
          pass
           
    else:
      continue
  return probabilities

def get_probabilities_new(
  energy,
  det_inputs, 
  det_relation_regions, 
  det_relation_surfaces,
  map_reg_type,
  map_reg_inv,
  eq_nodes,
  map_surf,
  coarse_nodes_surfaces,
  symmetry
):
  """Function to calculate the probabilities only for the big hex assembly, 
  according with all the hard-coded data
  """
  coarse_node_scores = read_detectors_data_new(det_inputs)

  p_nodes = calculate_probabilities_main_nodes_new(
    energy,
    coarse_node_scores,
    det_inputs,
    det_relation_regions, 
    det_relation_surfaces,
    map_reg_type,
  )


  p_nodes_converted = convert_surf_reg(
    p_nodes, map_reg_inv, map_surf, coarse_nodes_surfaces
  )

  p_all_nodes = fill_probabilities_new(
    p_nodes_converted, map_reg_inv, eq_nodes, map_surf, coarse_nodes_surfaces,
    symmetry
  )
  
  return p_all_nodes

def convert_surf_reg(p_nodes, map_reg_inv, map_surf, coarse_nodes_surfaces):
  new_probabilities = {}

  # First convert regions and surfaces ids of p_nodes
  for nid, prob in p_nodes.items():
    new_probabilities[nid] = {"regions": {}, "surfaces": {}}

    for reg, prob_reg in prob["regions"].items():
      new_reg = map_reg_inv[nid][reg]
      new_probabilities[nid]["regions"][new_reg] = {"regions": {}, "surfaces": {}}
      prob_reg_reg = prob_reg["regions"]
      prob_reg_surf = prob_reg["surfaces"]
      for reg_p, values in prob_reg_reg.items():
        new_reg_p = map_reg_inv[nid][reg_p]
        new_probabilities[nid]["regions"][new_reg]["regions"][new_reg_p] = values
      for surf_p, values in prob_reg_surf.items():
        new_surf_p_dir = map_surf[nid][surf_p]
        new_surf_p = coarse_nodes_surfaces[nid][new_surf_p_dir]["s_id"]
        new_probabilities[nid]["regions"][new_reg]["surfaces"][new_surf_p] = values
    for surf, prob_surf in prob["surfaces"].items():
      new_surf_dir = map_surf[nid][surf]
      new_surf = coarse_nodes_surfaces[nid][new_surf_dir]["s_id"]

      new_probabilities[nid]["surfaces"][new_surf] = {"regions": {}, "surfaces": {}}
      prob_surf_reg = prob_surf["regions"]
      prob_surf_surf = prob_surf["surfaces"]
      for reg_p, values in prob_surf_reg.items():
        new_reg_p = map_reg_inv[nid][reg_p]
        new_probabilities[nid]["surfaces"][new_surf]["regions"][new_reg_p] = values
      for surf_p, values in prob_surf_surf.items():
        new_surf_p_dir = map_surf[nid][surf_p]
        new_surf_p = coarse_nodes_surfaces[nid][new_surf_p_dir]["s_id"]
        new_probabilities[nid]["surfaces"][new_surf]["surfaces"][new_surf_p] = values
      

  return new_probabilities
  
def fill_probabilities_new(
  p_nodes, map_reg_inv, eq_nodes, map_surf, coarse_nodes_surfaces, symmetry
):
  new_probabilities = p_nodes

  def find_surf_direction(nid, sid):
    surfs_node = coarse_nodes_surfaces[nid]
    for dir_, surf_data in surfs_node.items():
      if surf_data is None: continue
      id_ = surfs_node[dir_]["s_id"]
      if id_ == sid: 
        return dir_
  

  for nid, same_nodes in eq_nodes.items():
    for neq in same_nodes:
      if neq in p_nodes: continue
      else:
        new_probabilities[neq] = {"regions": {}, "surfaces": {}}

        for r_id, prob_reg in p_nodes[nid]["regions"].items():
          node, reg = r_id.split("_")
          r_id_new = f"{neq}_{reg}"
          new_probabilities[neq]["regions"][r_id_new] = {"regions": {}, "surfaces": {}}
          for rp_id, values  in prob_reg["regions"].items():
            # reg -> reg --------------------------------------------------
            node, reg_p = rp_id.split("_")
            rp_id_new = f"{neq}_{reg_p}" 
            new_probabilities[neq]["regions"][r_id_new]["regions"][rp_id_new] = values.copy()
          
          for sp_id, values in prob_reg["surfaces"].items():
            # reg -> surf  --------------------------------------------------
            sp_id_dir = find_surf_direction(nid, sp_id) # dir of main node
            sp_id_dir_symm = find_new_dir_symm(
              nid, neq, sp_id_dir, symmetry
            )
            sp_id_new = coarse_nodes_surfaces[neq][sp_id_dir_symm]["s_id"]
            new_probabilities[neq]["regions"][r_id_new]["surfaces"][sp_id_new] = values.copy()

        for s_id, prob_surf in p_nodes[nid]["surfaces"].items():
          s_id_dir = find_surf_direction(nid, s_id) # dir of main node
          s_id_dir_symm = find_new_dir_symm(
            nid, neq, s_id_dir, symmetry
          )
          s_id_new = coarse_nodes_surfaces[neq][s_id_dir_symm]["s_id"]
          new_probabilities[neq]["surfaces"][s_id_new] = {"regions": {}, "surfaces": {}}
          for rp_id, values  in prob_surf["regions"].items():
            # surf -> reg --------------------------------------------------
            node, reg_p = rp_id.split("_")
            rp_id_new = f"{neq}_{reg_p}" 
            new_probabilities[neq]["surfaces"][s_id_new]["regions"][rp_id_new] = values.copy()
          
          for sp_id, values in prob_surf["surfaces"].items():
            # surf -> surf  --------------------------------------------------
            sp_id_dir = find_surf_direction(nid, sp_id) # dir of main node
            sp_id_dir_symm = find_new_dir_symm(
              nid, neq, sp_id_dir, symmetry
            )
            sp_id_new = coarse_nodes_surfaces[neq][sp_id_dir_symm]["s_id"]
            new_probabilities[neq]["surfaces"][s_id_new]["surfaces"][sp_id_new] = values.copy()
     
  return new_probabilities

def find_new_dir_symm(nid, neq, dir_, symmetry):
  mirror_changes = {
    "right": {
      "top": "top",
      "right": "left",
      "bottom": "bottom",
      "left": "right"
    },
    "down": {
      "top": "bottom",
      "right": "right",
      "bottom": "top",
      "left": "left"
    },
    "right_down": {
      "top": "bottom",
      "right": "left",
      "bottom": "top",
      "left": "right",
    }
  }
  symmetry_type = symmetry[nid][neq]
  if "same" in symmetry_type: 
    return dir_
  elif "mirror" in symmetry_type:
    mirror_type = symmetry_type["mirror"]
    new_dir = mirror_changes[mirror_type][dir_]
    return new_dir

def calculate_sum_probabilities(probabilities_unique_nodes, energy_g):
    sum_prob_unique_nodes = {}

    for id_ in probabilities_unique_nodes.keys():
        sum_prob_unique_nodes[id_] = {
            "regions": {}, "surfaces": {}
        }
        regions = list(probabilities_unique_nodes[id_]["regions"].keys()) 
        surfaces = list(probabilities_unique_nodes[id_]["surfaces"].keys()) 
        for r in regions:
            sum_prob_r = np.zeros(energy_g)
            for rp in regions:
                sum_prob_r += probabilities_unique_nodes[id_]["regions"][r]["regions"][rp]
            for sp in surfaces:
                sum_prob_r += probabilities_unique_nodes[id_]["regions"][r]["surfaces"][sp]
            sum_prob_unique_nodes[id_]["regions"][r] = sum_prob_r
        for s in surfaces:
            sum_prob_s = np.zeros(energy_g)
            for rp in regions:
                sum_prob_s += probabilities_unique_nodes[id_]["surfaces"][s]["regions"][rp]
            for sp in surfaces:
                sum_prob_s += probabilities_unique_nodes[id_]["surfaces"][s]["surfaces"][sp]
            sum_prob_unique_nodes[id_]["surfaces"][s] = sum_prob_s
    return sum_prob_unique_nodes

def check_reciprocity(probabilities, xs, energy_g, mesh_info):
    reciprocity = {}
    for n_id, prob_n in probabilities.items():
        reciprocity[n_id] = {
            "regions": {},
            "surfaces": {}
        }
        for r_i in prob_n["regions"]:
            # checking region to region
            reciprocity[n_id]["regions"][r_i] = {
                "regions": {},
                "surfaces": {}
            }
            for r_j in prob_n["regions"][r_i]["regions"]:
                reciprocity[n_id]["regions"][r_i]["regions"][r_j] = np.zeros(energy_g)
                for g in range(energy_g):
                    prob_j_i = prob_n["regions"][r_j]["regions"][r_i][g]
                    prob_i_j_rec = xs[r_j]["total"][g] * mesh_info.all_regions_vol[r_j] * prob_j_i
                    prob_i_j_rec /= (xs[r_i]["total"][g] * mesh_info.all_regions_vol[r_i])

                    prob_i_j = prob_n["regions"][r_i]["regions"][r_j][g]
                    diff = ( prob_i_j - prob_i_j_rec ) * 100 / prob_i_j
                    reciprocity[n_id]["regions"][r_i]["regions"][r_j][g] = diff
            # checking region to surface
            for s_a in prob_n["regions"][r_i]["surfaces"]:
                radius_wigner = mesh_info.all_surfaces_area[s_a] / np.sqrt(np.pi) # because pitch is equal to surface area in this case
                reciprocity[n_id]["regions"][r_i]["surfaces"][s_a] = np.zeros(energy_g)
                for g in range(energy_g):
                    prob_a_i = prob_n["surfaces"][s_a]["regions"][r_i][g]

                    prob_i_a_rec = 2 * np.pi * radius_wigner * prob_a_i / 4
                    prob_i_a_rec /= (4 * mesh_info.all_regions_vol[r_i] * xs[r_i]["total"][g])

                    prob_i_a = prob_n["regions"][r_i]["surfaces"][s_a][g]
                    diff = ( prob_i_a - prob_i_a_rec ) * 100 / prob_i_a
                    reciprocity[n_id]["regions"][r_i]["surfaces"][s_a][g] = diff
        
        for s_a in prob_n["surfaces"]:
            radius_wigner = mesh_info.all_surfaces_area[s_a] / np.sqrt(np.pi) # because pitch is equal to surface area in this case
            reciprocity[n_id]["surfaces"][s_a] = {
                "regions": {},
                "surfaces": {}
            }
            # checking surface to region
            for r_j in prob_n["surfaces"][s_a]["regions"]:
                reciprocity[n_id]["surfaces"][s_a]["regions"][r_j] = np.zeros(energy_g)
                for g in range(energy_g):
                    prob_j_a = prob_n["regions"][r_j]["surfaces"][s_a][g]
                    prob_a_j_rec = 4 * mesh_info.all_regions_vol[r_j] * xs[r_j]["total"][g] * prob_j_a
                    prob_a_j_rec /= (2 * np.pi * radius_wigner / 4)

                    prob_a_j = prob_n["surfaces"][s_a]["regions"][r_j][g]
                    diff = ( prob_a_j - prob_a_j_rec ) * 100 / prob_a_j
                    reciprocity[n_id]["surfaces"][s_a]["regions"][r_j][g] = diff
            # checking surface to surface
            pass
        
        
    
    return reciprocity
