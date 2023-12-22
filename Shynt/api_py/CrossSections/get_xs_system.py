from .extractor_xs import get_cross_sections

def  get_xs_data(
  eq_regions, root, xs_inputs, transport_correction=False, 
  scattering_production=False
):
  """ Method to get the XS for all the regions in all nodes

  Parameters
  ----------

  Returns
  -------

  """
  energy_g = root.energy_grid.energy_groups
  coarse_nodes = root.mesh.coarse_mesh.coarse_nodes

  xs = get_cross_sections(
    energy_g, xs_inputs, coarse_nodes, scattering_production
  )

  print("XS retrieved ------------------")
  


  if transport_correction:
    print("Calculating transport correction ...")
    xs = calculate_transport_corrected_xs(xs, energy_g)
  else:
    for cid in xs: xs[cid]["scatter"] = xs[cid]["scatter_p0"]

  # filling probabilities to every similar node
  new_xs = {}
  for reg_eq, main_reg in eq_regions.items():
    # Filling XS
    new_xs[reg_eq] = xs[main_reg]
    
  
  return new_xs



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
    print("region ", cid)
    print("scatt_p0")
    print(xs[cid]["scatter_p0"])
    print("scatt_p1")
    print(xs[cid]["scatter_p1"])
    print("fission")
    print(xs[cid]["fission"])
    # Scattering
    scatt_tr0 = xs[cid]["scatter_p0"]
    scatt_p1 = xs[cid]["scatter_p1"]
    for g in range(energy_g):
      sum_p1 = np.sum(scatt_p1[:][g])
      print(g, sum_p1)
      scatt_tr0[g][g] = scatt_tr0[g][g] - sum_p1
      

    
    # Total
    total_tr0 = xs[cid]["total"]
    absorption = xs[cid]["absorption"],
    # print("absorption_xs", xs[cid]["absorption"])
    # print(absorption)
    for g in range(energy_g):    
      sum_scat = np.sum(scatt_tr0[:][g])
      
      total_tr0[g] = xs[cid]["absorption"][g] + sum_scat
    
    xs_tr_0[cid]["total"] = total_tr0
    xs_tr_0[cid]["scatter"] = scatt_tr0
    print("Scat_tr0")
    print(scatt_tr0)
    print("total_tr0", total_tr0)

  return xs_tr_0