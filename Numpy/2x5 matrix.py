
import numpy as np

# First row: reverse order of even integers from 2 through 10
first_row = np.arange(10, 1, -2)

# Second row: odd integers from 1 through 9
second_row = np.arange(1, 10, 2)

# Combine into a 2x5 array
array_2x5 = np.array([first_row, second_row])

print(array_2x5)