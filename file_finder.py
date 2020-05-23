

import  os

start_dir = "/Users/cf397/Pictures"
file_list = []

for(dir_path, subdir_list, file_list) in os.walk(start_dir, topdown=True, onerror=None, followlinks=False):
    for file in file_list:
         print("D|", dir_path, "|", file)
    for subdir in subdir_list:
        print("subdir = ", subdir)
