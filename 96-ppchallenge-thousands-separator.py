#!/usr/bin/env python3
# Day 96

# challenge from https://pythonprinciples.com/challenges
# last of these
'''
Challenge
Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".

Hint: 
Convert the number to a string and iterate over each digit. Iterate backwards, or start by reversing the string, to make your life easier.
'''
'''
# >>> num = 123456789
# >>> print(type(num))
# <class 'int'>
# >>> thous = format(num, ",")
# >>> print(thous)
# 123,456,789
# >>> print(type(num))
# <class 'int'>
'''

def format_number(numberr):
   thous = format(numberr, ",")
   return thous

print(format_number(123456789))
print(type(format_number(123456789)))
