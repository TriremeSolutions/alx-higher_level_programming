#!/usr/bin/python3
def no_c(my_string):
    chopped = [i for i in my_string if not (i != 'C' or i != 'c']
    return ("".join(chopped))
