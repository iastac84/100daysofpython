#!/usr/bin/env python3
# Day 61

# Python script to read in a JSON file and output specific elements or data from that JSON file. 

import json

# Function to read JSON from a file and output specific elements
 
import json

def read_and_output_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            
            # Assuming data is a list of dictionaries with 'name' key
            for item in data:
                name = item.get('name', 'Name not found')
                favoriteFruit = item.get('favoriteFruit', 'Name not found')
                print(f'Name: {name}, favourite fruit: {favoriteFruit}')
            
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    json_file_path = './files/sample1.json'
    read_and_output_json(json_file_path)

