#!/usr/bin/env python3
# Day 32

'''
script demonstrates three common use cases of regular expressions:
'''

import re

# Example 1: Matching a pattern in a string
text = "Hello, this is a sample text with some numbers 12345 and symbols #@!$"
pattern = r"\b[a-zA-Z]+\b"  # Matches alphabetic words

matches = re.findall(pattern, text)
print("Example 1:")
print("Matches:", matches)
print()

# Example 2: Extracting data using capture groups
text = "John Doe, 30 years old, Email: john@example.com"
pattern = r"([A-Za-z ]+), (\d+) years old, Email: (\S+)"

match = re.search(pattern, text)
if match:
    name = match.group(1)
    age = match.group(2)
    email = match.group(3)

    print("Example 2:")
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print()

# Example 3: Replacing patterns in a string
text = "Hello, world! How are you doing?"

new_text = re.sub(r"world", "Python", text)

print("Example 3:")
print("Original Text:", text)
print("Modified Text:", new_text)

