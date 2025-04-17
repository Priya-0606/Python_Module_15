# 23) Write a Python program to search for a word in a string using re.search().

print("-----------------------Re Search--------------------------------\n")

import re

text = "Python is a powerful programming language."

word = "powerful"

match = re.search(rf"\b{word}\b", text)

if match:
    print(f"Word '{word}' found at position: ", match.start())
else:
    print(f"Word '{word}' not found in the text.")