from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES requires 8-byte key
key = b'8bytekey'  # Must be exactly 8 bytes
block_size = 8     # DES block size is 8 bytes

# Get user input
plaintext = input("Enter the message to encrypt: ")

# Encrypt using ECB mode
cipher = DES.new(key, DES.MODE_ECB)
padded_text = pad(plaintext.encode(), block_size)
encrypted = cipher.encrypt(padded_text)
print("Encrypted (hex):", encrypted.hex())

# Decrypt
cipher_decrypt = DES.new(key, DES.MODE_ECB)
decrypted = unpad(cipher_decrypt.decrypt(encrypted), block_size)
print("Decrypted text:", decrypted.decode())
