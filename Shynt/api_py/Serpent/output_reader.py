# import serpentTools
import numpy as np

class DetectorOutput:
  tallies = []
  errors = None

def read_res_file(fname):
  res = {}
  constants = [
    'INF_TOT', 'INF_NSF', 'INF_FISS', 'INF_CAPT', 'INF_ABS', 'INF_CHIT',
    'INF_S0', 'INF_S1', 'INF_SP0', 'INF_SP1', 'INF_SCATT0', 'INF_SCATT1', 
    'INF_SCATT2', 'INF_SCATT3', 'INF_SCATT4', 'INF_SCATT5', 'INF_SCATT6', 
    'INF_SCATT7'
  ]
  
  read_gcu = False
  with open(fname, "r") as f:
    for line in f:
      line_sp = line.split()
      if len(line_sp) > 0:
        if line_sp[0] == 'GC_UNIVERSE_NAME':
          gcu_name = line_sp[-2][1:-1]
          res[gcu_name] = {}
          read_gcu = True
        if line_sp[0] in constants:
          data = line_sp[6:-1]
          xs_read = True
          xs_vector = []
          sigma_vector = []
          for val in data:
            if xs_read: 
              xs_vector.append(float(val))
            else:
              sigma_vector.append(float(val))
            xs_read = not xs_read
          res[gcu_name][line_sp[0]] = np.array(xs_vector)
  return res


def read_res_file_metadata(fname):
  res = {}
  constants = [
    'TOT_CPU_TIME', 'RUNNING_TIME', 'OMP_THREADS', 'MPI_TASKS',
  ]

  metadata = {}
  
  read_gcu = False
  with open(fname, "r") as f:
    for line in f:
      line_splitted = line.split()
      
      if len(line_splitted) > 0:
        if line_splitted[0] == 'CPU_TYPE':
          metadata['CPU_TYPE'] = ' '.join(line_splitted[5:-1])
        if line_splitted[0] in constants:
          val = line_splitted[-2]
          metadata[line_splitted[0]] = float(val)
          
          
  return metadata



def read_detector_file(fname):
  """
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
  data = {
    '': DetectorOutput()
  }
  tallies = []
  errors = []
  with open(fname, "r") as f:
    counts = False
    energy = False
    det_name = ''
    for line in f:
      line_sp = line.split()
      # ---------------------------------------
      # Obtain detector name
      if line.startswith("DET"):
        det_name = line_sp[0].split("DET")[1]
        if det_name[-1] == "E":
          det_name = det_name[:-1]
          
          data[det_name].tallies = np.array(tallies)
          data[det_name].errors = np.array(errors)

          counts = False
        else:
          data[det_name] = DetectorOutput()
          counts = True
      
        tallies = []
        errors = []
      # ---------------------------------------
      if counts and len(line_sp) == 12:
        tally = float(line_sp[-2])
        error = float(line_sp[-1])
        tallies.append(tally)
        errors.append(error)

      
  return data


def read_detectors_data_Own(det_inputs):
  coarse_node_scores = {}
  for id_, inp in det_inputs.items():
    coarse_node_scores[id_] = { }
    for file_ in inp:
      det_file_name = ""
      if not isinstance(file_, str):
        det_file_name = file_['name'] + "_det0.m"
      else:
        det_file_name = file_ + "_det0.m"
      # data_detector_serp_tools = serpentTools.read(det_file_name)
      # detectors_data = data_detector_serp_tools.detectors
      data_detector = read_detector_file(det_file_name)
      coarse_node_scores[id_].update(data_detector)
      
  return coarse_node_scores


def read_detectors_data_serpentTools(det_inputs):
  coarse_node_scores = {}
  for id_, inp in det_inputs.items():
    coarse_node_scores[id_] = { }
    for file_ in inp:
      det_file_name = ""
      if not isinstance(file_, str):
        det_file_name = file_['name'] + "_det0.m"
      else:
        det_file_name = file_ + "_det0.m"
      # data_detector_serp_tools = serpentTools.read(det_file_name)
      # detectors_data = data_detector_serp_tools.detectors
      # coarse_node_scores[id_].update(detectors_data)
      
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