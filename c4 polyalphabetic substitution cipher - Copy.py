# affine_breaker.py
from collections import Counter
def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1 = egcd(b, a%b)
    return (g, y1, x1 - (a//b)*y1)
def modinv(a,m):
    g,x,y = egcd(a,m)
    return x % m if g==1 else None

def solve_for_a_b(cipher_most, plain_guess):
    # cipher_most and plain_guess are numeric 0..25
    solutions=[]
    for a in range(26):
        if egcd(a,26)[0] != 1: continue
        inv = modinv(a,26)
        # equation: (a * p + b) mod26 = c  -> b = c - a*p (mod26)
        # we only have pairs of guesses; we'll handle externally.
        solutions.append(a)
    return solutions

def try_break(ciphertext, map1=('B','E'), map2=('U','T')):
    ct = ''.join(ch.upper() for ch in ciphertext if ch.isalpha())
    c1 = ord(map1[0]) - 65; p1 = ord(map1[1]) - 65
    c2 = ord(map2[0]) - 65; p2 = ord(map2[1]) - 65
    candidates=[]
    for a in range(26):
        if egcd(a,26)[0] != 1: continue
        b = (c1 - a*p1) % 26
        if (a*p2 + b) % 26 == c2:
            # decrypt and show
            inv = modinv(a,26)
            pt = ''.join(chr((inv*(ord(ch)-65 - b))%26 + 65) for ch in ct)
            candidates.append((a,b,pt))
    return candidates

if __name__=="__main__":
    # Example ciphertext artificially created:
    ct = "BUPK BUPK BUBB BUBU"  # place holder
    print("Trying map B->E and U->T")
    sols = try_break(ct, ('B','E'), ('U','T'))
    if sols:
        for a,b,pt in sols:
            print("Found a,b:",a,b,"Plain:",pt)
    else:
        print("No solution with that mapping found. Try other plaintext guesses for the frequent letters.")
