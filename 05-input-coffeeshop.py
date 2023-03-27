#!/usr/bin/env python3

# Let's start a coffee shop!
# Let's build a simple robot Barista!

# Variables
COFFEESHOPNAME = "iastac84"
print ("Hello, welcome to " + COFFEESHOPNAME + " Coffee!!!")

# Prompt user for input 
NAME = input ("What is your name?\n")

print ("Hello " + NAME + " thank you for coming in today!\n\n")

MENU = "Black Coffee, Espresso, Latte, Cappucino"
PRICE = 7

# Prompt user for input again (note, no verification of user input at this stage) 
ORDER = input (NAME + ", what would you like from our menu today? We have....\n" + MENU + "\n")
QTY = input ("Sounds good " + NAME + ", how many cups of " + ORDER + " would you like?\n")
print ("")

# Convert string to integer with int function
TOTAL= PRICE * int(QTY)

# You can concatenate Strings, not integer
# Convert interger to string
print ("Thanks " + NAME + ", that will be $" + str(TOTAL) + " please")
