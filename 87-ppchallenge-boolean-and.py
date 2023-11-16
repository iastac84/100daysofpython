#!/usr/bin/env python3
# Day 85

# challenge from https://pythonprinciples.com/challenges

'''
Challenge: 
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
'''

def triple_and(params_list):

    result = all(element == params_list[0] for element in params_list)

    if (result):
        return True
    else:
        return False

print(triple_and([1, 1, 1]))
print(triple_and([7, 7, 7, 8]))
print(triple_and(["a", "a", "a", "a"]))
print(triple_and(["a", "b", "b", "a"]))
