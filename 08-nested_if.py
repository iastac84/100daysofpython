#!/usr/bin/env python3
# Day 8

# Script to return tax rates for shopping in Canada
# where rates differ from province to province
# Using nested if, where an action depends on a combination of conditions  

country = input("What country do you live in?\n")
tax = 0

if country.lower() == 'canada':
    province = input ("What province do you live in?\n")
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
    print("For someone from " + province + " tax is calcuted at " + str (tax) + " %")
    exit(15) 
else:
    tax = 0
print("For someone from " + country + " tax is calcuted at " + str (tax) + " %")
