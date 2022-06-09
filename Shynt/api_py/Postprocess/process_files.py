
from os import system
from Shynt.api_py.Geometry.mesh_info import MeshInfo
from Shynt.api_py.Geometry.universes import HexagonalLatticeTypeX, SquareLattice

import serpentTools
import csv


def regions_to_plot(root_universe, line="", code=""):
    # Extracting cells from root model
    model_cell = root_universe.model_cell
    outside_cell = root_universe.outside_cell

    coarse_nodes = model_cell.global_mesh.coarse_nodes
    coarse_nodes_map = model_cell.global_mesh.coarse_nodes_map
    fine_nodes = model_cell.local_mesh.fine_nodes

    # Generating mesh info
    mesh_info = MeshInfo(coarse_nodes, fine_nodes, coarse_nodes_map)
    if isinstance(model_cell.content, SquareLattice):
        mesh_info.type_system = "squared"
    elif isinstance(model_cell.content, HexagonalLatticeTypeX):
        mesh_info.type_system = "hexagonal"

    map_system = mesh_info.coarse_nodes_map

    print(map_system)
    # First the coarse nodes ........................................................
    coarse_nodes_to_plot = []
    if line == "diagonal":
        coarse_nodes_to_plot = [map_system[c][c] for c in range(len(map_system))]
    
    # Then the regions of the node ..................................................
    regions_to_plot = []
    for c_id in coarse_nodes_to_plot:
        regions_mat_rel = mesh_info.region_type_rel[c_id]
        if code == "serp":
            regions_to_plot.append(regions_mat_rel["other"])
            regions_to_plot.append(regions_mat_rel["fuel"])
            regions_to_plot.append(regions_mat_rel["other"])
        elif code == "hybrid":
            regions_to_plot.append(regions_mat_rel["fuel"])
            regions_to_plot.append(regions_mat_rel["other"])
            regions_to_plot.append(regions_mat_rel["fuel"])

    return regions_to_plot


def get_flux_from_detector_file(det_out_file):
    system_serp = serpentTools.read(det_out_file)
    detectors = system_serp.detectors
    flux = detectors["flux_by_cell_by_group"].tallies
    errors = detectors["flux_by_cell_by_group"].errors
    
    return flux, errors


def get_flux_from_shynt_output(out_file):
    flux = {}
    with open(out_file, newline='') as csvfile:
        flux_reader = csv.reader(csvfile)
        for row in flux_reader:
            try:
                energ = int(row[0].split()[0]) - 1
                coarse_id = int(row[1].split()[0])
                reg_id = int(row[2].split()[0])
                material = row[3].split()[0]
                scalar_flux = float(row[4].split()[0])    
                if energ not in flux:
                    flux[energ] = {
                        reg_id: scalar_flux
                    }
                else:
                    flux[energ][reg_id] = scalar_flux
            except ValueError:
                # do nothing
                pass
    return flux
    