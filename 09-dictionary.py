#!/usr/bin/env python3
# Day 9

# Collections
# Dictionaries vs Lists


# Dictionary - key and value pairs
alien_0 = { "color" : "green" , "points" : 5}
print(alien_0)
alien_0 ["home planet"] = "Tatooine"  # Add key pair
alien_0 ["speed"] = "Slow"            # Add key pair
print(alien_0)
print(f"The alien is {alien_0['color']}.")
alien_0 ["color"] = "Blue"            # Change value
print(f"The alien is now {alien_0['color']}.")
print("")

# Creating a List with
# the use of multiple values
List = ["Luton", "Vs", "Watford", "Kenilworth Road"]
print("List containing multiple values: ")
print(List[0]) 
print(List[2])
print(List[3])
   
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [["Luton", "Morris", "Adebayo"] , ["Watford", "Bachmann", "Cathcart"]]
print("\nMulti-Dimensional List: ")
print(List)
print(List[0])                         # Print first list in the nest
