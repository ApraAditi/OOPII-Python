# Using a for loop to iterate over a list
numbers = [1, 2, 3, 4, 5]

print("Using for loop:")
for num in numbers:
    print(num)

# Using a for loop to iterate over a range
print("\nUsing for loop with range:")
for i in range(1, 6):
    print(i)


# Using nested for loops to print a multiplication table
print("\nMultiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
