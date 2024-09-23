#using built-in function
decimal_num = int(input("Enter a decimal number: "))

print("The decimal value of", decimal_num, "is:")
print(bin(decimal_num), "in binary.")
print(oct(decimal_num), "in octal.")
print(hex(decimal_num), "in hexadecimal.")

# using user define function
def convert_base(num, base):
  result = ""
  while num > 0:
    remainder = num % base
    result = str(remainder) + result
    num //= base
  return result

def convert_to_binary(num):
  return convert_base(num, 2)

def convert_to_octal(num):
  return convert_base(num, 8)

def convert_to_hexadecimal(num):
  return convert_base(num, 16)

decimal_num = int(input("Enter a decimal number: "))

binary_num = convert_to_binary(decimal_num)
octal_num = convert_to_octal(decimal_num)
hexadecimal_num = convert_to_hexadecimal(decimal_num)

print("Binary:", binary_num)
print("Octal:", octal_num)
print("Hexadecimal:", hexadecimal_num)