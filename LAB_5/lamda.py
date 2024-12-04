# Lambda function to calculate the square of a number
square_function = lambda x: x ** 2

# Taking input from the user
num = int(input("Enter a number: "))

# Calculating the square of the number using the lambda function
result = square_function(num)

# Printing the result
print(f"The square of {num} is {result}")
