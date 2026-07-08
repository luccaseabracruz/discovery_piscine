#! /usr/bin/env python3

try:
    n1 = int(input("Give me the first number: "))
    n2 = int(input("Give me the second number: "))
except:
    print("This is not a number.")
    exit()
print("Thank you!")
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
if n2 != 0:
    print(f"{n1} / {n2} = {n1 // n2}")
else:
    print(f"{n1} / {n2} = impossible.")
print(f"{n1} * {n2} = {n1 * n2}")