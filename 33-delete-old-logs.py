#!/usr/bin/env python3
# Day 33

'''
Python script that achieves the task of deleting log entries for the previous day
'''

import os
import datetime

# Define the log directory path
LOG_DIR = "/path/to/logs"

# Get the date of the previous day
previous_day = datetime.date.today() - datetime.timedelta(days=1)
previous_day_str = previous_day.strftime("%Y-%m-%d")

# Iterate over log files in the directory and delete entries for the previous day
for root, dirs, files in os.walk(LOG_DIR):
    for file in files:
        if file.endswith(".log"):
            file_path = os.path.join(root, file)
            with open(file_path, "r+") as log_file:
                lines = log_file.readlines()
                log_file.seek(0)
                log_file.truncate()
                for line in lines:
                    if previous_day_str not in line:
                        log_file.write(line)

