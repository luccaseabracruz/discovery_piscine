#! /usr/bin/env python3

my_list =  [2, 8, 9, 48, 8, 22, -12, 2]
my_set = set()
print(my_list)
for i in my_list:
    if i > 5:
        my_set.add(i + 2)
print(my_set)