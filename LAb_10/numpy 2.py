import numpy as np

# Creating an array of ages
ages = np.array([23, 45, 18, 30, 50])

# 1. Converting to float type
float_ages = ages.astype(float)
print("Ages as float type:", float_ages)

# 2. Subtracting 2 years from a copy of the original ages
modified_ages = ages.copy()
modified_ages -= 2
print("Modified ages (after subtracting 2):", modified_ages)
print("Original ages remain intact:", ages)

# 3. Identifying ages 21 or older
adult_indices = np.where(ages >= 21)[0]
print("Indices with ages 21 or older:", adult_indices)

# 4. Array properties and summary statistics
print("Array shape:", ages.shape)
print("Number of dimensions:", ages.ndim)
print("Total number of elements:", ages.size)
print("Size of each item in bytes:", ages.itemsize)
print("Array data type:", ages.dtype)

# Sorting and statistical operations
print("Sorted ages:", np.sort(ages))
print("Oldest age:", ages.max())
print("Youngest age:", ages.min())
print("Total sum of ages:", ages.sum())
print("Average age:", ages.mean())

# Slicing operations
print("Ages from index 0, 2, 4:", ages[::2])
print("Ages from 2nd to 4th element:", ages[-3:-1])
print("Ages from index 1 to 3:", ages[1:4])
