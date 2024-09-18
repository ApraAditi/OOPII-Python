def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

string_to_reverse = input("Enter a string: ")

reversed_string = reverse_string(string_to_reverse)
print("Reversed string:", reversed_string)