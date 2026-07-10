#! /usr/bin/env python3

def average(class_list: dict):
    class_len = len(class_list)
    if (class_len < 1):
        return 0.00
    else:
        return sum(class_list.values()) / len(class_list)

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")