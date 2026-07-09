#! /usr/bin/env python3

import sys

if (len(sys.argv) < 2):
    print("none")
    sys.exit()
sufix = "ism"
sufix_len = len(sufix)
for arg in sys.argv[1:]:
    arg_len = len(arg)
    if arg_len > 0 and arg.find(sufix, -3) == -1:
        print("%s%s" % (arg, sufix))