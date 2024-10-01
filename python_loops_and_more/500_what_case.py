#!/usr/bin/python3

def is_case(c):
    ascii_value = ord(c)
    if ascii_value in range(65, 91):
        return False
    elif ascii_value in range(97, 123):
        return True

