# q35_one_time_pad_vigenere.py
def otp_encrypt(pt, keystream):
    s = ''.join(ch for ch in pt.lower() if ch.isalpha())
    out = ''.join(chr((ord(s[i])-97 + keystream[i]) % 26 + 97) for i in range(len(s)))
    return out

def otp_decrypt(ct, keystream):
    out = ''.join(chr((ord(ct[i])-97 - keystream[i]) % 26 + 97) for i in range(len(ct)))
    return out

pt = "sendmoremoney"
ks = [3,19,5, 9,0,1,7,23,15,21,14,11,11]
ct = otp_encrypt(pt, ks)
print("Plain:", pt)
print("Keystream:", ks)
print("Cipher:", ct)
print("Decrypted:", otp_decrypt(ct, ks))
