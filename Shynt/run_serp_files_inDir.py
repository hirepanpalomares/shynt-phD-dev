import os

from os.path import isfile, join
import sys

"""
    Python script to run serpent files in a directory
"""


def run_serp_file_in_a_directory(omp):
  serp_files_in_dir = [f for f in os.listdir() if ".serp" in f]
  for serp_f in serp_files_in_dir:
    try:
      assert(isfile(serp_f + "_res.m")) 
    except AssertionError:
      command = f"sss2.1.32 {serp_f} -omp {omp}"
      os.system(command)


def run_serp_directories(omp):
  serp_dirs = [f for f in os.listdir() if "global_cell_type" in f]
  for dir_ in serp_dirs:
    print(dir_)
  pass

if __name__=="__main__":
  arg = sys.argv[1:]
  omp = 1
  if "-omp" in arg:
    omp = arg[1]
  run_serp_file_in_a_directory(omp)
