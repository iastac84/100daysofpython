#!/usr/bin/env python3
# Day 79

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Divisible by 3
Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.

Alt use the modulo operator %
'''

def div_3(x):
    if x % 3 == 0:
        print("Remainder of", x, "% 3", "is", (x % 3))
        return True
    else:
        print("Remainder of", x, "% 3", "is", (x % 3))
        return False


print(div_3(88))
print(div_3(666))
