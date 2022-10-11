import os


for g in range(8):
  write_file = open("plot_map_serpent_flux_aux.py", "w")
  with open("plot_fluxmap_serpent.py", "r") as py_file:
    for line in py_file:
      if line.startswith("g_plot"):
        write_file.write(f"g_plot = {g}\n")
      else:
        write_file.write(line)
  write_file.close()
  os.system('python plot_map_serpent_flux_aux.py')