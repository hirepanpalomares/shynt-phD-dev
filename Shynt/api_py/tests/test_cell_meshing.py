import unittest

import Shynt
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed


class TestGlobalMesh(unittest.TestCase):

    def test_pin_problem(self):
        pin_fuel1 = Shynt.universes.Pin("pin_fuel")
        mat_lev = [None, None]
        rad_lev = [0.4335, None]
        pin_fuel1.add_pin_levels(mat_lev, rad_lev)
        outer_boundary = Shynt.surfaces.InfiniteSquareCylinderZ(0.0, 0.0, 0.6475, boundary="reflective")
        reg = -outer_boundary
        model_cell = Shynt.cells.Cell(
            "pin_problem", 
            region=-outer_boundary, 
            fill=pin_fuel1
        )
        meshed_model_cell = Shynt.mesh.make_mesh(
            model_cell, 
            global_mesh_type="pin_cell", 
            local_mesh_type="material"
        )
        assert len(meshed_model_cell.global_mesh.coarse_nodes) == 1, print(test_did_not_passed("GLOBAL MESH FOR PIN CELL PROBLEM"), end="")
        assert len(meshed_model_cell.surface_area_relation) == 4, print(test_did_not_passed("GLOBAL MESH FOR PIN CELL PROBLEM"), end="")
        for id_global in meshed_model_cell.global_mesh.coarse_nodes:
            local_nodes = meshed_model_cell.local_mesh.fine_nodes[id_global] 
            assert len(local_nodes) == 2, print(test_did_not_passed("GLOBAL MESH FOR PIN CELL PROBLEM"), end="")


        print(test_did_passed("GLOBAL MESH FOR PIN CELL PROBLEM"), end="")



if __name__ == "__main__":
    unittest.main()
    
    