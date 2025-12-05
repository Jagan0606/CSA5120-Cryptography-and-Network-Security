# otp_vigenere.py
def otp_encrypt(pt, keystream):
    pt = ''.join(ch.upper() for ch in pt if ch.isalpha())
    out=[]
    for i,ch in enumerate(pt):
        k = keystream[i]
        out.append(chr(((ord(ch)-65 + k) % 26) + 65))
    return ''.join(out)

def otp_decrypt(ct, keystream):
    out=[]
    for i,ch in enumerate(ct):
        k = keystream[i]
        out.append(chr(((ord(ch)-65 - k) % 26) + 65))
    return ''.join(out)

if __name__=="__main__":
    pt = "sendmoremoney"
    key = [9,0,1,7,23,15,21,14,11,11,2,8,9]
    ct = otp_encrypt(pt, key)
    print("Plain:", pt)
    print("Keystream:", key)
    print("Cipher:", ct)
    print("Decrypt:", otp_decrypt(ct, key))
