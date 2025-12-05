# hill_encrypt_decrypt.py
import math

MOD = 26

def mat_mul(A,B):
    # A: 2x2, B: 2x1 -> 2x1
    return [ (A[0][0]*B[0] + A[0][1]*B[1]) % MOD,
             (A[1][0]*B[0] + A[1][1]*B[1]) % MOD ]

def det2(A):
    return (A[0][0]*A[1][1] - A[0][1]*A[1][0]) % MOD

def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1 = egcd(b, a%b)
    return (g, y1, x1 - (a//b)*y1)

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g!=1: return None
    return x % m

def inverse_key(A):
    d = det2(A)
    invd = modinv(d, MOD)
    if invd is None:
        raise ValueError("Key not invertible modulo 26")
    invA = [
        [( A[1][1] * invd) % MOD, ((-A[0][1]) * invd) % MOD],
        [((-A[1][0]) * invd) % MOD, ( A[0][0] * invd) % MOD]
    ]
    return invA

def text_to_pairs(s):
    s = ''.join(ch for ch in s.lower() if ch.isalpha())
    if len(s)%2==1: s += 'x'
    pairs = []
    for i in range(0,len(s),2):
        pairs.append([ord(s[i]) - 97, ord(s[i+1]) - 97])
    return pairs

def pairs_to_text(pairs):
    return ''.join(chr(p[0]+97)+chr(p[1]+97) for p in pairs)

if __name__=="__main__":
    K = [[9,4],[5,7]]
    invK = inverse_key(K)
    pt = "meet me at the usual place at ten rather than eight oclock"
    pairs = text_to_pairs(pt)
    # Encrypt
    ct_pairs = []
    for v in pairs:
        res = mat_mul(K, v)
        ct_pairs.append(res)
    ct = pairs_to_text(ct_pairs)
    # Decrypt
    dec_pairs=[]
    for v in ct_pairs:
        dec_pairs.append(mat_mul(invK, v))
    dec = pairs_to_text(dec_pairs)

    print("Key K =", K)
    print("Inverse Key K^-1 =", invK)
    print()
    print("Plain (letters only):", ''.join(ch for ch in pt.lower() if ch.isalpha()))
    print("Ciphertext:", ct)
    print("Decrypted:", dec)
