import sys
import os
import sys
from pathlib import Path



class OutputFile:

    def __init__(self, root, keff, flux, iter_number, convergence, mesh_info):
        self.root = root
        self.keff = keff
        self.flux = flux
        self.iterations = iter_number
        self.convergence_keff = convergence[0]
        self.convergence_flux = convergence[1]
        self.mesh_info = mesh_info

        input_file_argument = sys.argv[0]
        self.input_file_name = input_file_argument.split("/")[-1]
        self.input_file_name = self.input_file_name.split(".")[0]

        input_file_absolute = str(Path(input_file_argument).absolute())
        input_file_dir = "/".join(input_file_absolute.split("/")[:-1]) + "/"

        self.output_dir = input_file_dir + "output_RMM"
    

        try:
            assert(os.path.isdir(self.output_dir))
        except AssertionError:
            os.mkdir(self.output_dir)

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

        with open(self.output_dir+f"/{self.input_file_name}_rmm_flux.out", "w") as file_:
            file_.write(self.__write_flux())
    

    def __write_energy(self):
        statement = ""
        statement += f"Energy structure: {self.root.energy_grid.name}\n"
        statement += f"Energy bins: {self.root.energy_grid.energy_mesh}\n"
        statement += f"Energy groups: {self.root.energy_grid.energy_groups}\n"

        return statement

    def __write_flux(self):
        numEner = self.root.energy_grid.energy_groups
        coarse_nodes = self.mesh_info.coarse_order

        statement = "Energy_group, coarse_node_id, region_id, scalar_flux\n"
        for g in range(numEner):
            for n_id in coarse_nodes:
                for reg_id, flux in self.flux[g][n_id].items():
                    statement += f"{g+1}, {n_id}, {reg_id}, {flux}\n"
        return statement


class OutputFileReader:

    def __init__(self):
        pass

    def read(self):
        pass