#!/usr/bin/env python3
# Day 34

'''
Python script that can convert time between different time zones using the datetime and pytz libraries.
Before we proceed, please make sure you have the pytz library installed. You can install it by running pip install pytz in your terminal.
'''

import datetime
import pytz

def convert_time_to_timezone(time_str, from_timezone, to_timezone):
    # Parse the input time string
    time_format = "%Y-%m-%d %H:%M:%S"  # Customize the format as per your input
    time = datetime.datetime.strptime(time_str, time_format)

    # Set the source timezone
    source_timezone = pytz.timezone(from_timezone)
    time = source_timezone.localize(time)

    # Convert the time to the target timezone
    target_timezone = pytz.timezone(to_timezone)
    converted_time = time.astimezone(target_timezone)

    return converted_time

# Example usage
time_str = "2023-07-05 14:30:00"  # Input time string
from_timezone = "America/New_York"  # Source timezone
to_timezone = "Asia/Tokyo"  # Target timezone

converted_time = convert_time_to_timezone(time_str, from_timezone, to_timezone)
print("Converted time:")
print(time_str, "at", from_timezone, "converts to:")
print(converted_time.strftime("%Y-%m-%d %H:%M:%S"), "at", to_timezone)

