import numpy as np

"""
    This file will contain the probabilities of previous cases 
    obtained in Chalmers by Huaiqian.
    Also this file will contain functions to compare them with
    other sets of probabilities.

    The order of energy groups is fast --> thermal
"""


p_fuel = {
    "fuel": np.array([0.20675, 0.24482]),
    "coolant": np.array([0.12699, 0.27405]),
    "surfaces": {
        3: np.array([0.16645, 0.1203]),
        4: np.array([0.16669, 0.12063]),
        5: np.array([0.16651, 0.12016]),
        6: np.array([0.16662, 0.12004])
    }
}

p_coolant = {
    "fuel": np.array([0.08148, 0.07995]),
    "coolant": np.array([0.2283, 0.38662]),
    "surfaces": {
        3: np.array([0.17248, 0.13336]),
        4: np.array([0.17259, 0.13337]),
        5: np.array([0.1727, 0.13335]),
        6: np.array([0.17245, 0.13334])
    }
}

p_surfaces = {
    3: {
        "fuel": np.array([0.12558, 0.12233]),
        "coolant": np.array([0.23916, 0.50323]),
        "surfaces": {
            3: np.array([0, 0]),
            4: np.array([0.21601, 0.10782]),
            5: np.array([0.20964, 0.1332]),
            6: np.array([0.20961, 0.13342])
        }
    },
    4: {
        "fuel": np.array([0.12554, 0.12195]),
        "coolant": np.array([0.23923, 0.50284]),
        "surfaces": {
            3: np.array([0.21588, 0.10789]),
            4: np.array([0, 0]),
            5: np.array([0.20974, 0.13352]),
            6: np.array([0.2096, 0.1338])
        }
    },
    5: {
        "fuel": np.array([0.12531, 0.12187]),
        "coolant": np.array([0.23914, 0.50316]),
        "surfaces": {
            3: np.array([0.20983, 0.13356]),
            4: np.array([0.20954, 0.13361]),
            5: np.array([0, 0]),
            6: np.array([0.21618, 0.1078])
        }
    },
    6: {
        "fuel": np.array([0.12536, 0.12199]),
        "coolant": np.array([0.23931, 0.50299]),
        "surfaces": {
            3: np.array([0.20944, 0.13338]),
            4: np.array([0.20962, 0.13354]),
            5: np.array([0.21627, 0.1081]),
            6: np.array([0, 0])
        }
    },
}

def compare_fuel(p_new):
    difference = { 
        "fuel": (p_new["fuel"] - p_fuel["fuel"])*100/p_fuel["fuel"],
        "coolant": (p_new["coolant"] - p_fuel["coolant"])*100/p_fuel["coolant"],
        "surfaces": {
            3: (p_new["surfaces"][3] - p_fuel["surfaces"][3])*100/p_fuel["surfaces"][3],
            4: (p_new["surfaces"][4] - p_fuel["surfaces"][4])*100/p_fuel["surfaces"][4],
            5: (p_new["surfaces"][5] - p_fuel["surfaces"][5])*100/p_fuel["surfaces"][5],
            6: (p_new["surfaces"][6] - p_fuel["surfaces"][6])*100/p_fuel["surfaces"][6]
        }
    }
    return difference

def compare_coolant(p_new):
    difference = { 
        "fuel": (p_new["fuel"] - p_coolant["fuel"])*100/p_coolant["fuel"],
        "coolant": (p_new["coolant"] - p_coolant["coolant"])*100/p_coolant["coolant"],
        "surfaces": {
            3: (p_new["surfaces"][3] - p_coolant["surfaces"][3])*100/p_coolant["surfaces"][3],
            4: (p_new["surfaces"][4] - p_coolant["surfaces"][4])*100/p_coolant["surfaces"][4],
            5: (p_new["surfaces"][5] - p_coolant["surfaces"][5])*100/p_coolant["surfaces"][5],
            6: (p_new["surfaces"][6] - p_coolant["surfaces"][6])*100/p_coolant["surfaces"][6]
        }
    }
    return difference

def compare_surfaces(p_new):
    difference = {
        3: {
            "fuel": (p_new[3]["fuel"] - p_surfaces[3]["fuel"])*100/p_surfaces[3]["fuel"],
            "coolant": (p_new[3]["coolant"] - p_surfaces[3]["coolant"])*100/p_surfaces[3]["coolant"],
            "surfaces": {
                3: p_new[3]["surfaces"][3],
                4: (p_new[3]["surfaces"][4] - p_surfaces[3]["surfaces"][4])*100/p_surfaces[3]["surfaces"][4],
                5: (p_new[3]["surfaces"][5] - p_surfaces[3]["surfaces"][5])*100/p_surfaces[3]["surfaces"][5],
                6: (p_new[3]["surfaces"][6] - p_surfaces[3]["surfaces"][6])*100/p_surfaces[3]["surfaces"][6]
            }
        },
        4: {
            "fuel": (p_new[4]["fuel"] - p_surfaces[4]["fuel"])*100/p_surfaces[4]["fuel"],
            "coolant": (p_new[4]["coolant"] - p_surfaces[4]["coolant"])*100/p_surfaces[4]["coolant"],
            "surfaces": {
                3: (p_new[4]["surfaces"][3] - p_surfaces[4]["surfaces"][3])*100/p_surfaces[4]["surfaces"][3],
                4: p_new[4]["surfaces"][4],
                5: (p_new[4]["surfaces"][5] - p_surfaces[4]["surfaces"][5])*100/p_surfaces[4]["surfaces"][5],
                6: (p_new[4]["surfaces"][6] - p_surfaces[4]["surfaces"][6])*100/p_surfaces[4]["surfaces"][6]
            }
        },
        5: {
            "fuel": (p_new[5]["fuel"] - p_surfaces[5]["fuel"])*100/p_surfaces[5]["fuel"],
            "coolant": (p_new[5]["coolant"] - p_surfaces[5]["coolant"])*100/p_surfaces[5]["coolant"],
            "surfaces": {
                3: (p_new[5]["surfaces"][3] - p_surfaces[5]["surfaces"][3])*100/p_surfaces[5]["surfaces"][3],
                4: (p_new[5]["surfaces"][4] - p_surfaces[5]["surfaces"][4])*100/p_surfaces[5]["surfaces"][4],
                5: p_new[5]["surfaces"][5],
                6: (p_new[5]["surfaces"][6] - p_surfaces[5]["surfaces"][6])*100/p_surfaces[5]["surfaces"][6]
            }
        },
        6: {
            "fuel": (p_new[6]["fuel"] - p_surfaces[6]["fuel"])*100/p_surfaces[6]["fuel"],
            "coolant": (p_new[6]["coolant"] - p_surfaces[6]["coolant"])*100/p_surfaces[6]["coolant"],
            "surfaces": {
                3: (p_new[6]["surfaces"][3] - p_surfaces[6]["surfaces"][3])*100/p_surfaces[6]["surfaces"][3],
                4: (p_new[6]["surfaces"][4] - p_surfaces[6]["surfaces"][4])*100/p_surfaces[6]["surfaces"][4],
                5: (p_new[6]["surfaces"][5] - p_surfaces[6]["surfaces"][5])*100/p_surfaces[6]["surfaces"][5],
                6: p_new[6]["surfaces"][6]
            }
        },
    }
    return difference