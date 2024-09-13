for number in range (5, 10):
  print (number, end = ' ')
  
print("\n")  
for number in range (0, 10, 2):
  print (number, end = ' ')  
  
print("\n")   
for number in range (10, 0, -2):
  print (number, end = ' ')  
 
#Problem  
print("\n")   
total = 0
for number in range (2, 101, 2):
  total += number
total  