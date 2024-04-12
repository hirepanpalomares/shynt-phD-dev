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

  def __init__(self, histories, active, unactive, seed=0):
    self.__histories = histories
    self.__active_cycles = active
    self.__unactive_cycles = unactive
    self.__seed = seed
  
  def serpent_syntax(self, type_of_calculation, c_id='', src_name='', gcut=1):
    serpent_syntax = ''
    if type_of_calculation == 'criticality':
      serpent_syntax += f"set pop {self.__histories} {self.__active_cycles} "
      serpent_syntax += f"{self.__unactive_cycles}\n"
      if self.__seed:
        serpent_syntax += f"set seed {self.__seed}\n"
    elif type_of_calculation == 'source':
      serpent_syntax += f'src {src_name}\n'
      serpent_syntax += f'sc {c_id}\n'
      serpent_syntax += f'sb 8 0\n'
      serpent_syntax += f'7.49000000E-04 0\n'
      serpent_syntax += f'1.50000000E-02 5\n'
      serpent_syntax += f'4.09000000E-02 5\n'
      serpent_syntax += f'1.11000000E-01 5\n'
      serpent_syntax += f'3.02000000E-01 5\n'
      serpent_syntax += f'8.21000000E-01 5\n'
      serpent_syntax += f'2.23000000E+00 5\n'
      serpent_syntax += f'2.00000000E+01 5\n\n'
      batches = self.__active_cycles 
      total_npop = self.__histories * batches
      serpent_syntax += f'set nps {total_npop} {batches}\n'
      serpent_syntax += f'set gcut {gcut}\n'

    return serpent_syntax


  @property
  def serp_dir_name(self):
    serp_dir = f'serpent_files_{self.histories}_{self.active_cycles}_'
    serp_dir += f'{self.unactive_cycles}'
    return serp_dir
  
  @property
  def dir_name(self):
    serp_dir = f'{self.histories}_{self.active_cycles}_'
    serp_dir += f'{self.unactive_cycles}'
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
    
