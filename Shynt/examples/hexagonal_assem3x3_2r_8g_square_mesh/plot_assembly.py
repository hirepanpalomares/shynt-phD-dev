import hex_assem3x3
from Shynt.api_py.Drawer.cell_drawing import PlotAssembly


assem = hex_assem3x3.assembly_cell
rectangles =  hex_assem3x3.root_universe.mesh.coarse_mesh.rectangles

PlotAssembly(
  hex_assem3x3.assembly_cell, 
  dimensions=(300,300), 
  name="hex_assem_fig"
)


print(rectangles)
# name="hex_assem_global_mesh", 
# name="hex_assem_3x3_mesh", 
# rectangles=rectangles,
# rectangles=[]


