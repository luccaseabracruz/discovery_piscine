#! /usr/bin/env python3

try:
    n = float(input("Give me a number: "))
except:
    print("This is not a number.")
    exit()
if (n - int(n) == 0):
    print("This number is an integer.")
else:
    print("This number is a decimal.")