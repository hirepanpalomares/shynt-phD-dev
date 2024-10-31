import asyncio
import subprocess
import sys
import os



def run_detector_files(det_inputs):
  for id_coarse, inp in det_inputs.items():
    for file_ in inp:
      # print(file_.name)
      # command = f"gnome-terminal -x sh -c \"sss2.1.32 {file_.name}; bash\" " # To run in another terminal (testing it)
      try:
        assert(os.path.isfile(file_.name + "_res.m")) 
      except AssertionError:
        command = f"sss2.1.32 {file_.name} -omp 20"
        os.system(command)
  return 0


def run_xs_files(xs_inputs):
  for id_coarse, xs_inp in xs_inputs.items():
    # print(xs_inp.name)
    command_xs_gen = f"sss2.1.32 {xs_inp.name} -omp 20"
    try:
      assert(os.path.isfile(xs_inp.name + "_res.m")) 
    except AssertionError:
      os.system(command_xs_gen)
  return 0


