#!/usr/bin/env python3
# Day 81

# challenge from https://pythonprinciples.com/challenges

'''
https://www.w3schools.com/python/python_howto_reverse_string.asp : 
There is no built-in function to reverse a String in Python.
The fastest (and easiest?) way is to use a slice that steps backwards, -1.
'''

def palindrome(string):
   reverseit = string[::-1] 
   return reverseit

print(palindrome("Hello World"))
