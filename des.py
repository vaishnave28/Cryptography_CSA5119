from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES requires an 8-byte (64-bit) key
key = b'abcdefgh'  # 8 characters

# Create DES cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Input plaintext
plaintext = input("Enter plaintext: ")

# Convert to bytes and pad to 8-byte block
padded_text = pad(plaintext.encode(), 8)

# Encrypt
encrypted = cipher.encrypt(padded_text)
print("Encrypted:", encrypted.hex())

# Decrypt
decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted:", decrypted.decode())
