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
    "Marvelous": "online",
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

def myiterator(mydictkeys):
    for x in (mydictkeys):    # Can also use:  for x in (mydictkeys.keys()):
      print(x)

print ("Get Keys.................................")
myiterator(statuses)
print ()
myiterator(thisdict)

def myiteratorvalues(mydictvalues):
    for x in (mydictvalues.values()):
      print(x)

print ()
print ("Get Values...............................")
myiteratorvalues(statuses)
print ()
myiteratorvalues(thisdict)
