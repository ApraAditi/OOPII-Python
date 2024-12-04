# Function to check if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to count how many numbers in a list are even and odd
def count_even_and_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:  
        if num % 2 == 0:  
            even_count += 1
        else: 
            odd_count += 1
    
    print(f"Total even numbers: {even_count}")
    print(f"Total odd numbers: {odd_count}")

# Function to calculate the sum of all even numbers in a list
def calculate_sum_of_even(numbers):
    even_sum = 0
    for num in numbers:  
        if num % 2 == 0:  
            even_sum += num
    return even_sum

# Function to calculate the sum of all odd numbers in a list
def calculate_sum_of_odd(numbers):
    odd_sum = 0
    for num in numbers:  
        if num % 2 != 0:  
            odd_sum += num
    return odd_sum

# Input: Checking a single number
number = int(input("Enter a number: "))
result = check_even_or_odd(number)
print(f"The number you entered is {result}.")

# List of numbers to work with
numbers_list = [10, 21, 4, 45, 66, 93, 11]

# Counting and printing the number of even and odd numbers
count_even_and_odd(numbers_list)

# Calculating and printing the sum of even and odd numbers
even_sum = calculate_sum_of_even(numbers_list)
odd_sum = calculate_sum_of_odd(numbers_list)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
