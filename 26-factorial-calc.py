#!/usr/bin/env python3
# Day 26

'''
In this script, we define a function called factorial that takes a number n as input and calculates its factorial recursively. The factorial of 0 is defined as 1, and for any other number n, it is calculated by multiplying n with the factorial of n-1.

The user is prompted to enter a number, which is then converted to an integer using int(). The factorial of the entered number is calculated using the factorial function, and the result is printed to the console.
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(number)

# Print the result
print("The factorial of", number, "is", result)

