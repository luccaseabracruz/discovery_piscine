#!/usr/bin/env python3

try:
    x = int(input("Enter the first number: "))
except:
    print("This is not a number")
    exit()
try:
    y = int(input("Enter the second number: "))
except:
    print("This is not a number")
    exit()

res = x * y
print(f"{x} x {y} = {res}")
if (res > 0):
    print("The result is positive.")
elif (res < 0):
    print("The result is negative.")
else:
    print("The result is positive and negative.")