import numpy as np

import Shynt
from Shynt.api_py.Drawer.cell_drawing import plot_cell
from Shynt.api_py.Mesh.mesh_helpers import make_mesh
# from Shynt.api_py.Geometry.mesh import make_mesh


# Defining isotopes ----------------------------------------------------
u235 = Shynt.materials.Isotope("92235.09c")
u238 = Shynt.materials.Isotope("92238.09c")
oxygen09 = Shynt.materials.Isotope("8016.09c")

oxygen06 = Shynt.materials.Isotope("8016.06c")
hydrogen = Shynt.materials.Isotope("1001.06c")
helium06 = Shynt.materials.Isotope("2004.06c")

carbon_nat = Shynt.materials.Isotope("C-nat.03c")
si_28 = Shynt.materials.Isotope("Si-28.03c")
si_29 = Shynt.materials.Isotope("Si-29.03c")
si_30 = Shynt.materials.Isotope("Si-30.03c")
p_31 = Shynt.materials.Isotope("P-31.03c")
ti_46 = Shynt.materials.Isotope("Ti-46.03c")
ti_47 = Shynt.materials.Isotope("Ti-47.03c")
ti_48 = Shynt.materials.Isotope("Ti-48.03c")
ti_49 = Shynt.materials.Isotope("Ti-49.03c")
ti_50 = Shynt.materials.Isotope("Ti-50.03c")
cr_50 = Shynt.materials.Isotope("Cr-50.03c")
cr_52 = Shynt.materials.Isotope("Cr-52.03c")
cr_53 = Shynt.materials.Isotope("Cr-53.03c")
cr_54 = Shynt.materials.Isotope("Cr-54.03c")
mn_55 = Shynt.materials.Isotope("Mn-55.03c")
fe_54 = Shynt.materials.Isotope("Fe-54.03c")
fe_56 = Shynt.materials.Isotope("Fe-56.03c")
fe_57 = Shynt.materials.Isotope("Fe-57.03c")
fe_58 = Shynt.materials.Isotope("Fe-58.03c")
ni_58 = Shynt.materials.Isotope("Ni-58.03c")
ni_60 = Shynt.materials.Isotope("Ni-60.03c")
ni_61 = Shynt.materials.Isotope("Ni-61.03c")
ni_62 = Shynt.materials.Isotope("Ni-62.03c")
ni_64 = Shynt.materials.Isotope("Ni-64.03c")
mo_92 = Shynt.materials.Isotope("Mo-92.03c")
mo_94 = Shynt.materials.Isotope("Mo-94.03c")
mo_95 = Shynt.materials.Isotope("Mo-95.03c")
mo_96 = Shynt.materials.Isotope("Mo-96.03c")
mo_97 = Shynt.materials.Isotope("Mo-97.03c")
mo_98 = Shynt.materials.Isotope("Mo-98.03c")
mo_100 = Shynt.materials.Isotope("Mo-100.03c")

# Montecarlo params and libraries --------------------------------------
mc_params = Shynt.montecarlo.MontecarloParams(5000, 1500, 250)
libraries = Shynt.libraries.SerpentLibraries(acelib='"jeff311/sss_jeff311u.xsdata"', therm="therm lwtr lwj3.11t")
energy_grid = Shynt.energy.Grid([0, 0.625E-06, 20], name="2groups_grid") # MeV

# Defining materials -------------------------------------------------
fuel1 = Shynt.materials.Material("fuel1", mass_density=10.424, color=(255, 255, 102))
fuel1.addIsotope(u235, mass_fraction=0.015867)
fuel1.addIsotope(u238, mass_fraction=0.86563)
fuel1.addIsotope(oxygen09, mass_fraction=0.1185)

fuel2 = Shynt.materials.Material("fuel2", mass_density=10.424, color=(255, 153, 51))
fuel2.addIsotope(u235, mass_fraction=0.018512)
fuel2.addIsotope(u238, mass_fraction=0.86299)
fuel2.addIsotope(oxygen09, mass_fraction=0.1185)

fuel3 = Shynt.materials.Material("fuel3", mass_density=10.424, color=(255, 102, 102))
fuel3.addIsotope(u235, mass_fraction=0.022919)
fuel3.addIsotope(u238, mass_fraction=0.85858)
fuel3.addIsotope(oxygen09, mass_fraction=0.1185)

fuel4 = Shynt.materials.Material("fuel4", mass_density=10.424, color=(255, 102, 204))
fuel4.addIsotope(u235, mass_fraction=0.026445)
fuel4.addIsotope(u238, mass_fraction=0.85505)
fuel4.addIsotope(oxygen09, mass_fraction=0.1185)

fuel5 = Shynt.materials.Material("fuel5", mass_density=10.424, color=(204, 204, 0))
fuel5.addIsotope(u235, mass_fraction=0.029971)
fuel5.addIsotope(u238, mass_fraction=0.85153)
fuel5.addIsotope(oxygen09, mass_fraction=0.1185)

fuel6 = Shynt.materials.Material("fuel6", mass_density=10.424, color=(230,60,200))
fuel6.addIsotope(u235, mass_fraction=0.032615)
fuel6.addIsotope(u238, mass_fraction=0.84888)
fuel6.addIsotope(oxygen09, mass_fraction=0.1185)

coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.443760, color=(102, 204, 255))
coolant.addIsotope(oxygen06, atom_fraction=0.33333)
coolant.addIsotope(hydrogen, atom_fraction=0.66667)

composition_cladding = {
    "fractions": [
        (carbon_nat, 1.97913e-04), (si_28, 9.39458e-04), (si_29, 4.60789e-05), (si_30, 2.93992e-05),
        (p_31, 4.60060e-05), (ti_46, 3.41106e-05), (ti_47, 3.01070e-05), (ti_48, 2.92121e-04),
        (ti_49, 2.09995e-05), (ti_50, 1.97055e-05), (cr_50, 6.61142e-04), (cr_52, 1.22599e-02),
        (cr_53, 1.36391e-03), (cr_54, 3.33224e-04), (mn_55, 1.46981e-03), (fe_54, 3.33120e-03),
        (fe_56, 5.04275e-02), (fe_57, 1.14412e-03), (fe_58, 1.49639e-04), (ni_58, 7.81396e-03),
        (ni_60, 2.90969e-03), (ni_61, 1.24406e-04), (ni_62, 3.90285e-04), (ni_64, 9.62720e-05),
        (mo_92, 1.87735e-04), (mo_94, 1.15707e-04), (mo_95, 1.98193e-04), (mo_96, 2.06406e-04),
        (mo_97, 1.17638e-04), (mo_98, 2.95822e-04), (mo_100, 1.16718e-04)
    ],
    "type": "atom_density"
}
cladding = Shynt.materials.Material("cladding", composition=composition_cladding, options="sum tmp 453", color=(108, 112, 115))

# -------------------------------------------------------------
pin1 = Shynt.universes.Pin("pin_fuel1")
pin1.add_pin_levels([fuel1, cladding, coolant],[0.4335, 0.5, None])

pin2 = Shynt.universes.Pin("pin_fuel2")
pin2.add_pin_levels([fuel2, cladding, coolant],[0.4335, 0.5, None])

pin3 = Shynt.universes.Pin("pin_fuel3")
pin3.add_pin_levels([fuel3, cladding, coolant],[0.4335, 0.5, None])

pin4 = Shynt.universes.Pin("pin_fuel4")
pin4.add_pin_levels([fuel4, cladding, coolant],[0.4335, 0.5, None])

pin5 = Shynt.universes.Pin("pin_fuel5")
pin5.add_pin_levels([fuel5, cladding, coolant],[0.4335, 0.5, None])

pin6 = Shynt.universes.Pin("pin_fuel6")
pin6.add_pin_levels([fuel6, cladding, coolant],[0.4335, 0.5, None])


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
# Outside world
outside_cell = Shynt.cells.Cell("outside_world", fill="outside", region=+outer_boundary)

# meshed cell
model_cell_meshed = make_mesh(model_cell, global_mesh_type="pin_cell", local_mesh_type="material")


# Total Universe (root)
model_universe = Shynt.universes.Root(
    model_cell_meshed, outside_cell,
    energy_grid=energy_grid, 
    mcparams=mc_params, 
    libraries=libraries
)


plot_cell(model_cell, dimensions=(3000,3000), name="square 10x10_lattice_")
