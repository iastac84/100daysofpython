#!/usr/bin/env python3
# Day 95

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Counting parameters
Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.

For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.

Hint: 
The terminology you're looking for is this: you need to define a function that takes a variable number of arguments. As usual, google is your friend.

https://www.geeksforgeeks.org/args-kwargs-python/
'''

def param_count(*args):
    return len(args)

print ("The number of arguments is:", (param_count()))
print ("The number of arguments is:", (param_count("L", "T", "F", "C", 2, "C", "P", "F", "C", 1)))
