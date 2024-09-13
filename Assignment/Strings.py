sen = "Learning Python is fun and rewarding."

#Extract the substring using negative slicing.
print("The substring: ",sen[-28:-14])
print("\n")

#Modify the original string by replacing 
sen = "Learning Python is fun and rewarding."
new_sen = sen.replace("rewarding", "exciting")
print("After modifying the string: ",new_sen)
print("\n")


# #Insert the phrase
a = new_sen.find("exciting") #a = index of exciting
final_sen = new_sen[:a + len("exciting")] + ", " + "Keep practicing!" 
print("After insert the phrase: ",final_sen)
print("\n")


#Capitalize the first letter of each word
cap = final_sen.title()
print("After titteling: ",cap)