import numpy as np

# Create the two-dimensional array
array_2d = np.array([
    [x for x in range(2, 21, 2)],  # Even integers from 2 through 20
    [x for x in range(1, 22, 2)[:10]]  # First 10 odd integers to match the row length
])


# Print the array
print("Array:\n", array_2d)

# Check and print the dtype, ndim, shape, size, and itemsize
print("Data type (dtype):", array_2d.dtype)
print("Number of dimensions (ndim):", array_2d.ndim)
print("Shape of the array:", array_2d.shape)
print("Total number of elements (size):", array_2d.size)
print("Size of each element in bytes (itemsize):", array_2d.itemsize)