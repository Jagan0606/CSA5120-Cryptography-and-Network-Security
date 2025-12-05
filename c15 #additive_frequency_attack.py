# additive_frequency_attack.py
import re
from collections import Counter

COMMON = {"the","be","to","of","and","a","in","that","have","i","it","for","not","on","with","he","as","you"}

def score_plain(pt):
    words = re.findall(r"[a-z]+", pt.lower())
    if not words: return 0
    hits = sum(1 for w in words if w in COMMON)
    return hits + 0.01 * len(''.join(words))

def attack(ct, topn=10):
    ct = ''.join(ch for ch in ct if ch.isalpha())
    candidates=[]
    for k in range(26):
        pt = ''.join(chr((ord(ch.upper())-65 - k) % 26 + 65) for ch in ct)
        candidates.append((score_plain(pt), k, pt))
    candidates.sort(reverse=True)
    return candidates[:topn]

if __name__=="__main__":
    ct = "KHOOR ZRUOG"  # HELLO WORLD with shift 3
    res = attack(ct, topn=5)
    for score,k,pt in res:
        print("Shift:",k,"Score:",score,"Plain:",pt)
