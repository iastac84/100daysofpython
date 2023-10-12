#!/usr/bin/env python3
# Day 69

# challenge from https://pythonprinciples.com/challenges
'''
The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
For example, consider the following dictionary:
Adding people to the dictionary in this version
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

print()
print("The number of people online is",online_count(statuses))
print()
print("Let's add some Premier League footballers to the dictionary!") 

# Add people to dictionary
statuses["Marvelous"] = "offline"
statuses["Chiedozie"] = "online"
statuses["Pelly"] = "online"
statuses["Tom"] = "offline"
statuses["Reece"] = "offline"
statuses["Tahith"] = "online"
statuses["Elijah"] = "online"
statuses["Alfie"] = "offline"
statuses["Carlton"] = "online"
print(statuses)

print()
print("The number of people now online is",online_count(statuses))
print()
