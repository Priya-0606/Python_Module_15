#10) Write a Python program to print custom exceptions.
try:
    value = int(input("Enter a Number: "))

    if value < 0:
        raise Exception("Negative value is not allowed!")
    elif value == 0:
        raise Exception("Zero is not a valid input!")
    else:
        print(f"Valid input: {value}")

except Exception as e:
    print(f"Custom Exception: {e}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
      