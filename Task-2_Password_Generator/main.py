import random
import string

print("Welcome to the Random Password Generator")

# Ask the user for password length
length = int(input("Enter the desired password length: "))

# Define characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Create empty password
password = ""

# Generate password
for i in range(length):
    password += random.choice(characters)

# Display the password
print("Generated Password:", password)
