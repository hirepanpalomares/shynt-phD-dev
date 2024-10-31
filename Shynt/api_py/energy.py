class Grid:
  """
  A class to store the energy mesh to be used in the Response
  Matrix Calculations and the serpent simulations to calculate 
  the collision probabilities

  ...

  Attributes
  ----------
  energy_mesh : list

  groups : int
    Number of energy groups
  
  name : str

  bins_names_relation : dict

  bins : dict

  Methods
  -------
  __grid_bins()

  serpent_syntax()

  serpent_syntax_by_bins()

  """

  def __init__(self, energy_mesh, name=""):
    self.__energy_mesh = energy_mesh
    self.__groups = len(energy_mesh) - 1
    self.__name = name
    self.__bins_names_relation, self.__bins = self.__grid_bins()
      

  def __grid_bins(self):
    bins_names_relation = {}
    bins = {}
    for g in range(self.__groups):
        bin_name = f"{self.__name}_{g}"
        bin_ = (self.__energy_mesh[g], self.__energy_mesh[g+1])
        bins_names_relation[g] = bin_name
        bins[g] = bin_
    return bins_names_relation, bins

  def serpent_syntax(self):
    """
        
    """
    syntax = f"ene {self.__name} 1 \n"

    for ener in self.__energy_mesh:
        syntax += f"{format(ener, '.8E')} \n"
    syntax += "\n"
    
    return syntax
  
  def serpent_syntax_by_bins(self):
    """
        
    """
    syntax = ""
    for g, b_name in self.__bins_names_relation.items():
        syntax += f"ene {b_name} 1 {format(self.__bins[g][0], '.8E')} {format(self.__bins[g][1], '.8E')}\n"

    
    return syntax    
  
  
  @property
  def name(self):
    return self.__name

  @property
  def energy_mesh(self):
    return self.__energy_mesh

  @property
  def energy_groups(self):
    return self.__groups
  
  @property
  def bins_names_relation(self):
    return self.__bins_names_relation
  
  @property
  def bins(self):
    return self.__bins