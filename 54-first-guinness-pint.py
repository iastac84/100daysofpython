#!/usr/bin/env python3
# Day 54

"""
"""

# Prompt the user for their name
name = input("Hello mate, what's your name? ")

def findPubPrice(pub_name, pub_names, pub_prices):
    try:
        index = pub_names.index(pub_name)
        return pub_prices[index]
    except ValueError:
        return None

if __name__ == '__main__':
    pubs = ["The Cobblestone", "The Long Hall", "The Brazen Head", "The Temple Bar", "Peter's Pub", "Brogans"]
    pubPrices = [7.20, 7.10, 7.40, 8.50, 6.90, 7.00]

    # Prompt the user to choose a pub from the list
    print("Here is a list of popular pubs in Dublin:")
    for i, pub in enumerate(pubs, start=1):
        print(f"{i}. {pub}")
    print("")

    choice = input(f"Right, {name} where are we going for a pint? ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(pubs):
            selected_pub = pubs[choice - 1]
            price = findPubPrice(selected_pub, pubs, pubPrices)

            if price is not None:
                pints = int(input(f"How many pints of Guinness do you want at {selected_pub}? "))
                amount_due = price * pints
                print(f"The amount due for {pints} pints of Guinness at {selected_pub} is {amount_due:.2f} euros.")
            else:
                print("Invalid pub selection.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

