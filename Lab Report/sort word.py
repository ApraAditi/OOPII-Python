
my_str = "Your random facts are always fascinating, Apra."

words = [word.lower() for word in my_str.split()]
words.sort()

print("The sorted words are:")
for word in words:
   print(word)
