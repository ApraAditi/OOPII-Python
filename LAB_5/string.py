# Initializing a string
original_string = "Hello, World!"

# Printing the original string
print("Original String:", original_string)

# Converting the string to uppercase
uppercase_string = original_string.upper()
print("Uppercase String:", uppercase_string)

# Converting the string to lowercase
lowercase_string = original_string.lower()
print("Lowercase String:", lowercase_string)

# Finding the length of the string
string_length = len(original_string)
print("Length of the String:", string_length)

# Replacing a substring
replaced_string = original_string.replace("World", "Python")
print("Replaced String:", replaced_string)

# Finding the position of a substring
position = original_string.find("World")
print("Position of 'World':", position)

# Slicing the string
sliced_string = original_string[7:12]
print("Sliced String:", sliced_string)

# Splitting the string into a list of words
split_string = original_string.split(", ")
print("Split String:", split_string)

# Joining a list of words into a string
joined_string = " ".join(split_string)
print("Joined String:", joined_string)

# Checking if the string starts with a specific substring
starts_with = original_string.startswith("Hello")
print("Starts with 'Hello':", starts_with)

# Checking if the string ends with a specific substring
ends_with = original_string.endswith("!")
print("Ends with '!':", ends_with)
