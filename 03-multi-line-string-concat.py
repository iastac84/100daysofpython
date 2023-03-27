#!/usr/bin/env python3
# Day 3

# Multi-line string
print("""I am Batman.
I am looking for the Penguin. 
Have you seen him?""")
print ("")

# Multi-line string with variables and concatenate
superhero1= "Batman"
superhero2= "Superman"
superhero3= "The Flash"
superhero4= "Spider-man "
print("What did you think of the movie? " + superhero1 + " Vs " + superhero2)
print ("")

# \n for newline character 
print ("A list of Superheros, \n" + "but who is the odd one out?....") 

# Join the variables into a list
superlist = '\n'.join([superhero2, superhero3, superhero4, superhero1])
print(superlist)

# Multiply
print("The odd one out is of course: " + superhero4 * 20)
