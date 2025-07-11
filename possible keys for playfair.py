from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Key must be either 16 or 24 bytes long
key = DES3.adjust_key_parity(get_random_bytes(24))
cipher = DES3.new(key, DES3.MODE_ECB)

# Message must be a multiple of 8 bytes
msg = b"HELLO123"  # 8 bytes
ciphertext = cipher.encrypt(msg)
print("Encrypted:", ciphertext)

# Decrypt
decipher = DES3.new(key, DES3.MODE_ECB)
plaintext = decipher.decrypt(ciphertext)
print("Decrypted:", plaintext)
