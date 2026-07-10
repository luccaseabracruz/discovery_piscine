#! /usr/bin/env python3
import sys

def greetings(name="noble stranger"):
    if  isinstance(name, str) == True:
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
