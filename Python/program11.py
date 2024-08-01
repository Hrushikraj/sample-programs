# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:23:49 2024

@author: HR Bharath Bhat
"""

import re

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File Contents:\n", contents)
            return contents
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def count_sentences(text):
    # Define a regular expression pattern to match sentences
    sentence_pattern = r'[.!?]+(?:\s|$)'
    
    # Find all matches for sentence endings
    sentences = re.split(sentence_pattern, text)
    
    # Filter out empty strings resulting from split
    sentences = [s for s in sentences if s.strip()]
    
    # Count the number of sentences
    num_sentences = len(sentences)
    return num_sentences

def main():
    filename = 'cyber.txt'  # Replace with your filename
    text = read_file(filename)

    if text:
        num_sentences = count_sentences(text)
        print(f"\nNumber of sentences in the file: {num_sentences}")

if __name__ == "__main__":
    main()
