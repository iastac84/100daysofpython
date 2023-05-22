#!/usr/bin/env python3
# Day 21

"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""

print ("Creating a Parent Class...") 
# Any class can be a parent class, so the syntax is the same as creating any other class
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Amarii", "Bell")
x.printname() 

#Use the Person class to create an object, and then execute the printname method:

print ("")
print ("Creating a Child Class...") 
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

x = Student("Tommy", "Lockyer")
x.printname()
