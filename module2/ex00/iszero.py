#!/usr/bin/env python3
try:
    n = int(input())
except:
    print("This is not a number.")
    exit()
if n != 0:
    print("This number is different from zero.")
else:
    print("This number is equal to zero.")