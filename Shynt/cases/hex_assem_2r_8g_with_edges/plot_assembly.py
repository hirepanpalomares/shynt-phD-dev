import hex_assem
from Shynt.api_py.Drawer.cell_drawing import plot_cell


assem = hex_assem.assembly_cell_meshed

plot_cell(
  assem, 
  dimensions=(2000,2000), 
  name="hex_assem_global_mesh", 
  rectangles=assem.global_mesh.points_mesh
)


