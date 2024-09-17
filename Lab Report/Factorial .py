import math

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial of negative numbers is not defined.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = math.factorial(number)
    print(f"The factorial of {number} is {factorial}.")