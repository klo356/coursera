#!/usr/bin/env python3

from multiprocessing import Pool
import os
import subprocess

src = "/data/prod/"
dest = "/data/prod_backup/"

def run(task):
  # Do something with task here
  print("Handling {}".format(task))
  subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
  for dirpath, dirnames, filenames in os.walk(src):
    print(f"Directory: {dirpath}")
    print(f"Subdirectories: {dirnames}")
    print(f"Files: {filenames}")
  exit(0)


  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)