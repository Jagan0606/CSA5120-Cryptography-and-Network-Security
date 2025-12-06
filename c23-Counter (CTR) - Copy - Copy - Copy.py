def xor(a,b): return ''.join('1' if x!=y else '0' for x,y in zip(a,b))

plaintext = "000000010000001000000100"
key       = "0111111101"
counter   = "00000000"

# expand key to 8 bits
key8 = key[:8]

keystream1 = xor(counter, key8)
keystream2 = xor("00000001", key8)
keystream3 = xor("00000010", key8)

blocks = [plaintext[:8], plaintext[8:16], plaintext[16:]]

cipher = xor(blocks[0], keystream1) + xor(blocks[1], keystream2) + xor(blocks[2], keystream3)
print("Cipher =", cipher)
