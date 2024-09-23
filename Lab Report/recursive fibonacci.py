def fibonacci_recursive(n):
    
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter the index of the Fibonacci number: "))

# Calculate the Fibonacci number
fibonacci_number = fibonacci_recursive(n)

print("The", n, "th Fibonacci number is:", fibonacci_number)