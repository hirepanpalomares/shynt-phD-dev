import numpy as np

from Shynt.api_py.materials import Material


def calculate_fuel_probabilities_uncertainty(
  p_fuel, fuel_errors, regions, surfaces, energy, fuel_regions, tneff
):
  p_fuel_uncertainty = {
    fr : {
      "regions": { },
      "surfaces": { }
    } for fr in fuel_regions
  }
  # Calculation of uncertainty
  for fr in fuel_regions:
    for r in regions:
      prob_ = p_fuel[fr]["regions"][r]
      sqrt_sum = np.zeros(energy)
      for rs in regions:
        if rs == r:
          sqrt_sum += np.power((np.ones(energy) - prob_), 2) * np.power(fuel_errors[fr]["regions"][rs], 2)
        else:
          sqrt_sum += np.power(prob_, 2) * np.power(fuel_errors[fr]["regions"][rs], 2)
      for s in surfaces:
        sqrt_sum += np.power(prob_, 2) * np.power(fuel_errors[fr]["surfaces"][s], 2)
      uncertainty = np.sqrt(sqrt_sum)/tneff
      p_fuel_uncertainty[fr]["regions"][r] = uncertainty
  for s in surfaces:
    prob_ = p_fuel[fr]["surfaces"][s]
    sqrt_sum = np.zeros(energy)
    for rs in regions:
      sqrt_sum += np.power(prob_, 2) * np.power(fuel_errors[fr]["regions"][rs], 2)
    for sp in surfaces:
      if sp == s:
        sqrt_sum += np.power((np.ones(energy) - prob_), 2) * np.power(fuel_errors[fr]["surfaces"][sp], 2)
      else:
        sqrt_sum += np.power(prob_, 2) * np.power(fuel_errors[fr]["surfaces"][sp], 2)
    uncertainty = np.sqrt(sqrt_sum)/tneff
    p_fuel_uncertainty[fr]["surfaces"][s] = uncertainty
  pass


def calculate_nonFuel_uncertainties(
  nonFuel_neutrons, nonFuel_errors, regions, surfaces, energy, nonFuel_regions,
  p_nonFuel
):

  p_nonFuel_uncertainty = {
      r: {
          "regions": {
              rp: None for rp in regions
          },
          "surfaces": {
              s: None for s in surfaces
          }
      } for r in nonFuel_regions
  }

  for nfr in nonFuel_regions:
      total_emmited_from_nonFuel = np.zeros(energy)
      for rp in regions:
          total_emmited_from_nonFuel += nonFuel_neutrons[nfr]["regions"][rp]
      for s in surfaces:
          total_emmited_from_nonFuel += nonFuel_neutrons[nfr]["surfaces"][s]

      # Calculation of uncertainty
      for r in regions:
          prob_ = p_nonFuel[nfr]["regions"][r]
          sqrt_sum = np.zeros(energy)
          for rs in regions:
              if rs == r:
                  sqrt_sum += np.power((np.ones(energy) - prob_), 2) * np.power(nonFuel_errors[nfr]["regions"][rs], 2)
              else:
                  sqrt_sum += np.power(prob_, 2) * np.power(nonFuel_errors[nfr]["regions"][rs], 2)
          for s in surfaces:
              sqrt_sum += np.power(prob_, 2) * np.power(nonFuel_errors[nfr]["surfaces"][s], 2)
          uncertainty = np.sqrt(sqrt_sum)/total_emmited_from_nonFuel
          p_nonFuel_uncertainty[nfr]["regions"][r] = uncertainty
      for s in surfaces:
          prob_ = p_nonFuel[nfr]["surfaces"][s]
          sqrt_sum = np.zeros(energy)
          for rs in regions:
              sqrt_sum += np.power(prob_, 2) * np.power(nonFuel_errors[nfr]["regions"][rs], 2)
          for sp in surfaces:
              if sp == s:
                  sqrt_sum += np.power((np.ones(energy) - prob_), 2) * np.power(nonFuel_errors[nfr]["surfaces"][sp], 2)
              else:
                  sqrt_sum += np.power(prob_, 2) * np.power(nonFuel_errors[nfr]["surfaces"][sp], 2)
          uncertainty = np.sqrt(sqrt_sum)/total_emmited_from_nonFuel
          p_nonFuel_uncertainty[nfr]["surfaces"][s] = uncertainty
  
  return p_nonFuel, p_nonFuel_uncertainty


def calculate_surface_uncertainties(
  surface_neutrons, surface_errors, energy, regions, surfaces,
  p_surfaces, total_emmited_from_surfaces
):

  p_surfaces_uncertainty = {
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
      total_emmited_from_surfaces[s] += surface_neutrons[s]["regions"][r]
    for sp in surfaces:
      total_emmited_from_surfaces[s] += surface_neutrons[s]["surfaces"][sp]
  for s in surfaces:
  
    # Calculation of uncertainty
    for r in regions:
      # Loop for the uncertainties from surface to region
      prob_ = p_surfaces[s]["regions"][r]
      sqrt_sum = np.zeros(energy)
      for r_sigma in regions:
        if r_sigma == r:
          sqrt_sum += np.power((np.ones(energy) - prob_), 2) * np.power(surface_errors[s]["regions"][r_sigma], 2)
        else:
          sqrt_sum += np.power(prob_, 2) * np.power(surface_errors[s]["regions"][r_sigma], 2)
      for s_sigma in surfaces:
        sqrt_sum += np.power(prob_, 2) * np.power(surface_errors[s]["surfaces"][s_sigma], 2)
      uncertainty = np.sqrt(sqrt_sum)/total_emmited_from_surfaces[s]
      p_surfaces_uncertainty[s]["regions"][r] = uncertainty
    for sp in surfaces:
      # Loop for the uncertainties from surface to surface
      prob_ = p_surfaces[s]["surfaces"][sp]
      sqrt_sum = np.zeros(energy)
      for r_sigma in regions:
        sqrt_sum += np.power(prob_, 2) * np.power(surface_errors[s]["regions"][r_sigma], 2)
      for sp_s in surfaces:
        if sp_s == sp:
          sqrt_sum += np.power((np.ones(energy) - prob_), 2) * np.power(surface_errors[s]["surfaces"][sp_s], 2)
        else:
          sqrt_sum += np.power(prob_, 2) * np.power(surface_errors[s]["surfaces"][sp_s], 2)
      uncertainty = np.sqrt(sqrt_sum)/total_emmited_from_surfaces[s]
      p_surfaces_uncertainty[s]["surfaces"][sp] = uncertainty

  return p_surfaces, p_surfaces_uncertainty

