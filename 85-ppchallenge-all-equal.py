#!/usr/bin/env python3
# Day 85

# challenge from https://pythonprinciples.com/challenges

'''
Challenge: 
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''

def all_equal(equal_list):

    result = all(element == equal_list[0] for element in equal_list)

    if (result):
        return True
    else:
        return False

print(all_equal([1, 1, 1]))
print(all_equal([7, 7, 7, 8]))
print(all_equal(["a", "a", "a", "a"]))
print(all_equal(["a", "b", "b", "a"]))
