import requests
import re
url="https://en.wikipedia.org/wiki/Bangalore"
html=requests.get(url)
draft = re.findall(r'<h3 .*>(.*?)</h3>', html.text)
print(draft)