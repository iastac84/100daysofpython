#!/usr/bin/env python3
# Day 83

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Up and down
Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6).

A shorter alternative solution, thanks to: 
https://dev.to/mahmoudessam/python-challenge14-35g8
'''

def up_down(x):
    return (x-1, x+1)

print(up_down(8))

