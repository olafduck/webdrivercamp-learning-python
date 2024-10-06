#!/usr/bin/python3

first_arg, second_arg = (1, 99), (-1, 1)

def tuple_addition(first_arg, second_arg):

    if len(first_arg) >= 2:
        return (first_arg[0] + second_arg[0], first_arg[1] + second_arg[1])
    elif len(first_arg) < 2:
        return (

print(tuple_addition(first_arg, second_arg))
