#!/usr/bin/env python3
# Day 73

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
'''

def add_dots(string):
    new_string = ".".join(string)
    return new_string

print(add_dots("Luton Town"))

def remove_dots(string):
    new_string = string
    result = new_string.replace(".", "")
    return result
print(remove_dots("L.T.F.C"))

