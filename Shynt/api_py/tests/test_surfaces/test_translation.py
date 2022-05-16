import unittest

import Shynt
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed



class TestSurfaceTranslation(unittest.TestCase):


    def test_2Dplane_x_translation(self):
        ttype = "TRANSLATION OF A 2D SURFACE PLANE-X"

        init_x0 = 0.0
        translation_vectors = [
            #(x,y)
            (0,1),
            (1,0),
            (0,-1),

            (-1,0),
            (1,1),
            (1,-1),

            (-1,1),
            (2,-1),
            (-2,1),

            (2,1),
            (1,2),
            (1,-2),
            (-1,2),
        ]
        answers = [ 
            # x0 values that is supposed to have (non rotated plane)
            {"x0":0.0, "p-neg":-1, "p-pos":+1},
            {"x0":1.0, "p-neg":0,  "p-pos":+2},
            {"x0":0.0, "p-neg":-1, "p-pos":+1},

            {"x0":-1.0, "p-neg":-2, "p-pos":0},
            {"x0":1.0, "p-neg":0, "p-pos":2},
            {"x0":1.0, "p-neg":0, "p-pos":2},

            {"x0":-1.0, "p-neg":-2, "p-pos":0},
            {"x0":2.0, "p-neg":1, "p-pos":3},
            {"x0":-2.0, "p-neg":-3, "p-pos":-1},

            {"x0":2.0, "p-neg":1, "p-pos":3},
            {"x0":1.0, "p-neg":0, "p-pos":2},
            {"x0":1.0, "p-neg":0, "p-pos":2},
            {"x0":-1.0, "p-neg":-2, "p-pos":0},
        ]

        surf1 = Shynt.surfaces.PlaneX(init_x0)
        for i in range(len(translation_vectors)):
            vec = translation_vectors[i]
            ans = answers[i]

            surf1.translate(vec)
            assert surf1.x0 == ans["x0"], print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            assert surf1.isPointNegativeSide(x=ans["p-neg"]), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            assert surf1.isPointPositiveSide(x=ans["p-pos"]), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")

            surf1.x0 = init_x0


        
        #assert surf1.isPointNegativeSide(x=+2, y=+1), print(test_did_not_passed(ttype), end="")
        
        print(test_did_passed(ttype), end="")
    
    def test_2Dplane_y_translation(self):
        ttype = "TRANSLATION OF A 2D SURFACE PLANE-Y"

        init_y0 = 0.0
        translation_vectors = [
            #(x,y)
            (0,1),
            (1,0),
            (0,-1),

            (-1,0),
            (1,1),
            (1,-1),

            (-1,1),
            (2,-1),
            (-2,1),

            (2,1),
            (1,2),
            (1,-2),
            (-1,2),
        ]
        answers = [ 
            # x0 values that is supposed to have (non rotated plane)
            {"y0":1.0, "p-neg":0, "p-pos":2},
            {"y0":0.0, "p-neg":-1,  "p-pos":1},
            {"y0":-1.0, "p-neg":-2, "p-pos":0},

            {"y0":0.0, "p-neg":-1,  "p-pos":1},
            {"y0":1.0, "p-neg":0, "p-pos":2},
            {"y0":-1.0, "p-neg":-2, "p-pos":0},

            {"y0":1.0, "p-neg":0, "p-pos":2},
            {"y0":-1.0, "p-neg":-2, "p-pos":0},
            {"y0":1.0, "p-neg":0, "p-pos":2},

            {"y0":1.0, "p-neg":0, "p-pos":2},
            {"y0":2.0, "p-neg":1, "p-pos":3},
            {"y0":-2.0, "p-neg":-3, "p-pos":-1},
            {"y0":2.0, "p-neg":-2, "p-pos":3},
        ]

        surf1 = Shynt.surfaces.PlaneY(init_y0)
        for i in range(len(translation_vectors)):
            vec = translation_vectors[i]
            ans = answers[i]

            surf1.translate(vec)
            assert surf1.y0 == ans["y0"], print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            assert surf1.isPointNegativeSide(y=ans["p-neg"]), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            assert surf1.isPointPositiveSide(y=ans["p-pos"]), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")

            surf1.y0 = init_y0


        
        #assert surf1.isPointNegativeSide(x=+2, y=+1), print(test_did_not_passed(ttype), end="")
        
        print(test_did_passed(ttype), end="")
    
    def test_2Dplane_x_rotated_translation(self):
        ttype = "TRANSLATION OF A 2D ROTATED SURFACE PLANE-X"

        init_x0 = 0.0
        rot_angle = 45

        translation_vectors = [
            (0,1),  
            (1,0),  
            (0,-1), 
            (-1,0), 
            (1,1),  
            (1,-1), 
            (-1,1),
            (2,-1),
            (-2,1),
            (2,1),
            (1,2),
            (1,-2),
            (-1,2),
        ]

        surf1 = Shynt.surfaces.PlaneX(init_x0)
        for i in range(len(translation_vectors)):
            surf1.rotate(rot_angle, (0,0))
            m = surf1.line_params["m"]  # doesn't change
            b = surf1.line_params["b"]  # it changes
            
            x_ref = 0
            y_ref = surf1.useFunction(x_ref)
            vec = translation_vectors[i]
            x_new = x_ref + vec[0]
            y_new = y_ref + vec[1]
            new_b =  y_new - m*x_new

            surf1.translate(vec)
            assert surf1.line_params["m"] == m, print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            assert surf1.line_params["b"] == new_b, print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            
            surf1.x0 = init_x0
            surf1.reset_rotation()
        
        print(test_did_passed(ttype), end="")

    def test_2Dplane_y_rotated_translation(self):
        ttype = "TRANSLATION OF A 2D ROTATED SURFACE PLANE-Y"

        init_y0 = 0.0
        rot_angle = 45

        translation_vectors = [
            (0,1),  
            (1,0),  
            (0,-1), 
            (-1,0), 
            (1,1),  
            (1,-1), 
            (-1,1),
            (2,-1),
            (-2,1),
            (2,1),
            (1,2),
            (1,-2),
            (-1,2),
        ]

        surf1 = Shynt.surfaces.PlaneY(init_y0)
        for i in range(len(translation_vectors)):
            surf1.rotate(rot_angle, (0,0))
            m = surf1.line_params["m"]  # doesn't change
            b = surf1.line_params["b"]  # it changes
            
            x_ref = 0
            y_ref = surf1.useFunction(x_ref)
            vec = translation_vectors[i]
            x_new = x_ref + vec[0]
            y_new = y_ref + vec[1]
            new_b =  y_new - m*x_new

            surf1.translate(vec)
            assert surf1.line_params["m"] == m, print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            assert surf1.line_params["b"] == new_b, print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            
            surf1.y0 = init_y0
            surf1.reset_rotation()
        
        print(test_did_passed(ttype), end="")
    
    def test_2D_hexagonX_surface_translation(self):
        ttype = "TRANSLATION OF A 2D SURFACE HEXAGON-X"

        init_y0 = 0.0
        init_x0 = 0.0
        half_width = 3
        

        translation_vectors = [
            (0*half_width*2.5,1*half_width*2.5),  
            (+1*half_width*2.5,+0*half_width*2.5),
            (+0*half_width*2.5,-1*half_width*2.5),
            (-1*half_width*2.5,+0*half_width*2.5),
            (+1*half_width*2.5,+1*half_width*2.5),
            (+1*half_width*2.5,-1*half_width*2.5),
            (-1*half_width*2.5,+1*half_width*2.5),
            (+2*half_width*2.5,-1*half_width*2.5),
            (-2*half_width*2.5,+1*half_width*2.5),
            (+2*half_width*2.5,+1*half_width*2.5),
            (+1*half_width*2.5,+2*half_width*2.5),
            (+1*half_width*2.5,-2*half_width*2.5),
            (-1*half_width*2.5,+2*half_width*2.5),
        ]

        smaller_hex1 = Shynt.surfaces.InfiniteHexagonalCylinderXtype(init_x0, init_y0, half_width*0.95)
        bigger_hex1 = Shynt.surfaces.InfiniteHexagonalCylinderXtype(init_x0, init_y0, half_width*1.05)
        points_smaller = smaller_hex1.get_vertex_points()
        points_smaller += smaller_hex1.get_side_middle_points()
        points_bigger = bigger_hex1.get_vertex_points()
        points_bigger += bigger_hex1.get_side_middle_points()


        for vec in translation_vectors:
            surf1 = Shynt.surfaces.InfiniteHexagonalCylinderXtype(init_x0, init_y0, half_width)
            surf1.translate(vec)            

            # checking smaller points
            for point in points_smaller:
                assert surf1.isPointPositiveSide(point), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            
            # checking translated smaller points 
            for point in points_smaller:
                point = (point[0]+vec[0], point[1]+vec[1])
                assert surf1.isPointNegativeSide(point), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")

        print(test_did_passed(ttype), end="")

    def test_2D_hexagonY_surface_translation(self):
        ttype = "TRANSLATION OF A 2D SURFACE HEXAGON-Y"

        init_y0 = 0.0
        init_x0 = 0.0
        half_width = 3
        

        translation_vectors = [
            (0*half_width*2.5,1*half_width*2.5),  
            (+1*half_width*2.5,+0*half_width*2.5),
            (+0*half_width*2.5,-1*half_width*2.5),
            (-1*half_width*2.5,+0*half_width*2.5),
            (+1*half_width*2.5,+1*half_width*2.5),
            (+1*half_width*2.5,-1*half_width*2.5),
            (-1*half_width*2.5,+1*half_width*2.5),
            (+2*half_width*2.5,-1*half_width*2.5),
            (-2*half_width*2.5,+1*half_width*2.5),
            (+2*half_width*2.5,+1*half_width*2.5),
            (+1*half_width*2.5,+2*half_width*2.5),
            (+1*half_width*2.5,-2*half_width*2.5),
            (-1*half_width*2.5,+2*half_width*2.5),
        ]

        smaller_hex1 = Shynt.surfaces.InfiniteHexagonalCylinderYtype(init_x0, init_y0, half_width*0.95)
        bigger_hex1 = Shynt.surfaces.InfiniteHexagonalCylinderYtype(init_x0, init_y0, half_width*1.05)
        points_smaller = smaller_hex1.get_vertex_points()
        points_smaller += smaller_hex1.get_side_middle_points()
        points_bigger = bigger_hex1.get_vertex_points()
        points_bigger += bigger_hex1.get_side_middle_points()


        for vec in translation_vectors:
            surf1 = Shynt.surfaces.InfiniteHexagonalCylinderYtype(init_x0, init_y0, half_width)
            surf1.translate(vec)            

            # checking smaller points
            for point in points_smaller:
                assert surf1.isPointPositiveSide(point), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")
            
            # checking translated smaller points 
            for point in points_smaller:
                point = (point[0]+vec[0], point[1]+vec[1])
                assert surf1.isPointNegativeSide(point), print(test_did_not_passed(ttype) + f" on translation vector {vec}", end="")

        print(test_did_passed(ttype), end="")



if __name__ == "__main__":
    # unittest.main()
    t = TestSurfaceTranslation()
    t.test_2D_hexagonX_surface_translation()

    