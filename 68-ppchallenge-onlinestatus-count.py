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

def online_count(peopledict):
    count = 0 
    for status in (peopledict.values()):    
      if status == "online":
         count += 1
    return count

print("The number of people is online is",online_count(statuses))
