import numpy as np


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
    fast_flux = flux[0]
    thermal_flux = flux[1]

    normalization_factor = np.max(np.array(list(fast_flux.values())))

    normalized_flux = {
        0: {}, 1: {}
    }

    for r_id, flux_value in thermal_flux.items():
        normalized_flux[0][r_id] = flux_value / normalization_factor
    for r_id, flux_value in fast_flux.items():
        normalized_flux[1][r_id] = flux_value / normalization_factor

    return normalized_flux