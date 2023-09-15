#!/usr/bin/env python3
# Day 58

# Back to the coffee shop to keep out the evil customers!

# Variables
COFFEESHOPNAME= "iastac84"
MENU = "Black Coffee @5.15, Espresso @4.99, Latte @5.55 and Cappucino @6.25"

print("")
print("#####################################################")
print ("Hello, welcome to " + COFFEESHOPNAME + " Coffee!!!")
print("#####################################################")

# Prompt user for input and return with Proper Case with title()
NAME = input ("What is your name?\n")
print("")

# Check for evil customers! 
if NAME.lower() == "ben" or NAME.lower() == "patricia" or NAME.lower() == "loki":
   evil_status = input("Are you evil " + NAME.title() + "? (yes or no) \n")
   if evil_status.title() != "Yes":
     print("\n" "C'mon " + NAME.title() + " we know you really are evil! Now get out!!\n")
     exit(66)

# If Ben, Patricia or Loki admit to being evil, ask them how many good deeds they have performed today! 
   print("")
   good_deeds = int(input("Fair play for being honest " + NAME.title() + ", how many good deeds have you done today? \n"))
   if evil_status.title() == "Yes" and good_deeds < 4:
     print("\n" "You are not welcome here " + NAME.title() + "!! Get out!! Come back when you've done some more good deeds!!\n")
     exit(33)
   else:
     print("")
     print("Hey " + NAME.title() + " we know you are evil but as you've been good today you can come in!!\n\n")
else:
   print ("Hello " + NAME.title() + " thank you for coming in today!\n\n")

