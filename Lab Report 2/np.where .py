import numpy as np

# Sample temperature data
temperatures = np.array([25, 18, 32, 12, 28, 22])

# Threshold and minimum temperature
threshold = 25
min_temp = 15

# Find indices where temperature exceeds the threshold
high_temp_indices = np.where(temperatures > threshold)

# Replace temperatures below the minimum threshold
temperatures = np.where(temperatures < min_temp, min_temp, temperatures)

print("Original temperatures:", temperatures)
print("Indices of temperatures above threshold:", high_temp_indices)
print("Temperatures after replacement:", temperatures)