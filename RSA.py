def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def encrypt(msg, e, n):
    cipher = [pow(ord(char), e, n) for char in msg]
    return cipher

def decrypt(cipher, d, n):
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)

# --- MAIN PROGRAM ---
# 1. Choose 2 prime numbers (for simplicity, small numbers)
p = 3
q = 11
n = p * q  # n = 33
phi = (p - 1) * (q - 1)  # phi = 20

# 2. Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 7
if gcd(e, phi) != 1:
    raise ValueError("e and phi are not coprime!")

# 3. Compute d (modular inverse of e mod phi)
d = mod_inverse(e, phi)
if d is None:
    raise ValueError("Modular inverse of e does not exist!")

# 4. Input message
message = input("Enter message (text): ")

# 5. Encrypt
encrypted = encrypt(message, e, n)
print("Encrypted message:", encrypted)

# 6. Decrypt
decrypted = decrypt(encrypted, d, n)
print("Decrypted message:", decrypted)
