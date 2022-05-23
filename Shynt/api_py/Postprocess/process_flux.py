
from os import system
from Shynt.api_py.Geometry.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice

import serpentTools
import csv


def plot_flux(serp_root_file, root_universe):
    # Extracting cells from root model
    model_cell = root_universe.model_cell
    outside_cell = root_universe.outside_cell

    energy_g = root_universe.energy_grid.energy_groups
    coarse_nodes = model_cell.global_mesh.coarse_nodes
    coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
    fine_nodes = model_cell.local_mesh.fine_nodes

    # Generating mesh info
    mesh_info = MeshInfo(coarse_nodes, fine_nodes, coarse_nodes_map)
    if isinstance(model_cell.content, SquareLattice):
        mesh_info.type_system = "squared"
    elif isinstance(model_cell.content, HexagonalLatticeTypeX):
        mesh_info.type_system = "hexagonal"
    
    cells_ids_in_detectors = list(serp_root_file.cells_for_flux.keys())
    detector_out_file = serp_root_file.name + "_det0.m"

    serp_flux, serp_errors = get_flux_from_detector_file(detector_out_file)
    shynt_flux = get_flux_from_shynt_output()

    pass


def get_flux_from_detector_file(det_out_file):
    system_serp = serpentTools.read(det_out_file)
    detectors = system_serp.detectors
    flux = detectors.tallies
    errors = detectors.errors
    
    return flux, errors


def get_flux_from_shynt_output(out_file):

    pass
    