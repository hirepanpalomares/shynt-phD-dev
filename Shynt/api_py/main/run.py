
from Shynt.api_py.Mesh.mesh_info import MeshInfo
from Shynt.api_py.Postprocess.write_output import OutputFile
from Shynt.api_py.Serpent.serpent_runners import run_detector_files, run_xs_files
from Shynt.api_py.Probabilities.get_probabilities_system import get_probabilities
from Shynt.api_py.CrossSections.get_xs_system import get_xs_data
from Shynt.api_py.ResponseMatrix.iterations import solveKeff_byGroup
from Shynt.api_py.Serpent.file_generator import generate_serpent_files

from Shynt.api_py.Geometry.cells import reset_cell_counter
from Shynt.api_py.Geometry.surfaces import reset_surface_counter


def run(
  root, server=True, name_out="", serp_dir="serpent_files", 
  run_serpent_files=True, run_RMM=True
):
    
  # Extracting model cell root model ------------------------------------------
  model_cell = root.cell

  # Generating mesh info ------------------------------------------------------
  mesh_info = MeshInfo(model_cell)
  
  # Generate local problems files, and file for cross section generation ------
  det_inputs, xs_inputs = generate_serpent_files(
    root, mesh_info.equal_nodes, serp_dir=serp_dir
  )
  
  # Running generated files ---------------------------------------------------
  if run_serpent_files:
    run_detector_files(det_inputs)
    run_xs_files(xs_inputs)

  keff = 1
  phi = []
  xs = {}
  if run_RMM:
    # get XS and probabilities ------------------------------------------------
    xs = get_xs_data(mesh_info, root, xs_inputs)
    probabilities, prob_sigma = get_probabilities(
      det_inputs, mesh_info, root, xs
    )
    reset_surface_counter()
    reset_cell_counter()
  
    # Solve iterative method --------------------------------------------------
    # solution = solveKeff(root, xs, probabilities, mesh_info, prob_sigma)
    solution = solveKeff_byGroup(
      root, xs, probabilities, mesh_info, prob_sigma
    )

    keff = solution["keff"]
    phi = solution["phi"]
    phi_sigma = solution["phi_sigma"]
    keff_convergence = solution["keff_convergence"]
    flux_convergence = solution["flux_convergence"]
    iterations = solution["iterations"]
    phi_src = solution["phi_source"]

    outfile = OutputFile(
      root, 
      keff, 
      phi,
      xs,
      phi_sigma, 
      iterations, 
      (keff_convergence, flux_convergence), 
      mesh_info, 
      name_out, 
      phi_src, 
      probabilities
    )
  
  return keff, phi



