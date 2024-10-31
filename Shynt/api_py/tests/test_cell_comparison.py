import unittest

import Shynt
from Shynt.api_py.Geometry.surfaces import InfiniteSquareCylinderZ
from Shynt.api_py.Geometry.universes import Pin
from Shynt.api_py.Geometry.utilities_geometry import declaring_pin_by_cells
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed

import materials_testing as mat



"""
    To run the tests:
    $: nose2 -v 

    To run specific test_file:
    $: nose2 -s file
"""


class TestCellComparisson(unittest.TestCase):


    def test_pin_cell_comparison(self):
        closing_surface = InfiniteSquareCylinderZ(0.0, 0.0, 0.6435)
        mat_lev_f1 = [mat.helium_gas, mat.inner_fuel, mat.helium_gas, mat.cladding, mat.na_coolant]
        rad_lev_f1 = [0.10000, 0.35700, 0.36947, 0.43035, None]
        mat_lev_cool = [mat.na_coolant]
        rad_lev_cool = [None]

        p_i = declaring_pin_by_cells(mat_lev_f1, rad_lev_f1, 0.0, 0.0, "pin_i", closing_surface)
        p_f = declaring_pin_by_cells(mat_lev_f1, rad_lev_f1, 0.0, 0.0, "pin_i", closing_surface)
        p_c = declaring_pin_by_cells(mat_lev_cool, rad_lev_cool, 0.0, 0.0, "pin_i", closing_surface)


        # Aqui testear toda la syntaxis de la geometria del lattice y ya con differentes pin
        assert  p_i == p_f




if __name__ == "__main__":
    unittest.main()
    # tt = TestCellComparisson()
    # tt.test_pin_universe()
    # tt.test_square_lattice_universe()
    