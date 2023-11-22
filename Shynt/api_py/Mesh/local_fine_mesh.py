
class FineMesh():
  """Class that represents the fine mesh inside a coarse node.

  Attributes
  ----------
  regions : dict

  Methods
  -------
  
  
  """
  def __init__(self, coarse_node):
    super().__init__()
    self.__coarse_node = coarse_node


  @property
  def coarse_node(self):
    return self.__coarse_node