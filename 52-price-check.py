#!/usr/bin/env python3
# Day 52

"""
Hackerrank exercise Nov 2021
"""

import math
import os
import random
import re
import sys 

# Complete the 'priceCheck' function below. 
#
# The function is expected to return an INTEGER
# The function accepts following parameters:
# 1. STRING_ARRAY products 
# 2. FLOAT_ARRAY productPrices
# 3. STRING_ARRAY productSold
# 4. FLOAT_ARRAY soldPrice

def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    error_count = 0
    
    # Create a dictionary to store the actual prices of products
    price_dict = {}
    for i in range(len(products)):
        price_dict[products[i]] = productPrices[i]
    
    # Iterate through the products sold
    for i in range(len(productSold)):
        product = productSold[i]
        actual_price = price_dict.get(product, -1)  # Get the actual price of the product, default to -1 if not found
        
        if actual_price == -1:
            # Product not found in the price dictionary
            error_count += 1
        elif actual_price != soldPrice[i]:
            # Sold price doesn't match the actual price
            error_count += 1
    
    return error_count

if __name__ == '__main__':
    products = ["eggs", "eggs", "milk", "cheese", "eggs", "chocolate"]
    productPrices = [2.89, 2.89, 3.29, 5.79, 2.89, 3.50]
    productSold = ["eggs", "eggs", "milk", "cheese", "eggs", "chocolate"]
    soldPrice = [2.99, 2.89, 3.29, 5.78, 2.89, 3.60]
    
    result = priceCheck(products, productPrices, productSold, soldPrice)
    print("Number of products missold:")
    print(result)

