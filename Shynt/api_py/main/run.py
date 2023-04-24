
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice
from Shynt.api_py.Postprocess.write_output import OutputFile
from Shynt.api_py.Serpent.serpent_runners import run_detector_files, run_xs_files
from Shynt.api_py.Probabilities.get_probabilities_system import get_probabilities, check_reciprocity
from Shynt.api_py.CrossSections.get_xs_system import get_xs_data
from Shynt.api_py.ResponseMatrix.iterations import solveKeff, solveKeff_byGroup
from Shynt.api_py.Serpent.file_generator import generate_serpent_files

from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype, InfiniteHexagonalCylinderYtype, InfiniteSquareCylinderZ, reset_surface_counter
from Shynt.api_py.Geometry.cells import reset_cell_counter
from Shynt.api_py.Probabilities.probability_writer import write_excel

import numpy as np



def run(root, server=True, name_out="", serp_dir="serpent_files"):
    
    # Extracting cells from root model
    model_cell = root.model_cell

    energy_g = root.energy_grid.energy_groups
    coarse_nodes = model_cell.global_mesh.coarse_nodes
    coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
    fine_nodes = model_cell.local_mesh.fine_nodes

    # Generating mesh info
    mesh_info = MeshInfo(coarse_nodes, fine_nodes, coarse_nodes_map)
    if isinstance(model_cell.region.surface, InfiniteSquareCylinderZ):
        mesh_info.type_system = "square"
    elif isinstance(model_cell.region.surface, InfiniteHexagonalCylinderXtype):
        mesh_info.type_system = "hexagonal"
    elif isinstance(model_cell.region.surface, InfiniteHexagonalCylinderYtype):
        mesh_info.type_system = "hexagonal"
    
    # ? Checking mesh info --------------------------------------------------------------------------
    # print(mesh_info.equal_nodes_rel)
    # print(mesh_info.coarse_region_rel)
    # print(mesh_info.region_type_rel_switched)
    # ? ---------------------------------------------------------------------------------------------



    # Generate local problems files, and file for cross section generation
    det_inputs, xs_inputs = generate_serpent_files(root, mesh_info.equal_nodes, serp_dir=serp_dir)
    # Running generated files
    run_detector_files(det_inputs)
    run_xs_files(xs_inputs)

    # raise SystemExit
    # get XS and probabilities
    xs = get_xs_data(mesh_info, root, xs_inputs)
    probabilities, prob_sigma = get_probabilities(det_inputs, mesh_info, root, xs)
    
    
    
    reset_surface_counter()
    reset_cell_counter()
    
    # Run detector files 
    # Solve iterative method ----------------------------------------------------
    # solution = solveKeff(root, xs, probabilities, mesh_info, prob_sigma)
    solution = solveKeff_byGroup(root, xs, probabilities, mesh_info, prob_sigma)


    keff = solution["keff"]
    phi = solution["phi"]
    phi_sigma = solution["phi_sigma"]
    keff_convergence = solution["keff_convergence"]
    flux_convergence = solution["flux_convergence"]
    iterations = solution["iterations"]
    phi_src = solution["phi_source"]

    outfile = OutputFile(
        root, keff, phi, phi_sigma, iterations, (keff_convergence, flux_convergence), mesh_info, name_out, phi_src, probabilities
    )
    return keff, phi



