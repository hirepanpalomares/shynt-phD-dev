import numpy as np

from Shynt.api_py.materials import Material

from . import compare


def get_moderator_counts(scores, det_relation, energy, regions, surfaces, fuel_region, coolant_region):
    """
        Method to extract the following rates:
            - mod --> regions
            - mod --> surface
    """
    moderator_counts = {
        "regions": {
            r: np.zeros(energy) for r in regions
        },
        "surfaces": {
            s: np.zeros(energy) for s in surfaces
        }
    }
    
    detectors = det_relation["regions"][coolant_region]

    for g in range(energy):
        for gp in range(energy):
            det_name_fuel = detectors["regions"][fuel_region][g][gp].name
            det_name_coolant = detectors["regions"][coolant_region][g][gp].name
            switching_index = energy - 1 - gp # To get array fast ---> thermal
            
            moderator_counts["regions"][fuel_region][switching_index] += abs(scores[det_name_fuel]["neutrons"][0][0])
            moderator_counts["regions"][coolant_region][switching_index] += abs(scores[det_name_coolant]["neutrons"][0][0])
            for s in surfaces:
                det_name_surface = detectors["surfaces"][s][g][gp].name
                moderator_counts["surfaces"][s][switching_index] += abs(scores[det_name_surface]["neutrons"][0][0])

    return moderator_counts

def get_fuel_counts(scores, det_relation, energy, regions, surfaces, fuel_region, coolant_region):
    """
        Method to extract the following rates:
            - fuel --> regions
            - fuel --> surfaces
    """  
    region_fuel_counts = {
        "regions": {
            r: np.zeros(energy) for r in regions
        },
        "surfaces": {
            s: np.zeros(energy) for s in surfaces
        }
    }
    
    detectors = det_relation["regions"][fuel_region]
    for g in range(energy):
        det_name_total = detectors["total"][g].name
        det_name_surf_coolant_incoming = detectors["surface&coolant"][g].name
        det_name_coolant = detectors["regions"][coolant_region][g].name

        switching_index = energy - 1 - g # To get array fast ---> thermal
        
        region_fuel_counts["regions"][coolant_region][switching_index] = abs(scores[det_name_coolant]["neutrons"][0][0])
        region_fuel_counts["regions"][fuel_region][switching_index] = abs(scores[det_name_total]["neutrons"][0][0])\
            - abs(scores[det_name_surf_coolant_incoming]["neutrons"][0][0])

        for s in surfaces:
            det_name_surface = detectors["surfaces"][s][g].name
            region_fuel_counts["surfaces"][s][switching_index] = abs(scores[det_name_surface]["neutrons"][0][0])
        
    return region_fuel_counts

def get_surface_counts(scores, det_relation, energy, regions, surfaces, fuel_region, coolant_region):
    """
        Method to extract the following rates:
            - surface --> regions
            - surface --> surface

    """

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

   

    for g in range(energy):
        for s in det_relation.keys():
            det_name_fuel = det_relation[s]["regions"][fuel_region][g].name
            det_name_coolant = det_relation[s]["regions"][coolant_region][g].name
            switching_index = energy - 1 - g  # To get array fast ---> thermal
            surface_counts[s]["regions"][fuel_region][switching_index] = abs(scores[det_name_fuel]["neutrons"][0][0])
            surface_counts[s]["regions"][coolant_region][switching_index] = abs(scores[det_name_coolant]["neutrons"][0][0])
            for sp in surfaces:
                det_name_surface = det_relation[s]["surfaces"][sp][g].name
                surface_counts[s]["surfaces"][sp][switching_index] = abs(scores[det_name_surface]["neutrons"][0][0])
    return surface_counts


def get_fuel_probabilities(fuel_neutrons, detector_relation, regions, surfaces, fuel_region, coolant_region):
    
    total_neutrons_emmited_from_fuel = fuel_neutrons["regions"][fuel_region] + fuel_neutrons["regions"][coolant_region]
    
    for s in surfaces:
        total_neutrons_emmited_from_fuel += fuel_neutrons["surfaces"][s]
    
    p_fuel = {
        "regions": {
            fuel_region: None,
            coolant_region: None
        },
        "surfaces": {
            s: None for s in surfaces
        }
    }

    p_fuel["regions"][fuel_region] = fuel_neutrons["regions"][fuel_region] / total_neutrons_emmited_from_fuel
    p_fuel["regions"][coolant_region] = fuel_neutrons["regions"][coolant_region]/total_neutrons_emmited_from_fuel

    for s in surfaces:
        p_fuel["surfaces"][s] = fuel_neutrons["surfaces"][s]/total_neutrons_emmited_from_fuel

    return p_fuel

def get_coolant_probabilities(coolant_neutrons, detector_relation, regions, surfaces, fuel_region, coolant_region):
   
    emmited_from_coolant = coolant_neutrons["regions"][fuel_region] + coolant_neutrons["regions"][coolant_region]
    for s in surfaces:
        emmited_from_coolant += coolant_neutrons["surfaces"][s]
    
    p_coolant = {
        "regions": {
            fuel_region: None,
            coolant_region: None
        },
        "surfaces": {
            s: None for s in surfaces
        }
    }

    p_coolant["regions"][fuel_region] = coolant_neutrons["regions"][fuel_region]/emmited_from_coolant
    p_coolant["regions"][coolant_region] = coolant_neutrons["regions"][coolant_region]/emmited_from_coolant
    for s in surfaces:
        p_coolant["surfaces"][s] = coolant_neutrons["surfaces"][s]/emmited_from_coolant
    
    return p_coolant

def get_surface_probabilities(surface_neutrons, detector_relation, energy_groups, regions, surfaces, fuel_region, coolant_region):
    emmited_from_surfaces = {
        s: np.zeros(energy_groups) for s in surfaces
    }

    for s in surfaces:
        # print(s)
        emmited_from_surfaces[s] = surface_neutrons[s]["regions"][fuel_region] + surface_neutrons[s]["regions"][coolant_region]
        for sp in surfaces:
            emmited_from_surfaces[s] += surface_neutrons[s]["surfaces"][sp]
    # print(emmited_from_surfaces)
    
    p_surfaces = {
        s: {
            "regions": {
                fuel_region: None,
                coolant_region: None
            },
            "surfaces": {
                sp: None for sp in surfaces
            }
        } for s in surfaces 
    }


    for s in surfaces:
        p_surfaces[s]["regions"][fuel_region] = surface_neutrons[s]["regions"][fuel_region]/emmited_from_surfaces[s]
        p_surfaces[s]["regions"][coolant_region] = surface_neutrons[s]["regions"][coolant_region]/emmited_from_surfaces[s]
        for sp in surfaces:
            p_surfaces[s]["surfaces"][sp] = surface_neutrons[s]["surfaces"][sp]/emmited_from_surfaces[s]
    
    return p_surfaces


def calculate_probabilities(coarse_node_scores, detector_relation, energy_groups, id_, mesh_info, coarse_nodes, fine_nodes):
    """
        # TODO: The number of detectors can be reduced (see bellow)

        The probability for a neutron to enter the cell through a given surface
        and go out through the same surface without interacting is CERO
        
        The energy structure of scores are ordered from thermal --> fast  

        ------------------------------------------------------------------------
        
        detector_relation.keys() - Relation of detectors by type of counters
        coarse_node_scores.keys() - scores of the detectors by name
    """
    
    

    # ----------------------------------------------------------------------------------------------------
    regions = mesh_info.coarse_region_rel[id_]
    surfaces = mesh_info.coarse_surface_rel[id_]

    fuel_region, coolant_region = helper_fuel_coolant_region(fine_nodes[id_])

    for type_ in detector_relation.keys():
        # print(type_)
        if type_ == "region_fuel":
            fuel_neutrons = get_fuel_counts(
                coarse_node_scores["region_fuel"], 
                detector_relation["region_fuel"], 
                energy_groups,
                regions, surfaces, fuel_region, coolant_region
            )
            fuel_probabilities = get_fuel_probabilities(
                fuel_neutrons, 
                detector_relation["region_fuel"],
                regions, surfaces, fuel_region, coolant_region
            )
        elif type_ == "region_coolant":
            coolant_neutrons = get_moderator_counts(
                coarse_node_scores["region_coolant"], 
                detector_relation["region_coolant"], 
                energy_groups, regions, surfaces, fuel_region, coolant_region
            )
            coolant_probabilities = get_coolant_probabilities(
                coolant_neutrons, 
                detector_relation["region_coolant"],
                regions, surfaces, fuel_region, coolant_region
            )
        elif type_ == "surfaces":
            surface_neutrons = get_surface_counts(
                coarse_node_scores["surfaces"], 
                detector_relation["surfaces"]["surfaces"], 
                energy_groups, regions, surfaces, fuel_region, coolant_region
            )
            surface_probabilities = get_surface_probabilities(
                surface_neutrons, 
                detector_relation, 
                energy_groups, regions, surfaces, fuel_region, coolant_region
            )
        else:
            print("Warning in calculate probabilities, type of detector not valid")
            raise SystemError


    # ----------------------------------------------------------------------------------------------------

    
    probabilities = {
        "regions": {
            fuel_region: fuel_probabilities,
            coolant_region: coolant_probabilities
        },
        "surfaces": surface_probabilities

    }
    return probabilities
        

def helper_fuel_coolant_region(fine_nodes):

    fuel_cell_id = None
    coolant_cell_id = None

    for reg in fine_nodes.values():
        cell = reg.cell
        if isinstance(cell.content, Material):
            if cell.content.isFuel:
                fuel_cell_id = cell.id
            else:
                coolant_cell_id = cell.id

    return fuel_cell_id, coolant_cell_id