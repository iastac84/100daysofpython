#!/usr/bin/env python3
# Day 77

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]

Hint
Start by defining an empty list as the result:
result = []
Then use a nested for loop to fill up the result.
'''

def flatten(lists):
   result = []
   for list in lists:
       for item in list:
          result.append(item)
   return result 
   

print(flatten([[1, 2], [3, 4], [5, 6]]))
