#!/usr/bin/env python3
# Day 20

"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
Python has a built-in package called re, which can be used to work with Regular Expressions.
"""

import re
print ('Search the string to see if it starts with "The" and ends with "Spain":')
print ()
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

