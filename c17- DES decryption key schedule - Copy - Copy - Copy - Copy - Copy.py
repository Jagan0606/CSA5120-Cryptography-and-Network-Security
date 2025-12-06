# Q17: DES decryption key schedule
# Simple program showing reversal of 16 DES round keys

def generate_keys():
    keys = [f"K{i}" for i in range(1, 17)]  # K1 .. K16
    return keys

def des_decryption_keys():
    keys = generate_keys()
    print("Encryption Keys Order : ", keys)
    print("Decryption Keys Order : ", list(reversed(keys)))

des_decryption_keys()
