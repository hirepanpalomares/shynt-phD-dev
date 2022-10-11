import numpy as np
import matplotlib as mpl


def normalize_serpent_flux(flux, energy_g):
    """
        Normalizes serpent flux extracted from detectors files

        flux[-1] is the fastest group

    """
    fast_flux = flux[energy_g-1]
    normalize_factor = np.max(fast_flux)

    normalized_flux = np.zeros(flux.shape)
    for g in range(energy_g):
        normalized_flux[g] = flux[g] / normalize_factor  
    
    return normalized_flux


def normalize_hybrid_flux(flux, energy_g):
    """
        Normalizes flux obtained from the Response Matrix Method

    """
    # thermal_flux = flux[1]
    # fast_flux = flux[0]
    # normalized_flux = {
    #     0: {}, # thermal
    #     1: {}  # fast
    # }
    

    # for r_id, flux_value in thermal_flux.items():
    #     normalized_flux[0][r_id] = flux_value / normalization_factor
        
    # for r_id, flux_value in fast_flux.items():
    #     normalized_flux[1][r_id] = flux_value / normalization_factor

    fast_flux = flux[0]
    normalization_factor = np.max(np.array(list(fast_flux.values())))
    
    normalized_flux = { }
    for g in range(energy_g):
        normalized_flux[g] = {}

        flux_g = flux[g]
        for r_id, flux_value in flux_g.items():
            normalized_flux[g][r_id] = flux_value / normalization_factor
    


    return normalized_flux


def normalized_flux_colors_by_group(flux, energy_g, color_map="jet", max_norm=None, min_norm=None):

    max_ = {}
    min_ = {}
    for g in range(energy_g):
        max_fval = 0
        min_fval = 1E+06
        for c_id, fval in flux[g].items():
            if fval > max_fval:
                max_fval = fval
            if fval < min_fval:
                min_fval = fval
        max_[g] = max_fval
        min_[g] = min_fval 

    cell_colors = {}
    cmap = mpl.cm.get_cmap(color_map)
    normalize = {}
    for g in range(energy_g):
        if max_norm and min_norm:
            norm = mpl.colors.Normalize(vmin=min_norm, vmax=max_norm)
        else:
            norm = mpl.colors.Normalize(vmin=min_[g], vmax=max_[g])
        cell_colors[g] = {}
        normalize[g] = norm
        for c_id, fval in flux[g].items():
            rgb_1 = cmap(norm(fval))[:-1]
            rgb_256 = []
            for r in rgb_1:
                rgb_256.append(int(r*255))
            
            cell_colors[g][c_id] = tuple(rgb_256)
            

    return cell_colors, normalize, cmap


def normalized_flux_colors_by_whole(flux, energy_g, color_map="jet"):

    
    max_fval = 0
    min_fval = 1E+06
    for g in range(energy_g):
        for c_id, fval in flux[g].items():
            if fval > max_fval:
                max_fval = fval
            if fval < min_fval:
                min_fval = fval
        
    print(min_fval, max_fval)
    cell_colors = {}
    cmap = mpl.cm.get_cmap(color_map)
    norm = mpl.colors.Normalize(vmin=min_fval, vmax=max_fval)
    for g in range(energy_g):
        cell_colors[g] = {}
        for c_id, fval in flux[g].items():
            rgb_1 = cmap(norm(fval))[:-1]
            rgb_256 = []
            for r in rgb_1:
                rgb_256.append(int(r*255))
            
            cell_colors[g][c_id] = tuple(rgb_256)
            

    return cell_colors, norm, cmap




