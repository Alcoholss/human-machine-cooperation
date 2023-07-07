import os

def get_root_dir():
    return os.path.join(os.path.split(os.path.realpath(__file__))[0], '..')