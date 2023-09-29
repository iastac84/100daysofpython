#!/usr/bin/env python3
# Day 65

# Python script to read in a JSON file and output specific elements or data from that JSON file. 

import json
import os

def get_country_captial(json_file_path):
   # Prompt the user to enter a country
   user_country_input = input("Enter a country: ")
   user_country = user_country_input.title()
   # Load the data from the external JSON file
   try:
       with open(json_file_path, "r") as json_file:
        countries_data = json.load(json_file)
   except FileNotFoundError:
       print("Error: Could not find the JSON file.")
       exit()
   # Create a list of country names for validation
   country_names = [country["country"] for country in countries_data["countries"]]
   # Validate the user's input
   if user_country in country_names:
       # Find the capital city
       for country in countries_data["countries"]:
           if country["country"] == user_country:
               capital = country["capital"]
               print(f"The capital city of {user_country} is {capital}.")
   else:
       print("Country " + user_country + " not found in the list.")

    
def main():
    print("Welcome to the captial city finder!")

    while True:
        get_country_captial(json_file_path)

        play_again = input("Do you want find another captial city? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for using the captial city query service! Have a great day!")
            break


if __name__ == "__main__":
    json_file_path = 'files/country-by-capital-city-list-countries.json'
    main()

