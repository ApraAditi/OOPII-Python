def swap_case(text):
  result = ""
  for char in text:
    if char.islower():
      result += char.upper()
    elif char.isupper():
      result += char.lower()
    else:
      result += char
  return result

text = "ThE sUn wAs ShInInG BrIgHtLy"
swapped_text = swap_case(text)
print("Swapped text:", swapped_text)