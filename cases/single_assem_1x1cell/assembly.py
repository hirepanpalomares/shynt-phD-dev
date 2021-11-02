
import numpy as np
import os 
import sys

import Shynt


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
energy_grid = Shynt.energy.Grid([0, 0.625E-06, 20]) # MeV

# Defining materials -------------------------------------------------
fuel1 = Shynt.materials.Material("fuel1", mass_density=10.424)
fuel1.addIsotope(u235, mass_fraction=0.015867)
fuel1.addIsotope(u238, mass_fraction=0.86563)
fuel1.addIsotope(oxygen09, mass_fraction=0.1185)

fuel2 = Shynt.materials.Material("fuel2", mass_density=10.424)
fuel2.addIsotope(u235, mass_fraction=0.018512)
fuel2.addIsotope(u238, mass_fraction=0.86299)
fuel2.addIsotope(oxygen09, mass_fraction=0.1185)

fuel3 = Shynt.materials.Material("fuel3", mass_density=10.424)
fuel3.addIsotope(u235, mass_fraction=0.022919)
fuel3.addIsotope(u238, mass_fraction=0.85858)
fuel3.addIsotope(oxygen09, mass_fraction=0.1185)

fuel4 = Shynt.materials.Material("fuel4", mass_density=10.424)
fuel4.addIsotope(u235, mass_fraction=0.026445)
fuel4.addIsotope(u238, mass_fraction=0.85505)
fuel4.addIsotope(oxygen09, mass_fraction=0.1185)

fuel5 = Shynt.materials.Material("fuel5", mass_density=10.424)
fuel5.addIsotope(u235, mass_fraction=0.029971)
fuel5.addIsotope(u238, mass_fraction=0.85153)
fuel5.addIsotope(oxygen09, mass_fraction=0.1185)

fuel6 = Shynt.materials.Material("fuel6", mass_density=10.424)
fuel6.addIsotope(u235, mass_fraction=0.032615)
fuel6.addIsotope(u238, mass_fraction=0.84888)
fuel6.addIsotope(oxygen09, mass_fraction=0.1185)

coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.6)
coolant.addIsotope(oxygen06, atom_fraction=0.33333)
coolant.addIsotope(hydrogen, atom_fraction=0.66667)

clading = Shynt.materials.Material("clading", mass_density=7.424)
clading.addIsotope(zyrconium, atom_fraction=1)

mat_helium = Shynt.materials.Material("helium", mass_density=0.0424)
mat_helium.addIsotope(helium06, atom_fraction=1.0)

# -------------------------------------------------------------

pin_fuel1 = Shynt.universes.Pin("pin_fuel1", material=fuel1, radius=0.4335)
pin_fuel1.add_level(clading, radius=0.4400)
pin_fuel1.add_level(coolant)

pin_fuel2 = Shynt.universes.Pin("pin_fuel2", material=fuel2, radius=0.4335)
pin_fuel2.add_level(clading, radius=0.4400)
pin_fuel2.add_level(coolant)

pin_fuel3 = Shynt.universes.Pin("pin_fuel3", material=fuel3, radius=0.4335, surroundings=coolant)
pin_fuel4 = Shynt.universes.Pin("pin_fuel4", material=fuel4, radius=0.4335, surroundings=coolant)
pin_fuel5 = Shynt.universes.Pin("pin_fuel5", material=fuel5, radius=0.4335, surroundings=coolant)
pin_fuel6 = Shynt.universes.Pin("pin_fuel6", material=fuel6, radius=0.4335, surroundings=coolant)


lattice_10x10 =  [
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

lattice_2x2 = [
    [pin_fuel1, pin_fuel2],
    [pin_fuel2, pin_fuel1]
]

# assembly_10x10 = Shynt.universes.SquareLattice("assembly", (0.0, 0.0), 1.2950, lattice_10x10)
assembly_2x2 = Shynt.universes.SquareLattice("assembly", (0.0, 0.0), 1.2950, lattice_2x2)



outer_boundary = Shynt.surfaces.InfiniteSquareCylinderZ(1.2950, 1.2950, 1.2950*2, boundary="reflective")

print("#"*50)
# Main problem cell
model_cell = Shynt.cells.Cell(
    "assembly_problem", 
    region=-outer_boundary, 
    fill=assembly_2x2
)


array = model_cell.content.array
# print(array)
# print(array[0][0].get_center(),  array[0][1].get_center())
# print(array[1][0].get_center(),  array[1][1].get_center())

# Make the Global and Local mesh

global_mesh_points = [
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()],
    [(), (), (), (), (), (), (), (), (), (), ()]
]


meshed_model_cell = Shynt.mesh.make_mesh(model_cell, global_mesh_type="pin_cell", local_mesh_type="material")


# Outside world
outside_cell = Shynt.cells.Cell("outside_world", region=+outer_boundary)

# Total Universe (root)
model_universe = Shynt.universes.Root(
    cells=[meshed_model_cell, outside_cell],
    energy_grid=energy_grid, 
    mcparams=mc_params, 
    libraries=libraries
)


Shynt.run(model_universe)


# sudo systemctl enable --now code-server@$USER



