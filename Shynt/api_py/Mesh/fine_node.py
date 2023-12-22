class FineNode():

    def __init__(self, cell) -> None:
        self.__cell = cell
        self.from_coarse_node = None
    
    @property
    def cell(self):
        return self.__cell