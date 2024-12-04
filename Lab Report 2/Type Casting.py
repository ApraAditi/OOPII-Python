import numpy as np

# Sample 2D NumPy array with string values
data = np.array([
    ['John', '25', '3000.50'],
    ['Jane', '30', '4500.75'],
    ['Doe', '22', '1500.00']
])

print("Original Data:")
print(data)
print("Data Types:", data.dtype)

converted_data = np.empty(data.shape, dtype=object)

converted_data[:, 0] = data[:, 0]

converted_data[:, 1] = data[:, 1].astype(int)

converted_data[:, 2] = data[:, 2].astype(float)

print("\nConverted Data:")
print(converted_data)
print("Data Types:", converted_data.dtype)