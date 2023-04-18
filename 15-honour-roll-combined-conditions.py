#!/usr/bin/env python3
# Day 15

# A Student makes the honor roll if their average score is >= 85
# and their lowest grade is not below 70

gpa = float(input("What was your Grade Point Average?\n"))
lowest_grade = float(input("what was your lowest grade?\n"))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
   honour_roll = False

if honour_roll:
    print("You made the honour roll")
else:
    print("Try harder next time!!!!!!")
