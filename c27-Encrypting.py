# q27_rsa_single_char_demo.py
# Small demo: RSA encrypt letters 0..25 and show trivial break by dictionary

# Toy RSA (not secure) for demonstration
p, q = 61, 53
n = p*q
e = 17
d = pow(e, -1, (p-1)*(q-1))

def encrypt_letter(ch):
    m = ord(ch) - 65
    return pow(m, e, n)

def break_cipher(ciphertexts):
    # Precompute dictionary
    table = {pow(i, e, n): i for i in range(26)}
    return ''.join(chr(table[c] + 65) for c in ciphertexts)

# Example message
msg = "HELLO"
cts = [encrypt_letter(ch) for ch in msg]
print("Ciphertexts:", cts)
print("Broken plaintext via precompute:", break_cipher(cts))
