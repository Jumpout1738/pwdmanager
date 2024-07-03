from db_manager import create_connection, create_table, add_password, get_all_passwords
from encryption import encrypt_password, decrypt_password, load_key
from password_generator import generate_password

def print_header():
    """Print the header information with ASCII art."""
    print("************************************")
    print("*                                  *")
    print("*    Welcome to Password Manager   *")
    print("*                                  *")
    print("*    Version 1.0                   *")
    print("*    Author: AVON                  *")
    print("*    Date: June 30, 2024           *")
    print("*                                  *")
    print("************************************\n")
    
    print("      ___   _   _   ___   _   _    ")
    print("     / _ \\ | | | | / _ \\ | \\ | ")
    print("    | | | || | | || | | ||  \\| |   ")
    print("    | |_| || |_| || |_| || |\\  |   ")
    print("     \\___/  \\___/  \\___/ |_| \\_\n")



def display_menu():
    """Display the main menu options."""
    print("Password Manager")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

def add_password_flow(conn):
    """Flow to add a new password to the database."""
    site_name = input("Enter site name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    add_password(conn, site_name, username, encrypted_password)
    print("Password added successfully.")

def view_passwords_flow(conn):
    """Flow to view all stored passwords."""
    key = load_key()
    passwords = get_all_passwords(conn)
    for row in passwords:
        decrypted_password = decrypt_password(row[3], key)
        print(f"Site: {row[1]}, Username: {row[2]}, Password: {decrypted_password}")

def main():
    print_header()  # Print the header when the script starts
    conn = create_connection()
    create_table(conn)
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_password_flow(conn)
        elif choice == "2":
            view_passwords_flow(conn)
        elif choice == "3":
            print(f"Generated Password: {generate_password()}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
