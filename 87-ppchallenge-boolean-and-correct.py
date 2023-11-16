#!/usr/bin/env python3
# Day 85

# challenge from https://pythonprinciples.com/challenges

'''
Challenge: 
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

The Python Boolean type has only two possible values:
1) True
0) False
No other value will have bool as its type. You can check the type of True and False with the built-in type():
'''

def triple_and(param1, param2, param3):

    if param1 == True and param2 == True and param3 == True: 
        return True
    else:
        return False

print(triple_and(1, 1, 1))
print(triple_and("a" == "a", 1, "LTFC" == "LTFC"))
print(triple_and("a" == "a", 321 == 321, "LTFC" == "LTFC"))
print(triple_and("a" == "a", 321 == 321, "LTFC" == "MUFC"))
