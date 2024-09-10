import sys
import os
import sys
from pathlib import Path
import numpy as np

from Shynt.api_py.Serpent.output_reader import read_res_file_metadata

class OutputFile:
  
  def __init__(self, 
    root, xs, probabilities, solution_data, nameOut
  ):
    self.root = root
    self.xs = xs

    self.keff_array = solution_data["keff"]
    self.flux = solution_data["phi"]
    self.flux_sigma = solution_data["phi_sigma"]
    self.jin = solution_data['jin']
    self.jout = solution_data['jout']

    self.convergence_keff = solution_data["keff_convergence"]
    self.convergence_flux = solution_data["phi_convergence"]
    self.iterations = solution_data["iterations"]
    self.transport_iterations = solution_data["transport_iterations"]
    self.phi_src = solution_data["phi_source"]
    self.time_matrixes = solution_data['time_matrixes']
    self.time_iter = solution_data['time_iterations']
    self.omp = solution_data['omp']

    self.mesh = root.mesh
    self.nameOut = nameOut
    self.probs = probabilities

    self.cpu_tot = 0.0
    
    print("Printing output ....")
    input_file_dir = os.getcwd() + '/'
    self.output_dir = input_file_dir + "output_RMM_" + nameOut
    try:
      assert(os.path.isdir(self.output_dir))
    except AssertionError:
      os.mkdir(self.output_dir)
    self.__write()
    print("Done")
  
  def calculate_computing_time(self):
    message = ""
    total_cputime = 0
    total_wall_time = 0
    for nid, data_files in self.root.detector_files.items():
      for dfl in data_files:
        message += '++++++++++++++++++\n'
        name = '/'.join(dfl['name'].split('/')[-3:])
        message += f"{name}\n"
        
        resFile = dfl['name'] + "_res.m"
        metadata = read_res_file_metadata(resFile)
        message += f"CPU:\t {metadata['CPU_TYPE']}\n"
        message += f"CPU time [min]:\t {metadata['TOT_CPU_TIME']}\n"
        message += f"Wall-clock time [min]:\t {metadata['RUNNING_TIME']}\n"
        message += f"OMP threads:\t {metadata['OMP_THREADS']}\n"
        message += f"MPI tasks:\t {metadata['MPI_TASKS']}\n"
        total_cputime += metadata['TOT_CPU_TIME']
        total_wall_time += metadata['RUNNING_TIME']
    message += '++++++++++++++++++\n'
    message += "Cross Sections generation\n"
    for nid, xs_file in self.root.xs_files.items():
      print(xs_file.name)
      name = '/'.join(xs_file.name.split('/')[-3:])
      message += f"{name}\n"
      
      resFile = xs_file.name + "_res.m"
      res = read_res_file_metadata(resFile)
      message += f"CPU:\t {metadata['CPU_TYPE']}\n"
      message += f"CPU time [min]:\t {metadata['TOT_CPU_TIME']}\n"
      message += f"Wall-clock time [min]:\t {metadata['RUNNING_TIME']}\n"
      message += f"OMP threads:\t {metadata['OMP_THREADS']}\n"
      message += f"MPI tasks:\t {metadata['MPI_TASKS']}\n"
      total_cputime += metadata['TOT_CPU_TIME']
      total_wall_time += metadata['RUNNING_TIME']


    message += "---------------------------------------------------------\n"
    message += f'TOTAL WALL CLOCK TIME [min]: \t {int(total_wall_time)}\n'
    message += f'TOTAL CPU TIME [min]: \t {int(total_cputime)}\n'

    self.cpu_tot = total_cputime

    return message


  def __write(self):
    with open(
      self.output_dir+f"/{self.nameOut}_rmm.out", "w"
    ) as f_:
      f_.write(f"Title: {self.root.name}\n\n")
      f_.write("-------------------------------------------- \n")
      f_.write(self.__write_energy())
      f_.write(f"")
      f_.write("-------------------------------------------- \n")
      f_.write(f"")
      f_.write(f"iterations: {self.iterations}\n")
      f_.write(f"Keff convergence: {self.convergence_keff}\n")
      f_.write(f"Flux convergence: {np.max(self.convergence_flux)}\n")
      f_.write(f"Time matrixes: {self.time_matrixes}\n")
      f_.write(f'Total CPU time Power Iteration: {self.time_iter} seconds\n')
      f_.write(f'Total CPU time ICM: {self.time_matrixes+self.time_iter} seconds\n')
      f_.write(f'openMP ICM: {self.omp}\n')
      f_.write("-------------------------------------------- \n")
      f_.write(f"Keff: {self.keff_array[self.iterations-1]}\n")
      f_.write("-------------------------------------------- \n")
      f_.write("Calculation of probabilities \n")
      f_.write(self.calculate_computing_time())
    with open(
      self.output_dir+f"/{self.nameOut}_rmm_flux.csv", "w"
    ) as f_:
      f_.write(self.__write_flux())
    
    with open(
      self.output_dir+f"/{self.nameOut}_rmm_J.csv", "w"
    ) as f_:
      f_.write(self.__write_current())


    with open(
      self.output_dir+f"/{self.nameOut}_rmm_keff_convergence.csv", "w"
    ) as f_:
      f_.write(
        self.__write_keff_file()
      )

    # with open(
    #   self.output_dir+f"/{self.input_file_name}_rmm_xs.csv", "w"
    # ) as f_:
    #   f_.write(self.__write_xs())

    # with open(
    #   self.output_dir+f"/{self.input_file_name}_rmm_source.csv", "w"
    # ) as f_:
    #     f_.write(self.__write_src())
  
  
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
  
  def __write_keff_file(self):
    numEner = self.root.energy_grid.energy_groups
    statement = "iteration,keff"
    for g in range(numEner):
      statement += f",phi_norm_g{g}"
    for g in range(numEner):
      statement += f",tr_it_g{g}"
    statement += "\n"
    num_iterations = self.keff_array.shape[0]
    for it in range(num_iterations):
      
      statement += f"{it+1},{self.keff_array[it]:.8E}"
      for g in range(numEner):
        statement += f",{self.convergence_flux[it][g]:.8E}"
      for g in range(numEner):
        statement += f",{self.transport_iterations[it][g]}"
      statement += "\n"
    return statement

  def __write_flux(self):
    numEner = self.root.energy_grid.energy_groups
    all_regions = self.mesh.all_regions_order
    numRegions = len(all_regions)
    regions_to_coarse_rel = self.mesh.create_regions_to_coarse_node_rel()
    coarse_nodes = self.mesh.coarse_mesh.coarse_nodes
    regions_volume = self.root.mesh.all_regions_vol
    statement = ""

    if self.flux_sigma:
      statement = "Energy_group,coarse_node_id,region_id,material,scalar_flux"
      statement += "sigma,volume\n"
      for g in range(numEner):
        for r in range(numRegions):
          reg_id = all_regions[r]
          n_id = regions_to_coarse_rel[reg_id]
          flux = self.flux[g][r]
          mat = coarse_nodes[n_id].fine_mesh.regions[reg_id].content.name
          vol = regions_volume[reg_id]
          statement += f"{g+1},{n_id},{reg_id},{mat},{flux},"
          statement += f"{self.flux_sigma[g][n_id][reg_id]},{vol}\n"
    else:
      statement = "Energy_group,coarse_node_id,region_id,material,scalar_flux,"
      statement += "volume\n"
      for g in range(numEner):
        for r in range(numRegions):
          reg_id = all_regions[r]
          n_id = regions_to_coarse_rel[reg_id]
          flux = self.flux[g][r]
          mat = coarse_nodes[n_id].fine_mesh.regions[reg_id].content.name
          vol = regions_volume[reg_id]
          statement += f"{g+1},{n_id},{reg_id},{mat},{flux},{vol}\n"
    return statement

  def __write_current(self):
    numEner = self.root.energy_grid.energy_groups
    all_surfaces = self.mesh.all_surfaces_order
    numSurfaces = len(all_surfaces)
    surfaces_to_coarse_rel = self.mesh.create_surfaces_to_coarse_node_rel()
    surfs_area = self.mesh.all_surfaces_area
    statement = ""

    
    statement = "Energy_group,coarse_node_id,sur_id,jin,jout,area\n"
    
    for g in range(numEner):
      for a in range(numSurfaces):
        surf_id = all_surfaces[a]
        n_id = surfaces_to_coarse_rel[surf_id]
        area = surfs_area[surf_id]
        jin = self.jin[g][a]
        jout = self.jout[g][a]

        statement += f"{g+1},{n_id},{surf_id},{jin},{jout},{area}\n"
    return statement


  def __write_xs(self):
    numEner = self.root.energy_grid.energy_groups
    coarse_nodes_ids = self.mesh.coarse_order
    coarse_regions_rel = self.root.mesh.coarse_mesh.coarse_nodes_regions
    
    regions_material = self.root.mesh.coarse_mesh.coarse_nodes_regions_material

    statement = "Energy_group,coarse_node_id,region_id,material,xs_tot,xs_fiss\n"
    for g in range(numEner):
      for n_id in coarse_nodes_ids:
        for reg_id in coarse_regions_rel[n_id]:
          mat = regions_material[reg_id]
          xs_fiss = self.xs[reg_id]["fission"][g]
          xs_tot = self.xs[reg_id]["total"][g]
          statement += f"{g+1},{n_id},{reg_id},{mat},{xs_tot},{xs_fiss}\n"
    return statement



class OutputFileReader:

    def __init__(self):
        pass

    def read(self):
        pass