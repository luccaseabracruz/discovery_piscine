#!/usr/bin/env python3

try:
    n = int(input())
except:
    print("This is not a number.")
    exit()
if (n > 0):
    print("This number is positive.")
elif n < 0:
    print("This number is negative.")
elif n == 0:
    print("This number is both positive and negative.")