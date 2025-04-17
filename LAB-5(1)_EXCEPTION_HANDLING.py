#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

def calc():    
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    try:
        if operator == '+':
            result = n1 + n2
        elif operator == '-':
            result = n1 - n2
        elif operator == '*':
            result = n1 * n2
        elif operator == '/':
            if n2 == 0: 
                raise ZeroDivisionError 
            result = n1 / n2
        else:
            print("Invalid input!")
            return

        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

calc()