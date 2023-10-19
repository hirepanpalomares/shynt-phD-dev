
class SerpentLibraries:

  """
  A class to store the libraries to be used in the serpent
  calculations

  ...

  Attributes
  ----------
  acelib : str

  thermal_scattering_data : str
  

  Methods
  -------

  """


  def __init__(self, acelib="", therm=""):
    self.__acelib = acelib
    self.__thermal_scattering_data = therm
    
  @property
  def serpent_syntax(self):
    return f"\nset acelib {self.__acelib} \n{self.__thermal_scattering_data}"
  
  @property
  def acelib(self):
    return self.__acelib
  
  @property
  def thermal_scattering_data(self):
    return self.__thermal_scattering_data
    

