#!/usr/bin/env python3
# Day 9

# From https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/
print ("From https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/") 
print ("......................")

# Program to fetch particular elements of structure
print ("Program to fetch particular elements of structure")
 
 
import time
 
 
# Creating dictionary and list
dict_name ={"bob":12, "john":11}
list_name =[2, 3, 4, 5, 1]
 
# Time taken by dictionary
x = time.time()
L = dict_name["bob"]
print (L)
y = time.time()
print("Time taken by dictionary:", y-x)
 
# Time taken by list
x = time.time()
L = list_name[2]
print (L)
y = time.time()
print("\nTime taken by list:", y-x)
