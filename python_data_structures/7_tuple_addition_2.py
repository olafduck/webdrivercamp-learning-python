#!/usr/bin/python3

def tuple_addition(first_arg=(0, ), second_arg=(0, )):
    
    if len(first_arg) > 0:
        first_first = first_arg[0]
    else:
        first_first = 0

    if len(second_arg) > 0:
        second_first = second_arg[0]
    else:
        second_first = 0

    if len(first_arg) > 1:
        first_second = first_arg[1]
    else:
        first_second = 0

    
    if len(second_arg) > 1:
        second_second = second_arg[1]
    else:
        second_second = 0

    return (first_first + second_first, first_second + second_second)


