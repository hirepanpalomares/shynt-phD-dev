from Shynt.api_py.Geometry.cells import Cell


class CoarseMesh():

  def __init__(self, cell: Cell) -> None:
    super().__init__()
    self.__cell = cell
  
  def calculate_surfaces_twins(self):
    """Class method to extract the surface twins of every node. It sweeps all
    surfaces and then call the method  find_surface_twin()

    Returns
    -------
    surface_twins : dict

    """

    num_coarse_nodes = len(self.coarse_nodes)
    print(f"Calculating surface twins for {num_coarse_nodes} coarse_nodes ...")

    surf_checked = {s_idx: False for s_idx in range(1,self.num_surfaces+2)}
    surface_twins = {s_idx: None for s_idx in range(1,self.num_surfaces+2)}
    for n_id, coarse_node in self.coarse_nodes.items():
      print(n_id, end=",")
      if n_id % 20 == 0: print()
      
      node_surfs = coarse_node.surfaces
      for s_id, points in node_surfs.items():
        if surf_checked[s_id]: continue
        twin = self.__find_surface_twin(n_id, points, s_id)
        # if n_id == 7: print(s_id, twin)
        if twin:
          surface_twins[s_id] = twin
          surface_twins[twin] = s_id
          surf_checked[twin] = True
          surf_checked[s_id] = True
    
    self.surface_twins = surface_twins
  
  def __find_surface_twin(self, n_id, points, s_id):
    """Class method to find the surface twin of one surface. It sweeps all the
    surfaces and compare the points  in order to determine wether is a twin or
    not.
    
    Parameters
    ----------
    n_id : int

    points : tuple

    rings : list

    Returns
    -------
    surf_twin : int or None
    """
    p1, p2 = points
    p1 = (round(p1[0], 10), round(p1[1], 10))
    p2 = (round(p2[0], 10), round(p2[1], 10))

    p1x, p1y = p1
    p2x, p2y = p2

    # if n_id <= 6: print("surf: ", s_id, p1,p2, "searching -----------")
    surf_twin = None

    # print(rings)
    
    for other_n_id, coarse_node in self.coarse_nodes.items():
      if n_id == other_n_id: continue      
      node_surfs = coarse_node.surfaces
      for s_id_other, points_other in node_surfs.items():
        p1_other, p2_other = points_other
        p1_other = (round(p1_other[0], 10), round(p1_other[1], 10))
        p2_other = (round(p2_other[0], 10), round(p2_other[1], 10)) 

        p1x_o, p1y_o = p1_other
        p2x_o, p2y_o = p2_other
        
        if p1x == p1x_o and p1y == p1y_o and p2x == p2x_o and p2y == p2y_o:
          return s_id_other
        
        if p1x == p2x_o and p1y == p2y_o and p2x == p1x_o and p2y == p1y_o:
          return s_id_other


  @property
  def cell(self) -> Cell:
    return self.__cell