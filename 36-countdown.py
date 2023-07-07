#!/usr/bin/env python3
# Day 36

'''
Python script that prompts the user for the time in seconds and then starts a countdown timer

In this script, the countdown_timer function takes the number of seconds as an argument and then uses a while loop to countdown from the given number of seconds to zero. The time.sleep(1) function is used to pause the script for one second between each iteration of the loop. Once the countdown reaches zero, it prints "Time's up!".
'''

import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

user_input = input("Enter the time in seconds: ")
try:
    seconds = int(user_input)
    countdown_timer(seconds)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

