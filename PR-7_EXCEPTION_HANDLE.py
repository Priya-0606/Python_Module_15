#7) Write a Python program to handle exceptions in a calculator.
def calculator(): 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2  # Might raise ZeroDivisionError
        else:
            print("Invalid operator!")
            return

        print(f"Result: {result}")

    except Exception as E:
        print(E,"Error!")

calculator()
