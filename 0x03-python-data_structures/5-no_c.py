#!/usr/bin/python3

def no_c(my_string):
    chopped = [n for n in my_string if n != 'C' and n != 'c']
    return ("".join(chopped))
