def count_substring_occurrences(string, substring):

  count = 0
  index = 0
  while index < len(string):
    index = string.find(substring, index)
    if index == -1:
      break
    count += 1
    index += 1
  return count

main_string = "the quick brown fox jumps over the lazy dog."
substring = "the"

occurrences = count_substring_occurrences(main_string, substring)
print("The substring", substring, "occurs", occurrences, "times in the string.\n", main_string)