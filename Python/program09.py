import re
import requests

# Download the text file from the URL
url = "https://www.py4e.com/code3/mbox.txt"
response = requests.get(url)
text = response.text

# Regular expression patterns for "From:" and "To:" email addresses
from_pattern = r'^From:\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
to_pattern = r'^To:\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

# Extract "From:" email addresses
from_emails = re.findall(from_pattern, text, re.MULTILINE)

# Extract "To:" email addresses
to_emails = re.findall(to_pattern, text, re.MULTILINE)

# Print the extracted email addresses
print("From: Email Addresses:")
for email in from_emails:
    print(email)

print("\nTo: Email Addresses:")
for email in to_emails:
    print(email)
