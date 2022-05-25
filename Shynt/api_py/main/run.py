
from Shynt.api_py.Geometry.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice
from Shynt.api_py.Postprocess.write_output import OutputFile
from Shynt.api_py.Serpent.serpent_runners import run_detector_files, run_xs_files
from Shynt.api_py.Probabilities.get_probabilities_system import get_probabilities_data
from Shynt.api_py.CrossSections.get_xs_system import get_xs_data
from Shynt.api_py.ResponseMatrix.iterations import solveKeff
from Shynt.api_py.Serpent.file_generator import generate_serpent_files

from Shynt.api_py.Geometry.surfaces import reset_surface_counter
from Shynt.api_py.Geometry.cells import reset_cell_counter



def run(root):
    
    # Extracting cells from root model
    model_cell = root.model_cell
    outside_cell = root.outside_cell

    energy_g = root.energy_grid.energy_groups
    coarse_nodes = model_cell.global_mesh.coarse_nodes
    coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
    fine_nodes = model_cell.local_mesh.fine_nodes

    # Generating mesh info
    mesh_info = MeshInfo(coarse_nodes, fine_nodes, coarse_nodes_map)
    if isinstance(model_cell.content, SquareLattice):
        mesh_info.type_system = "squared"
    elif isinstance(model_cell.content, HexagonalLatticeTypeX):
        mesh_info.type_system = "hexagonal"
    
    # Generate local problems files, and file for cross section generation
    det_inputs, xs_inputs = generate_serpent_files(root, mesh_info.equal_nodes)
    
    # Running generated files
    run_detector_files(det_inputs)
    run_xs_files(xs_inputs)

    # get XS and probabilities
    probabilities = get_probabilities_data(det_inputs, mesh_info, coarse_nodes, fine_nodes, energy_g)
    xs = get_xs_data(mesh_info, coarse_nodes, fine_nodes, energy_g, xs_inputs)


    reset_surface_counter()
    reset_cell_counter()

    # Run detector files 
    # Solve iterative method ----------------------------------------------------
    solution = solveKeff(
        coarse_nodes,
        energy_g, 
        xs, 
        probabilities, 
        mesh_info
    )

    keff = solution["keff"]
    phi = solution["phi"]
    keff_convergence = solution["keff_convergence"]
    flux_convergence = solution["flux_convergence"]
    iterations = solution["iterations"]

    outfile = OutputFile(
        root, keff, phi, iterations, (keff_convergence, flux_convergence), mesh_info
    )

    return keff, phi



