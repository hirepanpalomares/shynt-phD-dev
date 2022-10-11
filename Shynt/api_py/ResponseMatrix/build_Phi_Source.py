import numpy as np



def buildPhiSource(coarse_nodes, matrixT, source, energy_g):
    """
        This method builds the phi source vector of the system
        by energy group


        phi_source = {
            g0: array([]),
            g1: array([]),
            .
            .
            .
            gG: array([]),
        }
    """
    phi_source = {}
    for g in range(energy_g):
        mT = matrixT[g]
        q_vector = source[g]
        phi_s = np.matmul(mT, q_vector)
        phi_source[g] = phi_s
        # -------------------------------------
        rows_U, cols_U = mT.shape
        newMatU = np.zeros(mT.shape)
        source_phi = np.zeros(rows_U)
        for r in range(rows_U):
            term = 0
            for c in range(cols_U):
                newMatU[r][c] = mT[r][c] * q_vector[c]
                term += mT[r][c] * q_vector[c]
            source_phi[r] = term
        a = 0
    
    # print(phi_source)
    return phi_source

def buildPhiSource_sys(coarse_nodes, matrixT, source, energy_g):
    """
      
    """

    q_sys = []
    for g in range(energy_g):
        for val_ in source[g]:
            q_sys.append(val_)

    q_sys = np.array(q_sys)
    
    phi_source = np.matmul(matrixT, q_sys)

    return phi_source

def buildPhiSourceTBT(energy_g, mesh_info, probabilities, xs, keff, phi):
    phi_source = {}
    
    coarse_nodes = mesh_info.coarse_order
    coarse_nodes_regions = mesh_info.coarse_region_rel
    coarse_nodes_surfaces = mesh_info.coarse_surface_rel
    surface_areas = mesh_info.all_surfaces_area
    regions_volume = mesh_info.all_regions_vol

    for g in range(energy_g):
        phi_array = []
        for n_id in coarse_nodes:
            regions_n = coarse_nodes_regions[n_id]
            surfaces_n = coarse_nodes_surfaces[n_id]
            numRegions_n = len(regions_n)
            numSurfaces_n = len(surfaces_n)
    
            # Logic to calculate a term for a surface
            for j in range(numRegions_n):
                reg_j_id = regions_n[j]
                phi_val = 0
                for i in range(numRegions_n):
                    # Calculate Fraction
                    reg_i_id = regions_n[i]
                    vol_i = regions_volume[reg_i_id]
                    p_i_j = probabilities["regions"][reg_i_id]["regions"][reg_j_id][g]
                    xsTot = xs[reg_j_id]["total"][g]
                    vol_j = regions_volume[reg_j_id]

                    frac = (vol_i * p_i_j)/(xsTot * vol_j)

                    # Calculate Q
                    phi_i = 1
                    q_val = calculateQval(energy_g, xs[reg_i_id], keff, g, phi_i)
                    phi_val += frac*q_val
                #append value to array of each energy group
                phi_array.append(phi_val)
        phi_source[g] = phi_array

    return phi_source


def calculateQval(energy_g, xs, keff, g, phi_gp_i):
    q_val = 0
    for gp in range(energy_g):
        scatt_val = xs["scatter"][gp][g]
        fiss_val = xs["nuSigFission"][gp] * xs["chi"][g] / keff
        q_val += (scatt_val + fiss_val)*phi_gp_i

    return q_val

