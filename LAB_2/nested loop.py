# Using nested for loops to print a multiplication table
print("\nMultiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
