import unittest

import Shynt
from Shynt.api_py.Geometry.cells import Cell
from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderYtype
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed

import materials_testing

class TestUniverses(unittest.TestCase):


    def test_hexagonal_lattice(self):
        u235 = Shynt.materials.Isotope("92235.09c")
        u238 = Shynt.materials.Isotope("92238.09c")
        oxygen09 = Shynt.materials.Isotope("8016.09c")

        oxygen06 = Shynt.materials.Isotope("8016.06c")
        hydrogen = Shynt.materials.Isotope("1001.06c")
        helium06 = Shynt.materials.Isotope("2004.06c")
        
        fuel1 = Shynt.materials.Material("fuel1", mass_density=10.424)
        fuel1.addIsotope(u235, mass_fraction=0.015867)
        fuel1.addIsotope(u238, mass_fraction=0.86563)
        fuel1.addIsotope(oxygen09, mass_fraction=0.1185)

        coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.443760)
        coolant.addIsotope(oxygen06, atom_fraction=0.33333)
        coolant.addIsotope(hydrogen, atom_fraction=0.66667)

        p1 = Shynt.universes.Pin("pin_fuel1", surroundings=fuel1)
        pc = Shynt.universes.Pin("coolant", surroundings=coolant)

        hex_lat_array = [
            [pc, pc, pc, pc, pc],
            [pc, pc, p1, p1, pc],
            [pc, p1, p1, p1, pc],
            [pc, p1, p1, pc, pc],
            [pc, pc, pc, pc, pc],
        ]

        hex_lattice = HexagonalLatticeTypeX("assm_hex", (0,0), 2, hex_lat_array)
        hex_wrap = InfiniteHexagonalCylinderYtype(0, 0, 3, boundary="reflective")

        # Main problem cell
        assembly_cell = Cell("hex_assembly_problem", region=-hex_wrap, fill=hex_lattice)

    def test_square_lattice(self):
        p1 = Shynt.universes.Pin("pin_fuel1")
        p1.add_pin_levels(
            [materials_testing.inner_fuel, materials_testing.na_coolant],
            [0.4335, None]
        )

        lat_array = [
            [p1, p1, p1],
            [p1, p1, p1],
            [p1, p1, p1]
        ]
        
        lat = SquareLattice("assembly", (0.0, 0.0), 1.295, lat_array)


if __name__ == "__main__":
    # unittest.main()
    t = TestUniverses()
    # t.test_hexagonal_lattice()
    t.test_square_lattice()

    