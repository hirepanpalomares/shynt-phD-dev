import serpentTools


def read_detector_file(fname):
  """
    #!NOT USED ANYMORE; CHANGED FOR serpentTools module
  
    Helper to extract the data from the detectors

    -----------
    returns:
      - dectors data in a dictionary
    Structure of the dictionary

    dictionary = {
      "detector_name": {
        "neutrons": [
          (counts_g1, std_dev_g1), 
          ..., (counts_gN, std_dev_gN)
        ],
        "energy": [
          (energy_bin_1_low, energy_bin_1_high), 
          ..., 
          (energy_bin_N_low, energy_bin_N_high)
        ],
      },
    }
  """
  data = {}
  with open(fname, "r") as f:
    counts = False
    energy = False
    for line in f:
      line_sp = line.split()
      if line.startswith("DET"):
        det_name = line_sp[0].split("DET")[1]
        if det_name[-1] == "E":
          counts = False
          energy = True
          det_name = det_name[:-1]
        else:
          data[det_name] = {
            "neutrons": [],
            "energy": []
          }
          counts = True
          energy = False
      if counts and len(line_sp) == 12:
        g = int(line_sp[0]) - 1
        neutrons = float(line_sp[-2])
        std = float(line_sp[-1])
        data[det_name]["neutrons"].append((neutrons, std))
      if energy and len(line_sp) == 3 and line_sp[-1] != "[":
        g0 = float(line_sp[0])
        gf = float(line_sp[1])
        another_number = float(line_sp[2])
        data[det_name]["energy"].append((g0, gf))
  return data


def read_detectors_data(det_inputs):
  coarse_node_scores = {}
  for id_, inp in det_inputs.items():
    coarse_node_scores[id_] = { }
    for file_ in inp:
      det_file_name = ""
      if not isinstance(file_, str):
        det_file_name = file_.name + "_det0.m"
      else:
        det_file_name = file_ + "_det0.m"
      data_detector_serp_tools = serpentTools.read(det_file_name)
      detectors_data = data_detector_serp_tools.detectors
      coarse_node_scores[id_].update(detectors_data)
      
  return coarse_node_scores




def read_detectors_data_new(det_inputs):
  """For the hardcoded data of the big assembly
  """
  coarse_node_scores = {}
  for id_, inp in det_inputs.items():
    # id_ is a coarse node identifier
    coarse_node_scores[id_] = {
      
    }
    
    for file_ in inp:
      det_file_abs_name = file_ + "_det0.m"
      # print(det_file_name)
      file_data = serpentTools.read(det_file_abs_name)
      detectors_data = file_data.detectors
      
      coarse_node_scores[id_].update(detectors_data)


  return coarse_node_scores