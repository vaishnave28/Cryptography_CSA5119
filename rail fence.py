def rail_fence_encrypt(text, rails):
    fence = [''] * rails
    rail = 0
    direction = 1
    for char in text:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join(fence)

print(rail_fence_encrypt("HELLO WORLD", 3))
