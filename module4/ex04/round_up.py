#! /usr/bin/env python3

try:
    n = float(input("Give me a number: "))
except:
    print("This is not a number.")
    exit()
print(f"{int(n)}")