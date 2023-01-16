
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice
from Shynt.api_py.Postprocess.write_output import OutputFile
from Shynt.api_py.Serpent.serpent_runners import run_detector_files, run_xs_files
from Shynt.api_py.Probabilities.get_probabilities_system import get_probabilities, check_reciprocity
from Shynt.api_py.CrossSections.get_xs_system import get_xs_data
from Shynt.api_py.ResponseMatrix.iterations import solveKeff
from Shynt.api_py.Serpent.file_generator import generate_serpent_files

from Shynt.api_py.Geometry.surfaces import InfiniteHexagonalCylinderXtype, InfiniteHexagonalCylinderYtype, InfiniteSquareCylinderZ, reset_surface_counter
from Shynt.api_py.Geometry.cells import reset_cell_counter
from Shynt.api_py.Probabilities.probability_writer import write_excel

import numpy as np



def generate_MeshInfo(root):

    # Extracting cells from root model
    model_cell = root.model_cell
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
    # elif isinstance(model_cell.content, HexagonalLatticeTypeY):
    #     mesh_info.type_system = "hexagonal_y"

    return mesh_info


# def generate_serpent_files(root):
#     mesh_info = generate_MeshInfo(root)

#     # Generate local problems files, and file for cross section generation
#     det_inputs, xs_inputs = generate_serpent_files(root, mesh_info.equal_nodes, serp_dir)

#     return det_inputs, xs_inputs


def run_RMM(root, serpent_files, name_out=""):
     
    mesh_info = generate_MeshInfo(root)

    det_inputs, xs_inputs = serpent_files

    # get XS and probabilities
    probabilities = get_probabilities(det_inputs, mesh_info, root)
    xs = get_xs_data(mesh_info, root, xs_inputs)
    write_excel(probabilities, mesh_info, root)
    
    reset_surface_counter()
    reset_cell_counter()

    # Run detector files 
    # Solve iterative method ----------------------------------------------------
    solution = solveKeff(
        root,
        xs, 
        probabilities, 
        mesh_info
    )

    keff = solution["keff"]
    phi = solution["phi"]
    keff_convergence = solution["keff_convergence"]
    flux_convergence = solution["flux_convergence"]
    iterations = solution["iterations"]
    phi_src = solution["phi_source"]

    outfile = OutputFile(
        root, keff, phi, iterations, (keff_convergence, flux_convergence), mesh_info, name_out, phi_src
    )

    return keff, phi
    

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
    # elif isinstance(model_cell.content, HexagonalLatticeTypeY):
    #     mesh_info.type_system = "hexagonal_y"
    

    # Generate local problems files, and file for cross section generation
    det_inputs, xs_inputs = generate_serpent_files(root, mesh_info.equal_nodes, serp_dir=serp_dir)
    
    # raise SystemExit    
    # Running generated files
    run_detector_files(det_inputs)
    run_xs_files(xs_inputs)

    # raise SystemExit
    # get XS and probabilities
    xs = get_xs_data(mesh_info, root, xs_inputs)
    probabilities = get_probabilities(det_inputs, mesh_info, root, xs)
    
    
    reset_surface_counter()
    reset_cell_counter()
    # raise SystemExit
    
    # Run detector files 
    # Solve iterative method ----------------------------------------------------
    solution = solveKeff(
        root,
        xs, 
        probabilities, 
        mesh_info
    )

    keff = solution["keff"]
    phi = solution["phi"]
    keff_convergence = solution["keff_convergence"]
    flux_convergence = solution["flux_convergence"]
    iterations = solution["iterations"]
    phi_src = solution["phi_source"]

    outfile = OutputFile(
        root, keff, phi, iterations, (keff_convergence, flux_convergence), mesh_info, name_out, phi_src, probabilities
    )

    return keff, phi



