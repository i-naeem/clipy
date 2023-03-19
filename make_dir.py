"""
make_dir.py: A utility function that will help make directory easy.
"""
import os


def make_dir(dir_path):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        return

    os.mkdir(dir_path)
