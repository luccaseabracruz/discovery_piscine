#! /usr/bin/env python3

import math

try:
    n = float(input("Give me a number: "))
except:
    print("This is not a number.")
    exit()
print(f"{math.ceil(n)}")