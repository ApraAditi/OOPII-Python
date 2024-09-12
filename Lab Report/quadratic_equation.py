#Solve quadratic equation

import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:  # two real numbers
        print("Real and Different roots")
        print((-b + math.sqrt(discriminant)) / (2*a))
        print((-b - math.sqrt(discriminant)) / (2*a))
    elif discriminant == 0:  # exactly one real root
        print("Exactly one real root")
        print(-b / (2*a))
    else:  # complex roots
        print("Complex Roots")
        print((-b / (2*a), " +i", math.sqrt(-discriminant) / (2*a)))
        print((-b / (2*a), " -i", math.sqrt(-discriminant) / (2*a)))

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a == 0:
    print("The equation is no longer quadratic.")
else:
    quadratic_equation(a, b, c)