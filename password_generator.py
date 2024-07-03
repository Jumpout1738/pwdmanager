import random
import string

def generate_password(length=12):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Test password generation
if __name__ == "__main__":
    print(generate_password())
