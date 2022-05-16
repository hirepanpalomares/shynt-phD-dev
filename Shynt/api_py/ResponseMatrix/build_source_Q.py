from os import system
from matplotlib.pyplot import axis
import numpy as np

from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix


class SourceQ:


    def __init__(self, coarse_nodes, coarse_nodes_regions, energy_g, xs) -> None:
        self.__coarseNodes = coarse_nodes
        self.__coarseNodesRegions = coarse_nodes_regions
        
        self.__energyG = energy_g
        self.__xs = xs

        self.__fissionMatrix = self.__buildFissionMatrix() 
        self.__scatteringMatrix = self.__buildScatteringMatrix()
        
        self.__fissionSource = [] # for the power iteration formula
        self.__scatteringSource = {}
        
        


    def __buildFissionMatrix(self):
        """
            returns the fission matrix by node and by region in the node
        """
        fission = {}
        # print("chi: ", self.__xs[1][1]["chi"])
        # print("fiss: ", self.__xs[1][1]["nuSigFission"])
        # print("fission  ")
        for n_id in self.__coarseNodes:
            regions = self.__coarseNodesRegions[n_id]
            for r in regions:
                fission[r] = np.zeros((self.__energyG, self.__energyG))
                nuFiss_xs = self.__xs[r]["nuSigFission"]
                chi_xs = self.__xs[r]["chi"]
                for g in range(self.__energyG):
                    chi_g = chi_xs[g]
                    for gp in range(self.__energyG):
                        fission[r][g][gp] = chi_g * nuFiss_xs[gp]
        return fission
    

    def __buildScatteringMatrix(self):
        scattering = {}
        for n_id in self.__coarseNodes:
            regions = self.__coarseNodesRegions[n_id]
            for r in regions:
                scattMatrix = self.__xs[r]["scatter"]
                scattering[r] = scattMatrix
        return scattering


    def buildFissionSource(self, mesh_info, probabilities):
        """
            for the power iteration formula
            
            block matrix
        """
        coarse_nodes_order = mesh_info.coarse_order
        coarse_nodes_regions = mesh_info.coarse_region_rel
        all_regions = mesh_info.all_regions_order
        regions_vol = mesh_info.all_regions_vol


        array_of_matrixes = []
        for n_id in coarse_nodes_order:
            regions = coarse_nodes_regions[n_id]
            numRegions = len(regions)
            mF = np.zeros((numRegions*self.__energyG,numRegions*self.__energyG))
            for j in range(numRegions):
                reg_j = regions[j]
                vol_j = regions_vol[reg_j]
                for g in range(self.__energyG):
                    row_matrix = np.array([])
                    for i in range(numRegions):
                        reg_i = regions[i]
                        vol_i = regions_vol[reg_i]
                        prob = probabilities["regions"][reg_i]["regions"][reg_j][g]
                        array = self.__fissionMatrix[reg_i][g] * vol_i * prob
                        row_matrix = np.concatenate((row_matrix, array), axis=0)
                    index_mF_row = numRegions * j + g
                    mF[index_mF_row] = row_matrix
            array_of_matrixes.append(mF)
        
        big_fission_matrix = getBlockMatrix(array_of_matrixes)
        return big_fission_matrix
    
    
    def buildScatteringSource(self, flux):
        return 1


    def calculate_Qvector(self, keff, flux, total_regions):
        """
            It returns a dictionary with the source terms in it:

            sourceQ_byNode_byEnergy = {
                coarseNode_id: {
                    g_0: array([q_region_1_g0, q_region_2_g0, ..., q_region_I_g0]),
                    g_1: array([q_region_1_g1, q_region_2_g0, ..., q_region_I_g0]),
                    ...
                    ...
                    g_G:
                }
            }
        """

        # change order of fluxes
        numRegions = len(total_regions)
        flux_r_g = {
            total_regions[r]: [flux[g][r] for g in range(self.__energyG)] for r in range(numRegions)
        }
        
        _Q = {}
        for g in range(self.__energyG):
            _Q[g] = np.zeros(numRegions)

            for r in range(numRegions):
                r_id = total_regions[r]
                phi = flux_r_g[r_id]

                scatt_matrix = self.__scatteringMatrix[r_id].T
                fiss_matrix = self.__fissionMatrix[r_id]
                scattering_value = np.dot(scatt_matrix[g], phi)
                fission_value = np.dot(fiss_matrix[g], phi) / keff
                _Q[g][r] = scattering_value + fission_value   # / (4 * np.pi)       
                db = True      
        
        return _Q


    @property
    def fissionMatrix(self):
        return self.__fissionMatrix

    @property
    def scatteringMatrix(self):
        return self.__scatteringMatrix