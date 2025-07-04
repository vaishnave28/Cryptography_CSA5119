from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to perform DES encryption
def des_encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

# Function to perform DES decryption
def des_decrypt(cipher_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = des.decrypt(cipher_text)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()

# --- MAIN PROGRAM ---
# DES key must be 8 bytes long
key = b'8bytekey'  # 8 bytes key
plain_text = input("Enter plaintext to encrypt: ")

# Encrypting
encrypted = des_encrypt(plain_text, key)
print("Encrypted (in hex):", encrypted.hex())

# Decrypting
decrypted = des_decrypt(encrypted, key)
print("Decrypted text:", decrypted)
