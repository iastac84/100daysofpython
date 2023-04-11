#!/usr/bin/env python3
# Day 14

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# r - read, a - append, w - write, x - create

print (":::::print whole text:::::")
lyrics = open("files/rappers.txt", "r")
print(lyrics.read())

print (":::::print first 17 characters of the file:::::")
lyrics = open("files/rappers.txt", "r")
print(lyrics.read(17))
print()

print (":::::with readline() return single lines:::::")
print (":::::including end='' as each string contains trailing newlines:::::")
lyrics = open("files/rappers.txt", "r")
print(lyrics.readline(),end='')
print(lyrics.readline(),end='')
print()

print (":::::loop through the file line by line::::::")
print (":::::including end='' as each string contains trailing newlines:::::")
f = open("files/rappers.txt", "r")
for x in f:
  print(x,end='') 
