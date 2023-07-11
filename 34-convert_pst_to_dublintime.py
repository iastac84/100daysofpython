#!/usr/bin/env python3
# Day 34

'''
Python script that can convert time between different time zones using the datetime and pytz libraries.
Before we proceed, please make sure you have the pytz library installed. You can install it by running pip install pytz in your terminal.
'''

import datetime
import pytz

def convert_time_to_timezones(time_str, from_timezone, to_timezones):
    # Parse the input time string
    time_format = "%Y-%m-%d %H:%M:%S"  # Customize the format as per your input
    time = datetime.datetime.strptime(time_str, time_format)

    # Set the source timezone
    source_timezone = pytz.timezone(from_timezone)
    time = source_timezone.localize(time)

    converted_times = {}
    for to_timezone in to_timezones:
        # Convert the time to the target timezone
        target_timezone = pytz.timezone(to_timezone)
        converted_time = time.astimezone(target_timezone)
        converted_times[to_timezone] = converted_time

    return converted_times

# Example usage
#time_str = "2023-07-05 14:30:00"  # Input time string
time_str = input("Enter the time in Pleasanton, CA, USA (YYYY-MM-DD HH:MM:SS): ")
from_timezone = "America/Los_Angeles"  # Source timezone
to_timezones = ["Europe/Dublin"]  # Target timezones

print(time_str, "in Pleasanton, CA, USA converts to:")
print()

converted_times = convert_time_to_timezones(time_str, from_timezone, to_timezones)
for timezone, converted_time in converted_times.items():
    print(timezone, ":", converted_time.strftime("%Y-%m-%d %H:%M:%S"))

