import numpy as np

# Create a 1D NumPy array representing sensor data
sensor_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

num_rows = 3
num_cols = 4

# Check if the number of elements is divisible by the product of rows and columns
if len(sensor_data) % (num_rows * num_cols) == 0:
    # Reshape the array
    reshaped_data = sensor_data.reshape(num_rows, num_cols)
    print("Reshaped array:")
    print(reshaped_data)
else:
    print("Error: The number of elements in the array is not divisible by the product of rows and columns.")
    print("Possible solutions:")
    print("1. Pad the array with zeros to make it divisible.")
    print("2. Truncate the array to the nearest divisible length.")

    # Example of padding with zeros:
    padded_data = np.pad(sensor_data, (0, num_rows * num_cols - len(sensor_data)), 'constant', constant_values=0)
    reshaped_padded_data = padded_data.reshape(num_rows, num_cols)
    print("\nReshaped array after padding:")
    print(reshaped_padded_data)