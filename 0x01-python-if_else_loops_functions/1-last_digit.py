#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a1 = " and is greater than 5"
a2 = " and is 0"
a3 = " and is less than 6 and not 0"
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print(f"Last digit of {number} is {last}" + a1)
elif last == 0:
    print(f"Last digit of {number} is {last}" + a2)
else:
    print(F"Last digit of {number} is {last}" + a3)
