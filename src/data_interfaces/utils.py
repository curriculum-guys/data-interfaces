import os

def set_root(root):
    os.environ['interface_root'] = root

def get_root_dir(root=None):
    root = root if root else os.environ.get('interface_root', None)
    if root:
        exe_path = str(os.getcwd())
        split_str = exe_path.split(root)
        return split_str[0] + root
    else:
        raise Exception("Interface Root not defined!")

def create_dir(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)

def create_dirs(base_path, directories):
    incremental_path = base_path
    for directory in directories.split('/'):
        incremental_path += '/'+directory
        if not os.path.isdir(incremental_path):
            os.mkdir(incremental_path)

def remove_dir(directory):
    if os.path.isdir(directory):
        os.rmdir(directory)

def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)

def verify_file(path):
    if os.path.isfile(path):
        return True
