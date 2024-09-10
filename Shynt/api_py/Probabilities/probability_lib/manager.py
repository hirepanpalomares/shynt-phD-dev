import pandas as pd
import os
import numpy as np

def read(
  prob_file_name, energy
):
  
  
  script_dir = os.path.dirname(os.path.abspath(__file__))

  
  df = pd.read_csv(f"{script_dir}/{prob_file_name}")
  probabilities = {  }
  for index, row in df.iterrows():
    c_id = row["c_id"]
    from_type = f"{row['from']}s"
    to_type = f"{row['to']}s"
    from_id = row["from_id"]
    to_id = row["from_id"]
    g = row["g"]
    prob_value = row["probability"]

    if c_id not in probabilities:
      probabilities[c_id] = {
        "surfaces": {},
        "regions": {}
      }
    
    if from_id not in probabilities[c_id][from_type]:
      probabilities[c_id][from_type][from_id] = {
        "surfaces": {},
        "regions": {}
      }
    
    if to_id not in probabilities[c_id][from_type][from_id][to_type]:
      probabilities[c_id][from_type][from_id][to_type][to_id] = np.zeros(energy)

    probabilities[c_id][from_type][from_id][to_type][to_id][g] = prob_value
  
  return probabilities




def write(assembly_type, ures, void_serpent, symmetry_serpent, ene_struct):
  pass

