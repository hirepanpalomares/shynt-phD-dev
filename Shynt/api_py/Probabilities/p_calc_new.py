import numpy as np

def get_region_probabilities(
  neutrons, regions, surfaces, energy
):
  p_region = {
    "regions": { },
    "surfaces": { }
  }
  

  total_n = np.zeros(energy)
  for r in regions:
    total_n += neutrons["regions"][r]
  for s in surfaces:
    total_n += neutrons["surfaces"][s]
  # Calculation of probabilities
  for r in regions:
    p_region["regions"][r] = neutrons["regions"][r] / total_n
  for s in surfaces:
    p_region["surfaces"][s] = neutrons["surfaces"][s] / total_n

        


  return p_region

def get_surface_probabilities(
  surface_neutrons, energy, regions, surfaces
):

  p_surf = {
    "regions": {
      r: None for r in regions
    },
    "surfaces": {
      sp: None for sp in surfaces
    }
    
  }

  
  total_emmited = np.zeros(energy)
  for r in regions:
    total_emmited += surface_neutrons["regions"][r]
  for sp in surfaces:
    total_emmited += surface_neutrons["surfaces"][sp]

  # Calculate probabilities ------------------------------------
  for r in regions:
    p_surf["regions"][r] = surface_neutrons["regions"][r]/total_emmited
  for sp in surfaces:
    p_surf["surfaces"][sp] = surface_neutrons["surfaces"][sp]/total_emmited

      
  return p_surf

def get_nonFuel_counts(
  scores, detectors, regions, surfaces, reg
):
    """
        Method to extract the following rates:
            - mod --> regions
            - mod --> surface
    """
    nonFuel_counts = {
      "regions": { },
      "surfaces": { }
    }

    
      
    for rp in regions: 
      det_name_rp = detectors["regions"][rp].name
      nonFuel_counts["regions"][rp] = np.flip(
        abs(scores[det_name_rp].tallies)
      )

    for s in surfaces:
      det_name_surface = detectors["surfaces"][s].name
      nonFuel_counts["surfaces"][s] = np.flip(
        abs(scores[det_name_surface].tallies)
      )


    return nonFuel_counts

def get_fuel_counts(
  scores, detectors, regions, surfaces, fr
):
  """
    Method to extract the following rates:
        - fuel --> regions
        - fuel --> surfaces
    
    This methods counts the neutrons of every possible 
    interaction fuel -> clad, fuel -> coolant, etc
  """  
  fuel_regions_counts = {
    "regions": { },
    "surfaces": { }
  }

  
  # Total reaction rate in the fuel
  det_name_total = detectors["total"].name

  # All neutrons entering the fuel through surface
  det_name_all_incoming = detectors["all_to_fuelReg"].name

  # Neutrons  fuel to fuel 
  total_rate = abs(scores[det_name_total].tallies)
  incoming_fuel = abs(scores[det_name_all_incoming].tallies)
  neutrons_fuel_to_fuel = total_rate - incoming_fuel


  # Neutrons that interact in the fuel and then in other regions
  for rp in regions:
    if rp != fr:
      det_name_region = detectors["regions"][rp].name
      fuel_regions_counts["regions"][rp] = np.flip(
        abs(scores[det_name_region].tallies)
      )
    else:
      fuel_regions_counts["regions"][fr] = np.flip(neutrons_fuel_to_fuel)

  # Neutrons fuel to surfaces
  for s in surfaces:
    det_name_surface = detectors["surfaces"][s].name
    fuel_regions_counts["surfaces"][s] = np.flip(
      abs(scores[det_name_surface].tallies)
    )

  return fuel_regions_counts

def get_surface_counts(
  scores, detectors, energy, regions, surfaces
):
  """
      Method to extract the following rates:
          - surface --> regions
          - surface --> surface

  """

  # Preparing surface_counts
  surface_counts = {      
    "regions": {
      r: np.zeros(energy) for r in regions
    },
    "surfaces": {
      su: np.zeros(energy) for su in surfaces
    }
  }
  
  
  for r in regions:
    det_name_region = detectors["regions"][r].name
    surface_counts["regions"][r] = np.flip(
      abs(scores[det_name_region].tallies)
    )
  for sp in surfaces:
    det_name_surface = detectors["surfaces"][sp].name
    surface_counts["surfaces"][sp] = np.flip(
      abs(scores[det_name_surface].tallies)
    )

  return surface_counts



def calculate_probabilities_main_nodes_new(
  energy,
  coarse_node_scores,
  det_inputs,
  det_relation_regions, 
  det_relation_surfaces,
  map_reg_type
):                    
  """
      
  """
  
  
  probabilities = {}

  # ------------------------------------------------------------------------
  for n_id in det_inputs: # Loop for the different coarse nodes
    
    probabilities[n_id] = { 
      "regions": {},
      "surfaces": {}
    }
    
    surface_probabilities = {}
    regions = list(det_relation_regions[n_id].keys())
    surfaces = list(det_relation_surfaces[n_id].keys())
    for r_id in regions:
      reg_probabilities = {}
      neutrons = {}
      region_type = map_reg_type[n_id][r_id]
      detectors = det_relation_regions[n_id][r_id]
      if region_type == "fuel":
        neutrons = get_fuel_counts(
          coarse_node_scores[n_id],
          detectors,
          regions,
          surfaces,
          r_id
        )
      if region_type == "nonFuel":
        neutrons = get_nonFuel_counts(
          coarse_node_scores[n_id],
          detectors,
          regions,
          surfaces,
          r_id
        )
        
      reg_probabilities = get_region_probabilities(
        neutrons, regions, surfaces, energy
      )

      probabilities[n_id]["regions"][r_id] = reg_probabilities
    
    for s_id in surfaces:
      surf_probabilities = {}
      neutrons = {}
      detectors = det_relation_surfaces[n_id][s_id]
      surface_neutrons = get_surface_counts(
        coarse_node_scores[n_id],
        detectors,
        energy,
        regions,
        surfaces
      )
      surface_probabilities = get_surface_probabilities(
        surface_neutrons, energy, regions, surfaces
      )
      
      probabilities[n_id]["surfaces"][s_id] = surface_probabilities
      
  return probabilities
    

