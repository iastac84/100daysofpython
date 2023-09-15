#!/usr/bin/env python3
# Day 59

# Back to the coffee shop to keep out the evil customers!
# And another boolean example

# Variables
COFFEESHOPNAME= "iastac84"

print("")
print("#####################################################")
print ("Hello, welcome to " + COFFEESHOPNAME + " Coffee!!!")
print("#####################################################")

# Prompt user for input and return with Proper Case with title()
NAME = input ("What is your name?\n")
print("")

if not NAME.lower() == "ben":
   print("Come on in " + NAME.title() + "!!")
else:
   print("PLEASE GO AWAY " + NAME.upper() + "!!")
