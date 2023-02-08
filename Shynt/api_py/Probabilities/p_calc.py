import numpy as np

from Shynt.api_py.materials import Material


def get_nonFuel_counts(scores, det_relation, energy, regions, surfaces, fuel_region):
    """
        Method to extract the following rates:
            - mod --> regions
            - mod --> surface
    """
    nonFuel_counts = {
        r: {
            "regions": {
                r: np.zeros(energy) for r in regions
            },
            "surfaces": {
                s: np.zeros(energy) for s in surfaces
            }
        } for r in regions if r != fuel_region
    }
    

    for r in regions:
        if r != fuel_region:
            detectors = det_relation["regions"][r]
            for g in range(energy):
                for gp in range(energy):
                    if g < gp:
                        continue # To avoid upscaterring detectors
                    energy_index = energy - 1 - gp # To get array fast ---> thermal

                    for rp in regions: # rp is the region where the neutron intercts for the second time
                        det_name_rp = detectors["regions"][rp][g][gp].name
                        nonFuel_counts[r]["regions"][rp][energy_index] += abs(scores[det_name_rp].tallies)
                    
                    for s in surfaces:
                        det_name_surface = detectors["surfaces"][s][g][gp].name
                        nonFuel_counts[r]["surfaces"][s][energy_index] += abs(scores[det_name_surface].tallies)

    return nonFuel_counts

def get_fuel_counts(scores, det_relation, energy, regions, surfaces, fuel_region):
    """
        Method to extract the following rates:
            - fuel --> regions
            - fuel --> surfaces
        
        This methods counts the neutrons of every possible interaction fuel -> clad, fuel -> coolant, etc
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
        energy_index = energy - 1 - g # To get array fast ---> thermal
        # Total reaction rate in the fuel
        det_name_total = detectors["total"][g].name

        # All neutrons entering the fuel through surface
        det_name_all_incoming = detectors["all_to_fuelReg"][g].name

        # Neutrons that interact in the fuel and then in other regions
        for r in regions:
            if r != fuel_region:
                det_name_region = detectors["regions"][r][g].name
                region_fuel_counts["regions"][r][energy_index] = abs(scores[det_name_region].tallies)

        # Neutrons  fuel to fuel        
        region_fuel_counts["regions"][fuel_region][energy_index] = abs(scores[det_name_total].tallies)\
            - abs(scores[det_name_all_incoming].tallies)

        # Neutrons fuel to surfaces
        for s in surfaces:
            det_name_surface = detectors["surfaces"][s][g].name
            region_fuel_counts["surfaces"][s][energy_index] = abs(scores[det_name_surface].tallies)
        
    return region_fuel_counts

def get_surface_counts(scores, det_relation, energy, regions, surfaces):
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
            for r in regions:
                energy_index = energy - 1 - g  # To get array fast ---> thermal
                det_name_region = det_relation[s]["regions"][r][g].name
                surface_counts[s]["regions"][r][energy_index] = abs(scores[det_name_region].tallies)
                for sp in surfaces:
                    det_name_surface = det_relation[s]["surfaces"][sp][g].name
                    surface_counts[s]["surfaces"][sp][energy_index] = abs(scores[det_name_surface].tallies)
    return surface_counts

def get_fuel_probabilities(fuel_neutrons, regions, surfaces, energy, fuel_regions):
    

    p_fuel = {
        fr : {
            "regions": { },
            "surfaces": { }
        } for fr in fuel_regions
    }

    for fr in fuel_regions:
        total_neutrons_emmited_from_fuel = np.zeros(energy)
        for r in regions:
            total_neutrons_emmited_from_fuel += fuel_neutrons[fr]["regions"][r]
        for s in surfaces:
            total_neutrons_emmited_from_fuel += fuel_neutrons[fr]["surfaces"][s]
        # Calculation of probabilities
        for r in regions:
            p_fuel[fr]["regions"][r] = fuel_neutrons[fr]["regions"][r] / total_neutrons_emmited_from_fuel
        for s in surfaces:
            p_fuel[fr]["surfaces"][s] = fuel_neutrons[fr]["surfaces"][s] / total_neutrons_emmited_from_fuel

    return p_fuel

def get_nonFuel_probabilities(nonFuel_neutrons, regions, surfaces, energy, nonFuel_regions):
    
    p_nonFuel = {
        r: {
            "regions": {
                rp: None for rp in regions
            },
            "surfaces": {
                s: None for s in surfaces
            }
        } for r in nonFuel_regions
    }

    for r in nonFuel_regions:
        total_emmited_from_nonFuel = np.zeros(energy)
        for rp in regions:
           total_emmited_from_nonFuel += nonFuel_neutrons[r]["regions"][rp]
        for s in surfaces:
            total_emmited_from_nonFuel += nonFuel_neutrons[r]["surfaces"][s]

        # Calculating probabilities
        for rp in regions:
            p_nonFuel[r]["regions"][rp] = nonFuel_neutrons[r]["regions"][rp]/total_emmited_from_nonFuel
        for s in surfaces:
            p_nonFuel[r]["surfaces"][s] = nonFuel_neutrons[r]["surfaces"][s]/total_emmited_from_nonFuel
    
    return p_nonFuel

def get_surface_probabilities(surface_neutrons, energy_groups, regions, surfaces):
    total_emmited_from_surfaces = {
        s: np.zeros(energy_groups) for s in surfaces
    }

    for s in surfaces:
        for r in regions:
            total_emmited_from_surfaces[s] += surface_neutrons[s]["regions"][r]
        for sp in surfaces:
            total_emmited_from_surfaces[s] += surface_neutrons[s]["surfaces"][sp]
    
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
            p_surfaces[s]["regions"][r] = surface_neutrons[s]["regions"][r]/total_emmited_from_surfaces[s]
        for sp in surfaces:
            p_surfaces[s]["surfaces"][sp] = surface_neutrons[s]["surfaces"][sp]/total_emmited_from_surfaces[s]
    
    return p_surfaces


def get_nonFuel_counts_lessDet(scores, det_relation, energy, regions, surfaces, nonFuel_regions):
    """
        Method to extract the following rates:
            - mod --> regions
            - mod --> surface
    """
    nonFuel_counts = {
        r: {
            "regions": { },
            "surfaces": { }
        } for r in nonFuel_regions
    }
    

    for r in nonFuel_regions:
        
        detectors = det_relation["regions"][r]
        
        for rp in regions: # rp is the region where the neutron intercts for the second time
            det_name_rp = detectors["regions"][rp].name
            nonFuel_counts[r]["regions"][rp] = np.flip(abs(scores[det_name_rp].tallies))
        
        for s in surfaces:
            det_name_surface = detectors["surfaces"][s].name
            nonFuel_counts[r]["surfaces"][s] = np.flip(abs(scores[det_name_surface].tallies))

    return nonFuel_counts

def get_fuel_counts_lessDet(scores, det_relation, energy, regions, surfaces, fuel_regions):
    """
        Method to extract the following rates:
            - fuel --> regions
            - fuel --> surfaces
        
        This methods counts the neutrons of every possible interaction fuel -> clad, fuel -> coolant, etc
    """  
    fuel_regions_counts = {
        r: {
            "regions": { },
            "surfaces": { }
        } for r in fuel_regions
    }
    
    for fr, detectors in det_relation["regions"].items():
    
        # Total reaction rate in the fuel
        det_name_total = detectors["total"].name

        # All neutrons entering the fuel through surface
        det_name_all_incoming = detectors["all_to_fuelReg"].name

        # Neutrons that interact in the fuel and then in other regions
        for rp in regions:
            if rp != fr:
                det_name_region = detectors["regions"][rp].name
                fuel_regions_counts[fr]["regions"][rp] = np.flip(abs(scores[det_name_region].tallies))

        # Neutrons  fuel to fuel        
        fuel_regions_counts[fr]["regions"][fr] = np.flip(
            abs(scores[det_name_total].tallies) - abs(scores[det_name_all_incoming].tallies)
        )

        # Neutrons fuel to surfaces
        for s in surfaces:
            det_name_surface = detectors["surfaces"][s].name
            fuel_regions_counts[fr]["surfaces"][s] = np.flip(abs(scores[det_name_surface].tallies))
        
    return fuel_regions_counts

def get_surface_counts_lessDet(scores, det_relation, energy, regions, surfaces):
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

    
    for s in det_relation.keys():
        for r in regions:
            det_name_region = det_relation[s]["regions"][r].name
            surface_counts[s]["regions"][r] = np.flip(abs(scores[det_name_region].tallies))
            for sp in surfaces:
                det_name_surface = det_relation[s]["surfaces"][sp].name
                surface_counts[s]["surfaces"][sp] = np.flip(abs(scores[det_name_surface].tallies))
    return surface_counts

def calculate_probabilities_main_nodes(det_inputs, mesh_info, coarse_nodes, fine_nodes, energy_groups, coarse_node_scores, detector_relation):                    
    """
        # TODO: The number of detectors can be reduced (see bellow)

        The probability for a neutron to enter the cell through a given surface
        and go out through the same surface without interacting is CERO
        
        The energy structure of scores are ordered from thermal --> fast  

        ------------------------------------------------------------------------
        
        detector_relation.keys() - Relation of detectors by type of counters
        coarse_node_scores.keys() - scores of the detectors by name
    """
    
    
    probabilities = {}

    # ----------------------------------------------------------------------------------------------------
    for id_ in det_inputs: # Loop for the different coarse nodes
        regions = mesh_info.coarse_region_rel[id_]
        surfaces = mesh_info.coarse_surface_rel[id_]
        fuel_regions = [r for r in fine_nodes[id_] if fine_nodes[id_][r].cell.content.isFuel]
        nonFuel_regions = [r for r in fine_nodes[id_] if not fine_nodes[id_][r].cell.content.isFuel]

        probabilities[id_] = { 
            "regions": {},
            "surfaces": {}
        }
        region_probabilities = {}
        fuel_probabilities = {}
        nonFuel_probabilities = {}
        surface_probabilities = {}
        for type_ in detector_relation[id_].keys():
            if type_ == "region_fuel":
                fuel_neutrons = get_fuel_counts_lessDet(coarse_node_scores[id_]["region_fuel"],detector_relation[id_]["region_fuel"],energy_groups,regions,surfaces, fuel_regions)
                fuel_probabilities = get_fuel_probabilities(fuel_neutrons,regions,surfaces,energy_groups,fuel_regions)
                print(fuel_neutrons)
                print("-"*50)
            elif type_ == "region_nonFuel":
                nonFuel_neutrons = get_nonFuel_counts_lessDet(coarse_node_scores[id_]["region_nonFuel"],detector_relation[id_]["region_nonFuel"],energy_groups,regions,surfaces, nonFuel_regions)
                nonFuel_probabilities = get_nonFuel_probabilities(nonFuel_neutrons,regions,surfaces,energy_groups, nonFuel_regions)
                print(nonFuel_neutrons)
                print("-"*50)
            elif type_ == "surfaces":
                surface_neutrons = get_surface_counts_lessDet(coarse_node_scores[id_]["surfaces"],detector_relation[id_]["surfaces"]["surfaces"],energy_groups,regions,surfaces)
                print(surface_neutrons)
                surface_probabilities = get_surface_probabilities(surface_neutrons,energy_groups,regions,surfaces)
                probabilities[id_]["surfaces"] = surface_probabilities
            else:
                print("Warning in calculate probabilities, type of detector not valid")
                raise SystemError
        # ----------------------------------------------------------------------------------------------------
        input()
        probabilities[id_]["regions"].update(fuel_probabilities)
        probabilities[id_]["regions"].update(nonFuel_probabilities)
        probabilities[id_]["surfaces"].update(surface_probabilities)

    return probabilities
        