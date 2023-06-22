#!/usr/bin/env python3
# Day 28

'''
Calculate the date and time from epoch linux time
'''

import datetime

def calculate_date_time(epoch_time):
    timestamp = datetime.datetime.utcfromtimestamp(epoch_time)
    return timestamp

# Prompt the user to enter the epoch time
epoch_time = int(input("Enter the epoch time: "))

result = calculate_date_time(epoch_time)
print("UTC Date and time:", result)

