import numpy as np


class SourceQ:


    def __init__(self, coarse_nodes, energy_g, xs) -> None:
        self.__coarseNodes = coarse_nodes
        self.__energyG = energy_g
        self.__xs = xs

        self.__fissionMatrix = self.__buildFissionMatrix() 
        self.__scatteringMatrix = self.__buildScatteringMatrix()
        


    def __buildFissionMatrix(self):
        """
            returns the fission matrix by node and by region in the node
        """
        fission = {}
        # print("chi: ", self.__xs[1][1]["chi"])
        # print("fiss: ", self.__xs[1][1]["nuSigFission"])
        # print("fission  ")
        for n_id, node in self.__coarseNodes.items():
            regions = node.fine_nodes_ids
            fission[n_id] = {}
            for r in regions:
                fission[n_id][r] = np.zeros((self.__energyG, self.__energyG))
                nuFiss_xs = self.__xs[n_id][r]["nuSigFission"]
                chi_xs = self.__xs[n_id][r]["chi"]
                for g in range(self.__energyG):
                    chi_g = chi_xs[g]
                    for gp in range(self.__energyG):
                        fission[n_id][r][g][gp] = chi_g * nuFiss_xs[gp]
        return fission
    

    def __buildScatteringMatrix(self):
        scattering = {}
        for n_id, node in self.__coarseNodes.items():
            regions = node.fine_nodes_ids
            scattering[n_id] = {}
            for r in regions:
                scattMatrix = self.__xs[n_id][r]["scatter"]
                scattering[n_id][r] = scattMatrix
        print("scatter matrix ", scattering)
        return scattering


    def buildFissionSource(self, phi):
        # print("building fission source ....")
        fission_source = {}
        for n_id, node in self.__coarseNodes.items():
            fission_source[n_id] = {}
            regions = node.fine_nodes_ids
            numRegions = len(regions)
            for r in range(numRegions):
                region_id = regions[r]
                fission_source[n_id][region_id] = {}
                fission_matrix = self.__fissionMatrix[n_id][region_id]
                for g in range(self.__energyG):
                    
                    fiss_row = fission_matrix[g]
                    for gp in range(self.__energyG):
                        phi_val = phi[n_id][region_id][gp]
                        fiss_row[gp] *= phi_val
                    
                    fission_source[n_id][region_id][g] = np.sum(fiss_row) 
        

        # Filling total vector

        fission_source_vector_total = []
        for g in range(self.__energyG):
            for n_id, node in self.__coarseNodes.items():
                regions = node.fine_nodes_ids
                numRegions = len(regions)
                for r in range(numRegions):
                    region_id = regions[r]
                    fission_source_vector_total.append(fission_source[n_id][region_id][g])


        return np.array(fission_source_vector_total)
    
    def buildScatteringSource(self, phi):
    
        pass


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
                    sum_gp = 0.0
                    for gp in range(self.__energyG):
                        scatt_term = self.__scatteringMatrix[n_id][region_id][g][gp] * flux[n_id][region_id][gp]
                        fiss_term = self.__fissionMatrix[n_id][region_id][g][gp] * flux[n_id][region_id][gp] / keff
                        sum_gp += scatt_term + fiss_term
                    _Q[n_id][g][r] = sum_gp / (4 * np.pi)
                
        
        return _Q
    
    def calculateTotalSourceVector(self, keff, flux):
        source_Q = self.calculate_Qvector(keff, flux)
        
        print(source_Q)
        # Joining vectors
        total_source = np.array([])
        for g in range(self.__energyG):
            for n_id, node in self.__coarseNodes.items():
                total_source = np.concatenate((total_source, source_Q[n_id][g]), axis=0)
        print(total_source)
        return total_source


