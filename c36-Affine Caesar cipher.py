# q36_affine.py
import math
def egcd(a,b):
    if b==0: return a,1,0
    g,x,y = egcd(b, a%b)
    return g, y, x - (a//b)*y
def modinv(a,m):
    g,x,y = egcd(a,m)
    return x % m if g==1 else None

valid_a = [a for a in range(26) if math.gcd(a,26)==1]
print("Allowed a values:", valid_a)

def encrypt(text,a,b):
    return ''.join(chr(((a*(ord(c)-65)+b)%26)+65) for c in text)

def decrypt(ct,a,b):
    inv = modinv(a,26)
    if inv is None: raise Exception("a not invertible")
    return ''.join(chr(((inv*(ord(c)-65 - b))%26)+65) for c in ct)

pt="HELLO"
a,b=5,8
ct=encrypt(pt,a,b)
print("Cipher:",ct,"Decrypted:",decrypt(ct,a,b))
