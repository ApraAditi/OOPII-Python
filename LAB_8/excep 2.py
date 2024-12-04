# Function to check voting eligibility
def check_voting_eligibility(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote. You need to be at least 18 years old.")

# Taking age input from the user
try:
    age = int(input("Enter your age: "))
    check_voting_eligibility(age)
except ValueError:
    print("Invalid input. Please enter a valid age.")
