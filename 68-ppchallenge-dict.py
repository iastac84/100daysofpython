#!/usr/bin/env python3
# Day 68

# challenge from https://pythonprinciples.com/challenges
'''
Playing with dictionaries 
'''

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(statuses)
print ()
print ("Here we use an object type of:")
print (type(statuses))
print ()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print ()

def myiterator(mydict):
    for x in (mydict):
      print(x)

myiterator(statuses)
myiterator(thisdict)
