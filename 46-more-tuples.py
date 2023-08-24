#!/usr/bin/env python3
# Day 46

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable / immutable
# Tuples are written with round brackets.

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Creating a tuple
person = ("John", 30, "Male")

# Accessing tuple elements
print("Name:", person[0])
print("Age:", person[1])
print("Gender:", person[2])

# Unpacking tuple
name, age, gender = person
print("Unpacked Name:", name)
print("Unpacked Age:", age)
print("Unpacked Gender:", gender)

# Nested tuple
address = ("123 Main St", "Cityville", "12345")
person_with_address = person + address
print("Person with Address:", person_with_address)

# Tuple with different data types
mixed_tuple = ("Alice", 25, 3.14, True)

# Tuple as dictionary keys
grades = {("Math", "Alice"): 95, ("English", "Bob"): 88, ("Science", "Carol"): 92}
print("Math grade for Alice:", grades[("Math", "Alice")])

# Iterating through a tuple
fruits = ("apple", "banana", "orange")
for fruit in fruits:
    print("Fruit:", fruit)

# Checking membership in a tuple
print("Is 'banana' in fruits?", "banana" in fruits)

# Tuple methods
numbers = (2, 4, 6, 8, 10)
print("Length of numbers tuple:", len(numbers))
print("Maximum value in numbers tuple:", max(numbers))
print("Minimum value in numbers tuple:", min(numbers))
print("Sum of values in numbers tuple:", sum(numbers))

