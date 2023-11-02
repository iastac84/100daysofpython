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

Alternative - use string.split. Short version as per https://dev.to/mahmoudessam/python-challenge13-2fga
'''

def consecutive_zeros(bin_str):
    return max([len(string) for string in bin_str.split("1")])

print(consecutive_zeros("1001101000110"))
