import numpy as np

from Shynt.api_py.ResponseMatrix.matrix_utilities import getBlockMatrix


class SourceQ:
  """
  Class to represent the source of the system (fission and scattering)
  .......

  Attributes
  ----------
  __coarseNodes : dict
    Dictionary with the coarse nodes of the system
      key: node_id,
      value: CoarseNode
  __coarseNodes_regions : dict
    Dictionary with the regions of every coarse node, 
      key: node_id
      value: array with regions [...]
  __energyG : int
    Number of energy groups
  __xs : dict
    Dictionary with the cross sections values
      key: region_id
      value: dict with cross sections "fission", "total", etc
  __fissionMatrix : np.array()

  __scatteringMatrix : np.array()

  __fissionSource : np.array()

  __scatteringSource : dict


  Methods
  -------
  __buildFissionMatrix()

  __buildScatteringMatrix()

  buildFissionSource()

  buildScatteringSource()

  __orderFlux()

  calculateQvector()

  """

  def __init__(self, mesh, energy_g, xs) -> None:
    """
    Parameters
    ----------
    coarse_nodes : dict
      The coarse nodes of the system
    coarse_nodes_regiosn : dict
      The regions of every coarse node
    energy_g : int
      Number of energy groups
    xs : dict
      Cross sections of every region
    """
    self.__coarseNodes = mesh.coarse_mesh.coarse_nodes
    self.__energyG = energy_g
    self.__xs = xs

    self.__fissionMatrix = self.__buildFissionMatrix() 
    self.__scatteringMatrix = self.__buildScatteringMatrix()
    self.__fissionSource = [] # for the power iteration formula
    self.__scatteringSource = {}
      
  def __buildFissionMatrix(self):
    """
    Builds the fission matrix by region
    The fission matrix is expressed as follows:
    
    [
      [nuFiss_1*Chi_1, nuFiss_2*Chi_1, ..., nuFiss_G*Chi_1],
      [nuFiss_1*Chi_2, nuFiss_2*Chi_2, ..., nuFiss_G*Chi_2],
      [      :       ,        :      , ...,        :      ],
      [nuFiss_1*Chi_G, nuFiss_2*Chi_G, ..., nuFiss_G*Chi_G],
    ]

    Parameters
    ----------

    Returns
    -------
    fission : dict
      Fission matrixes of every region
    """
    fission = {}
   
    for n_id in self.__coarseNodes:
      regions = self.__coarseNodes[n_id].fine_mesh.regions
      for r in regions.keys():
        fission[r] = np.zeros((self.__energyG, self.__energyG))
        nuFiss_xs = self.__xs[r]["nuSigFission"]
        chi_xs = self.__xs[r]["chi"]
        for g in range(self.__energyG):
          chi_g = chi_xs[g]
          for gp in range(self.__energyG):
            fission[r][g][gp] = chi_g * nuFiss_xs[gp]
    return fission
  
  def __buildScatteringMatrix(self):
    """
    Builds the scattering matrix by region
    The fission matrix is expressed as follows:
    
    [
      [Scatt_1->1, Scatt_2->1, ..., Scatt_G->1],
      [Scatt_1->2, Scatt_2->2, ..., Scatt_G->2],
      [    :    ,     :    , ...,     :    ],
      [Scatt_1->G, Scatt_2->G, ..., Scatt_G->G],
    ]

    Parameters
    ----------

    Returns
    -------
    scattering : dict
      Scattering matrixes of every region


    """

    scattering = {}
    for n_id in self.__coarseNodes:
      regions = self.__coarseNodes[n_id].fine_mesh.regions
      for r in regions.keys():
        scattMatrix = self.__xs[r]["scatter"]
        scattering[r] = scattMatrix
    return scattering

  def __orderFlux(self, flux, total_regions):
    numRegions = len(total_regions)

    r_counter = 0
    g_counter = 0
    new_flux = {} # keys: g
    f_vector = np.zeros(numRegions)
    for val_ in flux:
      f_vector[r_counter] = val_
      r_counter += 1
      if r_counter == numRegions:
        r_counter = 0
        new_flux[g_counter] = f_vector
        g_counter += 1
        f_vector = np.zeros(numRegions)
    return new_flux

  def buildFissionSource(self, 
    mesh, probabilities
  ):
    """
    Method to build the Fission Source that is used to calculate the keff in
    the power iteration method. The fission source is a big block matrix where
    every block corresponds to the fission neutrons emission rate from the 
    regions inside the node.

    Each block has the following elements:

    f_{j,i,g,g'} = P_{j,i,g}*V_{j}*Chi_{j,g} * nuFiss_{j,g'} 

    mF = [
    [f_{j1,i1,g1,g1'} .. f_{j1,i1,g1,G'} .. f_{J,i1,g1,g1'} .. f_{J,i1,g1,G'}],
               :                   :                 :                  :
    [f_{j1,i1, G,g1'} .. f_{j1,i1, G,G'} .. f_{J,i1, G,g1'} .. f_{J,i1, G,G'}],
            :                   :                 :                  :
    [f_{j1, I, g1,g1'} .. f_{j1,I,g1,G'} .. f_{J, I,g1,g1'} .. f_{J, I,g1,G'}],
                :                  :                 :                  :
    [f_{j1, I,  G,g1'} .. f_{j1,I, G,G'} .. f_{J, I, G,g1'} .. f_{J, I, G,G'} ]
    ]


    Parameters
    ----------
    corse_nodes_ids : list

    coarse_nodes_regions : dict
      Dictionary of regions by corse node id
    regions_vol : dict
      Dictionary of region volumes
    probabilities : dict
      Dictionary of probabilities

    Returns
    -------
    big_fission_matrix : np.array()

    """

    coarse_nodes_ids = mesh.coarse_order
    regions_vol = mesh.all_regions_vol
    array_of_matrixes = []
    for n_id in coarse_nodes_ids:
      regions = list(self.__coarseNodes[n_id].fine_mesh.regions.keys())
      numRegions = len(regions)
      mF = np.zeros((numRegions*self.__energyG,numRegions*self.__energyG))
      for i in range(numRegions): 
        # "i" is  the region where the neutrons will go after fission 
        reg_i = regions[i]
        for g in range(self.__energyG): 
          # For each energy group in the region "i"
          row_matrix = np.array([]) # row of the block
          for j in range(numRegions): 
            # Region "j" is from the region the neutrons were emmited
            # Loop to concatenate the vector of the block
            reg_j = regions[j]
            vol_j = regions_vol[reg_j]
            prob = probabilities["regions"][reg_j]["regions"][reg_i][g]
            array = self.__fissionMatrix[reg_j][g] * vol_j * prob
            row_matrix = np.concatenate((row_matrix, array), axis=0)
          index_mF_row = i * self.__energyG  + g
          mF[index_mF_row] = row_matrix
      array_of_matrixes.append(mF)
    big_fission_matrix = getBlockMatrix(array_of_matrixes)
    return big_fission_matrix
  
  def calculate_Qvector(self, 
    keff, flux, total_regions, numRegions, fluxOrdered_bg=False
  ):
    """
    Method to calculate the source vectors for the Response matrix method
    
    _Q = { 
      g_0: array([q_i1_g0, q_i2_g0, ..., q_iI_g0]),
      g_1: array([q_i1_g1, q_i2_g1, ..., q_iI_g1]),
       :
      g_G: array([q_i1_gG, q_i2_gG, ..., q_iI_gG]),
    }

    Parameters
    ----------
    keff : float
      Neutron multiplication factor
    flux : dict
      Neutron scalar flux
    total_regions : np.array() 
      Regions of the system
    numRegions : int
      Number of regions in the system
    fluxOrdered_bg : bool, optional
      Variable to tell if the flux is ordered in a dictionary by energy group

    Returns
    -------
    _Q : dict
      Source vectors, with energy groups as keys

    """
    from math import pi
    
    if not fluxOrdered_bg:
      flux = self.__orderFlux(flux, total_regions)

    _Q = {g : np.zeros(numRegions) for g in range(self.__energyG)}

    for g in range(self.__energyG):
      for r in range(numRegions):
        r_id = total_regions[r]

        scatt_matrix = self.__scatteringMatrix[r_id]
        fiss_matrix = self.__fissionMatrix[r_id]

        scatt_term = 0.0
        fission_term = 0.0
        for gp in range(self.__energyG):
          # scattering --------------------
          scatt_term += scatt_matrix[g][gp] * flux[gp][r] 
          # fission -----------------------
          fission_term += fiss_matrix[g][gp] * flux[gp][r]

        _Q[g][r] = scatt_term + fission_term / keff
        _Q[g][r] = _Q[g][r] # / (pi*4)
    return _Q

  def build_big_scatt_matrix(self, mesh):
    numRegions = mesh.numRegions

    big_scatt = np.zeros((
      numRegions*self.__energyG, numRegions*self.__energyG
    ))
  
    regions = mesh.all_regions_order
  
    for r, r_id in enumerate(regions):
      
      scatt_matrix = self.__scatteringMatrix[r_id]
      for g in range(self.__energyG):
        col_index = g*numRegions + r
        for gp in range(self.__energyG):
          row_index = gp*numRegions + r
          big_scatt[row_index][col_index] = scatt_matrix[g][gp]
        
    return big_scatt
  
  def build_big_scatt_matrix_blocks(self, mesh):

    
    coarse_nodes = mesh.coarse_order
    coarse_nodes_regions = mesh.coarse_region_rel
   

    matrixes_Z_system = []
    for n_id in coarse_nodes:
      regions = coarse_nodes_regions[n_id]
      numRegions = len(regions)
      mZ_n_shape = (numRegions*self.__energyG, numRegions*self.__energyG)
      mZ_n = np.zeros(mZ_n_shape)
      for r, r_id in enumerate(regions):
        scatt_matrix = self.__scatteringMatrix[r_id]
        for g in range(self.__energyG):
          col_index = g*numRegions + r
          for gp in range(self.__energyG):
            row_index = gp*numRegions + r
            mZ_n[row_index][col_index] = scatt_matrix[g][gp]
      
      matrixes_Z_system.append(mZ_n)

    big_scatt = getBlockMatrix(matrixes_Z_system)
    return big_scatt
  
  def build_big_fission_matrix(self, mesh):
    numRegions = mesh.numRegions

    big_fiss = np.zeros((
      numRegions*self.__energyG, numRegions*self.__energyG
    ))

    regions = mesh.all_regions_order
    for r, r_id in enumerate(regions):
      
      fission_matrix = self.__fissionMatrix[r_id]
      for g in range(self.__energyG):
        col_index = g*numRegions + r
        for gp in range(self.__energyG):
          row_index = gp*numRegions + r
          big_fiss[row_index][col_index] = fission_matrix[g][gp]
        
    return big_fiss

  def build_big_fission_matrix_blocks(self, mesh):
    coarse_nodes = mesh.coarse_order
    coarse_nodes_regions = mesh.coarse_region_rel
   
    matrixes_F_system = []
    for n_id in coarse_nodes:
      regions = coarse_nodes_regions[n_id]
      numRegions = len(regions)
      mF_n_shape = (numRegions*self.__energyG, numRegions*self.__energyG)
      mF_n = np.zeros(mF_n_shape)

      for r, r_id in enumerate(regions):
        fission_matrix = self.__fissionMatrix[r_id]
        for g in range(self.__energyG):
          col_index = g*numRegions + r
          for gp in range(self.__energyG):
            row_index = gp*numRegions + r
            mF_n[row_index][col_index] = fission_matrix[g][gp]
          
      matrixes_F_system.append(mF_n)
    
    big_fiss = getBlockMatrix(matrixes_F_system)
    return big_fiss
  

  @property
  def fissionMatrix(self):
    return self.__fissionMatrix

  @property
  def scatteringMatrix(self):
    return self.__scatteringMatrix
