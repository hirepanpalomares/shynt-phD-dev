import serpentTools
from serpentTools.settings import rc
rc['serpentVersion'] = '2.1.32'




def get_cross_sections(energy_g, xs_inputs, fine_nodes):
    """
        Extract XS data  
        An open source library is used
        see (https://github.com/drewejohnson/serpent-tools)

        The XS are ordered from FAST ---> THERMAL
    """
    xs = {}
    
    for id_coarse, xs_inp in xs_inputs.items():
      resFile = xs_inp.name + "_res.m"
      res = serpentTools.read(resFile)
      xs[id_coarse] = {}
      for f_node in fine_nodes[id_coarse].values():
        cell = f_node.cell
        if cell.content.name == "void":
          continue
        gcu_name = xs_inp.xs_gcu[cell.id]
        universe = res.getUniv(gcu_name, burnup=0)

        xs_total = universe["infTot"]
        xs_nuFiss = universe["infNsf"]
        xs_fiss = universe["infFiss"]
        xs_gamma = universe["infCapt"]
        xs_chi = universe["infChit"]
        scatter_data = universe["infS0"]
        xs_scatterMatrix = scatter_data.reshape((energy_g, energy_g))
        xs[id_coarse][cell.id] = {
          "total": xs_total,
          "capture": xs_gamma,
          "nuSigFission": xs_nuFiss,
          "fission": xs_fiss,
          "chi": xs_chi,
          "scatter": xs_scatterMatrix.T

        }   
    
    
    debugging_breakingPoint = True
    
    # return get_HY_xs()
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