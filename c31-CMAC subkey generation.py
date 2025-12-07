# q31_cmac_subkeys.py
def left_shift(bits):
    out = ((bits << 1) & ((1<<bits_len)-1))
    carry = (bits >> (bits_len-1)) & 1
    return out, carry

def generate_subkeys(bits_len):
    global bits_len_global
    bits_len_global = bits_len
    Rb = 0x1B if bits_len==64 else 0x87  # 64->0x1B, 128->0x87
    # For demo use a toy "L" value (result of encrypting zero block)
    L = 0x8000000000000000 if bits_len==64 else 0x80000000000000000000000000000000
    # left shift L
    shifted = (L << 1) & ((1<<bits_len)-1)
    if (L >> (bits_len-1)) & 1:
        K1 = shifted ^ Rb
    else:
        K1 = shifted
    shifted2 = (K1 << 1) & ((1<<bits_len)-1)
    if (K1 >> (bits_len-1)) & 1:
        K2 = shifted2 ^ Rb
    else:
        K2 = shifted2
    return K1, K2

# Demo for 64-bit and 128-bit
K1_64, K2_64 = generate_subkeys(64)
K1_128, K2_128 = generate_subkeys(128)
print("64-bit K1,K2 (hex):", hex(K1_64), hex(K2_64))
print("128-bit K1,K2 (hex):", hex(K1_128), hex(K2_128))
