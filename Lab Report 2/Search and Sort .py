import numpy as np

# Sample scores
scores = np.array([85, 72, 90, 68, 80, 75])

# Search for specific scores
index_75 = np.where(scores == 75)
index_90 = np.where(scores == 90)

print("Index of 75:", index_75)
print("Index of 90:", index_90)

# Sort in ascending order
scores_ascending = np.sort(scores)
print("Ascending order:", scores_ascending)

# Sort in descending order
scores_descending = -np.sort(-scores)
print("Descending order:", scores_descending)