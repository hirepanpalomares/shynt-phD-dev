import os

from os.path import isfile, join
import sys

"""
    Python script to run serpent files in a directory
"""


def run_serp_file_in_a_directory(omp, dir_, plot=False):
  serp_files_in_dir = [f"{dir_}/{f}" for f in os.listdir(dir_) if ".serp" in f]
  for serp_f in serp_files_in_dir:
    print(serp_f)
    if ".serp." in serp_f or ".serp_" in serp_f: continue
    try:
      assert(isfile(serp_f + "_res.m")) 
      if plot:
        os.system(f"sss2.1.32 {serp_f} -omp {omp} -plot")
    except AssertionError:
      command = ""
      if plot:
        command = f"sss2.1.32 {serp_f} -omp {omp} -plot"
      else:
        command = f"sss2.1.32 {serp_f} -omp {omp}"
      os.system(command)


def run_serp_directories(omp, plot=False):
  serp_dirs = [f for f in os.listdir() if "global_cell_type" in f]
  for dir_ in serp_dirs:
    run_serp_file_in_a_directory(omp, dir_, plot=plot)

if __name__=="__main__":
  arg = sys.argv[1:]
  omp = 1
  if "-omp" in arg:
    omp = arg[1]
  if "-plot" in arg:
    run_serp_directories(omp, plot=True)
  else:
    run_serp_directories(omp, plot=False)
