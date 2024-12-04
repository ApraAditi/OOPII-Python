import numpy as np

# Create a 2D NumPy array
data = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

row_view = data[1, :]
print("Create a view of the second row:",row_view)

column_copy = data[:, 2].copy()
print("Create a deep copy of the third column: ",column_copy)

print("Original array:\n",data)

row_view[0] = 100
print("\nModified view:",row_view)

column_copy[1] = 200
print("\nModified copy:",column_copy)

print("\nOriginal array after modification:\n",data)
