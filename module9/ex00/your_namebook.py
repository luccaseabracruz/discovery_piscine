#! /usr/bin/env python3

def array_of_names(dictionary: dict):
    res = []
    for person in dictionary:
        full_name = f"{person.capitalize()} {dictionary.get(person).capitalize()}"
        res.append(full_name)
    return res

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
