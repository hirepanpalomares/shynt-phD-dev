import os


for g in range(8):
  print(f"g: {g}")
  write_file = open("plot_map_serpent_uncert_aux.py", "w")
  with open("plot_uncertmap_serpent.py", "r") as py_file:
    for line in py_file:
      if line.startswith("g_plot"):
        write_file.write(f"g_plot = {g}\n")
      else:
        write_file.write(line)
  write_file.close()
  os.system('python plot_map_serpent_uncert_aux.py')
  print("-"*100)