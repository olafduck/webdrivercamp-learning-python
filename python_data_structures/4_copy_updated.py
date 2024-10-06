#!/usr/bin/python3

original_list = [5, 4, 3, 2, 1]
copied_list = original_list[:]
index = 1
element_to_replace = 5

def replace_elem(list_param, list_idx, elem):
    if list_idx < 0 or list_idx >= len(list_param):
        print(list_)
    else:
        list_param[list_idx] = elem
        print(f'Copy: {list_param}')

replace_elem(copied_list, index, element_to_replace)
print(f'Original: {original_list}')
