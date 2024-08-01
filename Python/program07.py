# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:57:46 2024

@author: H BHARATH BHAT
"""
from collections import Counter
import string

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File Contents:\n", contents)
            return contents
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def build_histogram(text):
    # Remove punctuation and convert text to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()

    # Split text into words
    words = cleaned_text.split()

    # Build the histogram
    histogram = Counter(words)
    return histogram

def print_most_common_words(histogram, num_words=10):
    most_common = histogram.most_common(num_words)
    print(f"\n{num_words} Most Common Words:\n")
    for word, count in most_common:
        print(f"{word}: {count}")

def main():
    filename = 'cyber.txt'  # Replace with your filename
    text = read_file(filename)

    if text:
        histogram = build_histogram(text)
        print_most_common_words(histogram)

if __name__ == "__main__":
    main()

