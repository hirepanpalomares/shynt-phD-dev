import hex_assem3x3
from Shynt.api_py.Drawer.cell_drawing import plot_cell


assem = hex_assem3x3.assembly_cell_meshed
rectangles = assem.global_mesh.points_mesh
rectangles = []

plot_cell(
  assem, 
  dimensions=(3000,3000), 
  # name="hex_assem_global_mesh", 
  name="hex_assem", 
  rectangles=rectangles
)


