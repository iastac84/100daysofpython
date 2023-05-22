#!/usr/bin/env python3
# Day 21

'''
Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
'''

# Add the __init__() function to the Student class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Carlton", "Morris", 2023)
x.welcome()
