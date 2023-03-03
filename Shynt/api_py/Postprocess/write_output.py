import sys
import os
import sys
from pathlib import Path

from Shynt.api_py.Probabilities.probability_writer import write_excel



class OutputFile:

    def __init__(self, root, keff, flux, flux_sigma, iter_number, convergence, mesh_info, nameOut, phi_src, probs):
        self.root = root
        self.keff = keff
        self.flux = flux
        self.flux_sigma = flux_sigma
        self.iterations = iter_number
        self.convergence_keff = convergence[0]
        self.convergence_flux = convergence[1]
        self.mesh_info = mesh_info
        self.phi_src = phi_src
        self.nameOut = nameOut
        self.probs = probs


        input_file_argument = sys.argv[0]
        self.input_file_name = nameOut

        input_file_absolute = str(Path(input_file_argument).absolute())
        input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"

        self.output_dir = input_file_dir + "output_RMM_" + nameOut

        try:
            assert(os.path.isdir(self.output_dir))
        except AssertionError:
            os.mkdir(self.output_dir)
    
        write_excel(probs, mesh_info, root, self.output_dir)

        self.__write()
    

    def __write(self):
        with open(self.output_dir+f"/{self.input_file_name}_rmm.out", "w") as file_:
            file_.write(f"Title: {self.root.name}\n\n")
            file_.write("-------------------------------------------- \n")
            file_.write(self.__write_energy())
            file_.write(f"")
            file_.write("-------------------------------------------- \n")
            file_.write(f"")
            file_.write(f"iterations: {self.iterations}\n")
            file_.write(f"Keff convergence: {self.convergence_keff}\n")
            file_.write(f"Flux convergence: {self.convergence_flux}\n")
            file_.write("-------------------------------------------- \n")
            file_.write(f"Keff: {self.keff}")

        with open(self.output_dir+f"/{self.input_file_name}_rmm_flux.csv", "w") as file_:
            file_.write(self.__write_flux())

        with open(self.output_dir+f"/{self.input_file_name}_rmm_source.csv", "w") as file_:
            file_.write(self.__write_src())
    

    def __write_energy(self):
        statement = ""
        statement += f"Energy structure: {self.root.energy_grid.name}\n"
        statement += f"Energy bins: {self.root.energy_grid.energy_mesh}\n"
        statement += f"Energy groups: {self.root.energy_grid.energy_groups}\n"

        return statement

    def __write_src(self):
        statement = ""
        for src in self.phi_src:
            for val in src:
                statement += f"{val},"
            statement += "\n"
        return statement

    def __write_flux(self):
        numEner = self.root.energy_grid.energy_groups
        coarse_nodes_ids = self.mesh_info.coarse_order
        fine_nodes = self.root.model_cell.local_mesh.fine_nodes

        statement = "Energy_group,coarse_node_id,region_id,material,scalar_flux,sigma,volume\n"
        for g in range(numEner):
            for n_id in coarse_nodes_ids:
                for reg_id, flux in self.flux[g][n_id].items():
                    mat = fine_nodes[n_id][reg_id].cell.content.name
                    vol = fine_nodes[n_id][reg_id].cell.volume
                    statement += f"{g+1},{n_id},{reg_id},{mat},{flux},{self.flux_sigma[g][n_id][reg_id]},{vol}\n"
        return statement


class OutputFileReader:

    def __init__(self):
        pass

    def read(self):
        pass