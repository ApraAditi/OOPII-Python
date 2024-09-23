def find_lcm(num1, num2):
    max_num = max(num1, num2)

    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            return max_num
        max_num += 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is:", lcm)