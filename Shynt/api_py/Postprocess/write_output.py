import sys
import os
import sys
from pathlib import Path

from Shynt.api_py.Probabilities.probability_writer import write_excel



class OutputFile:

  def __init__(self, 
    root, 
    keff, 
    flux, 
    xs,
    flux_sigma, 
    iter_number, 
    convergence, 
    nameOut, 
    phi_src, 
    probs,
  ):
    self.root = root
    self.keff = keff
    self.flux = flux
    self.xs = xs
    self.flux_sigma = flux_sigma
    self.iterations = iter_number
    self.convergence_keff = convergence[0]
    self.convergence_flux = convergence[1]
    # self.mesh_info = mesh_info
    self.mesh = root.mesh
    self.phi_src = phi_src
    self.nameOut = nameOut
    self.probs = probs

    input_file_dir = os.getcwd() + '/'
    self.output_dir = input_file_dir + "output_RMM_" + nameOut
    try:
      assert(os.path.isdir(self.output_dir))
    except AssertionError:
      os.mkdir(self.output_dir)
    self.__write()
  

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
      f_.write(f"Flux convergence: {self.convergence_flux}\n")
      f_.write("-------------------------------------------- \n")
      f_.write(f"Keff: {self.keff}")

    with open(
      self.output_dir+f"/{self.nameOut}_rmm_flux.csv", "w"
    ) as f_:
      f_.write(self.__write_flux())

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

  def __write_flux(self):
    numEner = self.root.energy_grid.energy_groups
    all_regions = self.mesh.all_regions_order
    numRegions = len(all_regions)
    regions_to_coarse_rel = self.mesh.create_regions_to_coarse_node_rel()
    coarse_nodes = self.mesh.coarse_mesh.coarse_nodes
    regions_volume = self.root.mesh.all_regions_vol
    statement = ""

    if self.flux_sigma:
      statement = "Energy_group,coarse_node_id,region_id,material,scalar_flux,"
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