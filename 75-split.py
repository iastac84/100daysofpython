#!/usr/bin/env python3
# Day 75

# Splits
# Lots of different string methods:
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/ref_string_split.asp

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

txt = "Luton.Town.F.C."
x = txt.split(".", 2)
print(x)

