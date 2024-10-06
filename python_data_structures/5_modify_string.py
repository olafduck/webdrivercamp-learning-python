#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
    filtered_string = ''.join([char for char in some_string if char.lower() != 'a'])
    print(filtered_string)

remove_char(string)
