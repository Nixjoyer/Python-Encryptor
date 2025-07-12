#!/usr/bin/env python3

import hashlib
from cryptography.fernet import Fernet

def md5_hash(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

def main():
    message = input("Enter a message to encrypt: ")

    hash_value = md5_hash(message)
    print(f"MD5 Hash: {hash_value}")

    key = generate_key()
    print(f"Generated Key: {key.decode()}")

    encrypted = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted.decode()}")

    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
