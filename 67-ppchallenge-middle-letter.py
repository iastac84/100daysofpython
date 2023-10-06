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

input_string = str(input("Please enter your string: "))
num = len(input_string)

def mid(input_string):
    if(num % 2 == 0):
        print("Your string", input_string, "contains", num, "characters, an even number")
        print("")
    else:
        middle_character = num // 2 # Note the double /
        print ("The middle character in \""+input_string+"\" is", input_string[middle_character])

mid(input_string)
