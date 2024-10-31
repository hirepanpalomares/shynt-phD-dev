import unittest

import Shynt
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed


class TestGlobalMesh(unittest.TestCase):

    def test_pin_problem(self):
        pin_fuel1 = Shynt.universes.Pin("pin_fuel")
        
        outer_boundary = Shynt.surfaces.InfiniteSquareCylinderZ(
            0.0, 0.0, 0.6475, boundary="reflective"
        )
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
        global_mesh = meshed_model_cell.global_mesh

        coarse_nodes = global_mesh.coarse_nodes


        print()
        print(test_did_passed("GLOBAL MESH FOR PIN CELL PROBLEM"), end="")



if __name__ == "__main__":
    unittest.main()
    
    