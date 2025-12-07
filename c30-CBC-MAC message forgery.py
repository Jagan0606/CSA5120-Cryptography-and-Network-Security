# q30_cbc_mac_forge.py
def block_cipher_encrypt(block, key):
    # toy block cipher: XOR bytes (block and key are ints 0..255)
    return block ^ key

def cbc_mac(message_blocks, key, iv=0):
    prev = iv
    for b in message_blocks:
        prev = block_cipher_encrypt(prev ^ b, key)
    return prev

# single-block message X
X = [0x5A]  # one block
key = 0x0F
T = cbc_mac(X, key)
# compute message X || (X xor T)
X2 = X + [X[0] ^ T]
T2 = cbc_mac(X2, key)
print("T:", hex(T), "T2:", hex(T2))
