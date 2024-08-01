# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:05:51 2024

@author: Hrushik Raj S
"""

import os

def find_files_with_suffix(directory, suffix):
    matched_files = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                # Join the root directory with the file name to get the full path
                full_path = os.path.join(root, file)
                matched_files.append(full_path)

    return matched_files

def main():
    directory = r"C:/Users/HRUSHIK RAJ/Desktop/python-ppt"  # Replace with your target directory #paste the file location without file and in forward slashes
    suffix = '.txt'   # Replace with your target file suffix (e.g., '.txt', '.py')

    matching_files = find_files_with_suffix(directory, suffix)

    print(f"Files with suffix '{suffix}':")
    for file in matching_files:
        print(file)

if __name__ == "__main__":
    main()
