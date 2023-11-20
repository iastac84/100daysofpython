#!/usr/bin/env python3
# Day 90

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Challenge
Writing short code
Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
What makes this tricky is that your function body must only contain a single line of code.
Hint: You can use list comprehensions or the map built-in. Use google to learn more.

If you're using map, note that it will return a generator object, which you must convert to a list before your solution is accepted.
'''

def convert(li):
    # For each item in the list, convert the integer to string - list comprehension 
    print([str(i) for i in li]) 

convert([1, 2, 3])
