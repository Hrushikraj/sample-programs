# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:21:59 2024

@author: HRUSHIK RAJ S
"""

import re

# Sample sentence
sentence = "From rjlowe@iupui.edu Fri Jan 4 14:50:18 2008"

# Regular expression patterns
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
time_pattern = r'\b\d{2}:\d{2}:\d{2}\b'

# Extract the email address
email_match = re.search(email_pattern, sentence)
email_address = email_match.group(0) if email_match else None

# Extract the time of day
time_match = re.search(time_pattern, sentence)
time_of_day = time_match.group(0) if time_match else None

# Print the results
print(f"Email Address: {email_address}")
print(f"Time of Day: {time_of_day}")
