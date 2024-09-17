def armstrong_number(number):
  original_number = number
  sum_of_digits = 0
  num_digits = len(str(number))

  while number > 0:
    digit = number % 10
    sum_of_digits += digit ** num_digits
    number //= 10

  return sum_of_digits == original_number

number = int(input("Enter a number: "))
if armstrong_number(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")