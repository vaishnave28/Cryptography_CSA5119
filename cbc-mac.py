from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def cbc_mac(message, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=bytes(16))  # IV = 0
    padded = pad(message, AES.block_size)
    mac = cipher.encrypt(padded)[-16:]  # Take the last block
    return mac

# Example usage
key = get_random_bytes(16)
message = b"THIS IS A TEST"
tag = cbc_mac(message, key)

print("CBC-MAC Tag:", tag.hex())
