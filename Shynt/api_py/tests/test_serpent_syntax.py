import unittest

import Shynt
from Shynt.api_py.tests.printing_statements import test_did_not_passed, test_did_passed


"""
    To run the tests:
    $: nose2 -v 
"""

class TestUniverse(unittest.TestCase):


    def test_pin_universe(self):
        u235 = Shynt.materials.Isotope("92235.09c")
        u238 = Shynt.materials.Isotope("92238.09c")
        oxygen09 = Shynt.materials.Isotope("8016.09c")
        oxygen06 = Shynt.materials.Isotope("8016.06c")
        hydrogen = Shynt.materials.Isotope("1001.06c")
        fuel1 = Shynt.materials.Material("fuel1", mass_density=10.424)
        fuel1.addIsotope(u235, mass_fraction=0.015867)
        fuel1.addIsotope(u238, mass_fraction=0.86563)# Adding the isotope hydrogen to the
        fuel1.addIsotope(oxygen09, mass_fraction=0.1185)        
        coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.443760)
        coolant.addIsotope(oxygen06, atom_fraction=0.33333)
        coolant.addIsotope(hydrogen, atom_fraction=0.66667)

        pin1 = Shynt.universes.Pin("pin_fuel1", material=fuel1, radius=0.4335, surroundings=coolant)
        
        # Aqui testear toda la syntaxis de la geometria del pin y ya

    
    def test_square_lattice_universe(self):
        u235 = Shynt.materials.Isotope("92235.09c")
        u238 = Shynt.materials.Isotope("92238.09c")
        oxygen09 = Shynt.materials.Isotope("8016.09c")
        oxygen06 = Shynt.materials.Isotope("8016.06c")
        hydrogen = Shynt.materials.Isotope("1001.06c")
        fuel1 = Shynt.materials.Material("fuel1", mass_density=10.424)
        fuel1.addIsotope(u235, mass_fraction=0.015867)
        fuel1.addIsotope(u238, mass_fraction=0.86563)# Adding the isotope hydrogen to the
        fuel1.addIsotope(oxygen09, mass_fraction=0.1185)       
        fuel2 = Shynt.materials.Material("fuel2", mass_density=10.424)
        fuel2.addIsotope(u235, mass_fraction=0.018512)
        fuel2.addIsotope(u238, mass_fraction=0.86299)
        fuel2.addIsotope(oxygen09, mass_fraction=0.1185) 
        coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.443760)
        coolant.addIsotope(oxygen06, atom_fraction=0.33333)
        coolant.addIsotope(hydrogen, atom_fraction=0.66667)

        pin1 = Shynt.universes.Pin("pin_fuel1", material=fuel1, radius=0.4335, surroundings=coolant)
        pin1 = Shynt.universes.Pin("pin_fuel2", material=fuel2, radius=0.4335, surroundings=coolant)
        
        # Aqui testear toda la syntaxis de la geometria del lattice y ya con differentes pin



if __name__ == "__main__":
    unittest.main()
    