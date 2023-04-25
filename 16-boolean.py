#!/usr/bin/env python3
# Day 16

# Booleans represent one of two values: True or False

# Below when we compare two values, the expression is evaluated and Python returns the Boolean answer
print("Compare two values:")
print(10 > 9)
print(10 == 9)
print(10 < 9) 
print ()

# Print a message based on whether the condition is True or False
print("Print a message based on whether the condition is True or False:")
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
print ()

# Almost any value is evaluated to True if it has some sort of content.
print ("The bool() function allows you to evaluate any value, and give you True or False in return")
print(bool("Hello"))
print(bool(15))
