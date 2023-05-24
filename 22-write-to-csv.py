#!/usr/bin/env python3
# Day 22

import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Number'],
    ['Horvath', '34'],
    ['Osho', '32'],
    ['Lockyer', '4'],
    ['Bell', '29'],
    ['Drameh', '2'],
    ['Clark', '18'],
    ['Nakamba', '13'],
    ['Mpanzu', '17'],
    ['Doughty', '45'],
    ['Morris', '9'],
    ['Adebayo', '11'],
]

# Open the CSV file in write mode
with open('./files/output.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the data to the CSV file
    writer.writerows(data)
