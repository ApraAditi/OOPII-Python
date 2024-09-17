def check_number(num):
  if num > 0:
    return "Positive"
  elif num < 0:
    return "Negative"
  else:
    return "Zero"

# Get a number from the user
number = float(input("Enter a number: "))

# Check the number and print the result
result = check_number(number)
print(f"{number} is {result}.")