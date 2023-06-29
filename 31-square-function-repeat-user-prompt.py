#!/usr/bin/env python3
# Day 31

'''
Simple function that calculates the square of a number
Then asks the user if they want to calculate the square of another number. If the answer is "yes", it prompts for the next number and repeats the process. If the answer is "no", the loop is exited, and a farewell message is displayed.
'''

def square(num):
    result = num * num
    return result

# Function to prompt user for yes/no input
def get_user_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input == "yes" or user_input == "no":
            return user_input
        else:
            print("Please enter 'yes' or 'no'.")

# Prompt the user for the first number
num = float(input("Enter a number: "))

# Call the function and print the result
print("The square of", num, "is", square(num))

# Prompt the user if they want to calculate the square of another number
calculate_another = get_user_input("Do you want to calculate the square of another number? (yes/no): ")

while calculate_another == "yes":
    # Prompt the user for the next number
    num = float(input("Enter another number: "))

    # Call the square function and print the result
    print("The square of", num, "is", square(num))

    calculate_another = get_user_input("Do you want to calculate the square of another number? (yes/no): ")

print("Thank you for using the program!")
