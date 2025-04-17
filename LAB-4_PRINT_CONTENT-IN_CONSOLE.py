# Write a Python program to read the contents of a file and print them on the console.

f1 = open("Content.txt","w")

f1.write("Hello, Welcome to World of Coding!!\n")
f1.write("And this is the Python!\n")

f1.close()

f2 = open("Content.txt","r")
print("File Content :")
print(f2.read())
f2.close()
print("Successfully, Done.\n")