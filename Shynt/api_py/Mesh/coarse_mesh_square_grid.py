
from Shynt.api_py.Mesh.coarse_mesh import CoarseMesh

from Shynt.api_py.Geometry.universes import (
  HexagonalLatticeTypeX,
  Pin,
  Universe
)

import numpy as np



  
  
    

def fix_boundaries(self, nodes_surfaces):
  """Fixes the diagonal in the nodes on the boundary that are in the 
  diagonal of the hexagon 
  HARDCODED
  Nodes to fix:
    top_bottom_corners = [1,20,561,580]
    sides = [
      21,43,67,93,121,151,183,217,253,291,329,365,399,431,461,489,515,539,
      42,66,92,120,150,182,216,252,290,328,364,398,430,460,488,514,538,560
    ]

  Basically the function calculates from the points of the diagonal surface
  """

  n_surf = nodes_surfaces.copy()
  top_bottom_corners = [
    1,20,561,580
  ]
  sides = [
    21,43,67,93,121,151,183,217,253,291,329,365,399,431,461,489,515,539,
    42,66,92,120,150,182,216,252,290,328,364,398,430,460,488,514,538,560
  ]
  hexagon = super().cell.region.surface
  
  # ---------------------------------------------------
  #                   CORNERS
  # ---------------------------------------------------
  x1,y1 = n_surf[1]["top"]["points"][0]
  x2,y2 = n_surf[1]["top"]["points"][1]
  x1_new = hexagon.surf_F.useFunction(y1, given="y")
  n_surf[1]["top"]["points"] = ((x1_new,y1), (x2,y2))
  x1,y1 = n_surf[1]["left"]["points"][0]
  x2,y2 = n_surf[1]["left"]["points"][1]
  n_surf[1]["left"]["points"] = ((x1,y1), (x1_new,y2))
  # ----------------------------------------------
  x1,y1 = n_surf[20]["top"]["points"][0]
  x2,y2 = n_surf[20]["top"]["points"][1]
  x2_new = hexagon.surf_B.useFunction(y1, given="y")
  n_surf[20]["top"]["points"] = ((x1,y1), (x2_new,y2))
  x1,y1 = n_surf[20]["right"]["points"][0]
  x2,y2 = n_surf[20]["right"]["points"][1]
  n_surf[20]["right"]["points"] = ((x1,y1), (x2_new,y2))
  # ----------------------------------------------
  x1,y1 = n_surf[561]["bottom"]["points"][0]
  x2,y2 = n_surf[561]["bottom"]["points"][1]
  x1_new = hexagon.surf_E.useFunction(y1, given="y")
  n_surf[561]["bottom"]["points"] = ((x1_new,y1), (x2,y2))
  x1,y1 = n_surf[561]["left"]["points"][0]
  x2,y2 = n_surf[561]["left"]["points"][1]
  n_surf[561]["left"]["points"] = ((x1_new,y1), (x2,y2))
  # ----------------------------------------------
  x1,y1 = n_surf[580]["bottom"]["points"][0]
  x2,y2 = n_surf[580]["bottom"]["points"][1]
  x2_new = hexagon.surf_C.useFunction(y1, given="y")
  n_surf[580]["bottom"]["points"] = ((x1,y1), (x2_new,y2))
  x1,y1 = n_surf[580]["right"]["points"][0]
  x2,y2 = n_surf[580]["right"]["points"][1]
  n_surf[580]["right"]["points"] = ((x2_new,y1), (x2,y2))
  
  # ---------------------------------------------------
  #                   SIDES
  # ---------------------------------------------------
  
  def get_position_in_hexagon(point):
    """Mini function to find the place of the node in the hexagon
    giving a point of the top side of the rectangle
    """
    x, y = point
    if x < 0.0 and y > 0.0: return "upper_left"
    if x > 0.0 and y > 0.0: return "upper_right"
    if x < 0.0 and y <= 0.0: return "lower_left"
    if x > 0.0 and y <= 0.0: return "lower_right"

  surf_to_fix = {
    "upper_left": "left",
    "upper_right": "right",
    "lower_left": "left",
    "lower_right": "right"    
  }
  surf_to_remove = {
    "upper_left": "top",
    "upper_right": "top",
    "lower_left": "bottom",
    "lower_right": "bottom"    
  }
  surf_for_p1 = {
    "upper_left": "left",
    "upper_right": "right",
    "lower_left": "right",
    "lower_right": "left"    
  }
  surf_for_p2 = {
    "upper_left": "right",
    "upper_right": "left",
    "lower_left": "left",
    "lower_right": "right"    
  }

  for n_id in sides:
    random_top_point = n_surf[n_id]["top"]["points"][0]
    position = get_position_in_hexagon(random_top_point)
    s_fix = surf_to_fix[position]
    s_rem = surf_to_remove[position]
    new_p1 = n_surf[n_id][surf_for_p1[position]]["points"][0]
    new_p2 = n_surf[n_id][surf_for_p2[position]]["points"][1]
    
    n_surf[n_id][s_fix]["points"] = (new_p1,new_p2)
    n_surf[n_id][s_rem] = None

  return n_surf




