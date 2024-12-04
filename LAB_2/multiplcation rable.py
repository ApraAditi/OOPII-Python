# Function to print the multiplication table of a given number
def print_multiplication_table(number, upto=10):
    print(f"Multiplication Table for {number}")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

# Input: Taking the number for which the multiplication table is to be printed
num = int(input("Enter a number: "))
upto = int(input("Up to which number do you want to print the table? "))

# Printing the multiplication table
print_multiplication_table(num, upto)
