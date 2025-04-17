#6) Write a Python program to check the current position of the file cursor using tell()

f1 = "Content.txt"  

file = open(f1, "r")  
print("Cursor position at start:", file.tell())  

data = file.read(15)  
print("Data read:", data)
print("Cursor position after reading 10 characters:", file.tell())  

file.close()  # Close the file
