#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
    revList = my_list.reverse()
    for i in range(len(revList)):
        print("{:d}".format(revList[i]))
