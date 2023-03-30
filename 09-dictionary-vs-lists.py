#!/usr/bin/env python3
# Day 9

# From https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/
print ("From https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/") 
print ("......................")

# Program to demonstrate space-time trade-off between dictionary and list
print("Program to demonstrate space-time trade-off between dictionary and list")
 
 
# To calculate the time
# difference
import time
 
 
# Creating a dictionary
d ={'john':1, 'alex':2}
 
x = time.time()
 
# Accessing elements
print("Accessing dictionary elements:")
for key in d:
    print(d[key], end=" ")
 
y = time.time()
print("\nTime taken by dictionary:", y-x)
 
# Creating a List
c =[1, 2]
 
x = time.time()
 
print("\nAccessing List elements:")
for i in c:
    print(i, end=" ")
     
y = time.time()
print("\nTime taken by dictionary:", y-x)

