# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Printing the original list
print("Original List:", numbers)

# Adding elements to the list
numbers.append(6)
numbers.extend([7, 8, 9])

# Printing the list after adding elements
print("List after adding elements:", numbers)

# Removing elements from the list
numbers.remove(4)  # Removes the first occurrence of 4
popped_element = numbers.pop()  # Removes and returns the last element

# Printing the list after removing elements
print("List after removing elements:", numbers)
print("Popped element:", popped_element)

# Accessing elements in the list
first_element = numbers[0]
last_element = numbers[-1]

# Printing the accessed elements
print("First element:", first_element)
print("Last element:", last_element)

# Slicing the list
sublist = numbers[1:4]

# Printing the sliced list
print("Sliced List:", sublist)

# Iterating over the list
print("Iterating over the list:")
for num in numbers:
    print(num, end=" ")

print("\n")  # New line for separation

# Using list comprehensions to create a new list of squares
squares = [x**2 for x in numbers]
print("Squares:", squares)
