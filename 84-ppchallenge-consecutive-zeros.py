#!/usr/bin/env python3
# Day 84

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.

Note : the int type in Python is not iterable, so we cannot use a for loop to iterate over it.
'''

def consecutive_zeros(binary_string):
    countzeros = 0
    for each in str(binary_string):
      if each == "0":
         countzeros += 1
    return countzeros

print(consecutive_zeros(1001101000110))

