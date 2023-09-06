#!/usr/bin/env python3
# Day 53

"""
"""

import math
import os
import random
import re
import sys 

def findMostExpensivePub(pub_names, pub_prices):
    # Create a dictionary to store the prices of each pub
    pub_price_dict = dict(zip(pub_names, pub_prices))

    # Find the maximum price
    max_price = max(pub_prices)

    # Find the pub(s) with the maximum price
    expensive_pubs = [pub for pub, price in pub_price_dict.items() if price == max_price]

    return max_price, expensive_pubs

def findLeastExpensivePub(pub_names, pub_prices):
    # Create a dictionary to store the prices of each pub
    pub_price_dict = dict(zip(pub_names, pub_prices))

    # Find the lowest price
    min_price = min(pub_prices)

    # Find the pub(s) with the lowest price
    least_expensive_pubs = [pub for pub, price in pub_price_dict.items() if price == min_price]

    return min_price, least_expensive_pubs


if __name__ == '__main__':
    pubs = ["The Cobblestone", "The Long Hall", "The Brazen Head", "The Temple Bar", "Peter's Pub", "Brogans", "Kavanagh's"]
    pubPrices = [8.20, 7.10, 7.40, 8.50, 6.90, 7.00, 6.90]

    num_pubs = len(pubs)  # Get the number of listed pubs

    # Calculate the average price
    average_price = round(sum(pubPrices) / len(pubPrices), 2)

    # Get most expensive
    max_price, most_expensive_pubs = findMostExpensivePub(pubs, pubPrices)

    if most_expensive_pubs:
        print("The pub(s) with the most expensive pint of Guinness costing", max_price, "euros is/are")
        for pub in most_expensive_pubs:
            print(pub)
    else:
        print("There are no pubs in the list.")

    print("")

    # Get least expensive
    min_price, least_expensive_pubs = findLeastExpensivePub(pubs, pubPrices)

    if least_expensive_pubs:
        print("The pub(s) with the least expensive pint of Guinness costing", min_price, "euros is/are")
        for pub in least_expensive_pubs:
            print(pub)
    else:
        print("There are no pubs in the list.")

    print("")
    print("The average price of a pint of Guinness among the", num_pubs, "listed pubs is:", average_price, "euros.")
    print("")

    # Get the total price of a having a pint in each pub
    total_price = (sum(pubPrices)) 
    print("The cost of ordering a pint of Guinness in each of the", num_pubs, "pubs is", total_price, "euros.")
