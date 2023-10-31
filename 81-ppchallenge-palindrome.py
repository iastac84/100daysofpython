#!/usr/bin/env python3
# Day 81

# challenge from https://pythonprinciples.com/challenges

'''
Challenge: Palindrome
A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise

https://www.w3schools.com/python/python_howto_reverse_string.asp : 
There is no built-in function to reverse a String in Python.
The fastest (and easiest?) way is to use a slice that steps backwards, -1.
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

