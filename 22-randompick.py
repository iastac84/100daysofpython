#!/usr/bin/env python3
# Day 22

import csv
import random

# Open the CSV file in read mode
with open('./files/randompick.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Convert the CSV data to a list of rows
    rows = list(reader)
    
    # Choose a random row from the list
    random_row = random.choice(rows)
    
    # Convert the random row to a string
    random_row_str = str(random_row)
    
    # Do something with the randomly selected row string
    print("And the man of the match will be " + random_row_str + " !")
