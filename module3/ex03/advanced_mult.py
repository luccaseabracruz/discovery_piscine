#! /usr/bin/env python3

n = 0
while n <= 10:
    i = 0
    print(f"Table of {n}: ", end="")
    while i <= 10:
        if i < 10:
            print(f"{n * i}", end=" ")
        else:
            print(f"{n * i}")
        i += 1
    n += 1
