import random
import string

def generate_password(length):
    # Define possible characters (uppercase, lowercase, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Prompt user for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length should be at least 1.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")
s