from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)     # AES-128
iv = get_random_bytes(16)      # Initialization Vector
data = b"HELLO AES ENCRYPTION"

cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(data, 16))
print("Ciphertext:", ct)

dec = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(dec.decrypt(ct), 16)
print("Plaintext :", pt)
