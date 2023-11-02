#!/usr/bin/env python3
# Day 83

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Up and down
Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

For example, calling up_down(5) should return (4, 6).
'''

def up_down(num1):
   down = num1 - 1
   up = num1 + 1
   mytuple = ( down, up )
   return mytuple

print(up_down(7))

