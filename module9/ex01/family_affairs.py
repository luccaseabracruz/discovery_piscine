#! /usr/bin/env python3

def find_the_redheads(family: dict):
    filtered_list = list(filter(lambda person: family[person] == "red", family))
    return filtered_list

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))