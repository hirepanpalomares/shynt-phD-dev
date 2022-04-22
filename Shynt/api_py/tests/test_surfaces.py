import unittest

import Shynt
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed



class TestSurfaceFunctions(unittest.TestCase):


    def test_plane_y_rotation_2D(self):
        ttype = "ROTATION OF SURFACE PLANE-Y"

        surf1 = Shynt.surfaces.PlaneY(0.0)
        surf1.rotate(+45,(0,0))
        assert surf1.isPointNegativeSide(x=+2, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointNegativeSide(x=+1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointNegativeSide(x=-1, y=-2), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointPositiveSide(x=-2, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointPositiveSide(x=-1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointPositiveSide(x=+1, y=+2), print(test_did_not_passed(ttype), end="")

        surf2 = Shynt.surfaces.PlaneY(0.0)
        surf2.rotate(-45,(0,0))
        assert surf2.isPointNegativeSide(x=-2, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointNegativeSide(x=-1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointNegativeSide(x=+1, y=-2), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointPositiveSide(x=-1, y=+2), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointPositiveSide(x=+1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointPositiveSide(x=+2, y=-1), print(test_did_not_passed(ttype), end="")

        surf3 = Shynt.surfaces.PlaneY(0.0)
        surf3.rotate(+45,(1,0))
        assert surf3.isPointNegativeSide(x=+3, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointNegativeSide(x=+1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointNegativeSide(x=-1, y=-3), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=-1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=-1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=+1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=0, y=0), print(test_did_not_passed(ttype), end="")
        

        print(test_did_passed(ttype), end="")

    def test_plane_x_rotation_2D(self):
        ttype = "ROTATION OF SURFACE PLANE-X"

        surf1 = Shynt.surfaces.PlaneX(0.0)
        surf1.rotate(-45,(0,0))
        assert surf1.isPointNegativeSide(x=+2, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointNegativeSide(x=+1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointNegativeSide(x=-1, y=-2), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointPositiveSide(x=-2, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointPositiveSide(x=-1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf1.isPointPositiveSide(x=+1, y=+2), print(test_did_not_passed(ttype), end="")

        surf2 = Shynt.surfaces.PlaneX(0.0)
        surf2.rotate(+45,(0,0))
        assert surf2.isPointNegativeSide(x=-2, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointNegativeSide(x=-1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointNegativeSide(x=+1, y=-2), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointPositiveSide(x=-1, y=+2), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointPositiveSide(x=+1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf2.isPointPositiveSide(x=+2, y=-1), print(test_did_not_passed(ttype), end="")

        surf3 = Shynt.surfaces.PlaneX(1.0)
        surf3.rotate(-45,(1,0))
        assert surf3.isPointNegativeSide(x=+3, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointNegativeSide(x=+1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointNegativeSide(x=-1, y=-3), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=-1, y=-1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=-1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=+1, y=+1), print(test_did_not_passed(ttype), end="")
        assert surf3.isPointPositiveSide(x=0, y=0), print(test_did_not_passed(ttype), end="")
        

        print(test_did_passed(ttype), end="")
        print("\n")

    def test_hex_y_side(self):
        ttype = "POINTS SIDE FOR HEX-Y SURFACE"

        x0, y0, half_width = 0, 0, 4
        hex1 = Shynt.surfaces.InfiniteHexagonalCylinderYtype(x0, y0, half_width)
        print("-----")
        smaller_hex1 = Shynt.surfaces.InfiniteHexagonalCylinderYtype(x0, y0, half_width*0.95)
        bigger_hex1 = Shynt.surfaces.InfiniteHexagonalCylinderYtype(x0, y0, half_width*1.05)

        # print(hex1.get_vertex_points())
        # print(hex1.get_side_middle_points())

        points_smaller = smaller_hex1.get_vertex_points()
        points_smaller += smaller_hex1.get_side_middle_points()
        points_bigger = bigger_hex1.get_vertex_points()
        points_bigger += bigger_hex1.get_side_middle_points()

        print(smaller_hex1.get_vertex_points())
        """
            Los planos rotan bien, checar los vertex points.
            Están incorrectos y probablemente los side middle 
            points tambien estén incorrectos
        """
        print(smaller_hex1.get_side_middle_points())


        for p in points_smaller:
            print(p)
            assert hex1.isPointNegativeSide(p), print(test_did_not_passed(ttype), end="")
            raise SystemExit
        
        for p in points_bigger:
            assert hex1.isPointPositiveSide(p), print(test_did_not_passed(ttype), end="")
        
        print(test_did_passed(ttype), end="")

    
    def test_hex_x_side(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    t = TestSurfaceFunctions()
    # t.test_plane_y_rotation_2D()
    # t.test_plane_x_rotation_2D()
    t.test_hex_y_side()
    