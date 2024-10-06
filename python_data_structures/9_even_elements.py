#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]
new_list = []

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        new_list.append(True)
    else:
        new_list.append(False)

new_tuple = tuple(new_list)
print(my_list)
print(new_tuple)

