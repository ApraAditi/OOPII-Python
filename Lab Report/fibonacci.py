def fibonacci_sequence(n):
  if n <= 0:
    print("Please enter a positive integer.")
  elif n == 1:
    print(0)
  else:
    a, b = 0, 1
    for i in range(2, n + 1):
      c = a + b
      print(c)
      a, b = b, c
n = int(input("Enter the number of terms: "))
fibonacci_sequence(n)