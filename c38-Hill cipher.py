# q38_hill_known_plain.py
def egcd(a,b):
    if b==0: return a,1,0
    g,x,y = egcd(b,a%b)
    return g, y, x - (a//b)*y
def modinv(a,m):
    g,x,y = egcd(a,m)
    return x % m if g==1 else None

def mat_inv_2x2(P):
    det = (P[0][0]*P[1][1] - P[0][1]*P[1][0]) % 26
    inv_det = modinv(det,26)
    if inv_det is None: return None
    inv = [[P[1][1]*inv_det%26, (-P[0][1])*inv_det%26],
           [(-P[1][0])*inv_det%26, P[0][0]*inv_det%26]]
    return inv

def mat_mul(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%26, (A[0][0]*B[0][1]+A[0][1]*B[1][1])%26],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%26, (A[1][0]*B[0][1]+A[1][1]*B[1][1])%26]]

# Example: plaintext "HI" and "ME" -> ciphertext "UV" and "PQ"
P = [[7,12],[8,4]]  # columns: H(7), M(12) ; I(8), E(4)
C = [[20,15],[21,16]]  # U(20), P(15) ; V(21), Q(16)
invP = mat_inv_2x2(P)
K = mat_mul(C,invP)
print("Recovered Key K:", K)
