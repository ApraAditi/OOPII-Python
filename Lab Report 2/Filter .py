import numpy as np

# Sample product prices
prices = np.array([25, 35, 18, 42, 55, 28, 30])

# Price range for the sale
min_price = 20
max_price = 50

# Filter products within the price range
filtered_prices = prices[(prices >= min_price) & (prices <= max_price)]

print("Filtered prices:", filtered_prices)