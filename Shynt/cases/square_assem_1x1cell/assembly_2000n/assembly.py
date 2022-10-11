import numpy as np

import Shynt
from Shynt.api_py.Mesh.mesh_helpers import make_mesh
# from Shynt.api_py.Geometry.mesh import make_mesh


# Defining isotopes ----------------------------------------------------
u235 = Shynt.materials.Isotope("92235.09c")
u238 = Shynt.materials.Isotope("92238.09c")
oxygen09 = Shynt.materials.Isotope("8016.09c")

oxygen06 = Shynt.materials.Isotope("8016.06c")
hydrogen = Shynt.materials.Isotope("1001.06c")
helium06 = Shynt.materials.Isotope("2004.06c")

zyrconium = Shynt.materials.Isotope("40000.06")

# Montecarlo params and libraries --------------------------------------
mc_params = Shynt.montecarlo.MontecarloParams(2000, 500, 50, seed=1474468046)
libraries = Shynt.libraries.SerpentLibraries(acelib='"jeff311/sss_jeff311u.xsdata"', therm="therm lwtr lwj3.11t")
energy_grid = Shynt.energy.Grid([0, 0.625E-06, 20], name="2groups_grid") # MeV

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

coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.443760)
coolant.addIsotope(oxygen06, atom_fraction=0.33333)
coolant.addIsotope(hydrogen, atom_fraction=0.66667)

# -------------------------------------------------------------
pin1 = Shynt.universes.Pin("pin_fuel1")
pin1.add_pin_levels([fuel1, coolant],[0.4335, None])

pin2 = Shynt.universes.Pin("pin_fuel2")
pin2.add_pin_levels([fuel2, coolant],[0.4335, None])

pin3 = Shynt.universes.Pin("pin_fuel3")
pin3.add_pin_levels([fuel3, coolant],[0.4335, None])

pin4 = Shynt.universes.Pin("pin_fuel4")
pin4.add_pin_levels([fuel4, coolant],[0.4335, None])

pin5 = Shynt.universes.Pin("pin_fuel5")
pin5.add_pin_levels([fuel5, coolant],[0.4335, None])

pin6 = Shynt.universes.Pin("pin_fuel6")
pin6.add_pin_levels([fuel6, coolant],[0.4335, None])


lattice_10x10 =  [
    [pin2, pin2, pin3, pin5, pin5, pin5, pin5, pin3, pin2, pin2],
    [pin2, pin3, pin5, pin6, pin6, pin6, pin6, pin5, pin3, pin2],
    [pin3, pin5, pin6, pin6, pin6, pin6, pin6, pin6, pin5, pin3],
    [pin5, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin5],
    [pin5, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin5],
    [pin5, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin5],
    [pin5, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin6, pin5],
    [pin3, pin5, pin6, pin6, pin6, pin6, pin6, pin6, pin5, pin3],
    [pin2, pin3, pin5, pin6, pin6, pin6, pin6, pin5, pin3, pin2],
    [pin2, pin2, pin3, pin5, pin5, pin5, pin5, pin3, pin2, pin2]
]

assembly_10x10 = Shynt.universes.SquareLattice("assembly", (0.0, 0.0), 1.295, lattice_10x10)

outer_boundary = Shynt.surfaces.InfiniteSquareCylinderZ(0, 0, 1.2950*5, boundary="reflective")

# Main problem cell
model_cell = Shynt.cells.Cell("assembly_problem", region=-outer_boundary, fill=assembly_10x10)

# meshed cell
model_cell_meshed = make_mesh(model_cell, global_mesh_type="pin_cell", local_mesh_type="material")




# Outside world
outside_cell = Shynt.cells.Cell("outside_world", fill="outside", region=+outer_boundary)

# Total Universe (root)
model_universe = Shynt.universes.Root(
    model_cell_meshed, outside_cell,
    energy_grid=energy_grid, 
    mcparams=mc_params, 
    libraries=libraries
)


