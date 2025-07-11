from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES settings
key = get_random_bytes(16)  # 16 bytes = 128-bit key
iv = get_random_bytes(16)   # 16 bytes IV for CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt
plaintext = b'HELLO CBC MODE'  # must be padded to block size
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Ciphertext:", ciphertext)

# Decrypt
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted :", decrypted)
