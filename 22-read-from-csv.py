#!/usr/bin/env python3
# Day 22

import csv

# Open the CSV file in read mode
with open('./files/input.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Access each column value using indexing
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]
        # Do something with the column values
        print(col1, col2, col3)
