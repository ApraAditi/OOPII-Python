import numpy as np

# Sample 3D array
data = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]],
                 [[9, 10], [11, 12]]])

# Flatten the array
flattened_data = data.flatten()

print("Original 3D array:")
print(data)

print("\nFlattened 1D array:")
print(flattened_data)