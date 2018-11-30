#!/bin/env python3

import os
from sys import  argv

def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)


for arg in argv[1:]:
    if is_exe(arg):
        print(f'file {arg} is executable')
        exit(1)
