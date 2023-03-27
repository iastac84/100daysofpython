#!/usr/bin/env python3
# Day 6

# Let's start a coffee shop!
# Let's build a simple robot Barista!
# Building on 05-input-coffeeshop.py we verify the customer's choice and price the items differently

# Variables
COFFEESHOPNAME = "iastac84"
print ("Hello, welcome to " + COFFEESHOPNAME + " Coffee!!!")

# Prompt user for input
NAME = input ("What is your name?\n")

print ("Hello " + NAME + " thank you for coming in today!\n\n")

MENU = "Black Coffee @5.15, Espresso @4.95, Latte @5.55 and Cappucino @6.25"

# Prompt user for input again (with verification of user input this time)
ORDER = input (NAME + ", what would you like from our menu today? We have....\n" + MENU + "\n")

if ORDER.lower() == "black coffee":
    QTY = input ("Sounds good " + NAME + ", how many cups of " + ORDER + " would you like?\n")
    PRICE = 5.15
    print ("")
elif ORDER.lower() == "espresso":
    QTY = input ("Sounds good " + NAME + ", how many cups of " + ORDER + " would you like?\n")
    PRICE = 4.95
    print ("")
elif ORDER.lower() == "latte":
    QTY = input ("Sounds good " + NAME + ", how many cups of " + ORDER + " would you like?\n")
    PRICE = 5.55
    print ("")
elif ORDER.lower() == "cappucino":
    QTY = input ("Sounds good " + NAME + ", how many cups of " + ORDER + " would you like?\n")
    PRICE = 6.25
    print ("")
else:
    print ("Sorry " + NAME + " I didn't recognize your choice of " + ORDER)
    print ("Please try again")
    PRICE = 0  # set default value for PRICE
    exit(20)  # call exit as a function to exit the program

# Calculate the total price
TOTAL = PRICE * int(QTY)

# Use string formatting to display the total price with two decimal points
print("Thanks " + NAME + ", that will be $%.2f please" % TOTAL)
