#!/usr/bin/env python3
# Day 12

# This function will take a name and return the first initial
# Parameters:
#   name: name of person
# Return value
#   first letter of name passed in

def get_initial(name):
    initial = name[0:1].upper()
    return initial

# Ask for someone's name and return the initials
first_name = input('Enter your first name: ')
second_name = input('Enter your second name: ')

# Call get_initial function to retrieve first letter of name
first_name_initial = get_initial(first_name)
second_name_initial = get_initial(second_name)
print()
print('Your initials are: ' + first_name_initial + second_name_initial)
