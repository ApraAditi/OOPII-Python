import numpy as np

# Sales data for two branches
branch1_sales = np.array([100, 200, 300])
branch2_sales = np.array([400, 500, 600])

# Horizontal join (concatenate along the second axis)
horizontal_join = np.hstack((branch1_sales.reshape(-1, 1), branch2_sales.reshape(-1, 1)))

# Vertical join (concatenate along the first axis)
vertical_join = np.vstack((branch1_sales, branch2_sales))

print("Horizontal Join:")
print(horizontal_join)

print("\nVertical Join:")
print(vertical_join)