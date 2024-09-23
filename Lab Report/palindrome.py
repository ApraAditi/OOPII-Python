def isPalindrome(string): 
    if string == string[::-1]:  # Check if the string is equal to its reverse
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 

string = input("Enter string: ") 

print(isPalindrome(string))
