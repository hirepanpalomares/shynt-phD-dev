from Shynt.api_py.Geometry.cells import Cell


class CoarseMesh():

  def __init__(self, cell: Cell) -> None:
    super().__init__()
    self.__cell = cell

  @property
  def cell(self) -> Cell:
    return self.__cell