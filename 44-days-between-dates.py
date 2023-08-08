#!/usr/bin/env python3
# Day 44

from datetime import datetime

print ("Need to get back on the python horse!")
print ()

def calculate_days_between_dates(date1, date2):
    try:
        date_format = "%Y-%m-%d"  # Adjust this format to match your date input
        date1_obj = datetime.strptime(date1, date_format)
        date2_obj = datetime.strptime(date2, date_format)
        
        delta = date2_obj - date1_obj
        return abs(delta.days)  # Taking absolute value to ensure positive number of days
    except ValueError:
        return "Invalid date format"

# Example usage
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

days_difference = calculate_days_between_dates(date1, date2)
if isinstance(days_difference, int):
    print(f"Number of days between the two dates: {days_difference}")
else:
    print(days_difference)

