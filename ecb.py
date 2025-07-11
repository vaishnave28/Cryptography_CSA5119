from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES key (16 bytes = 128-bit)
key = get_random_bytes(16)

# Create ECB cipher
cipher = AES.new(key, AES.MODE_ECB)

# Plaintext (must be padded to block size)
plaintext = b'HELLO ECB MODE'
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Ciphertext:", ciphertext)

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted :", decrypted)
