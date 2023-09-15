#!/usr/bin/env python3
# Day 58

# Back to the coffee shop to keep out the evil customers!

# Variables
COFFEESHOPNAME= "iastac84"
MENU = "Black Coffee @5.15, Espresso @4.99, Latte @5.55 and Cappucino @6.25"

print ("Hello, welcome to " + COFFEESHOPNAME + " Coffee!!!")

# Prompt user for input and return with Proper Case with title()
NAME = input ("What is your name?\n")

# Check for evil customers! 
if NAME.lower() == "ben":
   evil_status = input("Are you evil " + NAME.title() + "? \n")
   if evil_status.title() == "Yes":
     print("You are not welcome here " + NAME.title() + "!! Get out!! But thanks for telling the truth about your evilness :)")
     exit(6)
   else:
     print("C'mon " + NAME.title() + " we know you really are evil! Now get out!!")
     exit(66)
else:
   print ("Hello " + NAME.title() + " thank you for coming in today!\n\n")

# Prompt user for input again (with verification of user input this time)
# Using .lower() so the user/client can use any capitalisation and we still match, with the output returned in Proper Case
ORDER = input (NAME.title() + ", what would you like from our menu today? We have....\n" + MENU + "\n")

if ORDER.lower() == "black coffee":
    QTY = input ("Sounds good " + NAME.title() + ", how many cups of " + ORDER.title() + " would you like?\n")
    PRICE = 5.15
    print ("")
elif ORDER.lower() == "espresso":
    QTY = input ("Sounds good " + NAME.title() + ", how many cups of " + ORDER.title() + " would you like?\n")
    PRICE = 4.99
    print ("")
elif ORDER.lower() == "latte":
    QTY = input ("Sounds good " + NAME.title() + ", how many cups of " + ORDER.title() + " would you like?\n")
    PRICE = 5.55
    print ("")
elif ORDER.lower() == "cappucino":
    QTY = input ("Sounds good " + NAME.title() + ", how many cups of " + ORDER.title() + " would you like?\n")
    PRICE = 6.25
    print ("")
else:
    print ("Sorry " + NAME.title() + " I didn't recognize your choice of " + ORDER.title())
    print ("Please try again")
    PRICE = 0  # set default value for PRICE
    exit(20)  # call exit as a function to exit the program

# Calculate the total price
TOTAL = PRICE * int(QTY)

# Use string formatting to display the total price with two decimal points
print("Thanks " + NAME.title() + ", that will be $%.2f please" % TOTAL)
