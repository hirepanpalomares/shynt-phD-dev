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
mc_params = Shynt.montecarlo.MontecarloParams(2000, 500, 50, seed=1474468046)
libraries = Shynt.libraries.SerpentLibraries(acelib='"jeff311/sss_jeff311u.xsdata"', therm="therm lwtr lwj3.11t")
energy_grid = Shynt.energy.Grid([0, 0.625E-06, 20], name="2groups_grid") # MeV

# Defining materials -------------------------------------------------
fuel1 = Shynt.materials.Material("fuel1", mass_density=10.424)
fuel1.addIsotope(u235, mass_fraction=0.015867)
fuel1.addIsotope(u238, mass_fraction=0.86563)
fuel1.addIsotope(oxygen09, mass_fraction=0.1185)

coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.443760)
coolant.addIsotope(oxygen06, atom_fraction=0.33333)
coolant.addIsotope(hydrogen, atom_fraction=0.66667)

clading = Shynt.materials.Material("clading", mass_density=7.5)
clading.addIsotope(zyrconium, atom_fraction=1)

mat_helium = Shynt.materials.Material("helium", mass_density=0.03)
mat_helium.addIsotope(helium06, atom_fraction=1.0)

# Defining pin universe ---------------------------------------

pin_fuel1 = Shynt.universes.Pin("pin_fuel1")
# mat_lev = [fuel1, mat_helium, clading, coolant]
# rad_lev = [0.4335, 0.4600, 0.5000, None]
mat_lev = [fuel1, coolant]
rad_lev = [0.4335, None]
pin_fuel1.add_pin_levels(mat_lev, rad_lev)
#print(pin_fuel1.pin_levels[0].cell.material.serpent_syntax)

outer_boundary = Shynt.surfaces.InfiniteSquareCylinderZ(0.0, 0.0, 0.6475, boundary="reflective")

reg = -outer_boundary

# a cell
model_cell = Shynt.cells.Cell("pin_problem", region=-outer_boundary, fill=pin_fuel1)


# still a cell
meshed_model_cell = Shynt.mesh.make_mesh(model_cell, global_mesh_type="pin_cell", local_mesh_type="material")


# Outside world
outside_cell = Shynt.cells.Cell("outside_world", region=+outer_boundary)



# Total Unverse (root)
model_universe = Shynt.universes.Root(
    [meshed_model_cell, outside_cell], 
    energy_grid=energy_grid, 
    mcparams=mc_params, 
    libraries=libraries, 
)




Shynt.run(model_universe)