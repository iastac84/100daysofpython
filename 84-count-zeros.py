#!/usr/bin/env python3
# Day 84

# Counting zeros

def counting_zeros(binary_string):
    countzeros = 0
    for each in str(binary_string):
      if each == "0":
         countzeros += 1
    return countzeros

print(counting_zeros(1001101000110))

