def add_matrices(matrix1, matrix2):
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    return "Matrices must have the same dimensions"

  result = []
  for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
      row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

  return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

sum_matrix = add_matrices(matrix1, matrix2)
print("Sum of matrices:")
for row in sum_matrix:
  print(row)