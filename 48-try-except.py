#!/usr/bin/env python3
# Day 48

# Simple example of a Python script that uses the try and except blocks to handle exceptions:

'''
In this script, the divide_numbers function attempts to divide two numbers. It uses the try block to contain the potentially problematic code, and if any exception occurs during the execution of the code inside the try block, the appropriate except block is executed. The except blocks in this case handle ZeroDivisionError (when dividing by zero) and TypeError (when the input types are not valid for division).

The example usage section demonstrates how to call the divide_numbers function and catch any exceptions that might be raised during its execution using a generic Exception handler. This way, the program can gracefully handle errors and display meaningful error messages instead of crashing.
'''

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

# Example usage
num1 = 10
num2 = 0

try:
    result = divide_numbers(num1, num2)
    print("Result:", result)
except Exception as e:
    print("An error occurred:", e)

