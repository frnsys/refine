import os

def files_exist(files):
    return lambda: not all(
            os.path.exists(f) for f in files)
