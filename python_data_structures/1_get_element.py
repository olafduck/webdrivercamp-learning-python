#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 2

def list_elem(list_param, list_idx):
    if list_idx < 0 or list_idx >= len(list_param):
        return None
    else:
        print(f"The element retrieved is {list_param[list_idx]}")

list_elem(list_, index)

