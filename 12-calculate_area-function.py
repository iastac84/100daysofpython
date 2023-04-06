#!/usr/bin/env python3
# Day 12

def calculate_area():
    """
    This function prompts the user to enter the length and width of a rectangle,
    and then calculates and returns the area of the rectangle.
    """
    length = float(input("Enter the length in meters of the garden room: "))
    width = float(input("Enter the width in meters: "))
    area = length * width
    return area

sqmeters = calculate_area()
print("The garden office will be", str(sqmeters) + " sq meters")

print ()
# Check if garden room is over 25 sq meters and therefore requires planning permission 
if sqmeters <= 25:
    print ("You do not need planning permission for your garden room")
else:
    print ("At " + str(sqmeters) + " sq meters, your garden room is over 25 sq meters and needs planning permission")

