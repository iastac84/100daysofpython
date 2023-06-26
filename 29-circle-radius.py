#!/usr/bin/env python3
# Day 29

'''
Script to calculate the area of a circle by multiplying the square of the radius by the mathematical constant pi from the math module.
'''

import math

# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius ** 2

# Print the result
print("The area of the circle is:", area)

