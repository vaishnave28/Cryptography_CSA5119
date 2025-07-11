p = b'HELLO'
k = b'XMCKL'
c = bytes([a ^ b for a, b in zip(p, k)])
print('Cipher:', c)
d = bytes([a ^ b for a, b in zip(c, k)])
print('Plain :', d)
