#! /usr/bin/env python3

import sys

def downcase_it(str):
    return str.casefold()

params = sys.argv[1:]
if len(params) < 1:
    print("none")
    sys.exit()
for arg in params:
    print(downcase_it(arg))
