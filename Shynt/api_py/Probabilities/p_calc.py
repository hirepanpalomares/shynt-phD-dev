import numpy as np

from Shynt.api_py.materials import Material

def get_fuel_counts(
  scores, detectors,regions, surfaces#, fuel_regions
):
  """ 
  Method to extract the following rates:
    - fuel --> regions
    - fuel --> surfaces
  
  This methods counts the neutrons of every possible interaction 
  fuel -> clad, fuel -> coolant, etc
  """  

  # Total reaction rate in the fuel
  det_name_total = detectors["total_rate"]

  # All neutrons entering the fuel through surface
  det_name_all_incoming = detectors["all_to_fuel"]

  # Neutrons  fuel to fuel        
  total_tallies = abs(scores[det_name_total].tallies)
  all_incoming_tallies = abs(scores[det_name_all_incoming].tallies)
  neutrons_fuel_to_fuel = total_tallies - all_incoming_tallies 
  
  total_errors = scores[det_name_total].errors
  all_inc_errors = scores[det_name_all_incoming].errors
  sqrt_sum = np.power(all_inc_errors,2) + np.power(total_errors,2)
  errors_fuel_to_fuel = np.sqrt(sqrt_sum)

  # Neutrons that interact in the fuel and then in other regions
  fuel_regions_counts = {}
  fuel_regions_errors = {}
  region_to_region = detectors["region_to_region"]
  cfr = None
  for rp in regions:
    if rp not in region_to_region: 
      cfr = rp
      fuel_regions_counts[cfr] = { "regions": {}, "surfaces": {} }
      fuel_regions_errors[cfr] = { "regions": {}, "surfaces": {} }

  for rp in regions:
    if rp != cfr:
      det_name = region_to_region[rp]
      region_tallies = np.flip(abs(scores[det_name].tallies))
      error_region_tallies = np.flip(abs(scores[det_name].errors))
      fuel_regions_counts[cfr]["regions"][rp] = region_tallies
      fuel_regions_errors[cfr]["regions"][rp] = error_region_tallies
      # print(f"reg_{cfr}_to_reg_{rp}: {region_tallies}")
      
    else:
      
      fuel_regions_counts[cfr]["regions"][cfr] = np.flip(neutrons_fuel_to_fuel)
      fuel_regions_errors[cfr]["regions"][cfr] = np.flip(errors_fuel_to_fuel)
      # print(f"reg_{cfr}_to_reg_{cfr}: {neutrons_fuel_to_fuel}")



  # Neutrons fuel to surfaces
  region_to_surfaces = detectors["region_to_surface"]
  for s in surfaces:
    det_name_surface = region_to_surfaces[s]
    surface_tallies = np.flip(abs(scores[det_name_surface].tallies))
    error_surface_tallies = np.flip(abs(scores[det_name_surface].errors))
    fuel_regions_counts[cfr]["surfaces"][s] = surface_tallies
    fuel_regions_errors[cfr]["surfaces"][s] = error_surface_tallies
    # print(f"reg_{cfr}_to_surf_{s}: {surface_tallies}")


      
  return fuel_regions_counts, fuel_regions_errors

def get_fuel_probabilities(
  fuel_neutrons, regions, surfaces, energy, fuel_regions
):
  p_fuel = {
    fr : {
      "regions": { },
      "surfaces": { }
    } for fr in fuel_regions
  }
  

  # tneff : total_neutrons_emmited_from_fuel
  for fr in fuel_regions:
    tneff = np.zeros(energy)
    for r in regions:
      tneff += fuel_neutrons[fr]["regions"][r]
    for s in surfaces:
      tneff += fuel_neutrons[fr]["surfaces"][s]
    # Calculation of probabilities
    for r in regions:
      p_fuel[fr]["regions"][r] = fuel_neutrons[fr]["regions"][r] / tneff
    for s in surfaces:
      p_fuel[fr]["surfaces"][s] = fuel_neutrons[fr]["surfaces"][s] / tneff

  
  return p_fuel

def get_nonFuel_counts(
  scores, detectors, regions, surfaces, nonFuel_regions
):
  """
  Method to extract the following rates:
    - mod --> regions
    - mod --> surface
  """
  

  # nonFuel_counts = {}
  # nonFuel_errors = {}
  region_to_region = detectors["region_to_region"]
  region_to_surface = detectors["region_to_surface"]
  # print(region_to_region)
  # print(region_to_surface)
  # print(detectors.keys())
  cnfr = None
  for rp in regions:
    if rp not in region_to_region: cnfr = rp
  nonFuel_counts = { cnfr: { "regions": { }, "surfaces": { } } }
  nonFuel_errors = { cnfr: { "regions": { }, "surfaces": { } } }
  
  # print(f"Region {cnfr}")

  # ppp = [print(i,j) for i, j in scores.items()]
  for rp, cell in regions.items(): 
    # print(rp, cell.content.name)
    if rp == cnfr: continue
    # rp is the region where the neutron intercts for the second time
    det_name_rp = region_to_region[rp]
    tallies = np.flip(abs(scores[det_name_rp].tallies))
    errors = np.flip(abs(scores[det_name_rp].errors))
    nonFuel_counts[cnfr]["regions"][rp] = tallies
    nonFuel_errors[cnfr]["regions"][rp] = errors
    # print(f"reg_{cnfr}_to_reg_{rp}: {tallies}")

  det_name_same_region = detectors["same_region"]
  same_region_tallies = np.flip(abs(scores[det_name_same_region].tallies))
  same_region_errors = np.flip(abs(scores[det_name_same_region].errors))
  # print(f"reg_{cnfr}_to_reg_{cnfr}: {same_region_tallies}")


  nonFuel_counts[cnfr]["regions"][cnfr] = same_region_tallies
  nonFuel_errors[cnfr]["regions"][cnfr] = same_region_errors

  
  for s in surfaces:
    det_name_surface = region_to_surface[s]
    tallies = np.flip(abs(scores[det_name_surface].tallies))
    errors = np.flip(abs(scores[det_name_surface].errors))
    nonFuel_counts[cnfr]["surfaces"][s] = tallies
    nonFuel_errors[cnfr]["surfaces"][s] = errors
    # print(f"reg_{cnfr}_to_surf_{s}: {tallies}")



  return nonFuel_counts, nonFuel_errors

def get_nonFuel_probabilities(
  nf_neutrons, regions, surfaces, energy, nonFuel_regions
):
    
  nfr = list(nf_neutrons.keys())[0]
  p_nonFuel = { nfr: { "regions": {}, "surfaces": {} } }
  # tne_nf : total neutrons emmited from non fuel
  tne_nf = np.zeros(energy)
  for rp in regions:
    tne_nf += nf_neutrons[nfr]["regions"][rp]
  for s in surfaces:
    tne_nf += nf_neutrons[nfr]["surfaces"][s]

  # Calculating probabilities
  for rp in regions:
    p_nonFuel[nfr]["regions"][rp] = nf_neutrons[nfr]["regions"][rp]/tne_nf
  for s in surfaces:
    p_nonFuel[nfr]["surfaces"][s] = nf_neutrons[nfr]["surfaces"][s]/tne_nf
   
  return p_nonFuel


def get_surface_counts(
  scores, detectors, energy, regions, surfaces
):
  """
  Method to extract the following rates:
    - surface --> regions
    - surface --> surface

  """
  # print(surfaces)

  # Preparing surface_counts
  surface_counts = {    
    s: {
      "regions": {
        r: np.zeros(energy) for r in regions
      },
      "surfaces": {
        su: np.zeros(energy) for su in surfaces
      }
    } for s in surfaces
  }
  surface_errors = {    
    s: {
      "regions": {
        r: np.zeros(energy) for r in regions
      },
      "surfaces": {
        su: np.zeros(energy) for su in surfaces
      }
    } for s in surfaces
  }

  # print(surfaces)
  for s in surfaces:
    # print(s)
    surface_to_region = detectors["surface_to_region"][s]
    surface_to_surface = detectors["surface_to_surface"][s]
    for r in regions:
      det_name_region = surface_to_region[r]
      region_tallies = np.flip(abs(scores[det_name_region].tallies))
      # print(f"surf_{s}_to_reg_{r}: {region_tallies}")
      error_region_tallies = np.flip(abs(scores[det_name_region].errors))
      surface_counts[s]["regions"][r] = region_tallies
      surface_errors[s]["regions"][r] = error_region_tallies
    for sp in surfaces:
      det_name_surface = surface_to_surface[sp]
      surf_tallies = np.flip(abs(scores[det_name_surface].tallies))
      error_surf_tallies = np.flip(abs(scores[det_name_surface].errors))
      # print(f"surf_{s}_to_surf_{sp}: {surf_tallies}")
      surface_counts[s]["surfaces"][sp] = surf_tallies
      surface_errors[s]["surfaces"][sp] = error_surf_tallies

  return surface_counts, surface_errors
  
def get_surface_probabilities(
  surf_neutrons, energy, regions, surfaces
):
  # tne_s : total neutrons emmited from surfaces
  # print(surf_neutrons[2]["regions"][13])
  tne_s = {
    s: np.zeros(energy) for s in surfaces
  }

  p_surfaces = {
    s: {
      "regions": {
        r: None for r in regions
      },
      "surfaces": {
        sp: None for sp in surfaces
      }
    } for s in surfaces 
  }

  
  for s in surfaces:

    for r in regions:
      tne_s[s] += surf_neutrons[s]["regions"][r]
      # print(s, surf_neutrons[s]["regions"][r])
    for sp in surfaces:
      tne_s[s] += surf_neutrons[s]["surfaces"][sp]
      # print(s, surf_neutrons[s]["surfaces"][sp])
    # print(s, tne_s[s], "total")

  # Calculate probabilities -------------------------------------------------
  for s in surfaces:
    for r in regions:
      p_surfaces[s]["regions"][r] = surf_neutrons[s]["regions"][r]/tne_s[s]
    for sp in surfaces:
      p_surfaces[s]["surfaces"][sp] = surf_neutrons[s]["surfaces"][sp]/tne_s[s]

  return p_surfaces


def calculate_probabilities_main_nodes(
  coarse_mesh, det_inputs, coarse_node_scores, energy
):                    
  """
    # TODO: The number of detectors can be reduced (see bellow)

    The probability for a neutron to enter the cell through a given surface
    and go out through the same surface without interacting is CERO
    
    The energy structure of scores are ordered from thermal --> fast  

    ------------------------------------------------------------------------
    
    coarse_node_scores.keys() - scores of the detectors by name
  """
  
  
  probabilities = {}
  uncertainties = {}
  equivalent_regions = coarse_mesh.equivalent_regions
  equivalent_surfaces = coarse_mesh.equivalent_surfaces
  coarse_nodes = coarse_mesh.coarse_nodes
  # ----------------------------------------------------------------------------------------------------
  for n_id in det_inputs: # Loop for the different coarse nodes
    print(n_id)
    regions = coarse_nodes[n_id].fine_mesh.regions
    surfaces = coarse_nodes[n_id].surfaces
    fuel_regions = [
      r for r, cell in regions.items() if cell.content.isFuel
    ]
    nonFuel_regions = [
      r for r, cell in regions.items() if not cell.content.isFuel
    ]
    probabilities[n_id] = { 
      "regions": {},
      "surfaces": {}
    }
    uncertainties[n_id] = { 
      "regions": {},
      "surfaces": {}
    }

    fuel_probabilities = {}
    nonFuel_probabilities = {}
    surface_probabilities = {}
    
    for detector_file in det_inputs[n_id]:
      type_ = detector_file.type_of_detectors
      detectors = detector_file.detectors_relation
      name_file = detector_file.name.split("/")[-1]
      if type_ == "region_fuel":
        fuel_neutrons, fuel_errors = get_fuel_counts(
          coarse_node_scores[n_id],
          detectors,
          regions,
          surfaces, 
          # fuel_regions
        )
        fuel_probabilities = get_fuel_probabilities(
          fuel_neutrons,
          regions,
          surfaces,
          energy,
          fuel_regions
        )
        # fuel_uncertainties = calculate_fuel_uncertainties()
      elif type_ == "region_nonFuel":
        print(f"Extracting non fuel region detector scores", end="")
        print(f"\tnode {n_id}\t\tfile name: {name_file}")

        nonFuel_neutrons, nonFuel_errors = get_nonFuel_counts(
          coarse_node_scores[n_id],
          detectors,
          regions,
          surfaces,
          nonFuel_regions
        )
        print(f"Calculating collision probabilities\t\tnode {n_id}", end="")
        print(f"\t\tfile name: {name_file}")
        
        nonFuel_probabilities = get_nonFuel_probabilities(
          nonFuel_neutrons,
          regions,
          surfaces,
          energy, 
          nonFuel_regions
        )

        # nonFuel_uncertainties = calculate_onnFuel_uncertainties()

        # print(nonFuel_uncertainty)
        # print("-"*50)
      elif type_ == "surfaces":
        # print("---------------------------------")
        surface_neutrons, surface_errors = get_surface_counts(
          coarse_node_scores[n_id],
          detectors,
          energy,
          regions,
          surfaces
        )
        # print(surface_neutrons)
        surface_probabilities  = get_surface_probabilities(
          surface_neutrons,
          energy,
          regions,
          surfaces
        )
        # surface_uncertainties = calculate_surface_uncertainties()

        probabilities[n_id]["surfaces"] = surface_probabilities
      else:
        print("Warning in calculate probabilities, type of detector not valid")
        raise SystemError
      probabilities[n_id]["regions"].update(fuel_probabilities)
      probabilities[n_id]["regions"].update(nonFuel_probabilities)
      probabilities[n_id]["surfaces"].update(surface_probabilities)
      # uncertainties[n_id]["regions"].update(fuel_prob_uncertainty)
      # uncertainties[n_id]["regions"].update(nonFuel_uncertainty)
      # uncertainties[n_id]["surfaces"].update(surface_uncertainties)





  return probabilities
    
