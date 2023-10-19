

from Shynt.api_py.Geometry.regions import (
  SurfaceSide,
  Region
)
from Shynt.api_py.materials import Material
from Shynt.api_py.Geometry.surfaces import Hexagon, InfiniteCylinderZ, InfiniteSquareCylinderZ, InfiniteRectangleCylinderZ


def is_pin_in_bin(pin, arr, global_nodes, local_nodes):
    """
        Function that tells if a pin is in an array 
        returns True if in the array exist a similar pin
        and False if it does not

        Parameters
        ---------------------------------
        
        pin     :   <class Cell> and it hast be filled with the Pin universe
        arr     :   <class list> array of cells
        
        ---------------------------------
    """
    for other in arr:
        # check number of total local problems
        num_local_other = len(local_nodes[other])
        num_local_pin = len(local_nodes[pin])
        if num_local_other == num_local_pin:
            # check that the pin is the same
            
            pin_array = global_nodes[other].cell.content
            pin_compare = global_nodes[pin].cell.content
            if pin_array == pin_compare:
              return True
            # return True
    return False


def get_equal_nodes(global_nodes, local_nodes):
  """

  """

  bins = {}
  for id_, coarse_node in global_nodes.items(): # sweep cells
    if coarse_node.geometry_info["type"] not in bins:
      bins[coarse_node.geometry_info["type"]] = [id_]
    else:
      bins[coarse_node.geometry_info["type"]].append(id_)
  return bins


def get_surface_equivalence(node, node_base):
  """
    returns the relation of which surfaces correspond to one
    equal node
  """
  node_cell = node.cell
  base_node_cell = node_base.cell

  cell_surface = node_cell.region.surface
  base_cell_surface = base_node_cell.region.surface
  # print(cell_surface)
  # print(base_cell_surface)
  if isinstance(cell_surface, InfiniteSquareCylinderZ) and isinstance(base_cell_surface, InfiniteSquareCylinderZ):
    return {
      cell_surface.surf_top.id: base_cell_surface.surf_top.id,
      cell_surface.surf_right.id: base_cell_surface.surf_right.id,
      cell_surface.surf_bottom.id: base_cell_surface.surf_bottom.id,
      cell_surface.surf_left.id: base_cell_surface.surf_left.id,
    }
  if isinstance(cell_surface, Hexagon) and isinstance(base_cell_surface, Hexagon):
    return {
      cell_surface.surf_A.id: base_cell_surface.surf_A.id,
      cell_surface.surf_B.id: base_cell_surface.surf_B.id,
      cell_surface.surf_C.id: base_cell_surface.surf_C.id,
      cell_surface.surf_D.id: base_cell_surface.surf_D.id,
      cell_surface.surf_E.id: base_cell_surface.surf_E.id,
      cell_surface.surf_F.id: base_cell_surface.surf_F.id,
    }
  if isinstance(cell_surface, InfiniteRectangleCylinderZ) and isinstance(base_cell_surface, InfiniteRectangleCylinderZ):
    
    symmetry = node.geometry_info["symmetry"][node_base.id]
    boundary_guide_base = node_base.geometry_info["surfaces_for_detectors"]["boundary_guide"]
    boundary_guide_other = node.geometry_info["surfaces_for_detectors"]["boundary_guide"]
    # print(symmetry)
    if "same" in symmetry:
      boundary_symmetry = {
        boundary_guide_other["right"]: boundary_guide_base["right"],
        boundary_guide_other["bottom"]: boundary_guide_base["bottom"],
        boundary_guide_other["left"]: boundary_guide_base["left"],
        boundary_guide_other["top"]: boundary_guide_base["top"],

      }
      # if node.geometry_info["type"] != "offset_side_edge":
      #   boundary_symmetry[boundary_guide_other["top"]] =  boundary_guide_base["top"]
      return boundary_symmetry
      
    elif "mirror" in symmetry:
      if symmetry["mirror"] == "right":
        boundary_symmetry = {
          boundary_guide_other["right"]: boundary_guide_base["left"],
          boundary_guide_other["bottom"]: boundary_guide_base["bottom"],
          boundary_guide_other["left"]: boundary_guide_base["right"],
          boundary_guide_other["top"]: boundary_guide_base["top"],
        }
        
        return boundary_symmetry
      
      elif symmetry["mirror"] == "right_down":
        boundary_symmetry = {
          boundary_guide_other["right"]: boundary_guide_base["left"],
          boundary_guide_other["left"]: boundary_guide_base["right"],
        }
        if node.geometry_info["type"] != "offset_side_edge":
          boundary_symmetry[boundary_guide_other["top"]] = boundary_guide_base["bottom"]
          boundary_symmetry[boundary_guide_other["bottom"]] = boundary_guide_base["top"]
        else:
          boundary_symmetry[boundary_guide_other["top"]] = boundary_guide_base["bottom"]
        return boundary_symmetry
      
      elif symmetry["mirror"] == "down":
        boundary_symmetry = {
          boundary_guide_other["right"]: boundary_guide_base["right"],
          boundary_guide_other["left"]: boundary_guide_base["left"],
        }
        if node.geometry_info["type"] != "offset_side_edge":
          boundary_symmetry[boundary_guide_other["bottom"]] = boundary_guide_base["top"]
          boundary_symmetry[boundary_guide_other["top"]] = boundary_guide_base["bottom"]
        else:
          boundary_symmetry[boundary_guide_other["top"]] = boundary_guide_base["bottom"]
          
        return boundary_symmetry
      else:
          raise SystemError
      
def change_boundary_guide(b_guide, symmetry):
  new_b_guide = {}
  if "same" in symmetry:
    return b_guide
  elif "mirror" in symmetry:
    if symmetry["mirror"] == "right":
      new_b_guide["top"] = b_guide["top"]
      new_b_guide["bottom"] = b_guide["bottom"]
      new_b_guide["right"] = b_guide["left"]
      new_b_guide["left"] = b_guide["right"]
      return new_b_guide
    elif symmetry["mirror"] == "right_down":
      new_b_guide["top"] = b_guide["bottom"]
      new_b_guide["bottom"] = b_guide["top"]
      new_b_guide["right"] = b_guide["left"]
      new_b_guide["left"] = b_guide["right"]
      return new_b_guide
    elif symmetry["mirror"] == "down":
      new_b_guide["top"] = b_guide["bottom"]
      new_b_guide["bottom"] = b_guide["top"]
      new_b_guide["left"] = b_guide["left"]
      new_b_guide["right"] = b_guide["right"]
         
      return new_b_guide
  else:
    raise SystemExit

def get_all_surfaces_in_a_cell(cell, surfaces=None):
    
    # input()
    from Shynt.api_py.Geometry.universes import Universe
    
    if surfaces is None:
        surfaces = {}
    if isinstance(cell.content, Material):
        # base case
        surfaces_enclosing_cell = cell.region.surfaces_of_region()
        return surfaces_enclosing_cell
    if isinstance(cell.content, Universe):
        # surface senclosing the cell
        surfaces_enclosing_cell = cell.region.surfaces_of_region()
        surfaces.update(surfaces_enclosing_cell)

        # surfaces in the cells of the universe
        universe = cell.content
        new_surfaces = get_all_surfaces_in_a_universe(universe)
        surfaces.update(new_surfaces)
        return surfaces


def get_all_surfaces_in_a_universe(universe):
    surfaces = {}
    for cell in universe.cells.values():
        surfaces.update(get_all_surfaces_in_a_cell(cell))
    return surfaces

def get_materials_in_cell(cell, materials=None):
  from Shynt.api_py.Geometry.universes import Universe
  if materials is None:
    materials = {}
  if isinstance(cell.content, Material):
    mat_name = cell.content.name
    materials[mat_name] = cell.content
    return materials
  elif isinstance(cell.content, Universe):
    universe_cells = cell.content.cells
    for c_id, cell in universe_cells.items():
        materials = get_materials_in_cell(cell, materials=materials)
    return materials

def declare_pin_by_cells(materials, radius, center_x, center_y, name_pin_universe, closing_surf):
    from .cells import Cell
    from Shynt.api_py.Geometry.universes import Universe, Pin

    cells = {}
    last_surf = None
    
    for l in range(len(materials)):
        mat = materials[l]
        r = radius[l]
        reg = None
        if r is None:
            if last_surf is None:
                reg = -closing_surf
            else:
                reg = +last_surf & -closing_surf
        else:
            surf = InfiniteCylinderZ(center_x, center_y, r)
            if last_surf is None:
                reg = -surf
            else:
                reg = +last_surf & -surf
            last_surf = surf
        name_for_cell = f"{name_pin_universe}_cell_c"
        c = Cell(name=name_for_cell, fill=mat, region=reg, universe=name_pin_universe)
        cells[c.id] = c
    pin = Universe(name_pin_universe, cells)
    
    return pin


def find_cylinder_cells_in_universe(universe):
 
 
  uni_cells = universe.cells
  cyl_cells = []
  for c_id, cell in uni_cells.items():
    if isinstance(cell.region, SurfaceSide):
      cell_surf = cell.region.surface
      if isinstance(cell_surf, InfiniteCylinderZ):
        cyl_cells = order_cylinders_grater_to_lower(cyl_cells, cell)
    elif isinstance(cell.region, Region):
      child1_surf = cell.region.child1.surface
      child2_surf = cell.region.child2.surface
      if isinstance(child1_surf, InfiniteCylinderZ):
        if isinstance(child2_surf, InfiniteCylinderZ):
          cyl_cells = order_cylinders_grater_to_lower(cyl_cells, cell)


  return cyl_cells


def order_cylinders_grater_to_lower(cylinders, cell):
  def find_greatest_radius(cylindrical_region):
    if isinstance(cylindrical_region, SurfaceSide):
      return cylindrical_region.surface.radius
    elif isinstance(cylindrical_region, Region):
      surf_1 = cylindrical_region.child1.surface
      surf_2 = cylindrical_region.child2.surface
      if surf_1.radius > surf_2.radius:
        return surf_1.radius
      else:
        return surf_2.radius
        
  
  cylinders_arr = cylinders.copy()
  num_cyls = len(cylinders_arr)
  if len(cylinders_arr) == 0:
    return [cell]
  
  radius_cell = find_greatest_radius(cell.region)
  # print(cell.region, radius_cell)
  for idx, cell_sweep in enumerate(cylinders_arr):
    # -----------------
    radius_sweep = find_greatest_radius(cell_sweep.region)
    if radius_cell > radius_sweep:
      cylinders_arr = cylinders_arr[:idx] + [cell] + cylinders_arr[idx:]
      return cylinders_arr
  cylinders_arr.append(cell)


  return cylinders_arr

