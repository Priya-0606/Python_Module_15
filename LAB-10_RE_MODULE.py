#Write a Python program to search for a word in a string using re.search(). 
#Write a Python program to match a word in a string using re.match().

print("-----------------------Re Search--------------------------------\n")

import re

text = "Python is a powerful programming language."

word = "powerful"

match = re.search(rf"\b{word}\b", text)

if match:
    print(f"Word '{word}' found at position: ", match.start())
else:
    print(f"Word '{word}' not found in the text.")


print("\n-----------------------Re Match--------------------------------\n")

word = "Python"

match = re.match(rf"\b{word}\b", text)

if match:
    print(f"Word '{word}' matched at the beginning of the string.\n")
else:
    print(f"Word '{word}' not found at the beginning.")
