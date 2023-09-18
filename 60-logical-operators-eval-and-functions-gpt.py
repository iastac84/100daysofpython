#!/usr/bin/env python3
# Day 60
 
# ChatGPT suggested improvements

import os

# Constants
COFFEESHOP_NAME = "iastac84"

def clear_screen():
    os.system('clear')  # You may need to replace 'clear' with 'cls' on Windows

def greet_customer():
    clear_screen()
    print("\n#####################################################")
    print(f"Hello, welcome to {COFFEESHOP_NAME} Coffee!!!")
    print("#####################################################")

def check_if_evil(name):
    evil_customers = {"ben", "patricia", "loki"}
    name = name.lower()
    if name in evil_customers:
        evil_status = input(f"Are you evil {name.title()}? (yes or no)\n").strip().lower()
        if evil_status != "yes":
            print(f"\nC'mon {name.title()} we know you really are evil! Now get out!!\n")
            exit(66)
        else:
            print(f"Fair play for being honest {name.title()}\n")
            ask_good_deeds(name)
    else:
        print(f"Hello {name.title()} thank you for coming in today!\n\n")
        exit(22)

def ask_good_deeds(name):
    while True:
        try:
            good_deeds = int(input(f"How many good deeds have you done so far today {name.title()}?\n").strip())
            if good_deeds >= 7:
                print(f"Hey {name.title()} we know you are evil but as you've been good today you can come in!!\n\n")
                exit(6)
            else:
                print(f"You are not welcome here {name.title()}!! Get out!! Come back when you've done some more good deeds!!\n")
        except ValueError:
            print("Please enter a valid number of good deeds.")

def main():
    greet_customer()
    name = input("What is your name?\n").strip()
    print("")
    check_if_evil(name)

if __name__ == "__main__":
    main()


'''
    Indentation and Consistency: Ensure that your code follows a consistent indentation style (typically 4 spaces per level). In Python, proper indentation is essential for code readability and functionality.

    Function Arguments: It's a good practice to pass arguments to functions rather than relying on global variables. Modify your functions to accept parameters, which makes your code more modular and easier to understand.

    Constants in UPPERCASE: Conventionally, constants are written in UPPERCASE to indicate that they should not be modified. So, it's better to use COFFEESHOPNAME instead of COFFEESHOPNAME.

    Avoid Global Variables: Whenever possible, avoid using global variables. Pass values as function parameters and return results as needed. Global variables can make your code harder to understand and maintain.

    User Input Validation: You should validate user inputs to handle unexpected input gracefully. For instance, if a user enters a non-integer when asked for the number of good deeds, your code should handle that.

    Clear Screen: The usage of os.system('clear') may not work on all systems. Consider using a cross-platform method to clear the screen.

    Error Handling: Consider adding proper error handling, especially when converting user input to integers or handling unexpected exceptions.

    Comments: While your code has some comments, consider adding more comments to explain the purpose of each function and to clarify complex logic.

'''
