#!/usr/bin/env python3
# Day 98

# 

import os

def search_string_in_files(directory, search_string):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):  # Change the extension as needed
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r') as file:
                        for line in file:
                            if line.startswith(search_string):
                                print(f"Found '{search_string}' at the start of a line in file: {file_path}")
                                break  # Remove this line if you want to find all occurrences
                except IOError:
                    print(f"Could not read file: {file_path}")

# Replace 'def' with the string you want to search for at the start of a line
search_string = 'def'
current_directory = '.'  # Indicates the current directory

search_string_in_files(current_directory, search_string)

