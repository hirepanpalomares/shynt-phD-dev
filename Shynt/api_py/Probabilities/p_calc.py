import numpy as np
from . import compare

"""
    fuel_to_x_prob = np.array([
        [
            [0.2068, 0.1273, 0.1665, 0.1665, 0.1664, 0.1665],
            [0.2069, 0.1270, 0.1665, 0.1666, 0.1664, 0.1665],
            [0.2070, 0.1266, 0.1667, 0.1666, 0.1666, 0.1666],
            [0.2071, 0.1262, 0.1666, 0.1668, 0.1666, 0.1666],
            [0.2072, 0.1260, 0.1665, 0.1667, 0.1668, 0.1668],
            [0.2072, 0.1258, 0.1669, 0.1667, 0.1666, 0.1668]
        ],
        [
            [0.2454, 0.2734, 0.1202, 0.1204, 0.1206, 0.1200],
            [0.2517, 0.2690, 0.1198, 0.1201, 0.1196, 0.1199],
            [0.2605, 0.2625, 0.1191, 0.1193, 0.1195, 0.1191],
            [0.2681, 0.2581, 0.1185, 0.1182, 0.1183, 0.1188],
            [0.2751, 0.2531, 0.1181, 0.1182, 0.1180, 0.1175],
            [0.2802, 0.2496, 0.1174, 0.1174, 0.1175, 0.1179]
        ]
    ])

    mod_to_x_prob = np.array([
        [
            [0.2284, 0.0818, 0.1724, 0.1724, 0.1725, 0.1725],
            [0.2284, 0.0818, 0.1723, 0.1728, 0.1725, 0.1722],
            [0.2282, 0.0822, 0.1725, 0.1724, 0.1724, 0.1723],
            [0.2277, 0.0824, 0.1725, 0.1726, 0.1724, 0.1723],
            [0.2275, 0.0826, 0.1723, 0.1726, 0.1726, 0.1725],
            [0.2273, 0.0827, 0.1724, 0.1724, 0.1725, 0.1725]
        ],
        [
            [0.3868, 0.0800, 0.1334, 0.1331, 0.1334, 0.1333],
            [0.3838, 0.0825, 0.1335, 0.1333, 0.1335, 0.1333],
            [0.3800, 0.0860, 0.1336, 0.1335, 0.1334, 0.1335],
            [0.3767, 0.0889, 0.1339, 0.1333, 0.1337, 0.1336],
            [0.3740, 0.0916, 0.1337, 0.1333, 0.1335, 0.1338],
            [0.3717, 0.0933, 0.1335, 0.1340, 0.1337, 0.1338]
        ]
    ])

    surf_to_x = np.array([
        #val(:,:,:,1)
        [
            [  #val(:,:,1,1) =
                [0.1256, 0.2392,      0, 0.2160, 0.2096, 0.2096],   
                [0.1255, 0.2392, 0.2159,      0, 0.2097, 0.2096],
                [0.1253, 0.2391, 0.2098, 0.2095,      0, 0.2162],
                [0.1254, 0.2393, 0.2094, 0.2096, 0.2163,      0]
            ],
            [#val(:,:,2,1) =
                [0.1223, 0.5032,      0, 0.1078, 0.1332, 0.1334],
                [0.1220, 0.5028, 0.1079,      0, 0.1335, 0.1338],
                [0.1219, 0.5032, 0.1336, 0.1336,      0, 0.1078],
                [0.1220, 0.5030, 0.1334, 0.1335, 0.1081,      0]
            ]
        ],
        #val(:,:,:,2)
        [
            [#val(:,:,1,2) =
                [0.1256, 0.2388,      0, 0.2163, 0.2096, 0.2096],
                [0.1254, 0.2388, 0.2166,      0, 0.2094, 0.2098],
                [0.1256, 0.2389, 0.2093, 0.2096,      0, 0.2165],
                [0.1256, 0.2389, 0.2096, 0.2094, 0.2166,      0]
            ],
            [#val(:,:,2,2) =
                [0.1261, 0.4991,      0, 0.1071, 0.1338, 0.1338],
                [0.1257, 0.4993, 0.1076,      0, 0.1337, 0.1337],
                [0.1259, 0.4988, 0.1343, 0.1340,      0, 0.1071],
                [0.1256, 0.4995, 0.1336, 0.1339, 0.1074,      0]
            ]
        ],
        #val(:,:,:,3)
        [
            [#val(:,:,1,3) =
                [0.1257, 0.2382,      0, 0.2166, 0.2097, 0.2098],
                [0.1260, 0.2380, 0.2165,      0, 0.2099, 0.2096],
                [0.1259, 0.2385, 0.2099, 0.2094,      0, 0.2163],
                [0.1258, 0.2383, 0.2097, 0.2100, 0.2162,      0]
            ],
            [#val(:,:,2,3) =
                [0.1311, 0.4954,      0, 0.1056, 0.1341, 0.1338],
                [0.1314, 0.4945, 0.1057,      0, 0.1346, 0.1339],
                [0.1307, 0.4950, 0.1345, 0.1341,      0, 0.1058],
                [0.1311, 0.4945, 0.1345, 0.1342, 0.1057,      0]
            ]
        ],
        #val(:,:,:,4)
        [
            [#val(:,:,1,4) =
                [0.1257, 0.2378,      0, 0.2163, 0.2100, 0.2102],
                [0.1261, 0.2378, 0.2162,      0, 0.2100, 0.2100],
                [0.1259, 0.2377, 0.2101, 0.2098,      0, 0.2165],
                [0.1258, 0.2376, 0.2099, 0.2102, 0.2164,      0]
            ],
            [#val(:,:,2,4) =
                [0.1349, 0.4921,      0, 0.1042, 0.1347, 0.1342],
                [0.1358, 0.4905, 0.1050,      0, 0.1347, 0.1340],
                [0.1353, 0.4910, 0.1345, 0.1346,      0, 0.1046],
                [0.1351, 0.4918, 0.1346, 0.1341, 0.1045,      0]
            ]
        ],
        #val(:,:,:,5)
        [
            [#val(:,:,1,5) =
                [0.1262, 0.2369,      0, 0.2163, 0.2103, 0.2103],
                [0.1263, 0.2371, 0.2165,      0, 0.2100, 0.2101],
                [0.1262, 0.2370, 0.2098, 0.2103,      0, 0.2167],
                [0.1262, 0.2370, 0.2100, 0.2101, 0.2167,      0]
            ],
            [#val(:,:,2,5) =
                [0.1393, 0.4881,      0, 0.1034, 0.1348, 0.1344],
                [0.1388, 0.4881, 0.1031,      0, 0.1349, 0.1351],
                [0.1384, 0.4873, 0.1352, 0.1348,      0, 0.1043],
                [0.1394, 0.4880, 0.1348, 0.1343, 0.1034,      0]
            ]
        ],
        #val(:,:,:,6)
        [
            [#val(:,:,1,6) =
                [0.1265, 0.2367,      0, 0.2168, 0.2100, 0.2101],
                [0.1262, 0.2368, 0.2167,      0, 0.2104, 0.2100],
                [0.1263, 0.2366, 0.2104, 0.2100,      0, 0.2167],
                [0.1262, 0.2367, 0.2102, 0.2103, 0.2166,      0]
            ],
            [#val(:,:,2,6) =
                [0.1414, 0.4861,      0, 0.1026, 0.1351, 0.1348],
                [0.1412, 0.4861, 0.1029,      0, 0.1349, 0.1349],
                [0.1421, 0.4846, 0.1350, 0.1354,      0, 0.1030],
                [0.1419, 0.4856, 0.1348, 0.1347, 0.1029,      0]
            ]
        ]
    ])
"""

"""
    # def get_total_rate_counts(coarse_node_scores, detector_relation):
    #     total_rate = {} # Total interactions in a region
    #     for region, det in detector_relation["total_rate"].items():
    #         det_name = det.name
    #         scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
    #         scores = scores[::-1] # switches ther energy group order to g=1=fast and g=n=thermal
    #         total_rate[region] = np.abs(np.array(scores))
        
    #     return total_rate

    # def get_surf_counts(coarse_node_scores, detector_relation):
    #     surf_count = {} # Neutrons that enter the cell through a surface
    #     for surf, det in detector_relation["surf_count"].items():
    #         det_name = det.name
    #         scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
    #         scores = scores[::-1] # switches ther energy group order to g=1=fast and g=n=thermal
    #         surf_count[surf] = np.abs(np.array(scores))
        
    #     return surf_count

    # def get_surf_to_surf_counts(coarse_node_scores, detector_relation):
    #     surf_to_surf_count = {} # Neutrons that enter a surface and exit through another surface
    #     for surf, det_group in detector_relation["surf_to_surf"].items():
    #         surf_to_surf_count[surf] = {} 
            
    #         for surf_out, det in det_group.items():
    #             det_name = det.name

    #             scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
    #             scores = scores[::-1] # switches ther energy group order to g=1=fast and g=n=thermal
    #             surf_to_surf_count[surf][surf_out] = np.abs(np.array(scores))
        
    #     return surf_to_surf_count

    # def get_surf_to_region_counds(coarse_node_scores, detector_relation):
    #     surf_to_region_count = {}
    #     for surf, det_group in detector_relation["surf_to_region"].items():
    #         surf_to_region_count[surf] = {} 
            
    #         for reg, det in det_group.items():
    #             det_name = det.name

    #             scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
    #             scores = scores[::-1] # switches ther energy group order to g=1=fast and g=n=thermal
    #             surf_to_region_count[surf][reg] = np.abs(np.array(scores))
        
    #     return surf_to_region_count

    # def get_region_to_region_counts(coarse_node_scores, detector_relation):
    #     region_to_region_count = {}
    #     for region, det_group in detector_relation["region_to_region"].items():
    #         region_to_region_count[region] = {} 
            
    #         for region_p, det in det_group.items():
    #             det_name = det.name

    #             scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
    #             scores = scores[::-1] # switches ther energy group order to g=1=fast and g=n=thermal
    #             region_to_region_count[region][region_p] = np.abs(np.array(scores))
        
    #     return region_to_region_count

    # def get_region_to_surf_counts(coarse_node_scores, detector_relation):
    #     region_to_surf_count = {}
    #     for region, det_group in detector_relation["region_to_surf"].items():
    #         region_to_surf_count[region] = {} 
            
    #         for surf, det in det_group.items():
    #             det_name = det.name

    #             scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
    #             scores = scores[::-1] # switches ther energy group order to g=1=fast and g=n=thermal
    #             region_to_surf_count[region][surf] = np.abs(np.array(scores))
    #     return region_to_surf_count
        
    # def calculate_neutrons_emitted_from_region(total_rate, surf_total, reg_to_reg, reg_to_surf, surf_to_reg):
    #     regions = total_rate.keys()
    #     surfaces = surf_total.keys()

    #     neutrons_emitted_from_region = {}
    #     neutrons_same_to_same = {}
    #     for reg_i in regions:
    #         energy_groups = len(total_rate[reg_i])
    #         neutrons_in_region = [0] * energy_groups

    #         # Adding region to region neutrons for i != j
    #         for reg_j in regions:
    #             if reg_j != reg_i: #  (Condition checked already, it is OK!!!)
    #                 neutrons_in_region += reg_to_reg[reg_i][reg_j]

    #         # Adding region to surface neutrons
    #         for surf_a in surfaces:
    #             neutrons_in_region += reg_to_surf[reg_i][surf_a]

    #         # Adding region_i to region_i 
    #         neutrons_same_to_same[reg_i] = total_rate[reg_i]
    #         for reg_j in regions:
    #             if reg_j != reg_i: 
    #                 neutrons_same_to_same[reg_i] -= reg_to_reg[reg_j][reg_i]

    #         for surf_a in surfaces:
    #             neutrons_same_to_same[reg_i] -= surf_to_reg[surf_a][reg_i]
    #         neutrons_in_region += neutrons_same_to_same[reg_i]

    #         neutrons_emitted_from_region[reg_i] = neutrons_in_region
    #     return neutrons_emitted_from_region, neutrons_same_to_same
"""


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
    print()
    for g in range(energy):
        for gp in range(energy):

            det_name_fuel = det_relation["fuel"][g][gp].name
            det_name_coolant = det_relation["coolant"][g][gp].name
            print(det_name_fuel)

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




def calculate_probabilities(coarse_node_scores, detector_relation, energy_groups, id_):
    """
        # TODO: The number of detectors can be reduced (see bellow)

        The probability for a neutron to enter the cell through a given surface
        and go out through the same surface without interacting is CERO

        ------------------------------------------------------------------------
        
        detector_relation.keys() - Relation of detectors by type of counters
        coarse_node_scores.keys() - scores of the detectors by name
    """
    
    
    # The energy structure of these scores are ordered from the fastest --> thermal ----------------------
    
    # total_rate = get_total_rate_counts(coarse_node_scores, detector_relation)
    # surf_total = get_surf_counts(coarse_node_scores, detector_relation)
    # surf_to_surf = get_surf_to_surf_counts(coarse_node_scores, detector_relation)
    # surf_to_reg = get_surf_to_region_counds(coarse_node_scores, detector_relation)
    # reg_to_reg = get_region_to_region_counts(coarse_node_scores, detector_relation)
    # reg_to_surf = get_region_to_surf_counts(coarse_node_scores, detector_relation)

    # print("Detector counts\n")
    # print(f"Total rate:\n{total_rate}\n")
    # print(f"Neutrons crossing the surface:\n{surf_total}\n")
    # print(f"Surface to surface:\n{surf_to_surf}\n")
    # print(f"Surface to region:\n{surf_to_reg}\n")
    # print(f"Region to region:\n{reg_to_reg}\n")
    # print(f"Region to surface:\n{reg_to_surf}\n")

    # ----------------------------------------------------------------------------------------------------

   
    # The energy structure of these scores are ordered from thermal --> fast  ----------------------------

    fuel_neutrons = get_fuel_counts(coarse_node_scores, detector_relation["fuel"], energy_groups)
    coolant_neutrons = get_moderator_counts(coarse_node_scores, detector_relation["coolant"], energy_groups)
    surface_neutrons = get_surface_counts(coarse_node_scores, detector_relation["surfaces"], energy_groups)

    # print(fuel_neutrons)
    # print(coolant_neutrons)
    # print(surface_neutrons)
    # ----------------------------------------------------------------------------------------------------



    print("-"*100)

    # total_neutrons = {}

    """
        a:  surface
        i:  region
        j:  region
        b:  surface

    """
    prob_a_j = {}
    prob_i_j = {}
    prob_a_b = {}
    prob_i_a = {}
    
    
    # Probabilities from fuel: ----------------------------------------------------------------------------

    emmited_from_fuel = fuel_neutrons["fuel"] + fuel_neutrons["coolant"]
    
    for s in detector_relation["surfaces"].keys():
        emmited_from_fuel += fuel_neutrons["surface"][s]
    print("Probabilities from the fuel to: \n")
    
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
    for s in detector_relation["surfaces"].keys():
        p_fuel["surfaces"][s] = fuel_neutrons["surface"][s]/emmited_from_fuel
    
    diff_fuel = compare.compare_fuel(p_fuel)
    print(p_fuel)
    print()
    print("Percentage difference: ")
    print(diff_fuel)
    # surfaces = [3, 4, 5, 6]
    # for g in range(energy_groups):
    #     a = [p_fuel["fuel"][g], p_fuel["coolant"][g]]
    #     for sp in surfaces:
    #         a.append(p_fuel[sp][g])
        # print(a)
        # print()
    print("-"*100)


    # ----------------------------------------------------------------------------------------------------

    # Probabilities from coolant: ------------------------------------------------------------------------

    emmited_from_coolant = coolant_neutrons["fuel"] + coolant_neutrons["coolant"]
    for s in detector_relation["surfaces"].keys():
        emmited_from_coolant += coolant_neutrons["surface"][s]
    
    
    print("Probabilities from the coolant to: \n")
    
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
    for s in detector_relation["surfaces"].keys():
        p_coolant["surfaces"][s] = coolant_neutrons["surface"][s]/emmited_from_coolant
    
    diff_coolant = compare.compare_coolant(p_coolant)
    print(p_coolant)
    print()
    print("Percentage difference: ")

    print(diff_coolant)
    # surfaces = [3, 4, 5, 6]
    # for g in range(energy_groups):
    #     a = [p_coolant["fuel"][g], p_coolant["coolant"][g]]
    #     for sp in surfaces:
    #         a.append(p_coolant[sp][g])
        #print(a)
        #print()
    print("-"*100)
    # ----------------------------------------------------------------------------------------------------

    # Probabilities from surfaces ------------------------------------------------------------------------
    emmited_from_surfaces = {
        s: np.zeros(energy_groups) for s in detector_relation["surfaces"].keys()
    }
    for s in detector_relation["surfaces"].keys():
        # print(s)
        emmited_from_surfaces[s] = surface_neutrons[s]["fuel"] + surface_neutrons[s]["coolant"]
        for sp in detector_relation["surfaces"].keys():
            emmited_from_surfaces[s] += surface_neutrons[s]["surface"][sp]
    # print(emmited_from_surfaces)
    
    
    #print("Probabilities from the surfaces to: \n")
    
    p_surfaces = {
        s: {
            "fuel": None,
            "coolant": None,
            "surfaces": {}
        } for s in detector_relation["surfaces"].keys() 
    }
    # print(p_surfaces)
    for s in detector_relation["surfaces"].keys():
        p_surfaces[s]["fuel"] = surface_neutrons[s]["fuel"]/emmited_from_surfaces[s]
        p_surfaces[s]["coolant"] = surface_neutrons[s]["coolant"]/emmited_from_surfaces[s]
        for sp in detector_relation["surfaces"].keys():
            p_surfaces[s]["surfaces"][sp] = surface_neutrons[s]["surface"][sp]/emmited_from_surfaces[s]
    
    
    diff_surfaces = compare.compare_surfaces(p_surfaces)
    print(p_surfaces)
    print()
    print("Percentage difference: ")

    print(diff_surfaces)
    
    # surfaces = [3, 4, 5, 6]
    # for g in range(energy_groups):
    #     for s in surfaces:
    #         a = [p_surfaces[s]["fuel"][g], p_surfaces[s]["coolant"][g]]
    #         for sp in surfaces:
    #             a.append(p_surfaces[s][sp][g])
            # print(a)
        # print()

    # for key, value in p_surfaces.items():
    #     print(key, value)
    print("-"*100)
    
    # ----------------------------------------------------------------------------------------------------


    # print(coarse_node_scores)
        

# det total_rate_coolant_g0  de 2groups_grid_0 dr -1 coolant dc 2 dfl 5 1 
# det total_rate_coolant_g1  de 2groups_grid_1 dr -1 coolant dc 2 dfl 6 1 
# det coolant_coolant_g0_to_g0  de 2groups_grid_0 dr -1 coolant dc 2 dfl 5 2  dfl 5 0  dfl 5 1 
# det coolant_fuel_g0_to_g0  de 2groups_grid_0 dr -1 fuel1 dc 1 dfl 5 2  dfl 5 0  dfl 5 1 
# det coolant_surface6_g0_to_g0 ds 6 1 de 2groups_grid_0   dfl 5 2  dfl 5 0 
# det coolant_surface4_g0_to_g0 ds 4 1 de 2groups_grid_0   dfl 5 2  dfl 5 0 
# det coolant_surface5_g0_to_g0 ds 5 -1 de 2groups_grid_0   dfl 5 2  dfl 5 0 
# det coolant_surface3_g0_to_g0 ds 3 -1 de 2groups_grid_0   dfl 5 2  dfl 5 0 
# det coolant_coolant_g0_to_g1  de 2groups_grid_1 dr -1 coolant dc 2 dfl 5 2  dfl 5 0  dfl 6 1 
# det coolant_fuel_g0_to_g1  de 2groups_grid_1 dr -1 fuel1 dc 1 dfl 5 2  dfl 5 0  dfl 6 1 
# det coolant_surface6_g0_to_g1 ds 6 1 de 2groups_grid_1   dfl 5 2  dfl 5 0 
# det coolant_surface4_g0_to_g1 ds 4 1 de 2groups_grid_1   dfl 5 2  dfl 5 0 
# det coolant_surface5_g0_to_g1 ds 5 -1 de 2groups_grid_1   dfl 5 2  dfl 5 0 
# det coolant_surface3_g0_to_g1 ds 3 -1 de 2groups_grid_1   dfl 5 2  dfl 5 0 
# det coolant_coolant_g1_to_g0  de 2groups_grid_0 dr -1 coolant dc 2 dfl 6 2  dfl 6 0  dfl 5 1 
# det coolant_fuel_g1_to_g0  de 2groups_grid_0 dr -1 fuel1 dc 1 dfl 6 2  dfl 6 0  dfl 5 1 
# det coolant_surface6_g1_to_g0 ds 6 1 de 2groups_grid_0   dfl 6 2  dfl 6 0 
# det coolant_surface4_g1_to_g0 ds 4 1 de 2groups_grid_0   dfl 6 2  dfl 6 0 
# det coolant_surface5_g1_to_g0 ds 5 -1 de 2groups_grid_0   dfl 6 2  dfl 6 0 
# det coolant_surface3_g1_to_g0 ds 3 -1 de 2groups_grid_0   dfl 6 2  dfl 6 0 
# det coolant_coolant_g1_to_g1  de 2groups_grid_1 dr -1 coolant dc 2 dfl 6 2  dfl 6 0  dfl 6 1 
# det coolant_fuel_g1_to_g1  de 2groups_grid_1 dr -1 fuel1 dc 1 dfl 6 2  dfl 6 0  dfl 6 1 
# det coolant_surface6_g1_to_g1 ds 6 1 de 2groups_grid_1   dfl 6 2  dfl 6 0 
# det coolant_surface4_g1_to_g1 ds 4 1 de 2groups_grid_1   dfl 6 2  dfl 6 0 
# det coolant_surface5_g1_to_g1 ds 5 -1 de 2groups_grid_1   dfl 6 2  dfl 6 0 
# det coolant_surface3_g1_to_g1 ds 3 -1 de 2groups_grid_1   dfl 6 2  dfl 6 0 