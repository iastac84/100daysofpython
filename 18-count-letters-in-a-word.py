#!/usr/bin/env python3
# Day 18

# Takes a word as an argument and counts the number of letters
"""
We define a function count_letters that takes a word as an argument and returns the number of letters in the word using the built-in len function.

In the if __name__ == '__main__' block, we get the word from the command line arguments using sys.argv[1], which gets the second command line argument (the first one is the name of the script itself). We then call count_letters to count the number of letters in the word.

Finally, we print the result using an f-string that includes the original word and the number of letters.
"""

import sys

def count_letters(word):
    """Count the number of letters in a word."""
    return len(word)

if __name__ == '__main__':
    # Get the word from the command line arguments
    word = sys.argv[1]

    # Count the letters in the word
    num_letters = count_letters(word)

    # Print the result
    print(f'The word "{word}" has {num_letters} letters.')
