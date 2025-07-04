def encrypt_additive(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shifted = (ord(char) - ord('A') + key) % 26
            encrypted += chr(shifted + ord('A'))
        else:
            encrypted += char
    return encrypted

def decrypt_additive(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = (ord(char) - ord('A') - key) % 26
            decrypted += chr(shifted + ord('A'))
        else:
            decrypted += char
    return decrypted

# --- MAIN PROGRAM ---
plaintext = input("Enter plaintext (A-Z only): ")
key = int(input("Enter key (0-25): "))

encrypted_text = encrypt_additive(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt_additive(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
