import random
import string

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Get user input for the password length
while True:
    try:
        password_length = int(input("Enter the length of the password you would like to generate: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Generate the password
password = generate_password(password_length)

# Print the password
print("Your password is:", password)



