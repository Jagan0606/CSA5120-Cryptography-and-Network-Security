# playfair.py
# Simple Playfair encryptor (I/J merged). Plaintext non-letters removed, pairs formed with 'X' filler.

def build_key_matrix(keyword):
    seen = set()
    table = []
    keyword = keyword.upper().replace('J','I')
    for ch in keyword:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            table.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J omitted, merged with I
        if ch not in seen:
            seen.add(ch)
            table.append(ch)
    matrix = [table[i*5:(i+1)*5] for i in range(5)]
    pos = {matrix[r][c]: (r,c) for r in range(5) for c in range(5)}
    return matrix, pos

def prepare_plaintext(pt):
    s = ''.join(ch.upper().replace('J','I') for ch in pt if ch.isalpha())
    res=[]
    i=0
    while i < len(s):
        a = s[i]
        b = s[i+1] if i+1 < len(s) else 'X'
        if a==b:
            res.append(a+'X')
            i+=1
        else:
            res.append(a+b)
            i+=2
    return res

def playfair_encrypt(keyword, plaintext):
    matrix,pos = build_key_matrix(keyword)
    pairs = prepare_plaintext(plaintext)
    out=[]
    for a,b in pairs:
        ra,ca = pos[a]; rb,cb = pos[b]
        if ra==rb:
            out.append(matrix[ra][(ca+1)%5] + matrix[rb][(cb+1)%5])
        elif ca==cb:
            out.append(matrix[(ra+1)%5][ca] + matrix[(rb+1)%5][cb])
        else:
            out.append(matrix[ra][cb] + matrix[rb][ca])
    return ' '.join(out)

if __name__ == "__main__":
    key = "MONARCHY"
    pt = "instruments"
    print("Key:", key)
    print("Plaintext:", pt)
    print("Ciphertext:", playfair_encrypt(key, pt))
