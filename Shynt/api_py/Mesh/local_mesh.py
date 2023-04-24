from Shynt.api_py.Geometry.surfaces import CylinderPad, PlaneX, PlaneY, InfiniteCylinderZ
from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderYtype
from Shynt.api_py.Geometry.surfaces import InfiniteRectangleCylinderZ

from Shynt.api_py.Geometry.regions import SurfaceSide

from Shynt.api_py.Geometry.universes import Universe

from Shynt.api_py.Geometry.cells import Cell

from Shynt.api_py.materials import Material

from Shynt.api_py.Mesh.fine_node import FineNode


class FineMesh(object):

    def __init__(self, coarse_nodes, local_mesh_type):
      self.type = local_mesh_type
      self.coarse_nodes = coarse_nodes

    # @property
    # def coarse_nodes(self):
    #   return self.coarse_nodes
    

    

class MaterialMesh(FineMesh):
    
  def __init__(self, coarse_nodes, local_mesh_type):
    super().__init__(coarse_nodes, local_mesh_type)
    self.fine_nodes = self.generate_fine_nodes()
  
  def generate_fine_nodes(self):
    fine_nodes = {}
    for n_id, coarse_node in self.coarse_nodes.items():
      nodes = self.get_material_nodes(coarse_node)
      fine_nodes[n_id] = nodes
      coarse_node.setFineNodes(nodes)
      return fine_nodes
  
  def get_material_nodes(self, coarse_node):
    """
        Method to extract the fine nodes by material from a given cell
        
        Parameters
        -------------------------------------------------------------
        node        :   Cell type filled with universe or material
        -------------------------------------------------------------

        returns Array(node_1, node_2, ..., node_N)
        
        each node is a Cell type
    """
    fill = coarse_node.cell.content
    if isinstance(fill, Universe):
      # if isinstance(fill, Pin):
      # get a cell for each level of the pin
      fine_nodes = {}
      universe_cells = fill.cells
      for c_id, cell in universe_cells.items():
          fine_node = FineNode(cell)
          fine_nodes[c_id] = fine_node
      return fine_nodes
    elif isinstance(fill, Material):
      print("Material here")
      fine_node = FineNode(coarse_node.cell)
      fine_nodes = {
          coarse_node.cell.id: fine_node
      }
      return fine_nodes
    else:
      print("***Error**** Cell has not been filled with no Material nor Universe ")
      print(f"Cell: {coarse_node.cell.name}")
      raise SystemExit
        

class CellMesh(FineMesh):
  
  def __init__(self, coarse_nodes, local_mesh_type):
    super().__init__(coarse_nodes, local_mesh_type)
    self.fine_nodes = self.generate_fine_nodes()
  
  def generate_fine_nodes(self):
    fine_nodes = {}
    for n_id, coarse_node in self.coarse_nodes.items():
      nodes = self.get_cells_nodes(coarse_node)
      fine_nodes[n_id] = nodes
      coarse_node.setFineNodes(nodes)
    return fine_nodes
        
  def get_cells_nodes(self, coarse_node):
    """
        Method to extract the fine nodes by cell from a given coarse_node
        
        Parameters
        -------------------------------------------------------------
        node        :   Cell type filled with universe or material
        -------------------------------------------------------------

        returns Array(node_1, node_2, ..., node_N)
        
        each node is a Cell type
    """
    fill = coarse_node.cell.content
    if isinstance(fill, Universe):
      fine_nodes = {}
      universe_cells = fill.cells
      for c_id, cell in universe_cells.items():
          fine_node = FineNode(cell)
          fine_nodes[c_id] = fine_node
      return fine_nodes
    
    else:
      print("***Error**** Cell has not been filled with no Material nor Universe ")
      print(f"Cell: {coarse_node.cell.name}")
      raise SystemExit  
  

class PieMesh(FineMesh):
  
  def __init__(self, coarse_nodes, local_mesh_type):
    super().__init__(coarse_nodes, local_mesh_type)


  def generate_fine_nodes(self):
    fine_nodes = {}
    
    mats_pie = self.type["pie"]
    slices = self.type["slices"]
    for n_id, coarse_node in self.coarse_nodes.items():
        nodes = self.get_pie_mesh(coarse_node, mats_pie, slices)
        fine_nodes[n_id] = nodes
        coarse_node.setFineNodes(nodes)
    return fine_nodes
        
  
  def get_fuel_cross_nodes(self, coarse_node):
        """
            Method to extract the fine nodes from a given cell in the form of
            a cross in the fuel, with the other regions (coolant) intact
            
            Parameters
            -------------------------------------------------------------
            node        :   Cell type filled with universe or material
            -------------------------------------------------------------

            returns Array(node_1, node_2, ..., node_N)
            
            each node is a Cell type
        """
        fill = coarse_node.cell.content
        if isinstance(fill, Universe):
            # if isinstance(fill, Pin):
            # get a cell for each level of the pin
            fine_nodes = {}

            universe_cells = fill.cells
            for c_id, cell in universe_cells.items():
                if cell.content.isFuel:
                    # Generate cell in a Pie slice form, clock-wise numeration
                    circle = cell.region.surface

                    x0, y0 = circle.center
                    r1, r2 = 0, circle.radius
                    pad_volume = math.pi * r2 * r2 / 4

                    pie_top_left_region = -CylinderPad(x0, y0, r1, r2, th1=90, th2=180)       #  TL
                    pie_top_right_region = -CylinderPad(x0, y0, r1, r2, th1=0, th2=90)        #  TR
                    pie_bottom_right_region = -CylinderPad(x0, y0, r1, r2, th1=270, th2=0)    #  BR
                    pie_bottom_left_region = -CylinderPad(x0, y0, r1, r2, th1=180, th2=270)   #  BL
            
                    pie_cell_top_left = Cell(name="pie_cell_top_left", fill=cell.content, region=pie_top_left_region, universe=cell.universe, volume=pad_volume)
                    pie_cell_top_right = Cell(name="pie_cell_top_right", fill=cell.content, region=pie_top_right_region, universe=cell.universe, volume=pad_volume)
                    pie_cell_bottom_right = Cell(name="pie_cell_bottom_right", fill=cell.content, region=pie_bottom_right_region, universe=cell.universe, volume=pad_volume)
                    pie_cell_bottom_left = Cell(name="pie_cell_bottom_left", fill=cell.content, region=pie_bottom_left_region, universe=cell.universe, volume=pad_volume)

                    # Generate an instance of FineNode with the pie slice
                    fine_nodes[pie_cell_top_left.id] = FineNode(pie_cell_top_left)
                    fine_nodes[pie_cell_top_right.id] = FineNode(pie_cell_top_right)
                    fine_nodes[pie_cell_bottom_left.id] = FineNode(pie_cell_bottom_left)
                    fine_nodes[pie_cell_bottom_right.id] = FineNode(pie_cell_bottom_right)
                else:
                    fine_node = FineNode(cell)
                    fine_nodes[c_id] = fine_node
            new_cells = {fn_id: fn.cell for fn_id,fn in fine_nodes.items()}
            coarse_node.cell.content.cells = new_cells
            return fine_nodes
        
        else:
            print("***Error**** Cell has not been filled with Universe Pin, to divide the fuel in a cross")
            print(f"Cell: {coarse_node.cell.name}")
            raise SystemExit
        pass

  def get_pie_mesh(self, coarse_node, materials, slices):
      """
          Method to extract the fine nodes from a given cell in the form of
          a pie in a material
          
          Parameters
          -------------------------------------------------------------
          node        :   Cell type filled with universe or material
          materials   :   Array of materials to be mashed in a pie form
          -------------------------------------------------------------

          returns Array(node_1, node_2, ..., node_N)
          
          each node is a Cell type
      """
      fill = coarse_node.cell.content
      external_surf = ""
      if isinstance(coarse_node.cell.region.surface, InfiniteSquareCylinderZ):
          external_surf = "square"
      elif isinstance(coarse_node.cell.region.surface, InfiniteHexagonalCylinderXtype):
          external_surf = "hexagon-x"
      elif isinstance(coarse_node.cell.region.surface, InfiniteHexagonalCylinderYtype):
          external_surf = "hexagon-y"
      if isinstance(fill, Universe):
          # if isinstance(fill, Pin):
          # get a cell for each level of the pin
          fine_nodes = {}
          similar_fine_nodes = {}
          universe_cells = fill.cells
          for c_id, cell in universe_cells.items():
              
              if cell.content.name in materials:

                  # print(cell.content.name)
                  # Generate cell in a pie slice form for  the material 
                  region = cell.region
                  r1, r2 = None, None
                  # x0, y0 = None, None
                  x0, y0 = 0.0, 0.0
                  pads = None
                  if isinstance(region, SurfaceSide) and isinstance(region.surface, InfiniteCylinderZ):
                      r1 = 0
                      r2 = cell.region.surface.radius
                      # x0, y0 = cell.region.surface.center
                      pads = self.get_cylinder_pads(x0, y0, r1, r2, cell, slices)  
                  else:
                      surf1 = cell.region.child1.surface
                      surf2 = cell.region.child2.surface
                      if isinstance(surf1, InfiniteCylinderZ) and isinstance(surf2, InfiniteCylinderZ):
                          r1 = surf1.radius
                          r2 = surf2.radius
                          # x0, y0 = surf1.center # Any circle
                          pads = self.get_cylinder_pads(x0, y0, r1, r2, cell, slices)
                      else:
                          pads = self.get_edge_pads(cell, external_surf, slices)
                  for c in pads:  
                      fine_nodes[c.id] = FineNode(c)
              else:
                  # Generate  just a material fine node
                  fine_node = FineNode(cell)
                  fine_nodes[c_id] = fine_node
          new_cells = {fn_id: fn.cell for fn_id,fn in fine_nodes.items()}
          coarse_node.cell.content.cells = new_cells
          return fine_nodes
      
      else:
          print("***Error**** Cell has not been filled with Universe Pin, to divide the fuel in a cross")
          print(f"Cell: {coarse_node.cell.name}")
          raise SystemExit
      pass

  

  def get_cylinder_pads(self, x0, y0, r1, r2, cell, slices):
      pad_volume = cell.volume / (len(slices)) 
      cell_slices = []
      for angle in slices:
          th1, th2 = angle
          slice_region = -CylinderPad(x0, y0, r1, r2, th1, th2)
          slice_cell = Cell(name=f"pie_cell_th1_{th1}_th2_{th2}", fill=cell.content, region=slice_region, universe=cell.universe, volume=pad_volume)
          cell_slices.append(slice_cell)
      
      return cell_slices
      

  def get_edge_pads(self, cell, external_surface, slices):
      # Is generally coolant
      # print(external_surface)
      if external_surface == "square" and len(slices) == 4:
          px = PlaneX(0.0)
          py = PlaneY(0.0)
          
          reg_coolant = cell.region 
          cool_pad_volume = cell.volume / 4 
          tl_cool_reg = reg_coolant & -px & +py
          tr_cool_reg = reg_coolant & +px & +py
          br_cool_reg = reg_coolant & +px & -py
          bl_cool_reg = reg_coolant & -px & -py

          tl = Cell(name="cool_cell_top_left", fill=cell.content, region=tl_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          tr = Cell(name="cool_cell_top_right", fill=cell.content, region=tr_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          br = Cell(name="cool_cell_bottom_right", fill=cell.content, region=br_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          bl = Cell(name="cool_cell_bottom_left", fill=cell.content, region=bl_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          return tl, tr, br, bl
      elif external_surface == "hexagon-x" and len(slices) == 6:
          reg_cell = cell.region
          pad_volume = cell.volume / 6
          
          p_central = PlaneX(0.0)
          p_1 = PlaneY(0.0)
          p_1.rotate(30, ref_point=(0.0,0.0))
          p_2 = PlaneY(0.0)
          p_2.rotate(-30, ref_point=(0.0,0.0))
          
          reg1 = reg_cell & +p_central & +p_1
          reg2 = reg_cell & -p_1 & +p_2
          reg3 = reg_cell & +p_central & -p_2
          reg4 = reg_cell & -p_central & -p_1
          reg5 = reg_cell & +p_1 & -p_2
          reg6 = reg_cell & -p_central & +p_2

          pie_1 = Cell(name="pie_1", fill=cell.content, region=reg1, volume=pad_volume, universe=cell.universe)
          pie_2 = Cell(name="pie_2", fill=cell.content, region=reg2, volume=pad_volume, universe=cell.universe)
          pie_3 = Cell(name="pie_3", fill=cell.content, region=reg3, volume=pad_volume, universe=cell.universe)
          pie_4 = Cell(name="pie_4", fill=cell.content, region=reg4, volume=pad_volume, universe=cell.universe)
          pie_5 = Cell(name="pie_5", fill=cell.content, region=reg5, volume=pad_volume, universe=cell.universe)
          pie_6 = Cell(name="pie_6", fill=cell.content, region=reg6, volume=pad_volume, universe=cell.universe)
          return pie_1, pie_2, pie_3, pie_4, pie_5, pie_6
      elif external_surface == "hexagon-x" and len(slices) == 4:
          px = PlaneX(0.0)
          py = PlaneY(0.0)
          
          reg_coolant = cell.region 
          cool_pad_volume = cell.volume / 4 
          tl_cool_reg = reg_coolant & -px & +py
          tr_cool_reg = reg_coolant & +px & +py
          br_cool_reg = reg_coolant & +px & -py
          bl_cool_reg = reg_coolant & -px & -py

          tl = Cell(name="cool_cell_top_left", fill=cell.content, region=tl_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          tr = Cell(name="cool_cell_top_right", fill=cell.content, region=tr_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          br = Cell(name="cool_cell_bottom_right", fill=cell.content, region=br_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          bl = Cell(name="cool_cell_bottom_left", fill=cell.content, region=bl_cool_reg, volume=cool_pad_volume, universe=cell.universe)
          return tl, tr, br, bl
      # elif external_surface == "hexagon-y" and len(slices) == 6:
      else:
          "not implemented yet"
          raise SystemError
              
