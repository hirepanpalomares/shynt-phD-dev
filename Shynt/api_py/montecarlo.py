class MontecarloParams:
  """
  A class to represent the Montecarlo parameters that will be used
  in the serpent calculation

  ...

  Attributes
  ----------
  histories : int
    number of particle histories to be used in the serpent
    calculation
  active : int
    number of active cycles for the montecarlo calculation
  unactive : int
    number of unactive cycles for the montecarlo 
    calculation
  seed : int
    seed of the random number generator for the montecarlo
    calculation

  Methods
  -------

  """

  def __init__(self, histories, active, unactive, seed=0, set_ures=False, set_bc=1):
    self.__histories = histories
    self.__active_cycles = active
    self.__unactive_cycles = unactive
    self.__seed = seed
    self.__set_ures = set_ures
    self.set_bc = set_bc
    self.src_calc = False
    self.no_void = False
  
  def serpent_syntax_criticality(self):
    serpent_syntax = ''
    serpent_syntax += f"set bc {self.set_bc} \n"
    serpent_syntax += f"set pop {self.__histories} "
    serpent_syntax += f"{self.__active_cycles} "
    serpent_syntax += f"{self.__unactive_cycles}\n"
    if self.__set_ures:
      serpent_syntax += "set ures 1 \n\n"
    if self.__seed:
      serpent_syntax += f"set seed {self.__seed}\n"
   
    return serpent_syntax

  def serpent_syntax_src_calc(self, energy, src_name, c_id, gcut=10):
    serpent_syntax = f'src {src_name}\n'
    serpent_syntax += f'sc {c_id}\n'
    num_energy = energy.energy_groups

    serpent_syntax += f'sb {num_energy+1} 0\n'

    serpent_syntax += f'{energy.energy_mesh[0]} 0\n' # first energy cut
    weight = 5 # Random number until now
    for energy_upper_lim in energy.energy_mesh[1:]:
      serpent_syntax += f'{energy_upper_lim} {weight}\n'
    serpent_syntax += '\n'

    batches = self.__active_cycles 
    total_npop = self.__histories * batches
    serpent_syntax += f'set nps {total_npop} {batches}\n'
    serpent_syntax += f'set gcut {gcut}\n'
    serpent_syntax += f"set bc {self.set_bc} \n"

    if self.__set_ures:
      serpent_syntax += "set ures 1 \n\n"


    return serpent_syntax

  @property
  def serp_dir_name(self):
    serp_dir = f'serpent_files_{self.histories}_{self.active_cycles}_'
    serp_dir += f'{self.unactive_cycles}_bc_{self.set_bc}'
    return serp_dir
  
  @property
  def dir_name(self):
    serp_dir = f'{self.histories}_{self.active_cycles}_'
    serp_dir += f'{self.unactive_cycles}'
    if self.__set_ures:
      serp_dir += '_ures1'
    if self.src_calc:
      serp_dir += '_src'
    if self.no_void:
      serp_dir += '_novoid'
    serp_dir += f'_bc{self.set_bc}'
    return serp_dir
  
  @property
  def histories(self):
    return self.__histories
  
  @property
  def active_cycles(self):
    return self.__active_cycles
  
  @property
  def unactive_cycles(self):
    return self.__unactive_cycles
  
  @histories.setter
  def histories(self, value):
    self.__histories = value
  
  @active_cycles.setter
  def active_cycles(self, value):
    self.__active_cycles = value
  
  @unactive_cycles.setter
  def unactive_cycles(self, value):
    self.__unactive_cycles = value
    
