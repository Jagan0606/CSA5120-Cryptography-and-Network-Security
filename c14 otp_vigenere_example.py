# otp_vigenere_example.py
def encrypt_otp(pt, keystream):
    s = ''.join(ch for ch in pt.lower() if ch.isalpha())
    out = []
    for i,ch in enumerate(s):
        k = keystream[i]
        out.append(chr((ord(ch)-97 + k) % 26 + 97))
    return ''.join(out)

def find_key_for_mapping(ct, target):
    ct_s = ''.join(ch for ch in ct.lower() if ch.isalpha())
    tgt_s = ''.join(ch for ch in target.lower() if ch.isalpha())
    if len(ct_s) != len(tgt_s):
        raise ValueError("lengths must match for this example")
    key = [ (ord(ct_s[i])-97 - (ord(tgt_s[i])-97)) % 26 for i in range(len(ct_s)) ]
    return key

if __name__=="__main__":
    pt = "send more money"
    keystream = [9,0,1,7,23,15,21,14,11,11,2,8,9]
    ct = encrypt_otp(pt, keystream)
    print("Plain:", pt)
    print("Keystream:", keystream)
    print("Ciphertext:", ct)

    # part b: find a key so that ciphertext decrypts to "cash not needed"
    target = "cash not needed"
    # need lengths equal; truncate/pad as needed to match lengths (here both have 13 letters)
    key_to_map = find_key_for_mapping(ct, target)
    print("To decrypt ciphertext to target:", target)
    print("Required keystream:", key_to_map)
