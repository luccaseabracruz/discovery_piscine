#! /usr/bin/env python3

import sys
import re

if len(sys.argv) == 3:
    res_list = re.findall(sys.argv[1], sys.argv[2])
    list_len = len(res_list)
    if list_len == 0:
        print("none")
    else:
        print(list_len)
else:
    print("none")