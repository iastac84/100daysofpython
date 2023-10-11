#!/usr/bin/env python3
# Day 68

# challenge from https://pythonprinciples.com/challenges
'''
Challenge:Online status
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:
'''

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print ("Here we use an object type of:")
print (type(statuses))
print ()

def online_count(statuses):
    for x in statuses:
      print(x)


