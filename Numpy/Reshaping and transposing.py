import numpy as np

# Define the array
array = np.array([
    [1, 3, 2, 4],
    [8, 6, 5, 7],
    [11, 10, 12, 9]
])

# a) Find the transpose of the given array
transpose_array = array.T
print("Transpose of the array:\n", transpose_array)

# b) Reshape the array (reshaping depends on the desired dimensions; let's reshape to 2x6 as an example)
reshaped_array = array.reshape(2, 6)
print("Reshaped array (2x6):\n", reshaped_array)

# c) Sort the array
sorted_array = np.sort(array, axis=None)  # Sort all elements into a single sorted array
print("Sorted array (flattened):", sorted_array)

# If sorting each row separately is required:
sorted_array_rows = np.sort(array, axis=1)  # Sort each row individually
print("Row-wise sorted array:\n", sorted_array_rows)
