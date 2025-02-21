

from cryptography.fernet import Fernet
import os


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    key_path = os.path.join(os.path.dirname(__file__), "secret.key")
    with open(key_path, "rb") as key_file:
        return key_file.read()


KEY = load_key()
cipher = Fernet(KEY)


def encrypt_message(message):
    return cipher.encrypt(message.encode())


def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()


if __name__ == "__main__":
    print(f"Encryption Key: {KEY.decode()}")

