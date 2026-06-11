import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits

password = random.sample(characters, length)

random.shuffle(password)

print("Generated Password:", "".join(password))