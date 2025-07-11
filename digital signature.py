from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Message
msg = b"Hello Digital Signature"

# Sign
sig = private_key.sign(msg, padding.PKCS1v15(), hashes.SHA256())

# Verify
public_key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
print("✅ Signature verified")
