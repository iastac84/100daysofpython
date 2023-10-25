#!/usr/bin/env python3
# Day 78

# challenge from https://pythonprinciples.com/challenges
'''
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.
For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
You may assume that no numbers are smaller or larger than -100 and 100.

Hint
Split the problem up into subproblems:
First find the smallest number.
Then find the largest number.
Then compute their difference and return it.
To find the smallest number you can use the min() built-in. Alternatively you can set smallest = 100 and loop over each number in the input list. Whenever you see a smaller one, set smallest to it.
'''

def largest_difference(numbers):
   numbers.sort()
   print(numbers[0])
   return numbers[0] 
   

print(largest_difference([[1, 2, 3, 4, 5, 6]]))

