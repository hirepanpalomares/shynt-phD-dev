import numpy as np
from . import compare


def get_moderator_counts(scores, det_relation, energy):
    """
        Method to extract the following rates:
            - mod --> mod
            - mod --> fuel
            - mod --> surface
    """
    moderator_counts = {
        "fuel": np.zeros(energy),
        "coolant": np.zeros(energy),
        "surface": {s: np.zeros(energy) for s in det_relation["surface"].keys()}
    }
    # scores:
    # 'total_rate_fuel_g0': {'neutrons': [(1.75715, 0.00086)], 'energy': [(0.0, 6.25e-07)]} 
    
    for g in range(energy):
        for gp in range(energy):
            det_name_fuel = det_relation["fuel"][g][gp].name
            det_name_coolant = det_relation["coolant"][g][gp].name
            

            switching_index = energy - 1 - gp # To get array fast ---> thermal
            
            moderator_counts["fuel"][switching_index] += abs(scores[det_name_fuel]["neutrons"][0][0])
            #print(gp, det_name_fuel, abs(scores[det_name_fuel]["neutrons"][0][0]))
            moderator_counts["coolant"][switching_index] += abs(scores[det_name_coolant]["neutrons"][0][0])
            for s in det_relation["surface"].keys():
                det_name_surface = det_relation["surface"][s][g][gp].name
                moderator_counts["surface"][s][switching_index] += abs(scores[det_name_surface]["neutrons"][0][0])


    # for g in range(energy):
    #     det_name_total = det_relation["total"][g].name
    #     moderator_counts["coolant"][g] = abs(scores[det_name_total]["neutrons"][0][0])
    #     moderator_counts["fuel"][g] -= moderator_counts
    #     for gp in range(energy):
    #         det_name_coolant = det_relation["coolant"][g][gp].name
            
    

    
    return moderator_counts

def get_fuel_counts(scores, det_relation, energy):
    """
        Method to extract the following rates:
            - fuel --> fuel
            - fuel --> coolant
            - fuel --> surface
    """
    
    fuel_counts = {
        "fuel": np.zeros(energy),
        "coolant": np.zeros(energy),
        "surface": {s: np.zeros(energy) for s in det_relation["surface"].keys()}
    }
    # scores:
    # 'total_rate_fuel_g0': {'neutrons': [(1.75715, 0.00086)], 'energy': [(0.0, 6.25e-07)]} 

    for g in range(energy):
        det_name_total = det_relation["total"][g].name
        det_name_surf_coolant_incoming = det_relation["surface&coolant"][g].name
        det_name_coolant = det_relation["coolant"][g].name

        switching_index = energy - 1 - g # To get array fast ---> thermal
        fuel_counts["coolant"][switching_index] = abs(scores[det_name_coolant]["neutrons"][0][0])
        for s in det_relation["surface"].keys():
            det_name_surface = det_relation["surface"][s][g].name
            fuel_counts["surface"][s][switching_index] = abs(scores[det_name_surface]["neutrons"][0][0])
        
        fuel_counts["fuel"][switching_index] = abs(scores[det_name_total]["neutrons"][0][0]) - abs(scores[det_name_surf_coolant_incoming]["neutrons"][0][0])
    return fuel_counts

def get_surface_counts(scores, det_relation, energy):
    """
        Method to extract the following rates:
            - surface --> fuel
            - surface --> coolant
            - surface --> surface

    """

    # Preparing surface_counts
    surface_counts = {    }
    for s in det_relation.keys():
        surface_counts[s] = {
            "fuel": np.zeros(energy),
            "coolant": np.zeros(energy),
            "surface": {  }
        }
        for sp in det_relation.keys():
            surface_counts[s]["surface"][sp] = np.zeros(energy)
    

    for g in range(energy):
        for s in det_relation.keys():
            det_name_fuel = det_relation[s]["fuel"][g].name
            # print(det_name_fuel)
            det_name_coolant = det_relation[s]["coolant"][g].name

            switching_index = energy - 1 - g  # To get array fast ---> thermal
            surface_counts[s]["fuel"][switching_index] = abs(scores[det_name_fuel]["neutrons"][0][0])
            surface_counts[s]["coolant"][switching_index] = abs(scores[det_name_coolant]["neutrons"][0][0])

            for sp in det_relation.keys():
                det_name_surface = det_relation[s][sp][g].name
                surface_counts[s]["surface"][sp][switching_index] = abs(scores[det_name_surface]["neutrons"][0][0])

                
    return surface_counts


def get_fuel_probabilities(fuel_neutrons, detector_relation):
    emmited_from_fuel = fuel_neutrons["fuel"] + fuel_neutrons["coolant"]
    
    for s in detector_relation["surfaces"]["surfaces"].keys():
        emmited_from_fuel += fuel_neutrons["surface"][s]
    
    p_fuel = {
        "fuel": None,
        "coolant": None,
        "surfaces": {
            3: None,
            4: None,
            5: None,
            6: None
        }
    }
    p_fuel["fuel"] = fuel_neutrons["fuel"]/emmited_from_fuel
    p_fuel["coolant"] = fuel_neutrons["coolant"]/emmited_from_fuel
    for s in detector_relation["surfaces"]["surfaces"].keys():
        p_fuel["surfaces"][s] = fuel_neutrons["surface"][s]/emmited_from_fuel
    
    diff_fuel = compare.compare_fuel(p_fuel)
    # print("Probabilities from the fuel to: \n")
    # print(p_fuel)
    # print()
    # print("Percentage difference: ")
    # print(diff_fuel)
    # surfaces = [3, 4, 5, 6]
    # for g in range(energy_groups):
    #     a = [p_fuel["fuel"][g], p_fuel["coolant"][g]]
    #     for sp in surfaces:
    #         a.append(p_fuel[sp][g])
        # print(a)
        # print()
    print("-"*100)
    return p_fuel

def get_coolant_probabilities(coolant_neutrons, detector_relation):
    emmited_from_coolant = coolant_neutrons["fuel"] + coolant_neutrons["coolant"]
    for s in detector_relation["surfaces"]["surfaces"].keys():
        emmited_from_coolant += coolant_neutrons["surface"][s]
    
    
    
    p_coolant = {
        "fuel": None,
        "coolant": None,
        "surfaces": {
            3: None,
            4: None,
            5: None,
            6: None
        }
    }

    p_coolant["fuel"] = coolant_neutrons["fuel"]/emmited_from_coolant
    p_coolant["coolant"] = coolant_neutrons["coolant"]/emmited_from_coolant
    for s in detector_relation["surfaces"]["surfaces"].keys():
        p_coolant["surfaces"][s] = coolant_neutrons["surface"][s]/emmited_from_coolant
    
    diff_coolant = compare.compare_coolant(p_coolant)
    # print("Probabilities from the coolant to: \n")
    # print(p_coolant)
    # print()
    # print("Percentage difference: ")
    # print(diff_coolant)
    return p_coolant

def get_surface_probabilities(surface_neutrons, detector_relation, energy_groups):
    emmited_from_surfaces = {
        s: np.zeros(energy_groups) for s in detector_relation["surfaces"].keys()
    }
    for s in detector_relation["surfaces"]["surfaces"].keys():
        # print(s)
        emmited_from_surfaces[s] = surface_neutrons[s]["fuel"] + surface_neutrons[s]["coolant"]
        for sp in detector_relation["surfaces"]["surfaces"].keys():
            emmited_from_surfaces[s] += surface_neutrons[s]["surface"][sp]
    # print(emmited_from_surfaces)
    
    
    
    p_surfaces = {
        s: {
            "fuel": None,
            "coolant": None,
            "surfaces": {}
        } for s in detector_relation["surfaces"]["surfaces"].keys() 
    }
    # print(p_surfaces)
    for s in detector_relation["surfaces"]["surfaces"].keys():
        p_surfaces[s]["fuel"] = surface_neutrons[s]["fuel"]/emmited_from_surfaces[s]
        p_surfaces[s]["coolant"] = surface_neutrons[s]["coolant"]/emmited_from_surfaces[s]
        for sp in detector_relation["surfaces"]["surfaces"].keys():
            p_surfaces[s]["surfaces"][sp] = surface_neutrons[s]["surface"][sp]/emmited_from_surfaces[s]
    
    
    diff_surfaces = compare.compare_surfaces(p_surfaces)
    # print("Probabilities from the surfaces to: \n")
    # print(p_surfaces)
    # print()
    # print("Percentage difference: ")
    # print(diff_surfaces)

    return p_surfaces


def calculate_probabilities(coarse_node_scores, detector_relation, energy_groups, id_):
    """
        # TODO: The number of detectors can be reduced (see bellow)

        The probability for a neutron to enter the cell through a given surface
        and go out through the same surface without interacting is CERO

        ------------------------------------------------------------------------
        
        detector_relation.keys() - Relation of detectors by type of counters
        coarse_node_scores.keys() - scores of the detectors by name
    """
    
    
    # ----------------------------------------------------------------------------------------------------

   
    # The energy structure of these scores are ordered from thermal --> fast  ----------------------------
    fuel_neutrons = get_fuel_counts(coarse_node_scores["fuel1"], detector_relation["fuel1"]["fuel"], energy_groups)
    coolant_neutrons = get_moderator_counts(coarse_node_scores["coolant"], detector_relation["coolant"]["coolant"], energy_groups)
    surface_neutrons = get_surface_counts(coarse_node_scores["surfaces"], detector_relation["surfaces"]["surfaces"], energy_groups)

    # print(fuel_neutrons)
    # print(coolant_neutrons)
    # print(surface_neutrons)
    # ----------------------------------------------------------------------------------------------------


    fuel_probabilities = get_fuel_probabilities(fuel_neutrons, detector_relation)
    coolant_probabilities = get_coolant_probabilities(coolant_neutrons, detector_relation)
    surface_probabilities = get_surface_probabilities(surface_neutrons, detector_relation, energy_groups)
    
    return {
        "fuel": fuel_probabilities,
        "coolant": coolant_probabilities,
        "surface": surface_probabilities
    }
        

