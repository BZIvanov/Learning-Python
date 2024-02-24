import random
import string

"""
Write a program that generates random passwords

Requirements:
- password length (10, 15)
- number of int numbers = random number
- number of lowercase letters = min 1
- number of lowercase letters = min 1
- number of special characters/symbols = min 1
"""

def generate_password():
    password_length = random.randint(10, 15)
    num_digits = random.randint(1, password_length - 3)  # Ensure at least 1 digit, 1 lowercase letter, and 1 uppercase letter
    num_lower = random.randint(1, password_length - num_digits - 2)  # Ensure at least 1 lowercase letter and 1 uppercase letter
    num_upper = password_length - num_digits - num_lower - 1  # Remainder for uppercase letters, leaving space for special character(s)

    digits = ''.join(random.choices(string.digits, k=num_digits))
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=num_lower))
    uppercase = ''.join(random.choices(string.ascii_uppercase, k=num_upper))
    symbols = ''.join(random.choices(string.punctuation, k=random.randint(1, password_length - num_digits - num_lower - num_upper)))  # Ensure at least 1 special character
  
    password_characters = digits + lowercase + uppercase + symbols
    password_list = list(password_characters)
    random.shuffle(password_list)

    return ''.join(password_list)

password = generate_password()
print(password)

