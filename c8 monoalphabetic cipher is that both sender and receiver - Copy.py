# additive_freq_attack.py
import re
from collections import Counter

COMMON_WORDS = {"THE","BE","TO","OF","AND","A","IN","THAT","HAVE","I","IT","FOR","NOT","ON","WITH","HE","AS","YOU","DO","AT"}

def score_plaintext(pt):
    words = re.findall(r"[A-Z]+", pt)
    if not words: return 0
    matches = sum(1 for w in words if w in COMMON_WORDS)
    return matches + 0.1*len(''.join(words))  # simple heuristic

def attack(ciphertext, topn=5):
    ct = ''.join(ch.upper() for ch in ciphertext if ch.isalpha())
    candidates=[]
    for k in range(26):
        pt = ''.join(chr((ord(ch)-65 - k)%26 + 65) for ch in ct)
        candidates.append((score_plaintext(pt), k, pt))
    candidates.sort(reverse=True)
    return candidates[:topn]

if __name__=="__main__":
    ct = "KHOOR ZRUOG"  # "HELLO WORLD" shifted by 3
    for score,k,pt in attack(ct, topn=5):
        print("Score:",score,"Shift:",k,"Plain:",pt)
