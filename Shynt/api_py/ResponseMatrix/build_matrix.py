import json
from mimetypes import init
import numpy as np


class Source:


    def __init__(self, coarse_nodes, energy_g, xs, keff, phi) -> None:
        self.__coarseNodes = coarse_nodes
        self.__energyG = energy_g
        self.__xs = xs
        self.__keff = keff
        self.__flux = phi

        self.__fissionMatrix = self.__buildFissionMatrix() 
        self.__scatteringMatrix = self.__buildScatteringMatrix()


    def __buildFissionMatrix(self):
        """
            returns the fission matrix by node and by region in the node
        """
        fission = {}
        # print("chi: ", self.__xs[1][1]["chi"])
        # print("fiss: ", self.__xs[1][1]["nuSigFission"])
        print("fission  ")
        for n_id, node in self.__coarseNodes.items():
            regions = node.fine_nodes_ids
            fission[n_id] = {}
            for r in regions:
                fission[n_id][r] = np.zeros((self.__energyG, self.__energyG))
                nuFiss = self.__xs[n_id][r]["nuSigFission"]
                chi = self.__xs[n_id][r]["chi"]
                print(r)
                for g in range(self.__energyG):
                    for gp in range(self.__energyG):
                        fission[n_id][r][g][gp] = chi[g] * nuFiss[gp]
                print(fission[n_id][r])
        print()
        print()
        return fission
    

    def __buildScatteringMatrix(self):
        scattering = {}
        print("scattering")
        for n_id, node in self.__coarseNodes.items():
            regions = node.fine_nodes_ids
            scattering[n_id] = {}
            for r in regions:
                print(r)
                scattMatrix = self.__xs[n_id][r]["scatter"]
                print(scattMatrix)
                scattering[n_id][r] = scattMatrix
        return scattering


    def calculate_Qvector(self, keff, flux):
        """
            It returns a dictionary with the source terms in it:

            sourceQ_byNode_byEnergy = {
                coarseNode_id: {
                    g_0: array([q_region_1_g0, q_region_2_g0, ..., q_region_I_g0]),
                    g_1: array([q_region_1_g1, q_region_2_g0, ..., q_region_I_g0]),
                    ...
                    ...
                    ...
                    g_G:
                }
            }
        """
        _Q = {}
        for n_id, node in self.__coarseNodes.items():
            _Q[n_id] = {}
            regions = node.fine_nodes_ids
            numRegions = len(regions)
            for g in range(self.__energyG):
                _Q[n_id][g] = np.zeros(numRegions)
                for r in range(numRegions):
                    region_id = regions[r]
                    _Q[n_id][g][r] += np.sum(self.__scatteringMatrix[n_id][region_id][g])
                    _Q[n_id][g][r] += np.sum(self.__fissionMatrix[n_id][region_id][g]) / keff
                    _Q[n_id][g][r] *= flux[n_id][region_id][g]
                # print(_Q[n_id][g])
                _Q[n_id][g] *= (1 / (4 * np.pi))
                # print(_Q[n_id][g])

        return _Q


def getInitializedPhi_byNode(coarse_nodes, energy_g):
    phi_vectors = {}

    for node_id, node in coarse_nodes.items():
        phi_vectors[node_id] = {}
        regions = node.fine_nodes_ids
        for r in regions:
            phi_vectors[node_id][r] = {}
            for g in range(energy_g):
                phi_vectors[node_id][r][g] = 1.0
    return phi_vectors

def getMatrixS_byGlobalNode(coarse_nodes, energy_g, xs, probabilities):
    matrix_S_byNode_byGroup = {}
 
    for c_id, node in coarse_nodes.items():
        # for each coarse node
        matrix_S_byNode_byGroup[c_id] = {}
        regions = node.fine_nodes_ids
        regions_volume = node.fine_nodes_volume
        surfaces_n = node.surface_ids
        surface_areas_n = node.surface_areas
        for g in range(energy_g):

            mS = build_S(  
                xs[c_id],
                probabilities[c_id]["surface"],
                surfaces_n,
                surface_areas_n,
                regions,
                regions_volume,
                g
            )
            matrix_S_byNode_byGroup[c_id][g] = mS   
        
    return matrix_S_byNode_byGroup

def getMatrixT_byGlobalNode(coarse_nodes, energy_g, xs, probabilities):
    matrix_T_byNode_byGroup = {}
    for n_id, node in coarse_nodes.items():
        matrix_T_byNode_byGroup[n_id] = {}
        regions = node.fine_nodes_ids
        regions_volume = node.fine_nodes_volume
        for g in range(energy_g):
            mT = build_T(
                xs[n_id],
                probabilities[n_id],
                regions,
                regions_volume,
                g
            )
            matrix_T_byNode_byGroup[n_id][g] = mT
    return matrix_T_byNode_byGroup

def getResponseMatrix_system(coarse_nodes, energy_g, probabilities):
    responseMatrix_byNode_byGroup = { }
    matrix_corners = {}
    node_order = [] # This is for the order of the surfaces in the response matrix 
    corner = (0,0) # Postion of the left upper corner of the matrix in the RM of the system
    for n_id, node in coarse_nodes.items():
        matrix_corners[n_id] = corner
        responseMatrix_byNode_byGroup[n_id] = {}
        surfaces_n = node.surface_ids
        node_order.append(n_id)
        surface_areas_n = node.surface_areas
        # print()
        # print()
        # print()
        # print()

        # print(surfaces_n)
        for g in range(energy_g):
            rm_n, rm_n_shape = build_R(
                probabilities[n_id]["surface"],
                surfaces_n,
                surface_areas_n,
                g
            ) 
            
            responseMatrix_byNode_byGroup[n_id][g] = rm_n
        corner = (
            corner[0] + rm_n_shape[0], 
            corner[1] + rm_n_shape[1]
        ) # The final value of the corner gives the RM shape for one energy group


    # Join rm for each group in one single matrix --------------
    responseMatrix_byGroup_shape = corner
    # print(responseMatrix_byGroup_shape)
    
    responseMatrix_byGroup = {}
    for g in range(energy_g):
        rm_g = np.zeros(responseMatrix_byGroup_shape) 
        for n_id in coarse_nodes.keys():
            corner_n = matrix_corners[n_id]
            resp_n_g = responseMatrix_byNode_byGroup[n_id][g]
            for r in range(resp_n_g.shape[0]):
                for c in range(resp_n_g.shape[1]):
                    rm_g[corner_n[0] + r][corner_n[1] + c] = resp_n_g[r][c]
            responseMatrix_byGroup[g] = rm_g
            # print(rm_g)
            # print()
    # print(responseMatrix_byGroup)
    return responseMatrix_byGroup, node_order

def getMatrixU_byGlobalNode(coarse_nodes, energy_g, probabilities):
    # We need matrix U for the source
    matrixU_byNode_byGroup = { }
    
    
    for n_id, node in coarse_nodes.items():
        matrixU_byNode_byGroup[n_id] = {}

        surfaces_n = node.surface_ids
        surface_areas_n = node.surface_areas
        regions = node.fine_nodes_ids
        regions_volume = node.fine_nodes_volume
        
        for g in range(energy_g):
            mat_u_n = build_U(
                probabilities[n_id],
                surfaces_n,
                surface_areas_n,
                regions,
                regions_volume,
                g,
            )
            # print(mat_u_n)
            matrixU_byNode_byGroup[n_id][g] = mat_u_n
            
    # print(matrixU_byNode_byGroup)
    return matrixU_byNode_byGroup

def getM_matrix(coarse_nodes, energy_g):
    
    matrix_M = {}

    numTotalSurfaces = 0
    for n_id, node in coarse_nodes.items():
        surfaces_n = node.surface_ids
        numTotalSurfaces += len(surfaces_n)

    matrix_M_len = numTotalSurfaces
    matrix_M = np.identity(matrix_M_len)
    
    print(matrix_M)
    return matrix_M

def build_S(xs, probabilities, surfaces, surface_areas, regions, regions_volume, g):
    numReg = len(regions)
    numSurf = len(surfaces)

    matrix_S_shape = (numReg, numSurf)
    mS = np.zeros(matrix_S_shape)

    cell_materials = ["fuel", "coolant"]

    for j in range(numReg):
        region_j_id = regions[j]
        vol_j = regions_volume[region_j_id]
        region_material_j = cell_materials[j]
        xsTotal_j = xs[region_j_id]["total"][g]
        for a in range(numSurf):
            s_id = surfaces[a]
            area_a = surface_areas[s_id]
            p_a_j = probabilities[s_id][region_material_j][g]
            mS[j][a] =  area_a * p_a_j / (xsTotal_j * vol_j)
    
            
    
    return mS

def build_R(probabilities, surfaces, surface_areas, g):
    """
        surfaces:   Array with the surfaces_ids of the corresponding coarse node, ex:
                    [3, 4, 5, 6]

        regions:    Array with the regions_ids of the corresponding coarse node, ex:
                    [1, 2, 3, 4]
    """
    numSurf = len(surfaces)

    responseMatrix_shape = (numSurf, numSurf)
    
    responseMatrix_n = np.zeros(responseMatrix_shape)

    for a in range(numSurf):
        surf_a_id = surfaces[a]
        area_a = surface_areas[surf_a_id]
        for b in range(numSurf):
            surf_b_id = surfaces[b]
            area_b = surface_areas[surf_b_id]
            p_b_a = probabilities[surf_b_id]["surfaces"][surf_a_id][g]
            responseMatrix_n[a][b] =  area_b * p_b_a / area_a

    return responseMatrix_n, responseMatrix_shape

def build_T(xs, probabilities, regions, regions_volume, g):
    numRegions = len(regions)
    matrix_T = np.zeros((numRegions, numRegions))

    cell_materials = ["fuel", "coolant"]

    for j in range(numRegions):
        region_j_id = regions[j]
        vol_j = regions_volume[region_j_id]
        material_region_j = cell_materials[j]
        xsTotal_j = xs[region_j_id]["total"][g]
        for i in range(numRegions):
            region_i_id = regions[i]
            vol_i = regions_volume[region_i_id]
            material_region_i = cell_materials[i]
            p_i_j = probabilities[material_region_i][material_region_j][g]
            matrix_T[j][i] =  vol_i * p_i_j / (xsTotal_j * vol_j)
    
    return matrix_T

def build_U(probabilities, surfaces, surface_areas, regions, regions_volume, g):
    """
        surfaces:   Array with the surfaces_ids of the corresponding coarse node, ex:
                    [3, 4, 5, 6]

        regions:    Array with the regions_ids of the corresponding coarse node, ex:
                    [1, 2, 3, 4]
    """
    numReg = len(regions)
    numSurf = len(surfaces)
    
    matrix_U_shape = (numSurf, numReg)
    matrix_U_n = np.zeros(matrix_U_shape)


    cell_materials = ["fuel", "coolant"]

    for a in range(numSurf):
        surf_id = surfaces[a]
        area_a = surface_areas[surf_id]
        for i in range(numReg):
            region_id = regions[i]
            region_name = cell_materials[i]
            vol_i = regions_volume[region_id]
            p_i_a = probabilities[region_name]["surfaces"][surf_id][g]
            matrix_U_n[a][i] =  vol_i * p_i_a / area_a


    return matrix_U_n





def buildJsource(matrixU, source, energy_g):
    j_source = {}
    print(matrixU)
    
    for g in range(energy_g):
        system_vector = np.array([])
        for n_id, values in matrixU.items():
            q_vector = source[n_id][g]
            
            j_s = np.matmul(matrixU[n_id][g], q_vector)
            system_vector = np.concatenate((system_vector, j_s), axis=0)
        #     print(system_vector)
        # print()
        j_source[g] = system_vector
            
    return j_source


def buildPhiSource(matrixT, source, energy_g):
    phi_source = {}
    
    for g in range(energy_g):
        phi_source[g] = {}
        for n_id, values in matrixT.items():
            q_vector = source[n_id][g]
            matrixSource =  matrixT[n_id][g] * q_vector
            vector_ = []
            for row in matrixSource:
                sum_ = np.sum(row)
                vector_.append(sum_)
            phi_source[g][n_id] = np.array(vector_)
        
    return phi_source