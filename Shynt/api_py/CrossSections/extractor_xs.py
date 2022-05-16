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
        for node in fine_nodes[id_coarse].values():
            cell = node.cell
            universe = res.getUniv(cell.gcuName, burnup=0)

            xs_total = universe["infTot"]
            xs_nuFiss = universe["infNsf"]
            xs_chi = universe["infChit"]
            scatter_data = universe["infS0"]
            xs_scatterMatrix = scatter_data.reshape((energy_g, energy_g))
            xs[id_coarse][cell.id] = {
                "total": xs_total,
                "nuSigFission": xs_nuFiss,
                "chi": xs_chi,
                "scatter": xs_scatterMatrix
            }   
    
    
    debugging_breakingPoint = True
    
    # return get_HY_xs()
    return xs