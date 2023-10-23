#!/usr/bin/env python3
# Day 76

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

Hint: You can compare how many times each letter appears in each string. Alternatively, sorting the letters in each string makes this much easier.
'''

def is_anagram(strg1, strg2):
   x = sorted(strg1)
   y = sorted(strg2)
   print(x)
   print(y)
   

is_anagram("typhoon", "opython")
is_anagram("Alice", "Bob")
