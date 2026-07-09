#! /usr/bin/env python3
import sys

def greetings(name="noble stranger"):
    if  isinstance(name, str) == False:
        print("Error! It was not a name.")
        sys.exit()
    print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
