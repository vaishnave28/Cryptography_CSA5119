def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    result = []
    for char in key:
        if char not in result and char.isalpha():
            result.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # I/J treated as same
        if char not in result:
            result.append(char)

    # 5x5 matrix
    matrix = [result[i*5:(i+1)*5] for i in range(5)]
    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def process_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    i = 0
    result = ''
    while i < len(text):
        a = text[i]
        b = ''
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1
        result += a + b
    return result

def encrypt_playfair(plaintext, matrix):
    plaintext = process_text(plaintext)
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext

def decrypt_playfair(ciphertext, matrix):
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    return plaintext

# --- MAIN PROGRAM ---
key = input("Enter key: ")
matrix = generate_key_matrix(key)

print("Key Matrix:")
for row in matrix:
    print(row)

plaintext = input("Enter plaintext: ")
ciphertext = encrypt_playfair(plaintext, matrix)
print("Encrypted Text:", ciphertext)

decrypted = decrypt_playfair(ciphertext, matrix)
print("Decrypted Text:", decrypted)
