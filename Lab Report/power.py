def calculate_power(base, exponent):
    return base ** exponent

base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))

result = calculate_power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")
