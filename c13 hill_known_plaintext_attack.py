# hill_known_plaintext_attack.py
# Given two plaintext digraphs p1,p2 and their ciphertexts c1,c2, compute key K (2x2)
def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1 = egcd(b, a%b)
    return (g, y1, x1 - (a//b)*y1)

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g!=1: return None
    return x % m

def mat_inv_2x2(P):
    det = (P[0][0]*P[1][1] - P[0][1]*P[1][0]) % 26
    inv_det = modinv(det,26)
    if inv_det is None:
        return None
    inv = [
        [(P[1][1]*inv_det)%26, ((-P[0][1])*inv_det)%26],
        [((-P[1][0])*inv_det)%26, (P[0][0]*inv_det)%26]
    ]
    for i in range(2):
        for j in range(2):
            inv[i][j] %= 26
    return inv

def mat_mul(A,B):
    # 2x2 * 2x2
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0])%26, (A[0][0]*B[0][1]+A[0][1]*B[1][1])%26],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%26, (A[1][0]*B[0][1]+A[1][1]*B[1][1])%26]]

if __name__=="__main__":
    # Example: suppose plaintext digraphs "hi" and "me" mapped to ciphertext "UV" and "PQ"
    # Convert to numeric column vectors and form P and C matrices:
    p1 = [ord('h')-97, ord('i')-97]
    p2 = [ord('m')-97, ord('e')-97]
    c1 = [ord('u')-97, ord('v')-97]
    c2 = [ord('p')-97, ord('q')-97]
    P = [[p1[0], p2[0]],[p1[1], p2[1]]]  # columns are p1,p2
    C = [[c1[0], c2[0]],[c1[1], c2[1]]]
    invP = mat_inv_2x2(P)
    if invP is None:
        print("Plaintext matrix not invertible — need different plaintext pairs.")
    else:
        K = mat_mul(C, invP)
        print("Recovered key K (mod26):", K)
