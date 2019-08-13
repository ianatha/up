#!/usr/bin/python

from __future__ import print_function
import os, sys
from os.path import expanduser

cwd = os.getcwd().split(os.sep)[::-1][:-1]
home = expanduser("~")

arg_input = None
if len(sys.argv) != 2:
    for i, dir in enumerate(cwd):
        print("% 2d. %s" % (i, dir), file=sys.stderr)
    print("? ", file=sys.stderr, end='')
    arg_input = raw_input()
else:
    arg_input = sys.argv[1]

levels_up = None

if arg_input.isdigit():
    levels_up = int(arg_input)
elif arg_input == '~' or arg_input == home:
    levels_up = -1
elif arg_input == '':
    levels_up = 0
else:
    match = arg_input
    try:
        levels_up = cwd.index(match)
    except:
        print("up: '%s' is neither a number, nor something in your path" % match, file=sys.stderr)
        print("__no_path_found__")

if levels_up > 0:
    print("../" * levels_up)
elif levels_up == -1:
    print("")
else:
    print(".")