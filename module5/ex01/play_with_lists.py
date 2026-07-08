#! /usr/bin/env python3

my_list =  [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original list: {my_list}")
for i in range(len(my_list)):
    my_list[i] += 2
print(f"New list: {my_list}")