from Shynt.api_py.Geometry.cells import Cell


class GlobalMesh():

  def __init__(self, cell: Cell) -> None:
    super().__init__()
    self.__cell = cell
    self.coarse_nodes_map = []
    self.surace_twins = {}
    self.coarse_nodes = {}

  @property
  def cell(self) -> Cell:
    return self.__cell