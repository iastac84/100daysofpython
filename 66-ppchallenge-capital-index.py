#!/usr/bin/env python3
# Day 66

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

https://docs.python.org/3/library/functions.html#enumerate
'''

def capital_indexes(string):
    return [i for i, char in enumerate(string) if char.isupper()]

print(capital_indexes("HeLlO, Hello, hola, We're at a place called Vertigo")) 
