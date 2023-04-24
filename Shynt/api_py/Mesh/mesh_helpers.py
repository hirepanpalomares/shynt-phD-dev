from Shynt.api_py.Mesh.global_mesh import PinCellMesh, SquareMesh
from Shynt.api_py.Mesh.local_mesh import MaterialMesh, CellMesh, PieMesh

from Shynt.api_py.Geometry.cells import Cell


def make_mesh(cell, global_mesh_type="", local_mesh_type="") -> Cell:
  """
  Helper method to construct the global and local meshes

  Probabbly the right way to get the GLOBAL MESH  and LOCAL MESH 
  is the following:
      1. Build the coarse nodes by getting the coordinates of the surfaces,
          being these circles, rectangles, squares or triangles, etc, etc.
      2. Now that you have the coordinates of all of these nodes we make for 
          each of these refine the space (pin, region etc) i.e. local mesh
      3. Once you refine (local meshes) of every corse node, determine which 
          are different to be able to compute the probabilities in serpent

  """
  global_mesh = None
  local_mesh = None

  if global_mesh_type == "pin_cell":    
    global_mesh = PinCellMesh(cell)
  elif global_mesh_type == "square_mesh_pin":
    global_mesh = SquareMesh(cell)

  if local_mesh_type == "material":
    local_mesh = MaterialMesh(global_mesh.coarse_nodes, local_mesh_type)
  elif local_mesh_type == "cell":
    local_mesh = CellMesh(global_mesh.coarse_nodes, local_mesh_type)
  elif local_mesh_type == "pie":
    local_mesh = PieMesh(global_mesh.coarse_nodes, local_mesh_type)
    
  cell.global_mesh = global_mesh
  cell.local_mesh = local_mesh

  
  return cell