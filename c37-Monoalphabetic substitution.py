# q37_monoattack.py
import random, re
from collections import Counter
EN_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
COMMON = {"the","and","that","have","for","not","with","you","this"}

def freq_mapping(ct):
    letters = [c for c in ct.upper() if c.isalpha()]
    freq = [p for p,_ in Counter(letters).most_common()]
    mapping = {}
    for i,ch in enumerate(freq):
        mapping[ch] = EN_FREQ[i]
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch not in mapping: mapping[ch] = '?'
    return mapping

def apply_map(ct,m):
    return ''.join(m[c] if c.isalpha() else c for c in ct.upper())

def score_plain(pt):
    words = re.findall(r"[A-Z]+", pt)
    return sum(len(w) for w in words if w.lower() in COMMON)

def hill_climb(ct, iters=2000):
    m = freq_mapping(ct)
    best = (score_plain(apply_map(ct,m)), m)
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for _ in range(iters):
        a,b = random.sample(letters,2)
        m2 = m.copy()
        # swap outputs for a and b
        m2[a], m2[b] = m2[b], m2[a]
        sc = score_plain(apply_map(ct,m2))
        if sc > best[0]:
            best = (sc, m2)
    return best

if __name__=="__main__":
    ciphertext = "GSRH RH Z HVXIVG"  # "THIS IS A SECRET" in Atbash for demo
    score,map_ = hill_climb(ciphertext, iters=5000)
    print("Best score:", score)
    print("Plain guess:", apply_map(ciphertext, map_))
