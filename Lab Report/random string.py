import random
import string

def generate_random_string(length):

  characters = string.ascii_letters + string.digits + string.punctuation
  random_string = ''.join(random.choice(characters) for x in range(length))
  return random_string

length = 10
random_string = generate_random_string(length)
print("Random string:", random_string)