import numpy as np

# Creating NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Printing the arrays
print("1D Array:")
print(array1)
print("\n2D Array:")
print(array2)

# Array arithmetic operations
print("\nArray addition:")
print(array1 + 10)

print("\nElement-wise array addition:")
print(array1 + array1)

print("\nArray multiplication:")
print(array1 * 2)

# Array slicing
print("\nSlicing 1D array (first three elements):")
print(array1[:3])

print("\nSlicing 2D array (first two rows and first two columns):")
print(array2[:2, :2])

# Array reshaping
reshaped_array = array2.reshape(1, 9)
print("\nReshaped 2D array to 1D array:")
print(reshaped_array)

# Array statistics
print("\nSum of elements in array1:")
print(np.sum(array1))

print("\nMean of elements in array2:")
print(np.mean(array2))

print("\nStandard deviation of elements in array2:")
print(np.std(array2))

# Linear algebra - matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)
print("\nMatrix multiplication result:")
print(matrix_product)
