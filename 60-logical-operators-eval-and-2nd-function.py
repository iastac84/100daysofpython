#!/usr/bin/env python3
# Day 60

# Back to the coffee shop to keep out the evil customers!
# Make repeatable code a function

# Variables
COFFEESHOPNAME= "iastac84"
good_deeds=1
evil_status="Yes"
 
import os
os.system('clear')
 

print("")
print("#####################################################")
print ("Hello, welcome to " + COFFEESHOPNAME + " Coffee!!!")
print("#####################################################")
print(evil_status)

# Function to check for evil customers! 
def check_if_evil():
    if NAME.lower() == "ben" or NAME.lower() == "patricia" or NAME.lower() == "loki":
       evil_status = input("Are you evil " + NAME.title() + "? (yes or no) \n")
       if evil_status.title() != "Yes":
         print("\n" "C'mon " + NAME.title() + " we know you really are evil! Now get out!!\n")
         exit(66)
       else:
         print("Fair play for being honest " + NAME.title() + "\n")
         ask_good_deeds() 
    else:
       print ("Hello " + NAME.title() + " thank you for coming in today!\n\n")
       evil_status="No"
       # print(evil_status)
       exit(22)

# Function to ask if Ben, Patricia or Loki admit to being evil, ask them how many good deeds they have performed today! 
def ask_good_deeds():
    good_deeds = int(input("How many good deeds have you done so far today " + NAME.title() + "? \n"))
    if evil_status.title() == "Yes" and good_deeds < 7:
      print("You are not welcome here " + NAME.title() + "!! Get out!! Come back when you've done some more good deeds!!\n")
    else:
      print("Hey " + NAME.title() + " we know you are evil but as you've been good today you can come in!!\n\n")
      exit(6)

# Prompt user for input and return with Proper Case with title()
NAME = input ("What is your name?\n")
print("")
check_if_evil()

while good_deeds < 7:
   print("30 minutes later...")
   ask_good_deeds() 
