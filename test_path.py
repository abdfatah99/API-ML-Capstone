"""
    problem statement: to access the api model, you should use path from root. 
                       example:
                       D:\Document\Semester 8 ...\ current workdir\ model.hdf5
                       to access model.hdf5, you have to specify from absolute root (D)

    solution: separate the root
              current working directory: curdir/model.hdf5
              root path: D:\document\...\

              join the current working dir with the root path
              result = os.path.join(root_path, curdir)
    
    src: https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure 

"""
import os

current_dir = os.listdir()
print(current_dir)


# get root dir
ROOT_DIR = os.path.abspath(os.curdir)
print(ROOT_DIR)

path = os.path.join(ROOT_DIR, "model_v3_15class.hdf5")
print(path)
