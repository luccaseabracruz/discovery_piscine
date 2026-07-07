#!/usr/bin/env python3

try:
	n = int(input("Enter a number less than 25\n"))
except:
	print("This is not a number.")
	exit()
if (n > 25):
	print("Error")
else:
	for i in range(n, 26):
		print(f"Inside the loop, my variable is {i}")