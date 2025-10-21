#!/usr/bin/env python3
# Day 31

'''
Simple function that calculates the square of a number
'''

def square(num):
    result = num * num
    return result

# Prompt the user to enter a number
num = float(input("Enter a number: "))

# Call the function and print the result
print("The square of", num, "is", square(num))

