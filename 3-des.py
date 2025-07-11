from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a valid 24-byte (3-key) Triple DES key
key = DES3.adjust_key_parity(get_random_bytes(24))
data = b"HELLO 3DES"  # Block size = 8 bytes
cipher = DES3.new(key, DES3.MODE_ECB)

# Encrypt
ciphertext = cipher.encrypt(pad(data, 8))
print("Encrypted:", ciphertext)

# Decrypt
plain = unpad(cipher.decrypt(ciphertext), 8)
print("Decrypted:", plain)
