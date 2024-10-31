import os
import unittest

import Shynt
from Shynt.api_py.ResponseMatrix.build_matrix_M import getM_matrix

import numpy as np

from Shynt.api_py.main.run_helpers import get_mesh_info


class TestJointCellVolume(unittest.TestCase):

    def test_matrix(self):
        # print("\n\n")
        
        a = np.array([
            [2,5],
            [3,1]
        ])

        b = np.array([
            [7,3],
            [1,4]
        ])
        c = np.array([
            [4,1],
            [3,10]
        ]) 

        vector = np.array([2,2])
        inv = np.linalg.inv(a)
        # print(a[0]*vector)
        # print("\n\n")
        assert 1 == 1


class TestTopoligcalRelation(unittest.TestCase):

    def test_matrix_calculation(self):
        Shynt.surfaces.reset_surface_counter()
        Shynt.cells.reset_cell_counter()
        # Montecarlo params and libraries --------------------------------------
        mc_params = Shynt.montecarlo.MontecarloParams(2000, 500, 50, seed=1474468046)
        libraries = Shynt.libraries.SerpentLibraries(acelib='"jeff311/sss_jeff311u.xsdata"', therm="therm lwtr lwj3.11t")
        energy_grid = Shynt.energy.Grid([0, 0.625E-06, 20], name="2groups_grid") # MeV

        # Defining isotopes ----------------------------------------------------
        u235 = Shynt.materials.Isotope("92235.09c")
        u238 = Shynt.materials.Isotope("92238.09c")
        oxygen09 = Shynt.materials.Isotope("8016.09c")

        oxygen06 = Shynt.materials.Isotope("8016.06c")
        hydrogen = Shynt.materials.Isotope("1001.06c")

        # Defining materials -------------------------------------------------
        fuel1 = Shynt.materials.Material("fuel1", mass_density=10.424)
        fuel1.addIsotope(u235, mass_fraction=0.015867)
        fuel1.addIsotope(u238, mass_fraction=0.86563)
        fuel1.addIsotope(oxygen09, mass_fraction=0.1185)

        fuel2 = Shynt.materials.Material("fuel2", mass_density=10.424)
        fuel2.addIsotope(u235, mass_fraction=0.018512)
        fuel2.addIsotope(u238, mass_fraction=0.86299)
        fuel2.addIsotope(oxygen09, mass_fraction=0.1185)

        coolant = Shynt.materials.Material("coolant", moder="lwtr 1001", mass_density=0.443760)
        coolant.addIsotope(oxygen06, atom_fraction=0.33333)
        coolant.addIsotope(hydrogen, atom_fraction=0.66667)

        pin1 = Shynt.universes.Pin("pin_fuel1", material=fuel1, radius=0.4335, surroundings=coolant)
        pin2 = Shynt.universes.Pin("pin_fuel2", material=fuel2, radius=0.4335, surroundings=coolant)


        lattice_2x2 =  [
            [pin1, pin2],
            [pin2, pin1]
        ]

        assembly_2x2 = Shynt.universes.SquareLattice("assembly", (0.0, 0.0), 1.295, lattice_2x2)

        outer_boundary = Shynt.surfaces.InfiniteSquareCylinderZ(0, 0, 1.2950, boundary="reflective")

        # Main problem cell
        model_cell = Shynt.cells.Cell("assembly_problem", region=-outer_boundary, fill=assembly_2x2)

        # meshed cell
        model_cell_meshed = Shynt.mesh.make_mesh(model_cell, global_mesh_type="pin_cell", local_mesh_type="material")
    
        coarse_nodes = model_cell_meshed.global_mesh.coarse_nodes
        coarse_nodes_map = model_cell_meshed.global_mesh.coarse_nodes_map
        fine_nodes = model_cell_meshed.local_mesh.fine_nodes

        mesh_info = get_mesh_info(coarse_nodes, fine_nodes, coarse_nodes_map)
        all_surfaces = mesh_info.all_surfaces_order
        matrixM_test = getM_matrix(coarse_nodes_map, coarse_nodes, all_surfaces) # ready 


        mM_base = np.array([
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  #   ->   5
            [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],  #   ->   6
            [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],  #   ->   8
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],  #   ->   7
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  #   ->   11
            [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],  #   ->   12
            [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],  #   ->   14
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],  #   ->   13
            [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],  #   ->   17
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],  #   ->   18
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],  #   ->   20
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],  #   ->   19
            [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],  #   ->   23
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],  #   ->   24
            [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],  #   ->   26
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],  #   ->   25
        ])

        assert (mM_base == matrixM_test).all()
        

    
        

if __name__ == "__main__":
    unittest.main()