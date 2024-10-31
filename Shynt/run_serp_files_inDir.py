import os

from os.path import isfile, join
import sys

"""
    Python script to run serpent files in a directory
"""

def run_serpent_file(omp, file_):
  try:
    assert(isfile(file_ + "_res.m")) 
  except AssertionError:
    command = f"sss2.1.32 {file_} -omp {omp}"
    os.system(command)

def run_serp_files_in_a_directory(omp, dir):
  serp_files_in_dir = [f for f in os.listdir(f"{dir}/") if ".serp" in f]
  for serp_f in serp_files_in_dir:
    try:
      assert ".serp." in serp_f
      assert ".serp_" in serp_f
    except AssertionError:
      run_serpent_file(omp, f"{dir}/{serp_f}")
      


def run_serp_directories(omp):
  serp_dirs = [f for f in os.listdir() if "global_cell_type" in f]
  for dir_ in serp_dirs:
    run_serp_files_in_a_directory(omp, dir_)


  

if __name__=="__main__":
  arg = sys.argv[1:]
  omp = 1
  if "-omp" in arg:
    omp = arg[1]
  run_serp_directories(omp)
