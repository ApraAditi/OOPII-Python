def remove_duplicates(my_list):
    return list(set(my_list))

string = input("Enter a list of elements separated by spaces: ")
my_list = string.split()

unique_list = remove_duplicates(my_list)
print("Unique elements:", unique_list)