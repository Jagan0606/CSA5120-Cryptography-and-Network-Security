# hill2x2.py
def mat_mul(A,B,mod=26):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%mod for j in range(len(B[0]))] for i in range(len(A))]

def det2(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1 = egcd(b, a%b)
    return (g, y1, x1 - (a//b)*y1)
def modinv(a,m):
    g,x,y = egcd(a,m)
    return x % m if g==1 else None

def invert_key(A):
    d = det2(A) % 26
    invd = modinv(d,26)
    if invd is None: raise ValueError("Key matrix not invertible mod 26")
    invA = [[ A[1][1]*invd %26, (-A[0][1])*invd %26],
            [(-A[1][0])*invd %26, A[0][0]*invd %26]]
    # normalize
    for i in range(2):
        for j in range(2):
            invA[i][j] %= 26
    return invA

def text_to_vec(s):
    s = ''.join(ch.upper() for ch in s if ch.isalpha())
    if len(s)%2: s += 'X'
    vecs=[]
    for i in range(0,len(s),2):
        vecs.append([[ord(s[i])-65],[ord(s[i+1])-65]])
    return vecs

def vec_to_text(vecs):
    out=[]
    for v in vecs:
        out.append(chr(v[0][0]+65)+chr(v[1][0]+65))
    return ''.join(out)

def encrypt(pt, key):
    vecs = text_to_vec(pt)
    out=[]
    for v in vecs:
        prod = mat_mul(key, v)
        out.append(prod)
    return vec_to_text(out)

def decrypt(ct, key):
    invK = invert_key(key)
    vecs = text_to_vec(ct)
    out=[]
    for v in vecs:
        prod = mat_mul(invK, v)
        out.append(prod)
    return vec_to_text(out)

if __name__=="__main__":
    K = [[9,4],[5,7]]
    pt = "meetmeattheusualplace"
    ct = encrypt(pt, K)
    print("Plain:", pt)
    print("Key:", K)
    print("Cipher:", ct)
    print("Decrypted:", decrypt(ct, K))
