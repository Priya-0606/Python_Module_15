#8) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

def read_file(f1):
    try:
        file = open(f1, "r")  
        data = file.read()
        print("File Contents:\n", data)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")

def divide_numbers():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2  # ZeroDivisionError would be raised if denominator is 0.
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Example Usage
f1 = "example.txt"  
read_file(f1)
divide_numbers()
