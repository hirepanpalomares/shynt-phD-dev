import serpentTools
from serpentTools.settings import rc
rc['serpentVersion'] = '2.1.32'




def get_cross_sections(
  energy_g, xs_inputs, coarse_nodes, scattering_production
  ):
  """
    Extract XS data  
    An open source library is used
    see (https://github.com/drewejohnson/serpent-tools)

    The XS are ordered from FAST ---> THERMAL
  """
  from numpy import flip

  varSet = rc.expandVariables()
  print(sorted(varSet))
  print(rc['xs.getInfXS'])
  xs = {}
  
  for id_coarse, xs_inp in xs_inputs.items():
    resFile = xs_inp.name + "_res.m"
    res = serpentTools.read(resFile)
    
    node_regions = coarse_nodes[id_coarse].fine_mesh.regions
    
    
    for reg_id, region in node_regions.items():
      cell = region
      if cell.content.name == "void":
        continue
      gcu_name = xs_inp.xs_gcu[reg_id]
      universe = res.getUniv(gcu_name, burnup=0)

      xs_total = universe["infTot"]
      xs_nuFiss = universe["infNsf"]
      xs_fiss = universe["infFiss"]
      xs_gamma = universe["infCapt"]
      xs_abs = universe["infAbs"]
      xs_chi = universe["infChit"]
      # print(xs_total)
      # print(xs_nuFiss)
      if scattering_production: 
        scatter_data_p0 = universe["infSp0"]
        scatter_data_p1 = universe["infSp1"]
      else:
        scatter_data_p0 = universe["infS0"]
        scatter_data_p1 = universe["infS1"]

      xs_scatterMatrix_p0 = scatter_data_p0.reshape((energy_g, energy_g))
      xs_scatterMatrix_p1 = scatter_data_p1.reshape((energy_g, energy_g))

      xs[cell.id] = {
        "total": xs_total,
        "capture": xs_gamma,
        "nuSigFission": xs_nuFiss,
        "fission": xs_fiss,
        "absorption": xs_abs,
        "chi": xs_chi,
        "scatter_p0": xs_scatterMatrix_p0.T,
        "scatter_p1": xs_scatterMatrix_p1.T
      }   
  
  return xs


def get_cross_sections_new(
  energy_g, xs_inputs, regions_ids, gcu_names, map_reg, coarse_nodes_regions,
  eq_nodes
):
  """Function to read XS only for the big hex assembly, according with all
  the hard-coded data
  """
  
  xs = {}
  
  for nid, xs_inp in xs_inputs.items():
    resFile = xs_inp + "_res.m"
    res = serpentTools.read(resFile)
    for region in regions_ids[nid]:
      material, rid = region
      mapped_reg = map_reg[nid][rid]
      
      gcu_name = gcu_names[nid][mapped_reg]
      universe = res.getUniv(gcu_name, burnup=0)

      xs_total = universe["infTot"]
      xs_nuFiss = universe["infNsf"]
      xs_fiss = universe["infFiss"]
      xs_gamma = universe["infCapt"]
      xs_chi = universe["infChit"]
      scatter_data = universe["infS0"]
      xs_scatterMatrix = scatter_data.reshape((energy_g, energy_g))
      xs[rid] = {
        "total": xs_total,
        "capture": xs_gamma,
        "nuSigFission": xs_nuFiss,
        "fission": xs_fiss,
        "chi": xs_chi,
        "scatter": xs_scatterMatrix.T

      }   
  
  # Fill the cross sections in the other nodes
  for nid, same_nodes in eq_nodes.items():
    for neq in same_nodes:
      
      for mat, region in regions_ids[nid]:
        node, reg = region.split("_")
        xs[f"{neq}_{reg}"] = xs[region].copy()
      
  return xs