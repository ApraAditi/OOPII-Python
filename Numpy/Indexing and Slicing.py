import numpy as np

# Define the array
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

# a) Select the second row
second_row = array[1]
print("Second row:", second_row)

# b) Select the first and third rows
first_third_rows = array[[0, 2]]
print("First and third rows:\n", first_third_rows)

# c) Select the middle three columns
middle_three_columns = array[:, 1:4]
print("Middle three columns:\n", middle_three_columns)

# d) Show 12 and 13 from the array
values_12_13 = array[2, 1:3]
print("Values 12 and 13:", values_12_13)

# e) Show reverse order of third row's values
reversed_third_row = array[2][::-1]
print("Reversed third row:", reversed_third_row)

# f) Select the fourth row and find max, min, sum, mean, std, and var
fourth_row = array[3]
max_val = np.max(fourth_row)
min_val = np.min(fourth_row)
sum_val = np.sum(fourth_row)
mean_val = np.mean(fourth_row)
std_val = np.std(fourth_row)
var_val = np.var(fourth_row)

print("Fourth row:", fourth_row)
print("Max:", max_val)
print("Min:", min_val)
print("Sum:", sum_val)
print("Mean:", mean_val)
print("Std Dev:", std_val)
print("Variance:", var_val)

# g) Find log10, log2, and natural log (log) of the first row
log10_first_row = np.log10(array[0])
log2_first_row = np.log2(array[0])
log_first_row = np.log(array[0])

print("Log10 of first row:", log10_first_row)
print("Log2 of first row:", log2_first_row)
print("Natural log of first row:", log_first_row)
