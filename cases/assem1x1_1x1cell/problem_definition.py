
import numpy as np
import os 
import sys

import Shynt



class Input(object):

        def __init__(self):
            self.pin_radius = 0.4335 # cm
            self.volume_fuel = self.pin_radius * self.pin_radius * np.pi

            self.pitch = 1.2950 # cm
            self.volume_moderator = self.pitch * self.pitch - self.volume_fuel

            self.number_of_pins = 6 # different pins
            self.energy_groups = 2
            self.regions_by_cell = 2
            self.cell_number = 100
            self.assembly = np.array([
                [2, 2, 3, 5, 5, 5, 5, 3, 2, 2],
                [2, 3, 5, 6, 6, 6, 6, 5, 3, 2],
                [3, 5, 6, 6, 6, 6, 6, 6, 5, 3],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [5, 6, 6, 6, 6, 6, 6, 6, 6, 5],
                [3, 5, 6, 6, 6, 6, 6, 6, 5, 3],
                [2, 3, 5, 6, 6, 6, 6, 5, 3, 2],
                [2, 2, 3, 5, 5, 5, 5, 3, 2, 2]
            ])

            self.num_fuel = 1
            self.num_moderator = 1

            self.surface_length = self.pitch          # surfaces through wich the probabilities
            self.num_surfaces = 4*self.cell_number    # are evaluated
            self.dir_path = os.path.dirname(os.path.realpath(__file__))
            self.group_constant_files = [
                './group_constant_generation/GroupConst1_res.m',
                './group_constant_generation/GroupConst2_res.m',
                './group_constant_generation/GroupConst3_res.m',
                './group_constant_generation/GroupConst4_res.m',
                './group_constant_generation/GroupConst5_res.m',
                './group_constant_generation/GroupConst6_res.m',
            ]
            self.absolute_path = '/home/hirepan/Documents/chalmers/codes/Shynt/repo/cases/assem1x1_1x1cell/'
            self.detector_fuel = [
                'detectors/fuel1toX_fixed_det0.m',
                'detectors/fuel2toX_fixed_det0.m',
                'detectors/fuel3toX_fixed_det0.m',
                'detectors/fuel4toX_fixed_det0.m',
                'detectors/fuel5toX_fixed_det0.m',
                'detectors/fuel6toX_fixed_det0.m',
            ]
            self.detector_moder = [
                'detectors/moder1toX_fixed5_det0.m',
                'detectors/moder2toX_fixed5_det0.m',
                'detectors/moder3toX_fixed5_det0.m',
                'detectors/moder4toX_fixed5_det0.m',
                'detectors/moder5toX_fixed5_det0.m',
                'detectors/moder6toX_fixed5_det0.m',
            ]
            self.detector_surf = [
                'detectors/surfacetoX1_det0.m',
                'detectors/surfacetoX2_det0.m',
                'detectors/surfacetoX3_det0.m',
                'detectors/surfacetoX4_det0.m',
                'detectors/surfacetoX5_det0.m',
                'detectors/surfacetoX6_det0.m',
            ]

            self.detector_names = [
                'DETrfueltotfast',
                'DETjinfuelfast',
                'DETrmjinfuelfast',
                'DETjoutfuelfast',
                'DETrfueltomodfast',
                'DETrfueltowfast',
                'DETrfueltoefast',
                'DETrfueltosfast',
                'DETrfueltonfast',
                'DETrfueltotthm',
                'DETjinfuelthm',
                'DETrmjinfuelthm',
                'DETjoutfuelthm',
                'DETrfueltomodthm',
                'DETrfueltowthm',
                'DETrfueltoethm',
                'DETrfueltosthm',
                'DETrfueltonthm'
            ]





# Defining isotopes ----------------------------------------------------
u235 = Shynt.materials.Isotope("92235.09c")
u238 = Shynt.materials.Isotope("92238.09c")
oxygen09 = Shynt.materials.Isotope("8016.09c")

oxygen06 = Shynt.materials.Isotope("8016.06c")
hydrogen = Shynt.materials.Isotope("1001.06c")
helium06 = Shynt.materials.Isotope("2004.06c")

zyrconium = Shynt.materials.Isotope("40000.06")

# Montecarlo params and libraries --------------------------------------
mc_params = Shynt.montecarlo.MontecarloParams(2000, 500, 50)
libraries = Shynt.libraries.SerpentLibraries(acelib="/home/segonpin/codesother/Serpent/xsdata/jeff311/sss_jeff311u.xsdata", therm="therm lwtr lwj3.11t")
energy = Shynt.energy.Grid([0, 0.625E-06, 20]) # MeV

# Defining materials -------------------------------------------------
fuel1 = Shynt.materials.Material("fuel1")
fuel1.addIsotope(u235, mass_fraction=0.015867)
fuel1.addIsotope(u238, mass_fraction=0.86563)
fuel1.addIsotope(oxygen09, mass_fraction=0.1185)

fuel2 = Shynt.materials.Material("fuel2")
fuel2.addIsotope(u235, mass_fraction=0.018512)
fuel2.addIsotope(u238, mass_fraction=0.86299)
fuel2.addIsotope(oxygen09, mass_fraction=0.1185)

fuel3 = Shynt.materials.Material("fuel3")
fuel3.addIsotope(u235, mass_fraction=0.022919)
fuel3.addIsotope(u238, mass_fraction=0.85858)
fuel3.addIsotope(oxygen09, mass_fraction=0.1185)

fuel4 = Shynt.materials.Material("fuel4")
fuel4.addIsotope(u235, mass_fraction=0.026445)
fuel4.addIsotope(u238, mass_fraction=0.85505)
fuel4.addIsotope(oxygen09, mass_fraction=0.1185)

fuel5 = Shynt.materials.Material("fuel5")
fuel5.addIsotope(u235, mass_fraction=0.029971)
fuel5.addIsotope(u238, mass_fraction=0.85153)
fuel5.addIsotope(oxygen09, mass_fraction=0.1185)

fuel6 = Shynt.materials.Material("fuel6")
fuel6.addIsotope(u235, mass_fraction=0.032615)
fuel6.addIsotope(u238, mass_fraction=0.84888)
fuel6.addIsotope(oxygen09, mass_fraction=0.1185)

coolant = Shynt.materials.Material("coolant", moder="lwtr 1001")
coolant.addIsotope(oxygen06, atom_fraction=0.33333)
coolant.addIsotope(hydrogen, atom_fraction=0.66667)

clading = Shynt.materials.Material("clading")
clading.addIsotope(zyrconium, atom_fraction=1)

mat_helium = Shynt.materials.Material("helium")
mat_helium.addIsotope(helium06, atom_fraction=1.0)

# -------------------------------------------------------------

pin_fuel1 = Shynt.universes.Pin("pin_fuel1", material=fuel1, radius=0.4335, surroundings=coolant)
pin_fuel2 = Shynt.universes.Pin("pin_fuel2", material=fuel2, radius=0.4335, surroundings=coolant)
pin_fuel3 = Shynt.universes.Pin("pin_fuel3", material=fuel3, radius=0.4335, surroundings=coolant)
pin_fuel4 = Shynt.universes.Pin("pin_fuel4", material=fuel4, radius=0.4335, surroundings=coolant)
pin_fuel5 = Shynt.universes.Pin("pin_fuel5", material=fuel5, radius=0.4335, surroundings=coolant)
pin_fuel6 = Shynt.universes.Pin("pin_fuel6", material=fuel6, radius=0.4335, surroundings=coolant)


lattice =  [
    [pin_fuel2, pin_fuel2, pin_fuel3, pin_fuel5, pin_fuel5, pin_fuel5, pin_fuel5, pin_fuel3, pin_fuel2, pin_fuel2],
    [pin_fuel2, pin_fuel3, pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5, pin_fuel3, pin_fuel2],
    [pin_fuel3, pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5, pin_fuel3],
    [pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5],
    [pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5],
    [pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5],
    [pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5],
    [pin_fuel3, pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5, pin_fuel3],
    [pin_fuel2, pin_fuel3, pin_fuel5, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel6, pin_fuel5, pin_fuel3, pin_fuel2],
    [pin_fuel2, pin_fuel2, pin_fuel3, pin_fuel5, pin_fuel5, pin_fuel5, pin_fuel5, pin_fuel3, pin_fuel2, pin_fuel2]
]

# assembly = Shynt.universes.SquareLattice("assembly", 1.2950, lattice)


































# # defining surfaces ---------------------------------------------------
# cyl1 = Shynt.surfaces.InfiniteCylinder("cyl1", 0, 0, 1.0)
# cyl2 = Shynt.surfaces.InfiniteCylinder("cyl2", 0, 0, 2.5)
# cyl3 = Shynt.surfaces.InfiniteCylinder("cyl3", 0, 0, 4.0)
# cyl4 = Shynt.surfaces.InfiniteCylinder("cyl4", 0, 0, 6.0)
# square = Shynt.surfaces.SquareCylinder("sqr1", 0, 0, 4)

# # creating surface sides (regions) ------------------------------------
# fuel_reg = -cyl2
# gap_reg = -cyl3 & +cyl2
# clad_reg = +cyl3 & -cyl4
# moder_reg = +cyl4 & -square 

# # creating cells
# fuel_c01 = Shynt.cells.Cell("fuel1-pin1", material=fuel1, region=fuel_reg)
# gap_c02 = Shynt.cells.Cell("gap1-pin1", material=mat_helium, region=gap_reg)
# clad_c03 = Shynt.cells.Cell("cladding-pin1", material=clading, region=clad_reg)
# cool_c04 = Shynt.cells.Cell("cool-pin1", material=coolant, region=moder_reg)







Shynt.surfaces.reset_surface_counter()




