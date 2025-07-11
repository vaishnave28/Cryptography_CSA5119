def egcd(a, b):
    return egcd(b, a % b) if b else (a, 1, 0)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    return x % m if g == 1 else None

def affine_encrypt(text, a, b):
    return ''.join([chr(((a * (ord(c)-65) + b) % 26) + 65) if c.isalpha() else c for c in text.upper()])

def affine_decrypt(cipher, a, b):
    a_inv = modinv(a, 26)
    return ''.join([chr(((a_inv * ((ord(c)-65) - b)) % 26) + 65) if c.isalpha() else c for c in cipher.upper()])

# Example:
pt = "HELLO"
ct = affine_encrypt(pt, a=5, b=8)
print("Cipher:", ct)
print("Plain :", affine_decrypt(ct, a=5, b=8))
