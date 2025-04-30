#!/usr/bin/env python3

from multiprocessing import Pool
import os
import subprocess

src = "data/prod/"
dest = "data/prod_backup/"
tasks=[]

#subprocess.call(["rsync", "-arq", src, dest])
def run(task):
    # Perform rsync for the given task (file)
    dest_path = task.replace(src, dest, 1)  # Replace src with dest in the path
    print("Backing up {} into {}".format(task, dest_path))
    #subprocess.call(["rsync", "-arq", task, dest_path])

if __name__ == "__main__":
  list_of_files = os.listdir(src)

  for filename in list_of_files:
    full_path = os.path.join(src, filename)
    tasks.append(full_path)
  print("task size : {}".format(len(tasks)))
  #exit(0)

  with Pool(len(tasks)) as pool:
    pool.map(run, tasks)

