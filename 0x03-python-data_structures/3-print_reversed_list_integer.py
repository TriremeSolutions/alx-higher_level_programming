#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
    revList = my_list.reverse()
    for i in revList:
        print("{:d}".format(i)
