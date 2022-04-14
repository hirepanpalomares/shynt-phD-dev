import unittest

import Shynt
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed



class TestSurfaceFunctions(unittest.TestCase):


    def test_plane_x_rotation_2D(self):
        surf = Shynt.surfaces.PlaneY(0.0)
        surf.rotate(+45,(0,0))
        
        assert(surf.isPointNegativeSide(y=1, x=2))



if __name__ == "__main__":
    unittest.main()
    