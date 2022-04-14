import numpy as np




def solveExplicit(coarse_nodes, fine_nodes, energy_g, xs, probabilities, mesh_info):
    
    phi_prev = {
        "fuel": [100, 100], # [g1, g2]
        "cool": [100, 100]  # [g1, g2]
    }

    keff_prev = 1
    
    tol = 1
    identityMatrix = np.identity(4)
    print("fuel")
    print(xs[1][1]["scatter"])
    print("coolant")
    print(xs[1][2]["scatter"])

    while tol > 1E-08:

        q = calculateSource(xs[1], keff_prev, phi_prev)
        # print(q)
        j_source = calculate_j_source(q, probabilities[1])
        rm = calculate_response_matrix(probabilities[1])

        j_out = {}
        for g in range(2):
            # Global problem
            mat2inv = identityMatrix - rm[g]
            inv = np.linalg.inv(mat2inv)
            # print(inv)
            # print(j_source[g])
            j_out[g] = np.matmul(inv, j_source[g])
        # print(j_out)
        
        # Local Problem
        phi_new = calculateFlux(xs[1], q, probabilities[1], j_out)
        
        x_prev_power = calculate_power_flux(xs[1], probabilities[1], phi_prev)
        x_new_power = calculate_power_flux(xs[1], probabilities[1], phi_new)

        # print(phi_prev)
        # print(phi_new)

        # print(x_new_power)
        # print(x_prev_power)

        new_keff = calculate_keff(x_prev_power, x_new_power, keff_prev)
        print(new_keff)


        tol = abs(new_keff - keff_prev)
        keff_prev = new_keff
        phi_prev = phi_new

        # break
        

        
        
    



def calculate_keff(prev_flux, new_flux, prev_keff):
    # concatenate fluxes
    
    # phi_prev = []
    # phi_new = []
    # for g in range(2):
    #     phi_prev.append(prev_flux["fuel"][g])
    #     phi_prev.append(prev_flux["cool"][g])
    #     phi_new.append(new_flux["fuel"][g])
    #     phi_new.append(new_flux["cool"][g])

    # phi_prev = np.array(phi_prev)
    # phi_new = np.array(phi_new)

    keff_new = prev_keff * np.inner(prev_flux, new_flux) / np.inner(prev_flux, prev_flux)

    return keff_new


def calculateSource(xs, k, flux):
    xs_fuel = xs[1]
    xs_cool = xs[2]
    scatter_fuel = xs_fuel["scatter"]
    scatter_cool = xs_cool["scatter"]
    nuFiss_fuel = xs_fuel["nuSigFission"]
    chi_fuel = xs_fuel["chi"]
    

    g0 = 0
    g1 = 1

    q_fuel_g0 = (scatter_fuel[g0][g0] * flux["fuel"][g0] + scatter_fuel[g1][g0] * flux["fuel"][g1] + \
        (chi_fuel[g0] / k) * (nuFiss_fuel[g0] * flux["fuel"][g0] + nuFiss_fuel[g1] * flux["fuel"][g1]))\
        / (4 * np.pi)
    

    q_fuel_g1 = (scatter_fuel[g0][g1] * flux["fuel"][g0] + scatter_fuel[g1][g1] * flux["fuel"][g1] + \
        (chi_fuel[g1] / k) * (nuFiss_fuel[g0] * flux["fuel"][g0] + nuFiss_fuel[g1] * flux["fuel"][g1])) \
        / (4 * np.pi)

    q_cool_g0 = (scatter_cool[g0][g0] * flux["cool"][g0] + scatter_cool[g1][g0] * flux["cool"][g1]) \
        / (4 * np.pi)

    q_cool_g1 = (scatter_cool[g0][g1] * flux["cool"][g0] + scatter_cool[g1][g1] * flux["cool"][g1]) \
        / (4 * np.pi)



    return {
        "fuel": [q_fuel_g0, q_fuel_g1],
        "coolant": [q_cool_g0, q_cool_g1]
    }


def calculate_j_source(q,prob):
    v_fuel = 0.590375
    v_cool = 1.08664983
    a_surf = 1.295

    g0 = 0
    g1 = 1
    j_s_g0 = np.array([
        (prob["fuel"]["surfaces"][3][g0] * v_fuel * q["fuel"][g0] + prob["coolant"]["surfaces"][3][g0] * v_cool * q["coolant"][g0])/a_surf,
        (prob["fuel"]["surfaces"][4][g0] * v_fuel * q["fuel"][g0] + prob["coolant"]["surfaces"][4][g0] * v_cool * q["coolant"][g0])/a_surf,
        (prob["fuel"]["surfaces"][5][g0] * v_fuel * q["fuel"][g0] + prob["coolant"]["surfaces"][5][g0] * v_cool * q["coolant"][g0])/a_surf,
        (prob["fuel"]["surfaces"][6][g0] * v_fuel * q["fuel"][g0] + prob["coolant"]["surfaces"][6][g0] * v_cool * q["coolant"][g0])/a_surf,
    ])

    j_s_g1 = np.array([
        (prob["fuel"]["surfaces"][3][g1] * v_fuel * q["fuel"][g1] + prob["coolant"]["surfaces"][3][g1] * v_cool * q["coolant"][g1])/a_surf,
        (prob["fuel"]["surfaces"][4][g1] * v_fuel * q["fuel"][g1] + prob["coolant"]["surfaces"][4][g1] * v_cool * q["coolant"][g1])/a_surf,
        (prob["fuel"]["surfaces"][5][g1] * v_fuel * q["fuel"][g1] + prob["coolant"]["surfaces"][5][g1] * v_cool * q["coolant"][g1])/a_surf,
        (prob["fuel"]["surfaces"][6][g1] * v_fuel * q["fuel"][g1] + prob["coolant"]["surfaces"][6][g1] * v_cool * q["coolant"][g1])/a_surf,
    ])

    return {
        0: j_s_g0,
        1: j_s_g1
    }


def calculate_response_matrix(prob):

    # print(prob["surface"][3].keys())
    
    rm_g0 = [
        [prob["surface"][3]["surfaces"][3][0], prob["surface"][4]["surfaces"][3][0], prob["surface"][5]["surfaces"][3][0], prob["surface"][6]["surfaces"][3][0]],
        [prob["surface"][3]["surfaces"][4][0], prob["surface"][4]["surfaces"][4][0], prob["surface"][5]["surfaces"][4][0], prob["surface"][6]["surfaces"][4][0]],
        [prob["surface"][3]["surfaces"][5][0], prob["surface"][4]["surfaces"][5][0], prob["surface"][5]["surfaces"][5][0], prob["surface"][6]["surfaces"][5][0]],
        [prob["surface"][3]["surfaces"][6][0], prob["surface"][4]["surfaces"][6][0], prob["surface"][5]["surfaces"][6][0], prob["surface"][6]["surfaces"][6][0]]
    ]

    rm_g1 = [
        [prob["surface"][3]["surfaces"][3][1], prob["surface"][4]["surfaces"][3][1], prob["surface"][5]["surfaces"][3][1], prob["surface"][6]["surfaces"][3][1]],
        [prob["surface"][3]["surfaces"][4][1], prob["surface"][4]["surfaces"][4][1], prob["surface"][5]["surfaces"][4][1], prob["surface"][6]["surfaces"][4][1]],
        [prob["surface"][3]["surfaces"][5][1], prob["surface"][4]["surfaces"][5][1], prob["surface"][5]["surfaces"][5][1], prob["surface"][6]["surfaces"][5][1]],
        [prob["surface"][3]["surfaces"][6][1], prob["surface"][4]["surfaces"][6][1], prob["surface"][5]["surfaces"][6][1], prob["surface"][6]["surfaces"][6][1]]
    ]
    

    return {
        0: np.array(rm_g0),
        1: np.array(rm_g1)
    }


def calculateFlux(xs, q, prob, j_in):
    v_fuel = 0.590375
    v_cool = 1.08664983
    a_surf = 1.295

    sigTotal_fuel = xs[1]["total"]
    sigTotal_cool= xs[2]["total"]

    g0 = 0
    g1 = 1

    flux_fuel_g0 = v_fuel * prob["fuel"]["fuel"][g0] * q["fuel"][g0] +\
        v_cool * prob["coolant"]["fuel"][g0] * q["coolant"][g0] +\
        a_surf * prob["surface"][3]["fuel"][g0] * j_in[g0][0] +\
        a_surf * prob["surface"][4]["fuel"][g0] * j_in[g0][1] +\
        a_surf * prob["surface"][5]["fuel"][g0] * j_in[g0][2] +\
        a_surf * prob["surface"][6]["fuel"][g0] * j_in[g0][3]
    flux_fuel_g0 /= (v_fuel*sigTotal_fuel[g0])
    
    flux_fuel_g1 = v_fuel * prob["fuel"]["fuel"][g1] * q["fuel"][g1] +\
        v_cool * prob["coolant"]["fuel"][g1] * q["coolant"][g1] +\
        a_surf * prob["surface"][3]["fuel"][g1] * j_in[g1][0] +\
        a_surf * prob["surface"][4]["fuel"][g1] * j_in[g1][1] +\
        a_surf * prob["surface"][5]["fuel"][g1] * j_in[g1][2] +\
        a_surf * prob["surface"][6]["fuel"][g1] * j_in[g1][3]
    flux_fuel_g1 /= (v_fuel*sigTotal_fuel[g1])

    
    flux_coolant_g0 = v_fuel * prob["fuel"]["coolant"][g0] * q["fuel"][g0] +\
        v_cool * prob["coolant"]["coolant"][g0] * q["coolant"][g0] +\
        a_surf * prob["surface"][3]["coolant"][g0] * j_in[g0][0] +\
        a_surf * prob["surface"][4]["coolant"][g0] * j_in[g0][1] +\
        a_surf * prob["surface"][5]["coolant"][g0] * j_in[g0][2] +\
        a_surf * prob["surface"][6]["coolant"][g0] * j_in[g0][3]
    flux_coolant_g0 /= (v_cool*sigTotal_cool[g0])
    
    
    flux_coolant_g1 = v_fuel * prob["fuel"]["coolant"][g1] * q["fuel"][g1] +\
        v_cool * prob["coolant"]["coolant"][g1] * q["coolant"][g1] +\
        a_surf * prob["surface"][3]["coolant"][g1] * j_in[g1][0] +\
        a_surf * prob["surface"][4]["coolant"][g1] * j_in[g1][1] +\
        a_surf * prob["surface"][5]["coolant"][g1] * j_in[g1][2] +\
        a_surf * prob["surface"][6]["coolant"][g1] * j_in[g1][3]
    flux_coolant_g1 /= (v_cool*sigTotal_cool[g1])


    return {
        "fuel": [flux_fuel_g0, flux_fuel_g1], # [g1, g2]
        "cool": [flux_coolant_g0, flux_coolant_g1]  # [g1, g2]
    }


def calculate_power_flux(xs, prob, flux):
    v_fuel = 0.590375
    

    xs_fuel = xs[1]

    nuFiss_fuel = xs_fuel["nuSigFission"]
    chi_fuel = xs_fuel["chi"]

    g0 = 0
    g1 = 1


    x_fuel_g0 = v_fuel * prob["fuel"]["fuel"][g0] * chi_fuel[g0] * (nuFiss_fuel[0] * flux["fuel"][0] +  nuFiss_fuel[1] * flux["fuel"][1]) 

    x_fuel_g1 = v_fuel * prob["fuel"]["fuel"][g1] * chi_fuel[g1] * (nuFiss_fuel[0] * flux["fuel"][0] +  nuFiss_fuel[1] * flux["fuel"][1]) 
    

    x_cool_g0 = v_fuel * prob["fuel"]["coolant"][g0] * chi_fuel[g0] * (nuFiss_fuel[0] * flux["fuel"][0] +  nuFiss_fuel[1] * flux["fuel"][1]) 

    x_cool_g1 = v_fuel * prob["fuel"]["coolant"][g1] * chi_fuel[g1] * (nuFiss_fuel[0] * flux["fuel"][0] +  nuFiss_fuel[1] * flux["fuel"][1]) 

    return np.array([
        x_fuel_g0,
        x_cool_g0,
        x_fuel_g1,
        x_cool_g1
    ])




