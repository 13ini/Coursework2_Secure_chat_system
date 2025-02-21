import unittest
from encryption import encrypt_message, decrypt_message

class TestEncryption(unittest.TestCase):
    def test_encryption_decryption(self):
        message = "Hello, Secure Chat!"
        encrypted = encrypt_message(message)
        decrypted = decrypt_message(encrypted)
        self.assertEqual(message, decrypted)

if __name__ == "__main__":
    unittest.main()
