import unittest

import Shynt
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed


"""
    To run the tests:
    $: nose2 -v 
"""

class TestSingleCellVolume(unittest.TestCase):


    def test_cylinderZ_2D(self):
        # Cylinder of 5 cm radius
        surf = Shynt.surfaces.InfiniteCylinderZ(0.0, 0.0, 5)
        cell = Shynt.cells.Cell(
            "test_cell",
            region=-surf,
            fill=None
        )
        vol = cell.volume
        assert vol == 78.53981633974483, print(test_did_not_passed("VOLUME OF CYLINDRIC CELL"), end="")
        print(test_did_passed("VOLUME OF CYLINDRIC CELL"), end="")
        


    def test_squareZ_2D(self):
        # Square of 5 cm side
        surf = Shynt.surfaces.InfiniteSquareCylinderZ(0.0, 0.0, 2.5)
        cell = Shynt.cells.Cell(
            "test_cell",
            region=-surf,
            fill=None
        )
        vol = cell.volume
        assert vol == 25, print(test_did_not_passed("VOLUME OF SQUARE CELL"), end="")
        print(test_did_passed("VOLUME OF SQUARE CELL"), end="")
    
    def test_hexagonal_cell_2D(self):
        
        pass



class TestJointCellVolume(unittest.TestCase):

    def test_pin_moderator(self):
        surf1 = Shynt.surfaces.InfiniteCylinderZ(0.0, 0.0, 4)
        surf2 = Shynt.surfaces.InfiniteSquareCylinderZ(0.0, 0.0, 5)
        region = -surf1 & +surf2
        cell = Shynt.cells.Cell(
            "test_cell",
            region=region,
            fill=None
        )
        vol = cell.volume
        assert vol == 49.73451754256331, print(test_did_not_passed("VOLUME OF MODERATOR ZONE PIN CELL"), end="")
        print(test_did_passed("VOLUME OF MODERATOR ZONE PIN CELL"), end="")



if __name__ == "__main__":
    unittest.main()
    