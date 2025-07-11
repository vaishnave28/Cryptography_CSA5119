import hashlib

msg = b"example message"

hash256 = hashlib.sha3_256(msg).hexdigest()
hash512 = hashlib.sha3_512(msg).hexdigest()

print("SHA3‑256:", hash256)
print("SHA3‑512:", hash512)
