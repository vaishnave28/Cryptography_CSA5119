def generate_key(text, key):
    key = key.upper()
    if len(text) == len(key):
        return key
    else:
        key = list(key)
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = generate_key(plaintext, key)
    cipher_text = ""
    for p, k in zip(plaintext, key):
        encrypted_char = chr((ord(p) + ord(k) - 2 * ord('A')) % 26 + ord('A'))
        cipher_text += encrypted_char
    return cipher_text

def decrypt_vigenere(ciphertext, key):
    key = generate_key(ciphertext, key)
    original_text = ""
    for c, k in zip(ciphertext, key):
        decrypted_char = chr((ord(c) - ord(k) + 26) % 26 + ord('A'))
        original_text += decrypted_char
    return original_text

# --- MAIN PROGRAM ---
plaintext = input("Enter plaintext (A-Z only): ").upper()
key = input("Enter key (A-Z only): ").upper()

encrypted = encrypt_vigenere(plaintext, key)
print("Encrypted Text:", encrypted)

decrypted = decrypt_vigenere(encrypted, key)
print("Decrypted Text:", decrypted)
