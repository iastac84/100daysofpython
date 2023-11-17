#!/usr/bin/env python3
# Day 89

# Group list of numbers into groups of 10

import csv

def read_csv_and_output_groups(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header
        numbers = [row[0] for row in csv_reader]

        for i in range(0, len(numbers), 10):
            group = numbers[i:i+10]
            print(','.join(group))

if __name__ == "__main__":
    file_to_read = './files/random_numbers.csv'
    read_csv_and_output_groups(file_to_read)
