from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)
    return key


def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()

    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_message():
    message = input("Enter message to encrypt: ")

    key = load_key()
    cipher = Fernet(key)

    encrypted = cipher.encrypt(message.encode())

    print("\nEncrypted Message:")
    print(encrypted.decode())


def decrypt_message():
    message = input("Enter encrypted message: ")

    key = load_key()
    cipher = Fernet(key)

    try:
        decrypted = cipher.decrypt(message.encode())

        print("\nDecrypted Message:")
        print(decrypted.decode())

    except Exception:
        print("Invalid encrypted message or key.")


while True:
    print("\n--- Data Encryption and Decryption Tool ---")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        encrypt_message()

    elif choice == "2":
        decrypt_message()

    elif choice == "3":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
