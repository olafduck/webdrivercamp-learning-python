#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]

def reverse_list(list_param):

    for num in range(-1, -len(list_param)-1, -1):
        print(list_param[num])

reverse_list(list_)

