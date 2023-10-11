#!/usr/bin/env python3
# Day 68

# challenge from https://pythonprinciples.com/challenges
'''
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
For example, consider the following dictionary:
'''

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

count = 0

def online_count(mydict):
    for x in (mydict.values()):    
      if x == "online":
          sum = count + 1
    print (sum)

online_count(statuses)
