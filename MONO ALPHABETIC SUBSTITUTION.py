import string

# Define the substitution key (must be 26 unique uppercase letters)
# Example: Key maps A→Q, B→W, C→E, ..., Z→M
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Build encryption and decryption dictionaries
def build_substitution_dicts(key):
    alphabet = string.ascii_uppercase
    encrypt_dict = dict(zip(alphabet, key))
    decrypt_dict = dict(zip(key, alphabet))
    return encrypt_dict, decrypt_dict

# Encrypt function
def encrypt_monoalpha(plaintext, encrypt_dict):
    plaintext = plaintext.upper().replace(" ", "")
    encrypted = ''
    for char in plaintext:
        if char.isalpha():
            encrypted += encrypt_dict[char]
        else:
            encrypted += char
    return encrypted

# Decrypt function
def decrypt_monoalpha(ciphertext, decrypt_dict):
    decrypted = ''
    for char in ciphertext:
        if char.isalpha():
            decrypted += decrypt_dict[char]
        else:
            decrypted += char
    return decrypted

# --- MAIN PROGRAM ---
plaintext = input("Enter plaintext (A-Z only): ")
encrypt_dict, decrypt_dict = build_substitution_dicts(key)

encrypted_text = encrypt_monoalpha(plaintext, encrypt_dict)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt_monoalpha(encrypted_text, decrypt_dict)
print("Decrypted Text:", decrypted_text)
