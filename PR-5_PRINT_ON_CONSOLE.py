#5) Write a Python program to read a file and print the data on the console.

f1 = "Content.txt"  #this is the file from Lab-1_FORMAT.py Code 

file = open(f1, "r")  
data = file.read()  
print(data)

file.close() 
