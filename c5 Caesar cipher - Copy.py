# mono_keyword.py
def build_cipher_from_keyword(keyword):
    keyword = ''.join(ch.upper() for ch in keyword if ch.isalpha())
    seen=set()
    cipher=[]
    for ch in keyword:
        if ch not in seen:
            seen.add(ch); cipher.append(ch)
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            cipher.append(ch)
    plain = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    mapping = {p:c for p,c in zip(plain,cipher)}
    inv = {c:p for p,c in mapping.items()}
    return mapping,inv

def encrypt(plaintext, mapping):
    return ''.join(mapping[ch] if ch.isalpha() else ch for ch in plaintext.upper())

def decrypt(ciphertext, inv):
    return ''.join(inv[ch] if ch.isalpha() else ch for ch in ciphertext.upper())

if __name__=="__main__":
    key="CIPHER"
    mapping,inv = build_cipher_from_keyword(key)
    pt = "attack at dawn"
    ct = encrypt(pt, mapping)
    print("Keyword:",key)
    print("Plain:",pt)
    print("Cipher:",ct)
    print("Decrypted:", decrypt(ct, inv))
