from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_AES(key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext

def decrypt_AES(key, ciphertext):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return decrypted.decode()

# Usage example
key = os.urandom(32)
message = "This is a secret message."

encrypted = encrypt_AES(key, message)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_AES(key, encrypted)
print(f"Decrypted: {decrypted}")
