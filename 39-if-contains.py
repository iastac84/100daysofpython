#!/usr/bin/env python3
# Day 39
# From https://www.learndatasci.com/solutions/python-string-contains/

strings = ['This string has apples', 'This string has oranges', 'This string has Apples']

for s in strings:
    if 'apples' in s.lower():
        print('Apples in string')
    else:
        print('Apples not in string')

