from cryptography.fernet import Fernet

def generate_key():
    """Generate and save a key for encryption."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from the file."""
    return open("secret.key", "rb").read()

def encrypt_password(password, key):
    """Encrypt the password using the provided key."""
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    """Decrypt the password using the provided key."""
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Generate the key initially (only once)
if __name__ == "__main__":
    generate_key()
