#!/usr/bin/env python3
# Day 67

# challenge from https://pythonprinciples.com/challenges
'''
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
Refs:
https://stackoverflow.com/questions/65229524/returning-odd-or-even-number-of-characters-from-user-input
https://www.learndatasci.com/solutions/python-double-slash-operator-floor-division/ - floor division (also sometimes known as integer division)
https://www.freecodecamp.org/news/python-find-in-list-how-to-find-the-index-of-an-item-or-element-in-a-list/
'''

# https://dev.to/mahmoudessam/python-challenges2-36j5 accepted solution at https://pythonprinciples.com/challenges

def mid(my_string):
    length = len(my_string) % 2
    if length == 0:
        return ""
    elif length != 0:
        middle = len(my_string) // 2
        return my_string[middle]

print(mid("LutonTownFC"))
