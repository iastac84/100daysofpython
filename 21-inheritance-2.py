#!/usr/bin/env python3
# Day 21

print ("Creating a Parent Class...") 
# Add the __init__() function to the Student class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Ethan", "Horvath")
x.printname()

