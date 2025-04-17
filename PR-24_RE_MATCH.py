#24) Write a Python program to match a word in a string using re.match()

import re

text = "Python is fun and powerful."

word = "Python"

match = re.match(rf"\b{word}\b", text)

if match:
    print(f"Word '{word}' matched at the beginning of the string.")
else:
    print(f"Word '{word}' not found at the beginning.")
