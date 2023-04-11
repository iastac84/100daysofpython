#!/usr/bin/env python3
# Day 13

# This function takes a parameter n and uses a for loop to print the numbers from 1 to n on separate lines. The range function is used to generate a sequence of numbers from 1 to n, and the loop iterates over this sequence, printing each number in turn.

# To use the function, you simply call it and pass in a value for n, as shown in the example usage. In this case, calling print_numbers(5) would print the numbers 1 to 5 on separate lines.

def print_numbers(n):
    for i in range(1, n+1):
        print(i)

# Example usage:
print_numbers(5)  # prints numbers 1 to 5 on separate lines
print()
print_numbers(9)  # prints numbers 1 to 5 on separate lines

