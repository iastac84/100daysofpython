#!/usr/bin/env python3
# Day 78

# https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/

# Python program to find smallest 
# number in a list
 
# list of numbers
list1 = [102, -20, 6, 45, 99, 123, 84]
 
# A few different methods
# sorting the list
list1.sort()
 
# printing the first element
print("Smallest element is:", list1[0])

# Get largest
list1.sort(reverse=True)

# printing the first element
print("Largest number is:", list1[0])

# Or use min / max
minnumber = min(list1)
maxnumber = max(list1)
print("min number is:", minnumber)
print("max number is:", maxnumber)

# Or using len
list1.sort()
listlenght = len(list1)
print("There are", listlenght, "numbers in the list")
secondhighno = listlenght -2 # minus 2 as the index starts at zero
print("The second highest number is:", list1[secondhighno])
