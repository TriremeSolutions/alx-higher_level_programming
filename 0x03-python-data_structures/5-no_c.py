#!/usr/bin/python3

def no_c(my_string):
    chopped = [n for n in my_string if not (n != 'C' or n != 'c')]
    return ("".join(chopped))
