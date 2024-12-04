# Function to perform division and handle potential exceptions
def safe_division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers.")
        return None
    else:
        return result
    finally:
        print("Execution of safe_division is complete.")

# Taking input from the user
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    # Performing the division
    result = safe_division(num1, num2)
    if result is not None:
        print(f"The result of division is: {result}")
