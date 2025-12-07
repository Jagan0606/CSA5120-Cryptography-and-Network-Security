# q26_rsa_leaked_demo.py
def rsa_encrypt(m, e, n): return pow(m, e, n)
def rsa_decrypt(c, d, n): return pow(c, d, n)

# Example keys
p, q = 59, 61
n = p*q
phi = (p-1)*(q-1)
e_old = 31
# compute d_old (given)
d_old = 2231

m = 123  # plaintext block
c = rsa_encrypt(m, e_old, n)
print("Ciphertext (old):", c)

# Attacker with leaked d_old can decrypt
print("Attacker recovers:", rsa_decrypt(c, d_old, n))

# Bob switches to a new e' but same n
e_new = 17
# attacker still has d_old and can decrypt the old ciphertext
print("Attacker still recovers (with leaked d_old):", rsa_decrypt(c, d_old, n))
