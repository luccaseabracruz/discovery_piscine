#! /usr/bin/env python3

my_list =  [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original list: {my_list}")
list_len = len(my_list)
i = 0
while (i < list_len):
    if my_list[i] > 5:
        my_list[i] += 2
        i += 1
    else:
        my_list.pop(i)
        list_len -= 1
print(f"New list: {my_list}")