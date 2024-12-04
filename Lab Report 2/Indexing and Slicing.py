import numpy as np

# Sample sales data (replace with your actual data)
sales_data = np.array([[100, 120, 150, 180],
                       [200, 250, 280, 300],
                       [150, 170, 190, 210],
                       [80, 100, 120, 140]])

# Sales data for the first three products
first_three_products = sales_data[:3, :]
print("First three products:\n", first_three_products)

# Sales data for all products in the last two months
last_two_months = sales_data[:, -2:]
print("Sales data for the last two months:\n", last_two_months)

# Sales data for the 2nd product in the 4th month
specific_sale = sales_data[1, 3]
print("Sales for the 2nd product in the 4th month:", specific_sale)