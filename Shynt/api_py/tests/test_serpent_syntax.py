import unittest

import Shynt
from Shynt.api_py.Geometry.universes import Pin
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed

import materials_testing as mat



"""
    To run the tests:
    $: nose2 -v 
"""


class TestUniverse(unittest.TestCase):


    def test_pin_universe(self):
        p_i = Pin("pin_inner")
        mat_lev = [mat.helium_gas, mat.inner_fuel, mat.helium_gas, mat.cladding, mat.na_coolant]
        rad_lev = [0.10000, 0.35700, 0.36947, 0.43035, None]
        p_i.add_pin_levels(mat_lev, rad_lev)


        # Aqui testear toda la syntaxis de la geometria del pin y ya

        p_i.serpent_universe_pin_by_cell_syntax()

    
    def test_square_lattice_universe(self):
        p_i = Pin("pin_inner")
        mat_lev = [mat.helium_gas, mat.inner_fuel, mat.helium_gas, mat.cladding, mat.na_coolant]
        rad_lev = [0.10000, 0.35700, 0.36947, 0.43035, None]
        p_i.add_pin_levels(mat_lev, rad_lev)

        p_c = Pin("pin_coolant")
        mat_lev = [mat.na_coolant]
        rad_lev = [None]
        p_c.add_pin_levels(mat_lev, rad_lev)

        mc_params = Shynt.montecarlo.MontecarloParams(2000, 500, 50, seed=1474468046)
        libraries = Shynt.libraries.SerpentLibraries(acelib='"jeff311/sss_jeff311u.xsdata"', therm="therm lwtr lwj3.11t")
        energy_grid = Shynt.energy.Grid([0, 0.625E-06, 20], name="2groups_grid") # MeV

        # Aqui testear toda la syntaxis de la geometria del lattice y ya con differentes pin

        lattice_2x2 =  [
            [p_i, p_c],
            [p_c, p_i],
        ]

        outer_boundary = Shynt.surfaces.InfiniteSquareCylinderZ(0, 0, 1.2950, boundary="reflective")
        
        assembly_2x2 = Shynt.universes.SquareLattice("assembly", (0.0, 0.0), 1.295, lattice_2x2)
        # assembly_2x2.serpent_syntax_pin_by_cell()

        model_cell = Shynt.cells.Cell("assembly_problem", region=-outer_boundary, fill=assembly_2x2)

        outside_cell = Shynt.cells.Cell("outside_world", region=+outer_boundary)

        model_universe = Shynt.universes.Root(
            model_cell, outside_cell,
            energy_grid=energy_grid, 
            mcparams=mc_params, 
            libraries=libraries,
            name ="Square lattice 2x2 - LWR system"
        )

        Shynt.file_generator.generate_root_serpent_file(model_universe)




if __name__ == "__main__":
    # unittest.main()
    tt = TestUniverse()
    # tt.test_pin_universe()
    tt.test_square_lattice_universe()
    