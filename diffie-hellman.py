# Publicly agreed prime (p) and base (g)
p = 23
g = 5

# Private keys
a = 6  # Alice's secret
b = 15 # Bob's secret

# Public keys
A = pow(g, a, p)  # Alice sends A
B = pow(g, b, p)  # Bob sends B

# Shared secrets
s_alice = pow(B, a, p)
s_bob   = pow(A, b, p)

print("Shared secret (Alice):", s_alice)
print("Shared secret (Bob)  :", s_bob)
