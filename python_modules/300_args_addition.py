#!/usr/bin/python3

import sys

arg_count = len(sys.argv)
cli_args = sys.argv
cli_arg_sum = 0

for idx in range(1, arg_count):
    cli_arg_sum += int(cli_args[idx])

print(cli_arg_sum)
         
