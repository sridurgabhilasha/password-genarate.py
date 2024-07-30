import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Define the characters to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Ensure the password contains at least one of each type of character
    all_characters = lowercase + uppercase + digits + punctuation
    
    # Randomly choose one character from each set to ensure diversity
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    # Fill the rest of the password length with random choices
    password += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

# Example usage
print(generate_password(12))
