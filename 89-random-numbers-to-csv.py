#!/usr/bin/env python3
# Day 89

# Generate 200 random numbers and save to csv

import random
import csv

def generate_random_numbers(num_of_numbers, num_length):
    random_numbers = []
    for _ in range(num_of_numbers):
        # Generate a random number with 7 digits
        number = ''.join(str(random.randint(0, 9)) for _ in range(num_length))
        random_numbers.append(number)
    return random_numbers

def save_to_csv(numbers):
    with open('./files/random_numbers.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Random Numbers'])
        for number in numbers:
            csv_writer.writerow([number])

if __name__ == "__main__":
    num_of_numbers = 200
    num_length = 7

    random_numbers = generate_random_numbers(num_of_numbers, num_length)
    save_to_csv(random_numbers)

    print(f"{num_of_numbers} random {num_length}-digit numbers generated and saved to 'random_numbers.csv'")
