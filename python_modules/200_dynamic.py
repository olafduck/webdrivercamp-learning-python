#!/usr/bin/python3
import sys

arg_count = len(sys.argv)

if arg_count == 1:
    print('0 arguments.')
elif arg_count == 1:
    print('1 argument:')
    print(f'1: {sys.argv[1]}')
else: 
    print(f'{arg_count - 1} arguments.')
    for i in range(1, arg_count):
        print(f'{i}: {sys.argv[i]}')
         
