#!/usr/bin/env python3
# Day 39
# From https://www.learndatasci.com/solutions/python-string-contains/

import re

strings = ['This string has apples', 'This string has oranges', 'This string has neither']

for s in strings:
    if re.search('apples', s):
        print('Apples in string')
    else:
        print('Apples not in string')

