#! /usr/bin/env python3

import sys
import array

if len(sys.argv) != 3:
    print("none")
    sys.exit()
try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
except:
    print("This is not a number.")
    sys.exit()
if n1 > n2:
    print("The first number must be smaller than the second number.")
    sys.exit()
my_arr = array.array('i', range(n1, n2 + 1))
print(my_arr.tolist())