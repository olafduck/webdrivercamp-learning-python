#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def replace_elem(list_param, list_idx, elem):
    if list_idx < 0 or list_idx >= len(list_param):
        print(list_)
    else:
        list_param[list_idx] = elem
        print(list_param)

replace_elem(list_, index, element_to_replace)

