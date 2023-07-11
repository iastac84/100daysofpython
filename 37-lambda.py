#!/usr/bin/env python3
# Day 37

'''
Lambda functions are not specific to AWS (Amazon Web Services). They are a feature of the Python programming language and can be used in any Python environment or project. 
'''

# Example 1: Using lambda with built-in functions
print("Example 1 demonstrates the usage of lambda functions with built-in functions like map() and filter(). We use map() to square each element of a list and filter() to keep only the even numbers.")

# Map: Apply a lambda function to each element of a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Filter: Filter elements from a list based on a condition defined by a lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
print("")


# Example 2: Sorting a list of tuples based on a specific element using lambda
print("Example 2 shows how lambda functions can be used as the key for sorting a list of tuples. We sort the list of students based on their age.")

students = [("Alice", 22), ("Bob", 19), ("Charlie", 21), ("David", 20)]

# Sort the list of tuples based on the second element (age)
students_sorted_by_age = sorted(students, key=lambda x: x[1])
print(students_sorted_by_age)
# Output: [('Bob', 19), ('David', 20), ('Charlie', 21), ('Alice', 22)]
print("")


# Example 3: Creating higher-order functions using lambda
print("Example 3 showcases the creation of higher-order functions using lambda. We define a multiply_by() function that returns a lambda function, and then we use it to create a function that multiplies a number by 5.")

def multiply_by(n):
    return lambda x: x * n

# Create a function that multiplies a number by 5
multiply_by_5 = multiply_by(5)

# Use the created function
result = multiply_by_5(10)
print(result)  # Output: 50

