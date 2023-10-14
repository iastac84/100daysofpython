#!/usr/bin/env python3
# Day 72

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Double letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
'''

def only_ints(num_1, num_2):
    if type(num_1) == int and type(num_2) == int:
        return True
    else: 
        return False

print(only_ints(1, 2)) 
print(only_ints("a", 1)) 
