#!/usr/bin/env python3

try:
	n = int(input("Enter a number\n"))
except:
	print("This is not a number.")
	exit()
for i in range(10):
	print(f"{i} x {n} = {i * n}")