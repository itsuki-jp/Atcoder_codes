import os
import sys

folder_path = f"{sys.argv[1]}/{sys.argv[1]}{sys.argv[2]}"
os.makedirs(folder_path)
for i in "ABCDE":
    file_path = f"{folder_path}/{sys.argv[1]} {sys.argv[2]} {i}.py"
    f = open(file_path, 'w')
    f.close()
