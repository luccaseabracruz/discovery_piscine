#! /usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    str_len = len(string)
    while (str_len < 8):
        string += 'Z'
        str_len += 1
    print(string)

args = sys.argv[1:]
if len(args) < 1:
    print("none")
    sys.exit()
for arg in args:
    arg_len = len(arg)
    if arg_len > 8:
        shrink(arg)
    elif arg_len < 8:
        enlarge(arg)
    else:
        print(arg)
