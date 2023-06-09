#!/usr/bin/env python3
# Day 17

"""
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""

print ("Classes and objects in their simplest form:")
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x) 
print()

# The __init__() Function
"""
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
""" 

print ("# __init__() Function:")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
