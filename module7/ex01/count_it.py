#! /usr/bin/env python3

import sys

if (len(sys.argv) < 2):
    print("none")
    sys.exit()
print(f"Parameters: {len(sys.argv) - 1}")
for arg in sys.argv[1:]:
    print(f"{arg}: {len(arg)}")