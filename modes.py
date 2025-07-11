from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

data = b"HELLO BLOCK CIPHER!!"  # 18 bytes
key = get_random_bytes(16)
iv = get_random_bytes(16)

# ECB
ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = ecb.encrypt(pad(data, 16))
print("ECB :", ct_ecb)

# CBC
cbc = AES.new(key, AES.MODE_CBC, iv)
ct_cbc = cbc.encrypt(pad(data, 16))
print("CBC :", ct_cbc)

# CFB
cfb = AES.new(key, AES.MODE_CFB, iv)
ct_cfb = cfb.encrypt(data)  # No padding needed
print("CFB :", ct_cfb)
