def sum_of_first_ten_natural_numbers():
    sum = 0
    for number in range(1, 11):
        sum += number
    return sum

sum = sum_of_first_ten_natural_numbers()
print("Sum of the first ten natural numbers:", sum)