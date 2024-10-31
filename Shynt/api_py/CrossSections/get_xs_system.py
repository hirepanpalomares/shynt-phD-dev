from .extractor_xs import get_cross_sections

def get_xs_files_data(xs_serpent_files):
  xs_files_data = {}
  # Create dictionary to not provide the entire SerpentInputFile class --------
  if len(xs_files_data) == 0:
    for id_coarse, xs_inp in xs_serpent_files.items():
      xs_files_data[id_coarse] = {
        'name': xs_inp.name,
        'xs_gcu': xs_inp.xs_gcu
      }
    
  return xs_files_data


      
def  get_xs_data(
  eq_regions, root, 
  xs_files_data, 
  mapped_regions={},
  transport_correction=False, 
  scattering_production=False, 
):
  """ Method to get the XS for all the regions in all nodes

  Parameters
  ----------

  xs_files[id_coarse] = {
    'name': "",
    'xs_gcu': {}
  }

  Returns
  -------

  """
  energy_g = root.energy_grid.energy_groups
  coarse_nodes = root.mesh.coarse_mesh.coarse_nodes

  
  # ---------------------------------------------------------------------------
  xs = get_cross_sections(
    energy_g, xs_files_data, coarse_nodes, scattering_production, 
    map_regions=mapped_regions
  )

  


  if transport_correction:
    print("Calculating transport correction ...")
    xs = calculate_transport_corrected_xs(xs, energy_g)
  else:
    for cid in xs: 
      xs[cid]["scatter"] = xs[cid]["scatter_p0"].tolist()
      xs[cid]["scatter_p1"] = xs[cid]["scatter_p1"].tolist()
      xs[cid]["scatter_p0"] = xs[cid]["scatter_p0"].tolist()
      xs[cid]["total"] = xs[cid]["total"].tolist()
      pass

  # filling probabilities to every similar node
  # new_xs = {}
  # print(xs.keys())
  # for reg_eq, main_reg in eq_regions.items():
    # print(reg_eq, main_reg)
    # Filling XS
    # new_xs[reg_eq] = xs[main_reg]
    
  print("XS retrieved ------------------")
  
  return xs


def get_xs_data_from_lib(json_file, ids_convert):
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

  xs = {}
  with open(json_file, 'r') as json_f:
    xs = json.load(json_f)
  
  xs = convert_keys_to_int(xs)

  converted_xs = {}
  
  for r_id in xs:
    r_id_conv = ids_convert["regions"][r_id]
    converted_xs[r_id_conv] = xs[r_id]


  return converted_xs


def calculate_transport_corrected_xs(xs, energy_g):
  import numpy as np

  xs_tr_0 = {
    
  }

  for cid in xs:
    xs_tr_0[cid] = {
      "capture": xs[cid]["capture"],
      "nuSigFission": xs[cid]["nuSigFission"],
      "fission": xs[cid]["fission"],
      "absorption": xs[cid]["absorption"],
      "chi": xs[cid]["chi"],      
    }
    # Calculation of transport correction -----------
    scatt_tr0 = xs[cid]["scatter_p0"]
    scatt_p1 = xs[cid]["scatter_p1"]
    total_tr0 = xs[cid]["total"]
    for gp in range(energy_g):
      # scattering
      sum_p1 = np.sum(scatt_p1[:][gp])
      scatt_tr0[gp][gp] = scatt_tr0[gp][gp] - sum_p1
    
      # Total      
      total_tr0[gp] = total_tr0[gp] - sum_p1
      
    xs_tr_0[cid]["total"] = total_tr0.tolist()
    xs_tr_0[cid]["scatter"] = scatt_tr0.tolist()
    xs[cid]["scatter_p1"] = xs[cid]["scatter_p1"].tolist()
    xs[cid]["scatter_p0"] = xs[cid]["scatter_p0"].tolist()


  return xs_tr_0