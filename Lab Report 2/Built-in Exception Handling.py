def divide_elements(values, divisor):
    try:
        for value in values:
            result = value / divisor
            print(f"{value} / {divisor} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Divisor must be a number.")

# Example usage
values = [10, 20, 30, 40]

try:
    divisor = int(input("Enter a divisor: "))
    divide_elements(values, divisor)
except ValueError:
    print("Error: Invalid input. Please enter a number.")