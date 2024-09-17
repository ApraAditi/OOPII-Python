def prime(num):  
    if num > 1:  
        for j in range(2, int(num/2) + 1):  
            if (num % j) == 0:  
                print(num, "is not a prime number")  
                break  
        else:  
            print(num, "is a prime number")  
    else:  
        print(num, "is not a prime number")  
num = int(input("Enter an input number:"))  
prime(num)  
