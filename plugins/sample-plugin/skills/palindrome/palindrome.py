#!/usr/bin/env python3
"""
Palindrome Generator
Takes a word or phrase and outputs its reverse.
"""

import sys

def reverse_string(text):
    """Reverse the input string."""
    return text[::-1]

if __name__ == "__main__":
    # Get input from command line arguments
    if len(sys.argv) < 2:
        print("Error: Please provide a word or phrase to reverse.")
        print("Usage: python palindrome.py <word or phrase>")
        sys.exit(1)

    # Join all arguments to handle phrases with spaces
    input_text = " ".join(sys.argv[1:])

    # Reverse the input
    reversed_text = reverse_string(input_text)

    # Display results
    print(f"Original: {input_text}")
    print(f"Reversed: {reversed_text}")
