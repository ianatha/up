#!/usr/bin/python

from __future__ import print_function
import os, sys

if len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        levels_up = int(sys.argv[1])
        print("../" * levels_up)
    else:
        match = sys.argv[1]
        cwd = os.getcwd().split(os.sep)[::-1][:-1]
        try:
            levels_up = cwd.index(match)
            print("../" * levels_up)
        except:
            print("up: '%s' is neither a number, nor something in your path" % match, file=sys.stderr)
            print("__no_path_found__")    
else:
    print("up: up [levels_up|parent_dir]", file=sys.stderr)
    print("__no_path_found__")    