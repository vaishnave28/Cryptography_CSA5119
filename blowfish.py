from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

data = b"HELLO BLOWFISH"
key = get_random_bytes(16)  # key: 4–56 bytes
iv = get_random_bytes(8)    # Blowfish block size = 8

# Encrypt
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(data, 8))
print("Ciphertext:", ciphertext)

# Decrypt
decipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
plaintext = unpad(decipher.decrypt(ciphertext), 8)
print("Plaintext :", plaintext)
