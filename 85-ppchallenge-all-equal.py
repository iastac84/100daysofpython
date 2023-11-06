#!/usr/bin/env python3
# Day 85

# challenge from https://pythonprinciples.com/challenges

'''
Challenge: 
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''

def palindrome(string):
   reverseit = string[::-1] 
   if string.casefold() == reverseit.casefold():
     return True
   else:
     return False

print(palindrome("abcdef"))
print(palindrome("abba"))
print(palindrome("Level"))

