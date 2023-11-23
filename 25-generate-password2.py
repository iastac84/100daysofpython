#!/usr/bin/env python3
# Day 25

'''
Python script that generates a random password based on user-specified criteria:
In this script, the generate_password function takes three parameters: length (the desired password length), include_digits (a boolean indicating whether to include digits in the password), and include_symbols (a boolean indicating whether to include symbols in the password).

The function creates a character set based on the user's preferences, using the string module from the Python standard library. It then uses random.choice in a loop to randomly select characters from the character set and build the password string.

The script prompts the user to enter the desired password length and specify whether they want to include digits and symbols. It then calls the generate_password function with the provided criteria and prints the generated password.

Update 20231123 to reduce the number of symbols/special characters
'''

import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True, max_symbols=3):
    # Define character sets based on user preferences
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_symbols:
        symbols = string.punctuation
        # Shuffle the symbols to randomize selection
        symbols = ''.join(random.sample(symbols, len(symbols)))
        # Ensure only a maximum of 'max_symbols' symbols are included
        chars += symbols[:max_symbols]

    # Generate password using random.choice
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Prompt user for password criteria
password_length = int(input("Enter the desired password length: "))
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate and print the password
password = generate_password(password_length, include_digits, include_symbols)
print("Generated Password:", password)

