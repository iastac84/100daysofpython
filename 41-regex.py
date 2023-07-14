#!/usr/bin/env python3
# Day 41

"""
In Python, you can use regular expressions and the re module to perform similar functionality as grep for pattern matching and searching within strings.
Here's an example of how you can use the re module to search for a pattern within a string:
"""

import re

def grep(pattern, text):
    matches = re.findall(pattern, text)
    return matches

# Example usage
input_text = "Hello, this is a sample text. It contains some words."
#pattern = r"\b\w+"
pattern = "word"

matches = grep(pattern, input_text)

if matches:
    for match in matches:
        print(match)
else:
    print("No matches found.")

