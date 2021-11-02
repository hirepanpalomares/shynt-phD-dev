import numpy as np


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

        
def get_total_rate_counts(coarse_node_scores, detector_relation):
    total_rate = {} # Total interactions in a region
    for region, det in detector_relation["total_rate"].items():
        det_name = det.name
        scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
        total_rate[region] = scores
    
    return total_rate

def get_surf_counts(coarse_node_scores, detector_relation):
    surf_count = {} # Neutrons that enter the cell through a surface
    for surf, det in detector_relation["surf_count"].items():
        det_name = det.name
        scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
        surf_count[surf] = scores
    
    return surf_count

def get_surf_to_surf_counts(coarse_node_scores, detector_relation):
    surf_to_surf_count = {} # Neutrons that enter a surface and exit through another surface
    for surf, det_group in detector_relation["surf_to_surf"].items():
        surf_to_surf_count[surf] = {} 
        
        for surf_out, det in det_group.items():
            det_name = det.name

            scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
            surf_to_surf_count[surf][surf_out] = scores 
    
    return surf_to_surf_count

def get_surf_to_region_counds(coarse_node_scores, detector_relation):
    surf_to_region_count = {}
    for surf, det_group in detector_relation["surf_to_region"].items():
        surf_to_region_count[surf] = {} 
        
        for reg, det in det_group.items():
            det_name = det.name

            scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
            surf_to_region_count[surf][reg] = scores 
    
    return surf_to_region_count

def get_region_to_region_counts(coarse_node_scores, detector_relation):
    region_to_region_count = {}
    for region, det_group in detector_relation["region_to_region"].items():
        region_to_region_count[region] = {} 
        
        for region_p, det in det_group.items():
            det_name = det.name

            scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
            region_to_region_count[region][region_p] = scores 
    
    return region_to_region_count

def get_region_to_surf_counts(coarse_node_scores, detector_relation):
    region_to_surf_count = {}
    for region, det_group in detector_relation["region_to_surf"].items():
        region_to_surf_count[region] = {} 
        
        for surf, det in det_group.items():
            det_name = det.name

            scores = [g[0] for g in coarse_node_scores[det_name]["neutrons"]]
            region_to_surf_count[region][surf] = scores 
    return region_to_surf_count
    



def calculate_probabilities(coarse_node_scores, detector_relation):
    """
    # TODO: The number of detectors can be reduced (see bellow)

    The probability for a neutron to enter the cell through a given surface
    and go out through the same surface without interacting is CERO

    ------------------------------------------------------------------------
    
    # TODO cell to surf counts are cero why? 
    
    detector_relation.keys() - Relation of detectors by type of counters
    coarse_node_scores.keys() - scores of the detectors by name
    """
    
    
    # return 1
    total_rate = get_total_rate_counts(coarse_node_scores, detector_relation)
    surf_total = get_surf_counts(coarse_node_scores, detector_relation)
    surf_to_surf = get_surf_to_surf_counts(coarse_node_scores, detector_relation)
    surf_to_reg = get_surf_to_region_counds(coarse_node_scores, detector_relation)
    reg_to_reg = get_region_to_region_counts(coarse_node_scores, detector_relation)
    reg_to_surf = get_region_to_surf_counts(coarse_node_scores, detector_relation)

    print(total_rate)
    # print(surf_total)
    # print(surf_to_surf)
    print(surf_to_reg)
    print(reg_to_reg)
    # print(reg_to_surf)

    # total_neutrons = {}

    """
        a:  surface
        i:  region
        j:  region
        b:  surface

    """
    P_a_j = {}
    P_i_j = {}
    P_b_a = {}
    P_i_a = {}
    regions = total_rate.keys()
    surfaces = surf_total.keys()
    for reg_i in regions:
        energy_groups = len(total_rate[reg_i])
        neutrons_in_region = [0] * energy_groups

        # Adding region to region neutrons
        for reg_j in regions:
            if reg_j != reg_i: # Check condition
                for g in range(energy_groups):
                    neutrons_in_region[g] += reg_to_reg[reg_i][reg_j][g]
        print(neutrons_in_region)

        # Adding region to surface neutrons
        for surf_a in surfaces:
            for g in range(energy_groups):
                neutrons_in_region[g] += reg_to_surf[reg_i][surf_a][g]
        
        print(neutrons_in_region)

        # Adding region_i to region_i 
        total_rate_neutrons = total_rate[reg_i]
        print(total_rate_neutrons)
        for reg_j in regions:
            if reg_j != reg_i: 
               for g in range(energy_groups):
                   total_rate_neutrons[g] -= reg_to_reg[reg_j][reg_i][g]
        print(total_rate_neutrons)

        for surf_a in surfaces:
            for g in range(energy_groups):
                total_rate_neutrons[g] -= surf_to_reg[surf_a][reg_i][g]
        print(total_rate_neutrons)
        break
    
       
    # print(coarse_node_scores)
        

