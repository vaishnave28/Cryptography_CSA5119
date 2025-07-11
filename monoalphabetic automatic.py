import random, string

def mono_encrypt(text):
    alpha = string.ascii_uppercase
    key = ''.join(random.sample(alpha, 26))
    table = str.maketrans(alpha, key)
    return text.upper().translate(table), key

def mono_decrypt(cipher, key):
    alpha = string.ascii_uppercase
    table = str.maketrans(key, alpha)
    return cipher.translate(table)

# Example usage
plain = "HELLO WORLD"
cipher, key = mono_encrypt(plain)
print("Cipher:", cipher)
print("Key   :", key)
print("Plain :", mono_decrypt(cipher, key))
