import os
def create_file_path(original_path, prefix=''):
    path = os.path.split(original_path)[0]
    fname = os.path.split(original_path)[1]
    fname = prefix + fname
    return os.path.join(path, fname)