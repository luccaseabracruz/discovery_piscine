#! /usr/bin/env python3

import sys

if (len(sys.argv) != 2):
    print("none")
    sys.exit()
counter = 0
for c in sys.argv[1]:
    if c == 'z':
        counter += 1
if (counter == 0):
    print("none")
else:
    print(counter * 'z')