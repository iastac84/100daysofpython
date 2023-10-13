#!/usr/bin/env python3
# Day 70

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Randomness
Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.
'''

import random

def random_number():
    # random integer from 1 to 100
    randomnumber = random.randint(1, 100)
    return randomnumber# random integer from 0 to 9

print(random_number())
print(random_number())

