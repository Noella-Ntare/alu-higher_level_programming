#!/usr/bin/python3
"""
This module provides a function for formatting a text by adding two new lines
after each of these characters: `.`, `?`, and `:`.
"""

def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: `.`, `?`, `:`.
    
    Args:
        text (str): The input text to be formatted.
    
    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialize variables
    formatted_text = ""
    skip_space = False  # To skip spaces after the characters
    
    for char in text:
        if char in ".:?":
            formatted_text += char + "\n\n"
            skip_space = True  # Skip any spaces after these characters
        elif skip_space and char == " ":
            continue
        else:
            formatted_text += char
            skip_space = False  # Reset skipping if no space encountered
    
    # Print the final formatted text
    print(formatted_text.strip(), end="")

