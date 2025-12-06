# simple XOR-based CBC demo to keep it easy

def xor(a, b): return ''.join('1' if x!=y else '0' for x,y in zip(a,b))

plaintext = "0000000100100011"
key       = "0111111101"
iv        = "10101010"

# Fake S-DES step using XOR with key repeated
key_expanded = (key * 4)[:16]

# CBC encryption
c1 = xor( xor(plaintext[:8], iv), key_expanded[:8] )
c2 = xor( xor(plaintext[8:], c1), key_expanded[8:] )

print("Ciphertext =", c1 + c2)
