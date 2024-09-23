def multiply_matrices(matrix1, matrix2):
  if len(matrix1[0]) != len(matrix2):
    return "Number of columns in the first matrix must be equal to the number of rows in the second matrix"

  result = []
  for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
      element = 0
      for k in range(len(matrix2)):
        element += matrix1[i][k] * matrix2[k][j]
      row.append(element)
    result.append(row)

  return result

# Example usage
matrix1 = [[1, 2], [4, 5]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

product_matrix = multiply_matrices(matrix1, matrix2)

print("Product of matrices:")
for row in product_matrix:
  print(row)