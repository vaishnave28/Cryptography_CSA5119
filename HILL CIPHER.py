def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists")

def matrix_mod_inverse(matrix, mod):
    a, b = matrix[0]
    c, d = matrix[1]
    det = (a * d - b * c) % mod
    det_inv = mod_inverse(det, mod)
    return [
        [(d * det_inv) % mod, (-b * det_inv) % mod],
        [(-c * det_inv) % mod, (a * det_inv) % mod]
    ]

def encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    cipher_text = ''
    for i in range(0, len(plaintext), 2):
        p1 = char_to_num(plaintext[i])
        p2 = char_to_num(plaintext[i+1])
        c1 = (key_matrix[0][0]*p1 + key_matrix[0][1]*p2) % 26
        c2 = (key_matrix[1][0]*p1 + key_matrix[1][1]*p2) % 26
        cipher_text += num_to_char(c1) + num_to_char(c2)
    return cipher_text

def decrypt(ciphertext, key_matrix):
    inv_key = matrix_mod_inverse(key_matrix, 26)
    decrypted_text = ''
    for i in range(0, len(ciphertext), 2):
        c1 = char_to_num(ciphertext[i])
        c2 = char_to_num(ciphertext[i+1])
        p1 = (inv_key[0][0]*c1 + inv_key[0][1]*c2) % 26
        p2 = (inv_key[1][0]*c1 + inv_key[1][1]*c2) % 26
        decrypted_text += num_to_char(p1) + num_to_char(p2)
    return decrypted_text

# Main program
key_matrix = [[3, 3], [2, 5]]  # Must be invertible mod 26

plaintext = input("Enter plaintext (A-Z only): ")
encrypted = encrypt(plaintext, key_matrix)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key_matrix)
print("Decrypted:", decrypted)
