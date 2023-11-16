#!/usr/bin/env python3
# Day 85

# challenge from https://pythonprinciples.com/challenges

'''
Challenge: 
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
'''

def triple_and(param1, param2, param3):

    if param1 == param2 == param3: 
        return True
    else:
        return False

print(triple_and(1, 1, 1))
print(triple_and(1, 3, 1))
print(triple_and("LTFC", "LTFC", "LTFC"))
print(triple_and("MUFC", "LTFC", "LTFC"))
