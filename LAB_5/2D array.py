# Initializing a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Function to print the matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="  ")
        print()

# Printing the original matrix
print("Original Matrix:")
print_matrix(matrix)
print()  # Empty line for separation

# Modifying an element in the matrix
matrix[1][1] = 10  # Changing the element at second row, second column to 10

# Printing the modified matrix
print("Modified Matrix:")
print_matrix(matrix)
print()  # Empty line for separation

# Adding a new row to the matrix
new_row = [10, 11, 12]
matrix.append(new_row)

# Printing the matrix after adding a new row
print("Matrix after adding a new row:")
print_matrix(matrix)
print()  # Empty line for separation

# Adding a new column to the matrix
for i in range(len(matrix)):
    matrix[i].append((i + 1) * 10)

# Printing the matrix after adding a new column
print("Matrix after adding a new column:")
print_matrix(matrix)
