#!/usr/bin/env python3
# Day 35

'''
script that counts down the days until Christmas:
'''

import datetime

def countdown_to_christmas():
    today = datetime.date.today()
    christmas = datetime.date(today.year, 12, 25)
    
    # Check if Christmas has already passed this year
    if today > christmas:
        christmas = datetime.date(today.year + 1, 12, 25)
    
    time_remaining = christmas - today
    return time_remaining.days

days_until_christmas = countdown_to_christmas()
print("Days until Christmas:", days_until_christmas)

