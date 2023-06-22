#!/usr/bin/env python3
# Day 27

'''
When you run this script, it will randomly select one of the inspirational quotes from the quotes list and print it to the console. You can add more quotes to the list if you'd like to expand the collection.
'''

import random

quotes = [
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The best way to predict the future is to create it. - Peter Drucker",
    "The stronger the team, the stronger the team - John Still"
]

def generate_inspiration():
    return random.choice(quotes)

if __name__ == "__main__":
    quote = generate_inspiration()
    print(quote)

