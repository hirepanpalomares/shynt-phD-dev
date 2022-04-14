
def print_probabilities(probabilities):
    to_print = "region_coolant"
    for g in range(2):
        for id_ in probabilities:
            vec = []
            for reg in probabilities[id_][to_print]["regions"]:
                vec.append(probabilities[id_][to_print]["regions"][reg][g])
            for surf in probabilities[id_][to_print]["surfaces"]:
                vec.append(probabilities[id_][to_print]["surfaces"][surf][g])
            # print(np.array(vec))
        # print()

    to_print = "surfaces"
    for g in range(2):
        for id_ in probabilities:
            
            for surf in probabilities[id_][to_print]:
                vec = []
                for reg in probabilities[id_][to_print][surf]["regions"]:
                    vec.append(probabilities[id_][to_print][surf]["regions"][reg][g])
                for surfp in probabilities[id_][to_print][surf]["surfaces"]:
                    vec.append(probabilities[id_][to_print][surf]["surfaces"][surfp][g])
                print(np.array(vec))
            print()

    print(probabilities[1]["surfaces"])
