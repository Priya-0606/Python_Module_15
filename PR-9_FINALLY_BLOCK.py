#9) Write a Python program to handle file exceptions and use the finally block for closing the file.

file = "Content.txt"  

try:
    file = open(file, 'r')  
    content = file.read()
    print("File content:")
    print(content)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
        file.close()
    