customers = ["Alice", "Bob", "Charlic", "David", "Eve"]
#a. Access the third customer
print("\nThird customer is: ",customers[2])

#b. Change the name
customers[1] = "Ben"
print("Changed customer name is: ",customers)

#c. Add a new customer name
customers.append("Frank")
print("Adding a customer name: ",customers)

#d. Remove the customer
customers.remove("David")
print("Removed the customer name: ",customers)

#e. Sort the customer names alphabetically
customers.sort()
print("Sort the name alphabetically: ",customers)
print("\n")