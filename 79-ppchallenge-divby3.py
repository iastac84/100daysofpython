#!/usr/bin/env python3
# Day 79

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Divisible by 3
Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.

Use https://docs.python.org/3/library/stdtypes.html#float.is_integer
'''

def div_3(number):
    dividedby3 = number / 3 
    if dividedby3.is_integer():
       return True
    return False
   

print(div_3(66))
print(div_3(44))
