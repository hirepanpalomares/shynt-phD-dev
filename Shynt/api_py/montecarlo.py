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

  def __init__(self, histories, active, unactive, seed=None):
    self.__histories = histories
    self.__active_cycles = active
    self.__unactive_cycles = unactive
    self.__seed = seed
   
  @property
  def serpent_syntax(self):
    serpent_syntax = f"set pop {self.__histories} {self.__active_cycles} {self.__unactive_cycles}\n"
    if self.__seed:
      serpent_syntax += f"set seed {self.__seed}\n"
    return serpent_syntax
  
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
    
