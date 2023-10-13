#!/usr/bin/env python3
# Day 71

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Type check
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
'''

def only_ints(num_1, num_2):
    if type(num_1) == int and type(num_2) == int:
        return True
    else: 
        return False

print(only_ints(1, 2)) 
print(only_ints("a", 1)) 
