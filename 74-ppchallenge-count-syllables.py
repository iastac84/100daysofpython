#!/usr/bin/env python3
# Day 74

# challenge from https://pythonprinciples.com/challenges
'''
Challenge
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:
'''

def countsylla(string):
    count = 1
    for each in (string):
      if each == "-":
         count += 1
    return count


print(countsylla("ho-tel"))
print(countsylla("cat"))
print(countsylla("met-a-phor"))
print(countsylla("ter-min-a-tor"))
