import numpy as np


def get_fuel_counts(
  scores, detectors,regions, surfaces, cfr#, fuel_regions
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
  # print(f'scores keys: {scores.keys()}')
  # print("current fuel region", cfr)
  fuel_regions_counts[cfr] = { "regions": {}, "surfaces": {} }
  fuel_regions_errors[cfr] = { "regions": {}, "surfaces": {} }
  
  for rp in regions:
    if rp != cfr:
      # print(rp)
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
  fuel_neutrons, regions, surfaces, energy, cfr
):
  p_fuel = {
    cfr : {
      "regions": { },
      "surfaces": { }
    }
  }
  

  # tneff : total_neutrons_emmited_from_fuel
  # print(fuel_regions)
  # print(fuel_neutrons.keys())
  tneff = np.zeros(energy)
  for r in regions:
    tneff += fuel_neutrons[cfr]["regions"][r]
  for s in surfaces:
    tneff += fuel_neutrons[cfr]["surfaces"][s]
  # Calculation of probabilities
  for r in regions:
    p_fuel[cfr]["regions"][r] = fuel_neutrons[cfr]["regions"][r] / tneff
    p_fuel[cfr]["regions"][r] = p_fuel[cfr]["regions"][r].tolist()
  for s in surfaces:
    p_fuel[cfr]["surfaces"][s] = fuel_neutrons[cfr]["surfaces"][s] / tneff
    p_fuel[cfr]["surfaces"][s] = p_fuel[cfr]["surfaces"][s].tolist()

  
  return p_fuel, tneff

def get_nonFuel_counts(
  scores, detectors, regions, surfaces, cnfr
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
  print(region_to_region)
  print(region_to_surface)

  # print(detectors.keys())
  
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
  nf_neutrons, regions, surfaces, energy, nfr
):
    
  
  # print(nfr, 'asdasdas')
  # raise SystemExit

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
    p_nonFuel[nfr]["regions"][rp] = p_nonFuel[nfr]["regions"][rp].tolist()

  for s in surfaces:
    p_nonFuel[nfr]["surfaces"][s] = nf_neutrons[nfr]["surfaces"][s]/tne_nf
    p_nonFuel[nfr]["surfaces"][s] = p_nonFuel[nfr]["surfaces"][s].tolist()
   
  return p_nonFuel, tne_nf

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
      if sp == s:
        surface_counts[s]["surfaces"][sp] = np.zeros(energy)
        surface_errors[s]["surfaces"][sp] = np.zeros(energy)
        continue
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
      p_surfaces[s]["regions"][r] = p_surfaces[s]["regions"][r].tolist()
    for sp in surfaces:
      p_surfaces[s]["surfaces"][sp] = surf_neutrons[s]["surfaces"][sp]/tne_s[s]
      p_surfaces[s]["surfaces"][sp] = p_surfaces[s]["surfaces"][sp].tolist()

  return p_surfaces, tne_s

def calculate_probabilities_main_nodes(
  coarse_mesh, coarse_node_scores, energy, det_inputs_data
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
  prob_uncertainties = {}
  # equivalent_regions = coarse_mesh.equivalent_regions
  # equivalent_surfaces = coarse_mesh.equivalent_surfaces
  coarse_nodes = coarse_mesh.coarse_nodes

  
  
  # ------------------------------------------------------------------------
  for n_id in det_inputs_data: # Loop for the different coarse nodes
    
    print("-"*50)
    print(f"node {n_id}")
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
    prob_uncertainties[n_id] = { 
      "regions": {},
      "surfaces": {}
    }

    fuel_probabilities = {}
    nonFuel_probabilities = {}
    surface_probabilities = {}
    
    for detector_file_data in det_inputs_data[n_id]:
      type_ = detector_file_data['type']
      detectors = detector_file_data['det_relation']
      name_file = detector_file_data['name']
      current_region = detector_file_data['region']
      # print(type_)
      print(name_file)
      print(current_region)
      if type_ == "region_fuel":
        fuel_neutrons, fuel_errors = get_fuel_counts(
          coarse_node_scores[n_id],
          detectors,
          regions,
          surfaces, 
          current_region,
        )
        # print(f'\t Fuel neutrons: {fuel_neutrons}')
        fuel_probabilities, tneff = get_fuel_probabilities(
          fuel_neutrons,
          regions,
          surfaces,
          energy,
          current_region
        )
        fuel_prob_uncertainties = calculate_probabilities_uncertainties(
          fuel_neutrons, fuel_errors, tneff, regions, surfaces, 
          current_region, energy
        )
        prob_uncertainties[n_id]["regions"].update(fuel_prob_uncertainties)
        probabilities[n_id]["regions"].update(fuel_probabilities)
      elif type_ == "region_nonFuel":
        # print(f"Extracting non fuel region detector scores")
        # print(f"node: {n_id}\nfile name: {name_file}")

        nonFuel_neutrons, nonFuel_errors = get_nonFuel_counts(
          coarse_node_scores[n_id],
          detectors,
          regions,
          surfaces,
          current_region
        )
        # print(f"Calculating collision probabilities")
        # print(f"node: {n_id}\nfile name: {name_file}")
        
        nonFuel_probabilities, tne_nf = get_nonFuel_probabilities(
          nonFuel_neutrons,
          regions,
          surfaces,
          energy, 
          current_region
        )

        nonFuel_prob_uncertainties = calculate_probabilities_uncertainties(
          nonFuel_neutrons, nonFuel_errors, tne_nf, regions, surfaces, 
          current_region, energy
        )
        prob_uncertainties[n_id]["regions"].update(nonFuel_prob_uncertainties)
        probabilities[n_id]["regions"].update(nonFuel_probabilities)
        # print(nonFuel_uncertainty)
      elif type_ == "surfaces":
        # print(f"Extracting surfaces detector scores")
        # print(f"node: {n_id}\nfile name: {name_file}")
        surface_neutrons, surface_errors = get_surface_counts(
          coarse_node_scores[n_id],
          detectors,
          energy,
          regions,
          surfaces
        )
        # print(surface_neutrons)
        # print(f"Calculating collision probabilitie")
        # print(f"node: {n_id}\nfile name: {name_file}")
        
        surface_probabilities, tne_s  = get_surface_probabilities(
          surface_neutrons,
          energy,
          regions,
          surfaces
        )
        surfaces_prob_uncertainties = {

        }
        for s in surface_probabilities:
          prob_sigma = calculate_probabilities_uncertainties(
            surface_neutrons, surface_errors, tne_s[s], regions,
            surfaces, s, energy
          )
          surfaces_prob_uncertainties.update(prob_sigma)

        # surface_uncertainties = calculate_surface_uncertainties()

        probabilities[n_id]["surfaces"] = surface_probabilities
        prob_uncertainties[n_id]["surfaces"].update(surfaces_prob_uncertainties)
      else:
        print("Warning in calculate probabilities, type of detector not valid")
        raise SystemError
      





  return probabilities, prob_uncertainties
    


def calculate_probabilities_uncertainties(
  neutrons, errors, tne, regions, surfaces, cr, energy_g
):
  # tne : Total neutrons emitted
  # cr : current region


  # print(errors)

  sigma_probabilities = {
    cr: {
      'regions': {},
      'surfaces': {}
    }
  }

  for r in regions:
    # Loop to calculate the sigma for the P_{f->r}

    sqrt_sum = np.zeros(energy_g)
    # print(cr, r)
    derivate = (neutrons[cr]['regions'][r]) / (tne * tne)
    for rp in regions:
      if rp == r:
        derivate = (tne - neutrons[cr]['regions'][r]) / (tne * tne)
      
      sigma_rp = errors[cr]['regions'][rp]

      sqrt_sum += derivate * derivate * sigma_rp * sigma_rp
    
    for sp in surfaces:
      sigma_sp = errors[cr]['surfaces'][sp]
      sqrt_sum += derivate * derivate * sigma_sp * sigma_sp
    
    sigma_pfr = np.sqrt(sqrt_sum)
    sigma_probabilities[cr]['regions'][r] = sigma_pfr
    # print(r, "---------------------------")
    # print(errors[cr]['regions'][r])
    # print(sigma_pfr)
  for s in surfaces:
    # Loop to calculate the sigma for the P_{f->s}

    sqrt_sum = np.zeros(energy_g)
    derivate = (neutrons[cr]['surfaces'][s]) / (tne * tne)
    for rp in regions:
      sigma_rp = errors[cr]['regions'][rp]
      sqrt_sum += derivate * derivate * sigma_rp * sigma_rp
    for sp in surfaces:
      if sp == s:
        derivate = (tne - neutrons[cr]['surfaces'][s]) / (tne * tne)
      sigma_sp = errors[cr]['surfaces'][sp]
      sqrt_sum += derivate * derivate * sigma_sp * sigma_sp
    
    sigma_pfs = np.sqrt(sqrt_sum)
    sigma_probabilities[cr]['surfaces'][s] = sigma_pfs

    # print(s, "---------------------------")
    # print(errors[cr]['surfaces'][s])
    # print(sigma_pfs)

  return sigma_probabilities

    