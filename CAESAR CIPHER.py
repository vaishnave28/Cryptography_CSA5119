def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char  # keep symbols/spaces as is
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += char
    return plaintext

# --- MAIN PROGRAM ---
message = input("Enter the message: ")
shift = int(input("Enter the shift key (0-25): "))

encrypted = encrypt_caesar(message, shift)
print("Encrypted Message:", encrypted)

decrypted = decrypt_caesar(encrypted, shift)
print("Decrypted Message:", decrypted)
