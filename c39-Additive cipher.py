# q39_additive_attack.py
import re
COMMON = {"the","and","to","of","a","in","that","is","it"}

def score(s):
    words = re.findall(r"[a-z]+", s.lower())
    return sum(1 for w in words if w in COMMON)

def attack(ct, topn=5):
    ct = ''.join(ch for ch in ct if ch.isalpha())
    candidates=[]
    for k in range(26):
        pt = ''.join(chr((ord(c.upper())-65 - k)%26 + 65) for c in ct)
        candidates.append((score(pt), k, pt))
    return sorted(candidates, reverse=True)[:topn]

if __name__=="__main__":
    ct="KHOOR ZRUOG"
    for sc,k,pt in attack(ct,5):
        print("Shift",k,"score",sc,"plaintext",pt)
