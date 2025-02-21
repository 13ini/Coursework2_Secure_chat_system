from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print(f"Key generated and saved as 'secret.key': {key.decode()}")
