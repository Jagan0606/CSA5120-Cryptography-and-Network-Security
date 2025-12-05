# playfair_custom_matrix.py
# Uses the exact 5x5 matrix provided (I/J combined).
def build_matrix():
    rows = [
        list("MFHIK"),
        list("UNOPQ"),
        list("ZVWXY"),
        list("ELARG"),
        list("DSTBC")
    ]
    pos = {}
    for r in range(5):
        for c in range(5):
            ch = rows[r][c]
            if ch == 'J': ch = 'I'
            pos[ch] = (r,c)
    return rows, pos

def preprocess(pt):
    s = ''.join(ch.upper() for ch in pt if ch.isalpha()).replace('J','I')
    # create digraphs with X filler
    out=[]
    i=0
    while i < len(s):
        a = s[i]
        b = s[i+1] if i+1 < len(s) else 'X'
        if a==b:
            out.append((a,'X'))
            i += 1
        else:
            out.append((a,b))
            i += 2
    return out

def encrypt_pair(a,b,mat,pos):
    r1,c1 = pos[a]; r2,c2 = pos[b]
    if r1==r2:
        return mat[r1][(c1+1)%5], mat[r2][(c2+1)%5]
    if c1==c2:
        return mat[(r1+1)%5][c1], mat[(r2+1)%5][c2]
    return mat[r1][c2], mat[r2][c1]

def playfair_encrypt(plaintext):
    mat,pos = build_matrix()
    pairs = preprocess(plaintext)
    cipher = []
    for a,b in pairs:
        c1,c2 = encrypt_pair(a,b,mat,pos)
        cipher.append(c1+c2)
    return ' '.join(cipher)

if __name__ == "__main__":
    pt = "Must see you over Cadogan West. Coming at once."
    print("Plaintext:", pt)
    ct = playfair_encrypt(pt)
    print("Ciphertext:", ct)
